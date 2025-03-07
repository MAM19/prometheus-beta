import os
import pathlib
from datetime import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file.

    Args:
        file_path (str or pathlib.Path): Path to the file.

    Returns:
        datetime: The creation time of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
        TypeError: If the file_path is not a string or Path object.
    """
    # Convert to Path object if it's a string
    if isinstance(file_path, str):
        file_path = pathlib.Path(file_path)
    
    # Validate input
    if not isinstance(file_path, pathlib.Path):
        raise TypeError("file_path must be a string or pathlib.Path object")
    
    # Check file exists
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Get creation time 
    try:
        # Use os.path.getctime for cross-platform creation time retrieval
        creation_timestamp = os.path.getctime(str(file_path))
        return datetime.fromtimestamp(creation_timestamp)
    except PermissionError:
        raise PermissionError(f"No permission to access file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error getting file creation date: {e}")