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
            # Only consider direct files in the exact directory, no subdirectories
            if entry.is_file() and entry.parent == dir_path:
                try:
                    file_size = entry.stat().st_size
                    
                    # Try to open the file to ensure it's actually readable
                    try:
                        with open(entry, 'rb') as f:
                            # Read entire file to verify complete readability
                            f.read()
                            
                            # Update largest file if size is larger and can be fully read
                            if file_size > largest_size and (largest_file is None or file_size > largest_size):
                                largest_file = str(entry.absolute())
                                largest_size = file_size
                    except (PermissionError, OSError):
                        # Skip unreadable files
                        continue
                except (PermissionError, OSError):
                    # Skip inaccessible files
                    continue
    except PermissionError:
        # If we can't list directory contents
        raise ValueError(f"Permission denied when accessing directory: {directory}")

    return largest_file