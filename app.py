from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, send_from_directory
from flask_login import LoginManager, login_user, login_required, logout_user
import bcrypt
import os
from werkzeug.utils import secure_filename
import base64

from app import create_app
from app.models.user import db, User
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
    return render_template('home.html')

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
        
        # Do NOT delete the file!
        # os.remove(filepath)
        
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
    return render_template('my_cvs.html')

if __name__ == '__main__':
    app.run(debug=False)