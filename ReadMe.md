
# Flask Covoiturage App

This is a Flask-based application that allows users to manage **covoiturages**. Users can register, log in, add new covoiturages, view details, and delete existing ones.

## Features

- User authentication (Sign Up, Login, Logout).
- Add covoiturages (departure location, destination, date, available seats).
- View all covoiturages.
- View details of specific covoiturages.
- Delete covoiturages.

## Requirements

- Python 3.8+
- Virtual environment (optional but recommended)

## Setup and Installation

1. Clone the Repository
    ```bash
    git clone https://github.com/Montahe-dridi/Web_services_project.git
    cd flask_covoiturage_app
    ```

2. Create and Activate Virtual Environment

    **On Linux/macOS**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **On Windows**:
    ```bash
    python -m venv venv
    venv\Scriptsctivate
    ```

3. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set Environment Variables

    **On Linux/macOS**:
    ```bash
    export FLASK_APP=project:create_app
    export FLASK_ENV=development
    ```

    **On Windows**:
    ```bash
    set FLASK_APP=project:create_app
    set FLASK_ENV=development
    ```

5. Initialize the Database
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. Run the Application
    ```bash
    flask run
    ```

## Application Usage

- Visit the app in your browser: `http://127.0.0.1:5000/`
- Use the navigation bar to access various features:
    - Home
    - Add Covoiturage
    - View All Covoiturages
    - Profile

## File Structure

```
flask_covoiturage_app/
│
├── project/
│   ├── init.py              # Application factory
│   ├── models.py            # Database models
│   ├── auth.py              # Authentication routes
│   ├── main.py              # Main application routes
│   ├── templates/           # HTML templates
│   └── static/              # Static files (CSS, JS, images)
│
├── migrations/              # Database migration files
├── requirements.txt         # Python dependencies
├── README.md                # Documentation
└── run.py                   # Entry point (optional)
```

## Example Routes

- **Add a New Covoiturage**
    - Route: `/add_covoiturage`
    - Methods: GET, POST

- **View All Covoiturages**
    - Route: `/covoiturages`
    - Method: GET

- **Delete a Covoiturage**
    - Route: `/delete_covoiturage/<int:id>`
    - Method: POST

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any bugs or feature requests.

## License

This project is licensed under the MIT License.
