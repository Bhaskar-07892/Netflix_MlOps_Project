import os 

folders = [
    "data",
    "src/netflix_analyzer"
]

files = [
    "src/netflix_analyzer/__init__.py",
    "src/netflix_analyzer/data_loader.py",
    "src/netflix_analyzer/analyzer.py",
    "src/netflix_analyzer/logger.py",
    "src/netflix_analyzer/exception.py",
    "src/netflix_analyzer/config.py",
    "run.py",
    "config.yaml",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "README.md"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Project structure created successfully!")