# Social Authentication with Google OAuth and Default Django Authentication System

This repository demonstrates how to implement social authentication using Google OAuth alongside Django's default authentication system. Social authentication allows users to sign in or sign up using their Google accounts, simplifying the registration process and enhancing user experience.

## Features

- Sign in with Google: Users can sign in to your Django application using their Google accounts.

- Sign up with Google: New users can create an account by signing up with their Google accounts.

- Associate Existing Accounts: Users can associate their Google accounts with their existing Django accounts.

- Enhanced User Experience: Social authentication streamlines the sign-up process and eliminates the need for users to remember additional passwords.

## Prerequisites

- Python 3.x

## Installation

1. Create and activate a virtual environment (Linux/MacOS/Windows):
   ```
   # Create virtual environment
   python -m venv venv

   # On Linux/MacOS:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

2. Clone the repository:
   ```
   git clone https://github.com/JoseMiracle/Social-Authentication.git
   cd Social-Authentication
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a Google OAuth application:
   - Go to the Google Developer Console: https://console.developers.google.com/
   - Create a new project and enable the Google+ API.
   - Go to "Credentials" and create OAuth 2.0 Client ID credentials.
   - Set the redirect URIs to `http://localhost:8000/accounts/google/login/callback/` and `http://yourdomain.com/accounts/google/login/callback/` (replace `yourdomain.com` with your actual domain).
   - Obtain the Client ID and Client Secret.
   -- In Django admin create/add a new Social application fill the Client ID and Client Secret fields with the obtained Client ID and Client Secret.

6. Pls create a file ".env" in thr root folder then add
   
   ```
   SECRET_KEY=*t61bk@qla68yzi1mr464eue963a%s40hwed@7dwijy-)_oyi0
   DEBUG=True
   ```


7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application in your web browser: `http://localhost:8000/`

## Usage

1. Click the "Sign In" or "Sign Up" button.

2. Choose "Sign in with Google" to sign in or create an account using your Google account.

3. After successful authentication, you will be redirected to the success page.

## Usage with Docker
   If you have Docker installed, you can quickly set up and run the application using Docker Compose:

1. Make sure you have Docker and Docker Compose installed.
2. Clone the repository:
   ```
   git clone https://github.com/JoseMiracle/Social-Authentication.git
   cd Social-Authentication  
   ```

3. Build and run the Docker containers
   ```
   docker-compose up
   ```
4. Access the application in your web browser: http://localhost:8000/


Make sure you have Docker and Docker Compose installed.

Clone the repository:
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to Skill Forge for giving me the task, I have been able to learn new things.
- Django: https://www.djangoproject.com/
- Django allauth: https://django-allauth.readthedocs.io/
- Google Developer Console: https://console.developers.google.com/
