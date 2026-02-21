# 🎬 Netflix Data Analyzer – Mini MLOps Project

A modular, configuration-driven Netflix dataset analysis pipeline built using Python.  
This project demonstrates MLOps-style architecture including structured logging, custom exception handling, CLI execution, and JSON metrics output.

---

## 🚀 Project Overview

This project performs analysis on the Netflix Movies and TV Shows dataset.

It:

- Loads configuration from a YAML file
- Reads a CSV dataset
- Filters data based on release year
- Computes key metrics
- Generates structured JSON output
- Logs complete execution flow
- Handles errors with detailed file and line information

---
## 📂 Project Structure

```bash
netflix-mlops-project/
├── config.yaml
├── run.py
├── requirements.txt
├── setup.py
├── README.md
├── .gitignore
├── metrics.json
├── logs/
├── data/
│   └── netflix_titles.csv
└── src/
    └── netflix_analyzer/
        ├── __init__.py
        ├── config.py
        ├── data_loader.py
        ├── analyzer.py
        ├── logger.py
        └── exception.py 
```


---

## 📊 Dataset

Dataset sourced from Kaggle:

Netflix Movies and TV Shows  
https://www.kaggle.com/datasets/shivamb/netflix-shows


---

## ⚙️ Configuration (config.yaml)

Example:

```yaml
project:
  version: "v1"

data:
  min_year: 2000