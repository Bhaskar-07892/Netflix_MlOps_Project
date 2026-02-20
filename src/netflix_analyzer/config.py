import os
import yaml
from netflix_analyzer.exception import ProjectException
from netflix_analyzer.logger import get_logger


# Create logger instance
logger = get_logger()


def load_config(config_path: str) -> dict:
    """
    Load configuration from YAML file.
    """

    try:
        logger.info(f"Loading configuration from: {config_path}")

        # Check if file exists
        if not os.path.exists(config_path):
            logger.error("Configuration file not found.")
            raise FileNotFoundError(f"Config file not found: {config_path}")

        # Open and load YAML
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        # Check if YAML is empty
        if config is None:
            logger.error("Configuration file is empty.")
            raise ValueError("Config file is empty.")

        logger.info("Configuration loaded successfully.")
        return config

    except Exception as e:
        logger.error(f"Error while loading config: {str(e)}")
        raise ProjectException(str(e))