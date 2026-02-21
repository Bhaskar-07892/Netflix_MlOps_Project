import pandas as pd
from netflix_analyzer.exception import ProjectException
from netflix_analyzer.logger import get_logger


def analyze_data(df: pd.DataFrame, min_year: int) -> dict:
    """
    Analyze Netflix dataset and return summary metrics.
    """

    logger = get_logger()
    logger.info("Starting data analysis...")

    try:
        # Filter by release year
        logger.info(f"Filtering data with min_year >= {min_year}")
        df_filtered = df[df["release_year"] >= min_year]

        if df_filtered.empty:
            logger.error("No data available after applying year filter.")
            raise ProjectException("No data available after applying min_year filter.")

        logger.info(f"Rows after filtering: {len(df_filtered)}")

        # Count totals
        total_titles = len(df_filtered)
        total_movies = len(df_filtered[df_filtered["type"] == "Movie"])
        total_tv_shows = len(df_filtered[df_filtered["type"] == "TV Show"])

        logger.info("Calculated total titles, movies, and TV shows.")

        # Most common genre
        most_common_genre = (
            df_filtered["listed_in"]
            .dropna()
            .str.split(", ")
            .explode()
            .mode()[0]
        )

        logger.info(f"Most common genre identified: {most_common_genre}")

        # Average release year
        average_release_year = int(df_filtered["release_year"].mean())
        logger.info(f"Average release year calculated: {average_release_year}")

        logger.info("Data analysis completed successfully.")

        return {
            "total_titles": total_titles,
            "total_movies": total_movies,
            "total_tv_shows": total_tv_shows,
            "most_common_genre": most_common_genre,
            "average_release_year": average_release_year,
        }

    except KeyError as e:
        logger.error(f"Missing required column: {str(e)}")
        raise ProjectException(f"Missing required column: {str(e)}")

    except Exception as e:
        logger.error(str(e))
        raise ProjectException(str(e))