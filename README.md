## Support Forum App

Welcome to the Support Forum App, a Django-based web application designed to facilitate discussions, questions, and assistance among users. This platform aims to provide a seamless experience for both administrators and users to engage in meaningful conversations and find solutions to their queries.

#### Features

- User Authentication
- Forums and Threads
- Search Functionality
- Installation
- Docker

To get started with the Support Forum App, follow these simple installation steps:

Clone the repository from GitHub:

```bash
git clone https://github.com/lebelokamogelo/support_forum.git
```

Navigate to the project directory:

```bash

cd support_forum
```

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Create a superuser account:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Access the application in your web browser at http://localhost:8000.

### Contributing

Contributions to the Support Forum App are welcomed and encouraged! If you'd like to contribute, please follow these steps:

- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Commit your changes and push to your fork.
- Submit a pull request detailing your changes.
