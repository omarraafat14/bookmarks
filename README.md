# Django Social Website Project

- This Django project lays the foundation for a social website, focusing on user account functionalities. 
- Users can register, manage passwords, edit profiles, and authenticate using traditional methods or social logins (Facebook, Twitter, Google). 
- Implements Advanced features like image sharing, interactions, and activity streams.

## Core Functionalities:

### User Accounts:
- User registration with email and password.
- Secure login and logout.
- Password reset functionality.
- Extended user profile with additional information (optional).
### Authentication:
- Built upon Django's built-in authentication framework.
- Custom authentication backend (optional, for advanced needs).
- Social authentication integration with Facebook, Twitter, and Google.
### Media Management:
- Configured for uploading profile pictures or other media files.
### Communication:
- Utilizing Django's messages framework for user feedback.


## Technical Features
This section provides a breakdown of the technical aspects involved:

### Authentication System:
- Login view creation.
- Django authentication framework integration.
- Password change and reset functionalities through templates.
- Custom authentication backend (optional).
### Social Authentication:
- Integration with Python Social Auth for social logins.
- Enabling authentication via Facebook, Twitter, and Google.
- Profile creation for users registering with social accounts.
### User Management:
- Extended user model with a custom profile model (optional).
- Preventing email address conflicts during registration.
### Advanced Features:
- Utilizing Django Extensions for development tools (optional).
- Secure server setup with HTTPS for user data protection.
- Custom form behavior configuration.
- JavaScript integration for interactive features.
- Building a bookmarklet for saving images directly from the web.
- Generating image thumbnails using easy-thumbnails library.
- Implementing asynchronous HTTP requests using JavaScript and Django.
- Implementing infinite scroll pagination for smooth content loading.
### Social Interaction Features:
- Creating many-to-many relationships for user follows and image bookmarks.
- Activity stream application to show user interactions and content.
- Generic relations for flexible model linking.
- Optimized QuerySets for efficient retrieval of related data.
- Using signals for denormalizing user data and improving performance.
### Performance Optimization:
- Django Debug Toolbar integration for debugging and performance analysis.
- Counting image views with Redis for efficient tracking.
- Creating a ranking of most viewed images using Redis.

## Getting Started

1. Prerequisites:
   - Python 3.x
   - Additional libraries for specific features (consult requirements.txt)
 2. Clone Repository:
    - `git clone https://github.com/omarraafat14/bookmarks.git`
3. Set Up Environment:
   - Install project dependencies: `pip install -r requirements.txt`
   - Configure database settings and optional social authentication credentials.
   - Run database migrations: python manage.py migrate
4. Run Development Server (HTTP):
   - `python manage.py runserver`
5. Explore the Project:
   - Start interacting with the authentication functionalities.



