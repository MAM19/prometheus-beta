import os
import pathlib

def find_largest_file(directory):
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        str: Absolute path to the largest file, or None if directory is empty or invalid.

    Raises:
        TypeError: If directory is not a string.
        ValueError: If directory path is invalid or not a directory.
    """
    # Validate input
    if not isinstance(directory, str):
        raise TypeError("Directory must be a string")

    # Convert to absolute path and validate
    try:
        dir_path = pathlib.Path(directory).resolve()
    except Exception:
        raise ValueError(f"Invalid directory path: {directory}")

    # Check if path exists and is a directory
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {directory}")

    # Find largest file
    largest_file = None
    largest_size = -1

    try:
        for entry in dir_path.iterdir():
            # Skip directories, only consider files
            if entry.is_file():
                try:
                    file_size = entry.stat().st_size
                    if file_size > largest_size:
                        largest_file = str(entry.absolute())
                        largest_size = file_size
                except (PermissionError, OSError):
                    # Skip files that can't be accessed
                    continue
    except PermissionError:
        # If we can't list directory contents
        raise ValueError(f"Permission denied when accessing directory: {directory}")

    return largest_file