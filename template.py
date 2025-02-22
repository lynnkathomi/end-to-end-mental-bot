import os
from pathlib import Path
import logging

# Setup logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    force=True  # This ensures our logging configuration is used
)

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    
]

# Print current working directory
current_dir = os.getcwd()
logging.info(f"Current working directory: {current_dir}")

# Print all existing files and directories before creation
logging.info("Existing files and directories:")
for item in os.listdir(current_dir):
    logging.info(f"- {item}")

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    logging.info(f"\nProcessing: {filepath}")
    logging.info(f"Directory: {filedir}, File: {filename}")

    try:
        # Create the directory if it doesn't exist
        if filedir and not filedir.exists():
            filedir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {filedir}")

        # Create the file if it doesn't exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            filepath.touch()
            logging.info(f"Created file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")

    except Exception as e:
        logging.error(f"Error processing {filepath}: {str(e)}")

# Print all files and directories after creation
logging.info("\nFiles and directories after script execution:")
for item in os.listdir(current_dir):
    logging.info(f"- {item}")

logging.info("Script completed")