Newspaper Project

 Overview

The Newspaper Project is a web application where individuals can create, post, edit, and delete articles. The application includes user authentication features such as login, sign-up, password reset via SMTP, and uses PostgreSQL as the database. This project demonstrates a full-stack implementation using Django.

Features

- User Authentication:**
  - User Registration
  - User Login
  - Password Reset (via SMTP)
  - User Logout

Article Management:
  - Create Articles
  - Edit Articles
  - Delete Articles
  - View Articles

Tech Stack

- Backend: Django
- Frontend: Django Templates
- Database:PostgreSQL
  Email Service:SMTP
- Authentication: Django Allauth

  
 Installation

Prerequisites

- Python 3.8+
- PostgreSQL
- Virtual Environment (virtualenv)

 Setup

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/newspaper_project.git
   cd newspaper_project
   ```

2. Create and Activate Virtual Environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL:
   - Create a PostgreSQL database and user.
   - Update `settings.py` with your database credentials.
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. Run Migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a Superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Configure SMTP for Password Reset:
   - Update `settings.py` with your SMTP credentials.
     ```python
     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
     EMAIL_HOST = 'smtp.your-email-provider.com'
     EMAIL_PORT = 587
     EMAIL_USE_TLS = True
     EMAIL_HOST_USER = 'your_email@example.com'
     EMAIL_HOST_PASSWORD = 'your_email_password'
     ```

8. Run the Development Server:
   ```bash
   python manage.py runserver
   ```

 Usage

1. Home Page:
   - View a list of published articles.

2. User Registration:
   - Sign up for a new account.

3. User Login:
   - Log in with your credentials.

4. Password Reset:
   - Request a password reset link via email.

5. Article Management:
   - Create, edit, and delete articles.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Contact

For any inquiries or support, please reach out to:

- Adusei Kwadwo Yeboah
- aduseikay8096@gmail.com

