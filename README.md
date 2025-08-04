# CRM Django Project

This is a Customer Relationship Management (CRM) system built with Django.

Live Demo
Access the live application here: https://alinist.pythonanywhere.com/home/

## Features

- **User Authentication**
    - User registration (sign-up)
    - User login and logout
    - Authentication required for dashboard and record management
        
- **Record Management**
    - Add new customer records
    - View details of individual records
    - Edit existing records
    - Delete records with confirmation and notifications
        
- **Dashboard**
    - Overview of all customer records displayed in a centralized dashboard
    - Records displayed with pagination and sorting (if implemented)
        
- **Search Functionality**
    - Search records by first name and/or last name with flexible matching
    - Supports searching by single or multiple terms
        
- **Notifications and Messages**
    - Informative feedback to users on actions (success, error, warnings) using Django messages framework

- **User Interface**    
    - Responsive and styled UI with Bootstrap and custom theme
    - Clear forms for registration, login, and record CRUD operations
    - Consistent layout with header, footer, and navigation components

## Setup & Installation

1. Clone the repository:  
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:  
    On Linux/macOS:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    On Windows (PowerShell):
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
    Or on Windows (cmd):
    ```cmd
    python -m venv venv
    venv\Scripts\activate.bat
    ```

3. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:  
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin):  
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:  
    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` in your browser.
