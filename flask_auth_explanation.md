Flask Authentication System Explanation
=====================================

1. Required Packages
-------------------
- Flask-Login: Handles user session management
- Flask-SQLAlchemy: Database ORM for user storage
- Werkzeug: Provides password hashing utilities

2. User Model Setup
------------------
The User model inherits from UserMixin (Flask-Login) and db.Model (SQLAlchemy):
```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
```

3. Authentication Flow
---------------------
a) Registration:
   - User submits username and password
   - Password is hashed using Werkzeug's generate_password_hash()
   - New user is created and stored in database
   - User is redirected to login page

b) Login:
   - User submits credentials
   - System checks if user exists
   - Password is verified using check_password_hash()
   - If valid, user is logged in using login_user()
   - Session is created and user is redirected

c) Protected Routes:
   - @login_required decorator ensures only authenticated users can access
   - Unauthorized users are redirected to login page
   - Current user is available via current_user

4. Key Components
----------------
a) Login Manager:
```python
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect unauthorized users here
```

b) User Loader:
```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

c) Password Hashing:
```python
# Hashing password during registration
hashed_password = generate_password_hash(password)

# Verifying password during login
check_password_hash(user.password, password)
```

5. Session Management
--------------------
- Flask-Login handles session creation and management
- Sessions are stored in cookies
- User remains logged in until:
  * They explicitly logout
  * Session expires
  * Browser cookies are cleared

6. Security Features
-------------------
- Passwords are never stored in plain text
- Session cookies are signed
- CSRF protection (if using Flask-WTF)
- Secure password hashing with Werkzeug

7. Common Routes
---------------
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login logic

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Handle registration logic

@app.route('/logout')
@login_required
def logout():
    # Handle logout logic
```

8. Best Practices
----------------
- Always use HTTPS in production
- Implement password complexity requirements
- Add rate limiting for login attempts
- Use secure session configuration
- Implement password reset functionality
- Add email verification if needed

9. Example Usage
---------------
```python
# Protecting a route
@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome {current_user.username}!'

# Checking if user is authenticated
if current_user.is_authenticated:
    # Do something for logged-in users
```

10. Common Issues & Solutions
---------------------------
- Session not persisting: Check SECRET_KEY configuration
- Login redirect loop: Verify login_view setting
- Password verification failing: Ensure consistent hashing method
- User not found: Check database connection and user loader

Remember:
--------
- Never store plain text passwords
- Always use HTTPS in production
- Implement proper error handling
- Add logging for security events
- Keep dependencies updated
- Follow security best practices 