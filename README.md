# Django Project

This is a Django project containing several applications.

## Project Structure

The project consists of the following Django apps:

*   **hello**: A basic application for greetings.
*   **newyear**: An application related to New Year functionality.
*   **tasks**: An application for task management.
*   **flights**: An airline management system. It handles Airports, Flights, and Passengers, allowing users to view flight details and book passengers.
*   **users**: Handles user authentication, providing login and logout functionality for the project.

## Getting Started

### Prerequisites

*   Python 3.10+
*   Django

### Installation

1.  Clone the repository.
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  Install the dependencies:
    ```bash
    pip install django
    # If you have other dependencies, install them here or via requirements.txt
    ```

### Running the Development Server

To start the server, run:

   ```bash
   python manage.py runserver
   ```