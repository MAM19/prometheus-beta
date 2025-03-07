import os
import pytest
import pathlib
from datetime import datetime, timedelta
from src.file_creation_date import get_file_creation_date

def test_get_file_creation_date():
    # Create a temporary file for testing
    temp_file_path = 'tests/temp_test_file.txt'
    
    try:
        # Create a temporary file
        with open(temp_file_path, 'w') as f:
            f.write('Test content')
        
        # Get creation date
        creation_date = get_file_creation_date(temp_file_path)
        
        # Check it's a datetime object
        assert isinstance(creation_date, datetime)
        
        # Check creation date is recent (within last minute)
        assert datetime.now() - creation_date < timedelta(minutes=1)
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

def test_get_file_creation_date_pathlib():
    # Create a temporary file for testing
    temp_file_path = pathlib.Path('tests/temp_test_file_pathlib.txt')
    
    try:
        # Create a temporary file
        temp_file_path.write_text('Test content')
        
        # Get creation date using pathlib Path object
        creation_date = get_file_creation_date(temp_file_path)
        
        # Check it's a datetime object
        assert isinstance(creation_date, datetime)
        
        # Check creation date is recent (within last minute)
        assert datetime.now() - creation_date < timedelta(minutes=1)
    
    finally:
        # Clean up the temporary file
        if temp_file_path.exists():
            temp_file_path.unlink()

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('nonexistent_file.txt')

def test_invalid_input_type():
    with pytest.raises(TypeError):
        get_file_creation_date(123)  # Invalid input type

def test_permission_error(mocker):
    # Simulate a permission error
    mocker.patch('os.path.getctime', side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        get_file_creation_date('tests/test_file_creation_date.py')