import os
import pytest
import shutil
from src.file_rename import rename_file

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    test_file = tmp_path / "original_file.txt"
    test_file.write_text("Test content")
    return test_file

def test_rename_file_same_directory(temp_file, tmp_path):
    """Test renaming a file within the same directory."""
    original_path = str(temp_file)
    new_path = str(tmp_path / "renamed_file.txt")
    
    result = rename_file(original_path, new_path)
    
    assert result == new_path
    assert os.path.exists(new_path)
    assert not os.path.exists(original_path)

def test_rename_file_different_directory(temp_file, tmp_path):
    """Test moving a file to a different directory."""
    original_path = str(temp_file)
    new_dir = tmp_path / "new_directory"
    new_dir.mkdir()
    new_path = str(new_dir / "moved_file.txt")
    
    result = rename_file(original_path, new_path)
    
    assert result == new_path
    assert os.path.exists(new_path)
    assert not os.path.exists(original_path)

def test_rename_file_nonexistent_source(tmp_path):
    """Test renaming a file that doesn't exist."""
    nonexistent_path = str(tmp_path / "nonexistent.txt")
    new_path = str(tmp_path / "new_file.txt")
    
    with pytest.raises(FileNotFoundError):
        rename_file(nonexistent_path, new_path)

def test_rename_file_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        rename_file(123, "path/to/file")
    with pytest.raises(TypeError):
        rename_file("path/to/file", 456)

def test_rename_file_directory_as_source(tmp_path):
    """Test attempting to rename a directory instead of a file."""
    test_dir = tmp_path / "test_directory"
    test_dir.mkdir()
    
    with pytest.raises(IsADirectoryError):
        rename_file(str(test_dir), str(tmp_path / "new_name"))