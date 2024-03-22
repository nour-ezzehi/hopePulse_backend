
# hopepulse
"Our website serves as a platform for campaign creators to initiate and manage fundraising campaigns aimed at addressing various causes and needs. These campaigns are showcased to potential donors who seek opportunities to contribute and make a positive impact. By connecting creators with donors, our platform facilitates meaningful collaborations and supports the realization of impactful initiatives."

## Features 🎞️

- User Registration 
- Profile Completion
- Campaign Creation if you are a campaign_creator
- Campaigns Viewing
- User Authentication
- Role-Based Access Control 


## Installation 🔧

### For the frontend:

1. **Clone the Repository**: Begin by cloning the frontend repository:

    ```bash
    git clone https://github.com/nour-ezzehi/hopePulse_frontend.git
    ```

2. **Install Frontend Packages**: Navigate to the cloned frontend directory and install the required packages using npm:

    ```bash
    cd hopePulse_frontend
    npm install
    ```

3. **Start the Frontend Development Server**: Once the packages are installed, start the frontend development server:

    ```bash
    npm run dev
    ```

    This command will compile the frontend code and start a development server. You can access the frontend application at the specified address (usually `http://localhost:3000`) in your web browser.

Now, your frontend development environment should be set up and ready for development.

### For the backend:

1. **Clone the Repository**: Start by cloning the backend repository:

    ```bash
    git clone https://github.com/nour-ezzehi/hopePulse_backend.git
    ```

2. **Create and Activate Virtual Environment**: Navigate to the project directory and create a virtual environment. Activate the virtual environment to isolate dependencies:

    ```bash
    cd hopePulse_backend
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    ```

3. **Install Dependencies**: Use pip, the Python package manager, to install the required packages:

    ```bash
    pip install django djangorestframework djangorestframework-simplejwt djoser psycopg2
    ```

    This command will install Django, Django Rest Framework, JWT Authentication, Djoser, and the PostgreSQL adapter psycopg2 along with their dependencies.

4. **Set Up PostgreSQL Database**: Ensure you have PostgreSQL installed on your system. Create a PostgreSQL database and configure the database settings in the `settings.py` file of your Django project.

5. **Apply Database Migrations**: Run the following command to apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. **Start the Backend Server**: Once the database is set up and migrations are applied, start the Django development server:

    ```bash
    python manage.py runserver
    ```

Now, your backend server should be up and running, ready to handle requests from the frontend.

## Technologies Used 📉
| Frontend           | Backend          |   
| ----------------- | ------------------------------------------------------------------ |
| [React.js]() | [Django]() |
| [React Router]() | [Django REST Framework]() |
| [Tailwind CSS]()| [PostgreSQL]() |
 [JWT Authentication]() | 	

## Authors
- [@Ezzehi Nour](https://github.com/nour-ezzehi);
