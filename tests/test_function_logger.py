import logging
import pytest
from src.function_logger import log_execution

# Create a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.INFO)

# Capture logs for verification
class LogCapture:
    def __init__(self, logger):
        self.logger = logger
        self.log_messages = []
        self.handler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.handler.stream.seek(0)
    
    def get_logs(self):
        self.handler.flush()
        self.handler.stream.seek(0)
        return [record.strip() for record in self.handler.stream.readlines()]

@log_execution(test_logger)
def sample_function(a: int, b: int) -> int:
    """Sample function for testing logging decorator"""
    return a + b

@log_execution(test_logger)
def error_function():
    """Sample function that raises an exception"""
    raise ValueError("Test error")

def test_log_execution_normal_case():
    # Capture logs
    log_capture = LogCapture(test_logger)
    
    # Call the decorated function
    result = sample_function(3, 4)
    
    # Verify result
    assert result == 7
    
    # Check log messages
    logs = log_capture.get_logs()
    assert len(logs) == 2
    assert "Executing sample_function(3, 4)" in logs[0]
    assert "Finished sample_function. Execution time:" in logs[1]

def test_log_execution_default_logger():
    # Use default logger decorator
    @log_execution()
    def default_log_func(x):
        return x * 2
    
    # Verify function works correctly
    assert default_log_func(5) == 10

def test_log_execution_exception():
    # Capture logs
    log_capture = LogCapture(test_logger)
    
    # Verify exception is raised and logged
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check log messages
    logs = log_capture.get_logs()
    assert len(logs) == 2
    assert "Executing error_function()" in logs[0]
    assert "Exception in error_function: Test error" in logs[1]

def test_log_execution_kwargs():
    # Capture logs
    log_capture = LogCapture(test_logger)
    
    # Call function with keyword arguments
    result = sample_function(a=5, b=7)
    
    # Verify result
    assert result == 12
    
    # Check log messages
    logs = log_capture.get_logs()
    assert len(logs) == 2
    assert "Executing sample_function(a=5, b=7)" in logs[0]
    assert "Finished sample_function. Execution time:" in logs[1]