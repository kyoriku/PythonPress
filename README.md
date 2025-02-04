# PythonPress
*A full-stack web application built with Python and Flask that enables users to create, share, and interact with news content in a social platform format*

## Built With
[![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white)](https://flask.palletsprojects.com/en/3.0.x/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00.svg?style=for-the-badge&logo=SQLAlchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Jinja](https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white)](https://jinja.palletsprojects.com/en/3.1.x/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-499848.svg?style=for-the-badge&logo=Gunicorn&logoColor=white)](https://gunicorn.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![CSS](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

## Table of Contents
- [Description](#description)
  - [Deployed Site](#deployed-site)
- [Features](#features)
- [Screenshots](#screenshots)
- [Technical Details](#technical-details)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Questions](#questions)

## Description
PythonPress is a full-stack web application that demonstrates modern Python web development using Flask. This platform provides a dynamic environment where users can share, discuss, and interact with news content in a social format. Built with SQLAlchemy ORM and robust authentication practices, the application implements secure user management, RESTful API endpoints, and interactive features.

The application uses bcrypt for password security and Flask sessions for authentication, enabling users to post articles, engage in discussions through comments, and participate in content curation through upvoting. The database architecture uses SQLAlchemy relationships to manage user data, posts, comments, and votes efficiently, while custom Jinja filters help format dates, URLs, and text content.

### Deployed Site
Visit the live website at: [https://pythonpress-64ffcf772c54.herokuapp.com](https://pythonpress-64ffcf772c54.herokuapp.com)

## Features
* **User Authentication**
  * Secure registration with email validation
  * Password hashing using bcrypt
  * Flask session-based authentication
  * Protected routes via login_required decorator
  * Automatic login after registration

* **Content Management**
  * Create posts with titles and URLs
  * Edit and delete post functionality
  * Personal dashboard for post management
  * Post history tracking with timestamps
  * URL sanitization and formatting

* **Interactive Features**
  * Comment system with user attribution
  * Upvoting functionality with vote counting
  * Dynamic comment updates
  * Post sorting by creation date
  * User-specific content filtering

* **User Interface**
  * Clean and intuitive dashboard design
  * Real-time content updates
  * Responsive layout for all devices
  * Dynamic form validation feedback
  * Streamlined post creation and editing

## Screenshots
![Home](assets/screenshots/PythonPress-Home.jpg) 
![Post](assets/screenshots/PythonPress-Post.jpg) 
![Dashboard](assets/screenshots/PythonPress-Dashboard.jpg) 
![Edit](assets/screenshots/PythonPress-Edit.jpg) 

## Technical Details
This newsfeed platform was built using the following technologies and features:

* **Flask Framework**: Modular application structure:
   * Blueprint organization for home, dashboard, and API routes
   * Custom login_required decorator for route protection
   * Session-based user state management
   * Custom Jinja filters for data formatting
   * Static file serving configuration

* **Database Architecture**: SQLAlchemy implementation:
   * User Model: Username, email, and hashed password fields
   * Post Model: Title, URL, and vote count with relationships
   * Comment Model: Text content with user attribution
   * Vote Model: Many-to-many relationship handling
   * Cascading deletes for related data

* **Authentication System**: 
   * Bcrypt password hashing with salt
   * Email validation with @ verification
   * Minimum password length enforcement
   * Session-based login tracking
   * Protected route access control

* **API Implementation**: 
   * RESTful endpoints for CRUD operations
   * JSON response formatting
   * Error handling with status codes
   * Transaction management with rollbacks
   * Asynchronous JavaScript requests

* **Frontend Features**: 
   * Date formatting for post timestamps
   * URL sanitization for post links
   * Word pluralization handling
   * Form validation and error display
   * Dynamic content updates without reload

## Installation
### Prerequisites:
* Python 3.x
* pip (Python package installer)
* MySQL (or another SQL database)

### Setup:
1. **Clone the Repository**
   ```bash
   git clone https://github.com/kyoriku/PythonPress.git 
   ```

2. **Navigate to the project directory**
   ```bash
   cd PythonPress
   ```

3. **Set up a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # for macOS/Linux
   # or
   venv\Scripts\activate  # for Windows
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**

   Create a `.env` file in the root directory with:
   ```bash
   DB_URL=mysql+pymysql://<username>:<password>@localhost/python_press_db
   ```

   *Replace `<username>` with your MySQL username, and `<password>` with your MySQL password*

6. **Initialize the database**
   ```sql
   mysql -u root -p
   CREATE DATABASE python_press_db;
   ```

## Usage
1. **Start the application**
   ```bash
   flask run
   ```

2. **Navigate to the website**
   ```bash
   http://127.0.0.1:5000
   ```

3. **Create an account to:**
   * Share and manage your posts
   * Engage with content through comments
   * Upvote interesting articles
   * Access your personal dashboard

## Contributing
Contributions are welcome! Here are ways you can help:

1. Fork the repository
2. Create a feature branch
    ```bash
    git checkout -b feature/YourFeature
    ```
3. Make your changes - this could include:
    * Adding new features
    * Improving the UI/UX
    * Optimizing database queries
    * Enhancing security
    * Bug fixes
4. Commit your changes
5. Push to your branch
6. Open a Pull Request

Please ensure your contributions:
* Follow the existing code style
* Include appropriate error handling
* Test all changes locally
* Include clear descriptions in your pull request

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge&logo=mit)](https://opensource.org/licenses/MIT)

This project is licensed under the [MIT](https://opensource.org/licenses/MIT) license - see the LICENSE file for details.

## Questions
For any questions, feel free to email me at devkyoriku@gmail.com.