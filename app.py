from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, send_from_directory, make_response
from flask_login import LoginManager, login_user, login_required, logout_user
import bcrypt
import os
from werkzeug.utils import secure_filename
import base64
from io import BytesIO
import tempfile
from xhtml2pdf import pisa
from pypdf import PdfReader, PdfWriter
import pdfkit
from datetime import datetime
from flask_login import current_user
import glob

from app import create_app
from app.models.user import db, User, CV, WorkExperience, Education, Style
from app.services.ats_service import analyze_cv

app = create_app()

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            login_user(user)
            return redirect(url_for('home'))
        
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))
        new_user = User(username=username, password=hashed.decode('utf-8'))
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/chatbot')
@login_required
def chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
@login_required
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    response = {
        'response': f"I received your message: {user_message}. This is a placeholder response.",
        'cv_update': f"<h4>CV Preview</h4><p>This is where the CV content will be updated based on the conversation.</p>"
    }
    
    return jsonify(response)

@app.route('/ats-checker')
@login_required
def ats_checker():
    return render_template('ats_checker.html')

@app.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/check-ats', methods=['POST'])
@login_required
def check_ats():
    if 'cv' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['cv']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Check file type
    allowed_extensions = {'.pdf', '.doc', '.docx'}
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in allowed_extensions:
        return jsonify({'error': 'Invalid file type. Please upload a PDF or Word document.'}), 400

    # Save file temporarily
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        file.save(filepath)
        
        # Read file content
        with open(filepath, 'rb') as f:
            file_content = f.read()
        
        # Convert to base64
        base64_content = base64.b64encode(file_content).decode('utf-8')
        
        # Analyze CV using our service
        analysis_result = analyze_cv(base64_content)
        
        
        # Return the analysis result and file URL
        file_url = url_for('uploaded_file', filename=filename)
        analysis_result['file_url'] = file_url
        return jsonify(analysis_result)
    
    except ValueError as e:
        # Clean up the temporary file
        # if os.path.exists(filepath):
        #     os.remove(filepath)
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Clean up the temporary file
        # if os.path.exists(filepath):
        #     os.remove(filepath)
        app.logger.error(f"Error in check_ats: {str(e)}")
        return jsonify({'error': 'An error occurred while analyzing your CV. Please try again.'}), 500

@app.route('/cv-maker')
@login_required
def cv_maker():
    return render_template('cv_maker_form.html')

@app.route('/my-cvs')
@login_required
def my_cvs():
    cvs = CV.query.filter_by(owner_id=current_user.id).all()
    # Get PDF file info and creation date for each CV
    cv_list = []
    for cv in cvs:
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'gen_cvs', f'cv_{cv.id}.pdf')
        if os.path.exists(pdf_path):
            date_created = datetime.fromtimestamp(os.path.getctime(pdf_path))
        else:
            date_created = None
        cv_list.append({
            'id': cv.id,
            'name': cv.full_name,
            'style': cv.style.name if cv.style else 'Modern',
            'pdf_exists': os.path.exists(pdf_path),
            'pdf_url': url_for('download_cv_pdf', cv_id=cv.id) if os.path.exists(pdf_path) else None,
            'date_created': date_created.strftime('%Y-%m-%d %H:%M') if date_created else 'N/A',
        })
    styles = ['Modern', 'Classic', 'Professional']
    return render_template('my_cvs.html', cvs=cv_list, styles=styles)

@app.route('/download-cv/<int:cv_id>')
@login_required
def download_cv_pdf(cv_id):
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'gen_cvs', f'cv_{cv_id}.pdf')
    if os.path.exists(pdf_path):
        return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], 'gen_cvs'), f'cv_{cv_id}.pdf')
    else:
        return '<h2>PDF not found</h2>', 404

@app.route('/preview-cv', methods=['POST'])
@login_required
def preview_cv():
    data = request.form.to_dict(flat=False)
    processed_data = {}
    for key, value in data.items():
        if key.endswith('[]'):
            processed_data[key] = value
        else:
            processed_data[key] = value[0] if value else ""
    return render_template('preview_cv.html', cv_data=processed_data)

def parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m").date()
        except ValueError:
            return None

@app.route('/generate-pdf', methods=['POST'])
@login_required
def generate_pdf():
    # Find wkhtmltopdf path (common Windows locations)
    possible_paths = [
        r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe',
    ]
    wkhtmltopdf_path = None
    for path in possible_paths:
        if os.path.exists(path):
            wkhtmltopdf_path = path
            break
    if not wkhtmltopdf_path:
        try:
            import subprocess
            path = subprocess.check_output(['where', 'wkhtmltopdf'], shell=True).decode('utf-8').strip()
            if path and os.path.exists(path):
                wkhtmltopdf_path = path
        except:
            pass
    if not wkhtmltopdf_path:
        return """
            <h2>wkhtmltopdf not found</h2>
            <p>Please download and install wkhtmltopdf from: 
            <a href='https://wkhtmltopdf.org/downloads.html'>https://wkhtmltopdf.org/downloads.html</a></p>
            <p>After installation, restart this application.</p>
            <p><a href="/preview-cv" onclick="window.history.back(); return false;">Go back</a></p>
        """, 500

    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    data = request.form.to_dict(flat=False)
    processed_data = {}
    for key, value in data.items():
        if key.endswith('[]'):
            processed_data[key] = value
        else:
            processed_data[key] = value[0] if value else ""

    # --- Save CV to database ---
    from flask_login import current_user
    from app.models.user import db, CV, WorkExperience, Education, Style
    import shutil

    # Map template to style_id
    style_map = {'modern': 'Modern', 'classic': 'Classic', 'professional': 'Professional'}
    style_name = style_map.get(processed_data.get('template', 'modern').lower(), 'Modern')
    style = Style.query.filter_by(name=style_name).first()
    style_id = style.id if style else 1

    # Create CV entry
    cv = CV(
        owner_id=current_user.id,
        full_name=processed_data.get('fullName', ''),
        job_title=processed_data.get('jobTitle', ''),
        email=processed_data.get('email', ''),
        phone_number=processed_data.get('phone', ''),
        address=processed_data.get('address', ''),
        professional_summary=processed_data.get('summary', ''),
        skills=processed_data.get('skills', ''),
        style_id=style_id
    )
    db.session.add(cv)
    db.session.flush()  # Get cv.id before commit

    # Add work experiences
    work_titles = processed_data.get('workTitle[]', [])
    work_companies = processed_data.get('workCompany[]', [])
    work_start_dates = processed_data.get('workStartDate[]', [])
    work_end_dates = processed_data.get('workEndDate[]', [])
    work_descriptions = processed_data.get('workDescription[]', [])
    for i in range(len(work_titles)):
        we = WorkExperience(
            cv_id=cv.id,
            job_title=work_titles[i],
            company=work_companies[i] if i < len(work_companies) else '',
            start_date=parse_date(work_start_dates[i]) if i < len(work_start_dates) else None,
            end_date=parse_date(work_end_dates[i]) if i < len(work_end_dates) and work_end_dates[i] else None,
            is_current=1 if (i < len(work_end_dates) and not work_end_dates[i]) else 0,
            description=work_descriptions[i] if i < len(work_descriptions) else ''
        )
        db.session.add(we)

    # Add educations
    edu_degrees = processed_data.get('educationDegree[]', [])
    edu_institutions = processed_data.get('educationInstitution[]', [])
    edu_start_dates = processed_data.get('educationStartDate[]', [])
    edu_end_dates = processed_data.get('educationEndDate[]', [])
    edu_descriptions = processed_data.get('educationDescription[]', [])
    for i in range(len(edu_degrees)):
        edu = Education(
            cv_id=cv.id,
            degree_certificate=edu_degrees[i],
            institution=edu_institutions[i] if i < len(edu_institutions) else '',
            start_date=parse_date(edu_start_dates[i]) if i < len(edu_start_dates) else None,
            end_date=parse_date(edu_end_dates[i]) if i < len(edu_end_dates) and edu_end_dates[i] else None,
            is_current=1 if (i < len(edu_end_dates) and not edu_end_dates[i]) else 0,
            description=edu_descriptions[i] if i < len(edu_descriptions) else ''
        )
        db.session.add(edu)

    db.session.commit()

    # --- Generate PDF ---
    html = render_template('cv_template.html', cv_data=processed_data)
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
        f.write(html.encode('utf-8'))
        html_file_path = f.name

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
        pdf_data = pdfkit.from_file(html_file_path, False, options=options, configuration=config)
        os.unlink(html_file_path)
        # Save PDF to uploads/gen_cvs/cv_<id>.pdf
        gen_cvs_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'gen_cvs')
        os.makedirs(gen_cvs_dir, exist_ok=True)
        pdf_path = os.path.join(gen_cvs_dir, f"cv_{cv.id}.pdf")
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_data)
        filename = f"cv_{cv.id}.pdf"
        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename={filename}'
        return response
    except Exception as e:
        os.unlink(html_file_path)
        error_message = f"<h2>PDF generation failed:</h2>"
        error_message += f"<p>{str(e)}</p>"
        error_message += f"<p>The application looked for wkhtmltopdf at: {wkhtmltopdf_path}</p>"
        error_message += f"<p>If wkhtmltopdf is installed elsewhere, please check the path.</p>"
        error_message += f"<p>Download wkhtmltopdf from: <a href='https://wkhtmltopdf.org/downloads.html'>https://wkhtmltopdf.org/downloads.html</a></p>"
        error_message += f"<p><a href='#' onclick='window.history.back(); return false;'>Go back</a></p>"
        return error_message, 500

if __name__ == '__main__':
    app.run(debug=True)