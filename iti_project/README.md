# CV Builder

A web-based tool that lets users create professional CVs/resumes step-by-step and export them as PDFs.

## Features

- Easy-to-use CV creation interface
- Multiple professional templates
- Dynamic work experience and education sections
- Export to PDF functionality
- Responsive design for mobile and desktop

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
  - Bootstrap 5 for styling
  - FontAwesome for icons
- **Backend**: Flask (Python)
  - WeasyPrint for HTML to PDF conversion

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd cv-builder
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
python app.py
```

4. Visit `http://127.0.0.1:5000` in your browser to use the application.

## Usage

1. Click "Create Your CV Now" on the homepage
2. Fill in your personal information, work experience, education, and skills
3. Choose a template design
4. Preview your CV
5. Generate a PDF to download

## Project Structure

```
cv-builder/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/                 # Static files
│   ├── css/                # CSS stylesheets
│   ├── js/                 # JavaScript files
│   └── img/                # Images
└── templates/              # HTML templates
    ├── index.html          # Homepage
    ├── create_cv.html      # CV creation form
    ├── preview_cv.html     # CV preview
    ├── cv_template.html    # Template for PDF generation
    └── cv_templates/       # Template variations
        ├── modern_preview.html
        ├── classic_preview.html
        └── professional_preview.html
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Bootstrap CSS Framework
- Font Awesome Icons
- WeasyPrint HTML to PDF converter 