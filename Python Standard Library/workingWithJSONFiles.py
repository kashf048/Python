import json
from pathlib import Path

# movies = [
#     { "id": 1, "title": "Avatar: The Way of Water", "year": 2023 },
#     { "id": 2, "title": "Deva", "year": 2025 },
#     { "id": 3, "title": "Harry Potter", "year": 2015 }
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)

# Read
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
print(movies[0]["title"])