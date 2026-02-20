import logging
import os
from datetime import datetime


def get_logger(log_dir: str = "logs", level: int = logging.INFO) -> logging.Logger:
    """
    Create and return a configured logger instance.
    """

    os.makedirs(log_dir, exist_ok=True)

    log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    log_file_path = os.path.join(log_dir, log_file)

    logger = logging.getLogger("netflix_analyzer")
    logger.setLevel(level)

    # Prevent duplicate handlers
    if not logger.handlers:

        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter(
            "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger