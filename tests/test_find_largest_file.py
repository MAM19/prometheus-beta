import os
import pytest
import tempfile
import pathlib

from src.find_largest_file import find_largest_file

def test_find_largest_file_basic():
    """Test finding the largest file in a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files with different sizes
        files = [
            ('small.txt', '10 bytes'),
            ('medium.txt', '100 bytes' * 10),
            ('large.txt', '1000 bytes' * 100)
        ]
        
        for filename, content in files:
            with open(os.path.join(tmpdir, filename), 'w') as f:
                f.write(content)
        
        largest_file = find_largest_file(tmpdir)
        assert largest_file.endswith('large.txt')

def test_find_largest_file_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        assert find_largest_file(tmpdir) is None

def test_find_largest_file_invalid_directory():
    """Test behavior with invalid directory inputs."""
    with pytest.raises(TypeError):
        find_largest_file(123)
    
    with pytest.raises(ValueError):
        find_largest_file('/nonexistent/path')

def test_find_largest_file_nested():
    """Test finding the largest file in a directory does not search subdirectories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create main directory and subdirectories
        os.makedirs(os.path.join(tmpdir, 'subdir1'))
        os.makedirs(os.path.join(tmpdir, 'subdir2'))
        
        # Create files of different sizes in different locations
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small file')
        
        with open(os.path.join(tmpdir, 'subdir1', 'medium.txt'), 'w') as f:
            f.write('medium file' * 10)
        
        # Expect None as no files are in root of directory
        largest_file = find_largest_file(tmpdir)
        assert largest_file is None

def test_find_largest_file_permissions(monkeypatch):
    """Test handling of files with different permission levels."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a file with large size but unreadable
        with open(os.path.join(tmpdir, 'protected.txt'), 'w') as f:
            f.write('large inaccessible file' * 1000)
        os.chmod(os.path.join(tmpdir, 'protected.txt'), 0o000)
        
        # Create a smaller, accessible file
        with open(os.path.join(tmpdir, 'normal.txt'), 'w') as f:
            f.write('normal file' * 10)
        
        try:
            largest_file = find_largest_file(tmpdir)
            assert largest_file is None
        finally:
            # Restore permissions for cleanup
            os.chmod(os.path.join(tmpdir, 'protected.txt'), 0o666)