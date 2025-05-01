# ITI_CV_Maker

# Interactive Resume Builder
**IMPORTANT LINKS**
- [**📝Project Board**](https://github.com/users/itsmoe15/projects/4)
- [**🧑‍💻Project Repo**](https://github.com/itsmoe15/ITI_CV_Maker/)
- [**📄Project Report**](https://docs.google.com/document/d/1DDLFYgg_SS64KCy9mG_lxH58C5Mj8EhpeS-acUqeazM/edit?usp=sharing)



## Project Overview
A comprehensive web-based application that allows users to create professional resumes through multiple approaches:
- Step-by-step form-based builder
- AI-powered conversational resume creation
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
│   │   ├── chatbot.py       # Resume creation chatbot
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

### AI Chatbot Resume Creator
- Conversational interface for resume creation
- Natural language processing for information extraction
- Guided question flow for comprehensive resumes

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
- **TBD**

### Resume Management
- **TBD**

### AI Features
- **TBD**

## Database Schema

### Users
- **TBD**

### Resumes
- **TBD**

### Resume Versions
- **TBD**

## Testing
Run tests with pytest:
```bash
pytest
```

### Test Coverage
Generate coverage reports:
```bash
pytest --cov=backend
```

## Common Issues & Solutions
- **TBD**
  
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
- DBMS **TBD** (might be SQL or *Supabase*)

### Staging Environment
- **TBD**

### Production Environment
- **TBD**

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
