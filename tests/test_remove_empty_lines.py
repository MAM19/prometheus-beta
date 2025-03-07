import os
import pytest
from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_standard_case(tmp_path):
    # Create a test file with some empty lines
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("Line 1\n\nLine 2\n   \nLine 3\n")
    
    # Call the function
    removed_count = remove_empty_lines(str(test_file))
    
    # Check file contents and return value
    assert removed_count == 2
    assert test_file.read_text() == "Line 1\nLine 2\nLine 3\n"

def test_remove_empty_lines_output_file(tmp_path):
    # Create input and output file paths
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    
    # Write test input
    input_file.write_text("Hello\n\nWorld\n\n")
    
    # Call function with separate output file
    removed_count = remove_empty_lines(str(input_file), str(output_file))
    
    # Check results
    assert removed_count == 2
    assert output_file.read_text() == "Hello\nWorld\n"
    assert input_file.read_text() == "Hello\n\nWorld\n\n"  # Original file unchanged

def test_remove_empty_lines_all_empty(tmp_path):
    # Create a file with only empty lines
    test_file = tmp_path / "empty.txt"
    test_file.write_text("\n   \n\n")
    
    # Call the function
    removed_count = remove_empty_lines(str(test_file))
    
    # Check file is now empty
    assert removed_count == 3
    assert test_file.read_text() == ""

def test_remove_empty_lines_no_empty(tmp_path):
    # Create a file with no empty lines
    test_file = tmp_path / "full.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3")
    
    # Call the function
    removed_count = remove_empty_lines(str(test_file))
    
    # Check file unchanged
    assert removed_count == 0
    assert test_file.read_text() == "Line 1\nLine 2\nLine 3"

def test_remove_empty_lines_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        remove_empty_lines(123)
    
    with pytest.raises(TypeError):
        remove_empty_lines("valid_file", 456)

def test_remove_empty_lines_file_not_found(tmp_path):
    # Test non-existent file
    non_existent_file = tmp_path / "does_not_exist.txt"
    
    with pytest.raises(FileNotFoundError):
        remove_empty_lines(str(non_existent_file))