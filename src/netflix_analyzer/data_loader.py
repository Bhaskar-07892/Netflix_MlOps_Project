import os
import pandas as pd
from netflix_analyzer.exception import ProjectException


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV data file and return pandas DataFrame.
    """

    # Check if file exists
    if not os.path.exists(file_path):
        raise ProjectException(f"Data file not found at: {file_path}")

    try:
        # Read CSV file
        df = pd.read_csv(file_path)

        # Check if file is empty
        if df.empty:
            raise ProjectException("Input data file is empty.")

        return df

    except pd.errors.EmptyDataError:
        raise ProjectException("CSV file is empty or invalid format.")

    except Exception as e:
        raise ProjectException(str(e))