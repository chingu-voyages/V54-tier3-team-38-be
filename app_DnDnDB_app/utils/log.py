import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more details
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Logs to a file
        logging.StreamHandler()  # Logs to the console
    ]
)

# Create a logger
logger = logging.getLogger(__name__)

# Example usage
logger.info("Logging is set up!")
