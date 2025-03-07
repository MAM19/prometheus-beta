import os
import shutil

def rename_file(source_path, destination_path):
    """
    Rename or move a file from source path to destination path.

    Args:
        source_path (str): The current path of the file.
        destination_path (str): The new path for the file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to rename/move the file.
        IsADirectoryError: If the source path is a directory instead of a file.
        OSError: For other OS-related errors during file renaming.

    Returns:
        str: The new path of the file after renaming/moving.
    """
    # Validate input paths
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Paths must be strings")
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Ensure source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory, not a file: {source_path}")
    
    # Ensure destination directory exists
    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    try:
        # Rename/move the file
        shutil.move(source_path, destination_path)
        return destination_path
    except PermissionError:
        raise PermissionError(f"Permission denied when renaming file from {source_path} to {destination_path}")
    except OSError as e:
        raise OSError(f"Error renaming file: {e}")