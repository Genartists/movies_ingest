
import os
import django
import csv
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'week11.settings')
django.setup()

from movies.models import Movie

def ingest_movies_from_csv(csv_path):
    """
    Ingest movies from a CSV file into the Django database.
    CSV format: title,year
    """
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['title'].strip()
            year = int(row['year'])
            Movie.objects.update_or_create(title=title, year=year)
    print(f"Loaded movies from {csv_path}")

def ingest_movies_from_json(json_path):
    """
    Ingest movies from a JSON file into the Django database.
    JSON format: [{"title": "...", "year": ...}, ...]
    """
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)
        for movie in data:
            title = movie['title'].strip()
            year = int(movie['year'])
            Movie.objects.update_or_create(title=title, year=year)
    print(f"Loaded movies from {json_path}")

if __name__ == "__main__":
    # Example usage
    csv_file = 'movies.csv'
    json_file = 'movies.json'
    if os.path.exists(csv_file):
        ingest_movies_from_csv(csv_file)
    if os.path.exists(json_file):
        ingest_movies_from_json(json_file)
