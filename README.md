# ITI_CV_Maker

---

## 👥 Team Members

|  **ID** |      **Name**      |                      **Github**                     |
|:-------:|:------------------:|:---------------------------------------------------:|
| 4231096 |  Mohammed Montaser |       [itsmoe15](https://github.com/itsmoe15)       |
| 4231094 | Ebtesam Abdelnaser | [EbtesamElnaser](https://github.com/EbtesamElnaser) |
| 4231091 | Esraa Salah        |       [Esraa905](https://github.com/Esraa905)       |
| 4231134 | Mohammed Osama     | [Mohamedoosamaa](https://github.com/mohamedoosamaa) |

---

# Interactive Resume Builder

## About the Project

**ITI_CV_Maker** is a comprehensive, web-based platform designed to empower users to create professional, modern, and ATS-friendly resumes with ease. Built as a graduation project for the ITI program, our goal was to bridge the gap between job seekers and the ever-evolving requirements of modern recruitment systems. We wanted to make resume creation accessible, interactive, and intelligent—helping users not only build but also optimize their CVs for real-world job applications.

### Why We Built This
- **Real-World Need:** Many job seekers struggle with resume formatting, keyword optimization, and keeping up with Applicant Tracking Systems (ATS). We wanted to solve these pain points with a user-friendly, intelligent tool.
- **Learning & Innovation:** This project was an opportunity for our team to apply and expand our skills in full-stack development, AI/NLP, and UI/UX design, while working collaboratively in a real-world software engineering workflow.
- **Team Collaboration:** We followed industry best practices—using GitHub for version control, feature branching, code reviews, and CI/CD pipelines—to simulate a professional development environment.

### What Makes ITI_CV_Maker Unique?
- **Step-by-Step Builder:** A guided, multi-step form helps users craft each section of their resume, with auto-save and live preview.
- **ATS Optimization:** Integrated AI modules analyze resumes for ATS compatibility, providing actionable feedback and keyword suggestions.
- **Multiple Templates:** Users can choose from a variety of professional templates and customize them to fit their personal style.
- **PDF Export:** High-quality PDF generation ensures resumes look great both digitally and in print.
- **Multi-Resume Management:** Save, clone, and manage multiple versions of your resume for different job applications.
- **Modern Tech Stack:** Built with Flask, Vanilla JS, and modern CSS, with a focus on scalability and maintainability.

---

**IMPORTANT LINKS**
- [**📝Project Board**](https://github.com/users/itsmoe15/projects/4)
- [**🧑‍💻Project Repo**](https://github.com/itsmoe15/ITI_CV_Maker/)
- [**📄Project Report**](https://docs.google.com/document/d/1DDLFYgg_SS64KCy9mG_lxH58C5Mj8EhpeS-acUqeazM/edit?usp=sharing)

---

## Project Overview
A comprehensive web-based application that allows users to create professional resumes through multiple approaches:
- Step-by-step form-based builder
- ATS resume optimization and checking

This development repository contains all code, documentation, and resources for the Interactive Resume Builder project.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Flask-Login
- **PDF Generation**: WeasyPrint
- **AI Integration**: Custom NLP models

## Project Structure
```
resume-builder/
├── backend/
│   ├── app.py               # Main Flask application
│   ├── config.py            # Configuration settings
│   ├── models/              # Database models
│   ├── routes/              # API endpoints
│   ├── services/            # Business logic
│   ├── ai/                  # AI modules
│   │   └── ats_checker.py   # ATS compatibility analyzer
│   └── utils/               # Helper functions
├── frontend/
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   ├── templates/           # HTML templates
│   ├── assets/              # Images, icons, etc.
│   └── resume-templates/    # Resume template designs
├── tests/                   # Test cases
│   ├── unit/                # Unit tests
│   └── integration/         # Integration tests
├── docs/                    # Documentation
│   ├── api/                 # API documentation
│   └── development/         # Development guides
├── .env.example             # Environment variables template
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Setup Instructions

### Prerequisites
- Python 3.10+
- Git

### Initial Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/itsmoe15/ITI_CV_Maker
   cd ITI_CV_Maker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


4. Run the development server:
   ```bash
   flask run --debug
   ```

5. Access the application at http://localhost:5000

## Development Workflow

### Branching Strategy
- `main`: Production-ready code [^1]
- `backend/*`: Backend code [^2]
- `frontend/*`: Backend code [^3]  
[^1] **Note**: The `main` branch should only contain production-ready code. All development should occur in feature branches.  
[^2] **Note**: The `backend` branch should only contain backend code. you must create branches for each feature to be developed.  
[^3] **Note**: The `frontend` branch should only contain frontend code.  you must create branches for each feature to be developed

### Commit Messages
Follow conventional commits format:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or modifying tests
- `chore:` Maintenance tasks

### Pull Request Process
1. Create a feature branch from `develop`
2. Implement changes and test locally
3. Push branch and create a PR to `develop`
4. Ensure CI passes and request review
5. Address review comments
6. Merge when approved

## Key Features & Implementation Details

### Authentication System
- User registration, login, password reset
- Session management
- Profile settings

### Resume Builder
- Multi-step form interface
- Auto-save functionality
- Section management (education, experience, skills, etc.)

### Resume Templates
- Multiple professional templates
- Customization options (colors, fonts, spacing)
- Live preview functionality

### PDF Export
- High-quality PDF generation
- Custom paper sizes and orientations
- Proper formatting preservation

### ATS Resume Checker
- Resume scoring against ATS algorithms
- Keyword analysis and suggestions
- Formatting and content recommendations
- Job description matching

### Multi-Resume Management
- Save multiple resume versions
- Version history
- Clone and modification capabilities

## API Endpoints

### Authentication
- `POST /login` — User login
- `POST /register` — User registration
- `GET /logout` — User logout

### Resume Management
- `GET /cv-maker` — Resume builder form
- `GET /my-cvs` — List user resumes
- `GET /download-cv/<cv_id>` — Download generated PDF
- `POST /preview-cv` — Preview resume
- `POST /generate-pdf` — Generate PDF from resume

### AI Features
- `GET /ats-checker` — ATS checker page
- `POST /check-ats` — Analyze resume for ATS compatibility

## Database Schema

### Users
- `id` (int, primary key)
- `username` (string, unique, required)
- `password` (string, required)

### Styles
- `id` (int, primary key)
- `name` (string, unique, required)

### CVs
- `id` (int, primary key)
- `owner_id` (int, foreign key to user)
- `full_name`, `job_title`, `email`, `phone_number` (string, required)
- `address`, `professional_summary`, `skills` (string/text)
- `style_id` (int, foreign key to style)

### Work Experience
- `id` (int, primary key)
- `cv_id` (int, foreign key to cv)
- `job_title`, `company` (string, required)
- `start_date`, `end_date` (date)
- `is_current` (bool)
- `description` (text)

### Education
- `id` (int, primary key)
- `cv_id` (int, foreign key to cv)
- `degree_certificate`, `institution` (string, required)
- `start_date`, `end_date` (date)
- `is_current` (bool)
- `description` (text)

## Testing

*Test cases are planned but not yet implemented in this repository.*

## Common Issues & Solutions

### Database Migrations
If you encounter migration issues:
```bash
flask db stamp head
flask db migrate
flask db upgrade
```

### PDF Generation
If PDF export fails, ensure WeasyPrint dependencies are installed:
- On Ubuntu/Debian: `apt-get install libcairo2-dev libpango1.0-dev libgdk-pixbuf2.0-dev libffi-dev shared-mime-info`
- On macOS: `brew install cairo pango gdk-pixbuf libffi`

## Deployment

### Development Environment
- Local Flask development server
- SQLite database (default, see `app/config/config.py`)

### Production Environment
- Deployable to any WSGI-compatible server (e.g., Gunicorn, uWSGI)
- Database can be upgraded to PostgreSQL with SQLAlchemy
- Environment variables for secrets and DB URI recommended

## Project Timeline
- **May 1-2**: Project Setup & Infrastructure
- **May 1-3**: User Authentication System
- **May 2-5**: Resume Builder Core UI
- **May 3-6**: Resume Templates & Styling
- **May 5-7**: Resume Export Functionality
- **May 6-10**: AI Chatbot Resume Creator
- **May 8-12**: ATS Resume Checker
- **May 10-13**: Multi-Resume Management
- **May 13-15**: Testing & Bug Fixing
- **May 14-15**: Documentation & Deployment

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [WeasyPrint Documentation](https://weasyprint.readthedocs.io/)
- [ATS Research Paper](https://github.com/srbhr/Resume-Matcher)
- [Resume Best Practices](https://resumegenius.com/blog/resume-help/resume-format)

## License
This project is proprietary and confidential. dont share it.
