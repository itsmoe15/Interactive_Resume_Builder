from flask import Flask, render_template, request, make_response, jsonify, send_file
import os
import pdfkit
from io import BytesIO
import json
import uuid
from datetime import datetime
import tempfile

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Function to find wkhtmltopdf executable
def find_wkhtmltopdf():
    # Common installation paths for wkhtmltopdf on Windows
    possible_paths = [
        r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe',
        # Add more possible paths if needed
    ]
    
    # Check if any of these paths exist
    for path in possible_paths:
        if os.path.exists(path):
            return path
            
    # If none of the predefined paths work, try to find it in PATH
    try:
        import subprocess
        path = subprocess.check_output(['where', 'wkhtmltopdf'], shell=True).decode('utf-8').strip()
        if path and os.path.exists(path):
            return path
    except:
        pass
        
    # Return None if not found
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-cv')
def create_cv():
    return render_template('create_cv.html')

@app.route('/preview-cv', methods=['POST'])
def preview_cv():
    # Get form data
    data = request.form.to_dict(flat=False)
    
    # Process the data to handle array fields properly
    processed_data = {}
    for key, value in data.items():
        if key.endswith('[]'):
            processed_data[key] = value
        else:
            processed_data[key] = value[0] if value else ""
    
    # Generate a unique ID for this CV
    cv_id = str(uuid.uuid4())
    
    # For now, we'll just pass the processed data to the template
    return render_template('preview_cv.html', cv_data=processed_data)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    # Find wkhtmltopdf path
    wkhtmltopdf_path = find_wkhtmltopdf()
    if not wkhtmltopdf_path:
        return """
            <h2>wkhtmltopdf not found</h2>
            <p>Please download and install wkhtmltopdf from: 
            <a href='https://wkhtmltopdf.org/downloads.html'>https://wkhtmltopdf.org/downloads.html</a></p>
            <p>After installation, restart this application.</p>
            <p><a href="/preview-cv" onclick="window.history.back(); return false;">Go back</a></p>
        """, 500
    
    # Configure pdfkit with the found path
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    
    # Get form data and process it to handle array fields properly
    data = request.form.to_dict(flat=False)
    processed_data = {}
    for key, value in data.items():
        if key.endswith('[]'):
            processed_data[key] = value
        else:
            processed_data[key] = value[0] if value else ""
    
    # Generate HTML from template
    html = render_template('cv_template.html', cv_data=processed_data)
    
    # Create a temporary file to store the HTML content
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
        f.write(html.encode('utf-8'))
        html_file_path = f.name
    
    # Configure pdfkit options
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'no-outline': None
    }
    
    try:
        # Generate PDF using pdfkit with explicit configuration
        pdf_data = pdfkit.from_file(html_file_path, False, options=options, configuration=config)
        
        # Remove temporary HTML file
        os.unlink(html_file_path)
        
        # Return PDF as a downloadable file
        filename = f"CV_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename={filename}'
        
        return response
    except Exception as e:
        # Handle errors
        os.unlink(html_file_path)  # Clean up the temporary file
        error_message = f"<h2>PDF generation failed:</h2>"
        error_message += f"<p>{str(e)}</p>"
        error_message += f"<p>The application looked for wkhtmltopdf at: {wkhtmltopdf_path}</p>"
        error_message += f"<p>If wkhtmltopdf is installed elsewhere, please check the path.</p>"
        error_message += f"<p>Download wkhtmltopdf from: <a href='https://wkhtmltopdf.org/downloads.html'>https://wkhtmltopdf.org/downloads.html</a></p>"
        error_message += f"<p><a href='#' onclick='window.history.back(); return false;'>Go back</a></p>"
        return error_message, 500

if __name__ == '__main__':
    app.run(debug=True, port=80) 