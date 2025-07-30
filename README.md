# Movies Inventory Data Ingestion Project

This project is a simple movie inventory system built with Django. It demonstrates core data engineering skills such as data ingestion, transformation, and loading using Python scripts and common data formats (CSV, JSON).

## Features

- Django backend with a Movie model (title, year)
- ETL scripts for importing movie data from CSV and JSON files into the database

## Getting Started

### Prerequisites

- Python 3.x
- Django (install via `pip install django`)
- (Optional) Git

### Setup Instructions

1. **Clone or download this repository.**

2. **Install dependencies:**
    ```bash
    pip install django
    ```

3. **Apply migrations to set up the database:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Add your data file (`movies.csv` or `movies.json`) to the project root.**
    - Sample `movies.csv`:
      ```
      title,year
      The Shawshank Redemption,1994
      Inception,2010
      The Matrix,1999
      ```
    - Sample `movies.json`:
      ```json
      [
        {"title": "The Shawshank Redemption", "year": 1994},
        {"title": "Inception", "year": 2010},
        {"title": "The Matrix", "year": 1999}
      ]
      ```

5. **Run the ingestion script to load your data:**
    ```bash
    python ingest_movies.py
    ```
    - The script will automatically detect and load from `movies.csv` and/or `movies.json` if present.

6. **(Optional) Start the Django development server and view your movies:**
    ```bash
    python manage.py runserver
    ```
    - Visit `http://127.0.0.1:8000/movies/` (if you have a corresponding view/template).

7. **Verify imported movies:**
    - Use the Django admin interface or shell:
      ```bash
      python manage.py shell
      >>> from movies.models import Movie
      >>> print(Movie.objects.all())
      ```

## Project Structure

.
├── manage.py
├── ingest_movies.py
├── movies.csv / movies.json
├── week11/
│ └── settings.py, ...
└── movies/
└── models.py, views.py, ...

yaml
Copy
Edit

## Author

- Harry Le

---

*This project is for demonstration and learning purposes, focused on essential data engineering and backend skills using Python and Django.*
