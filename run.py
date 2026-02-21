import json
import sys
import argparse

from netflix_analyzer.config import load_config
from netflix_analyzer.data_loader import load_data
from netflix_analyzer.analyzer import analyze_data
from netflix_analyzer.logger import get_logger
from netflix_analyzer.exception import ProjectException


def main():
    # CLI arguments
    parser = argparse.ArgumentParser(description="Netflix Data Analyzer")
    parser.add_argument("--config", type=str, required=True, help="Path to config.yaml")
    parser.add_argument("--input", type=str, required=True, help="Path to input CSV file")
    parser.add_argument("--output", type=str, required=True, help="Path to output JSON file")

    args = parser.parse_args()

    # Initialize logger
    logger = get_logger()
    logger.info("Application started.")

    try:
        # Load configuration
        logger.info("Loading configuration file...")
        config = load_config(args.config)

        min_year = config["data"]["min_year"]
        version = config["project"]["version"]

        logger.info(f"Configuration loaded successfully. Version: {version}")

        # Load data
        logger.info("Loading dataset...")
        df = load_data(args.input)
        logger.info(f"Dataset loaded successfully. Total rows: {len(df)}")

        # Analyze data
        logger.info("Starting analysis...")
        metrics = analyze_data(df, min_year)

        # Prepare final output
        output = {
            "version": version,
            "status": "success",
            **metrics
        }

        # Write JSON output
        with open(args.output, "w") as f:
            json.dump(output, f, indent=4)

        logger.info("Metrics successfully written to output file.")
        logger.info("Application completed successfully.")

        print(json.dumps(output, indent=4))

    except Exception as e:
        logger.error(str(e))

        error_output = {
            "status": "error",
            "message": str(e)
        }

        with open(args.output, "w") as f:
            json.dump(error_output, f, indent=4)

        sys.exit(1)


if __name__ == "__main__":
    main()