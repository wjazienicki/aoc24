# utils/input_handler.py
from pathlib import Path

def no_linebreaks(file_path):
    base_dir = Path(__file__).resolve().parent.parent  # Navigate up to the project root
    full_path = base_dir / file_path  # Append the relative file path

    with open(full_path, 'r') as file:
        content = file.read().replace("\n", "")
        return content
    
def readlines(file_path):
    base_dir = Path(__file__).resolve().parent.parent  # Navigate up to the project root
    full_path = base_dir / file_path  # Append the relative file path
    with open(full_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        return lines