import pytest
from src.fibonacci_generator import fibonacci_generator

def test_fibonacci_generator_basic_cases():
    """Test basic Fibonacci sequence generation."""
    assert fibonacci_generator(0) == []
    assert fibonacci_generator(1) == [0]
    assert fibonacci_generator(2) == [0, 1]
    assert fibonacci_generator(5) == [0, 1, 1, 2, 3]
    assert fibonacci_generator(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_generator_larger_sequence():
    """Test generation of a larger Fibonacci sequence."""
    sequence = fibonacci_generator(10)
    assert len(sequence) == 10
    # Verify the mathematical property of Fibonacci sequence
    for i in range(2, len(sequence)):
        assert sequence[i] == sequence[i-1] + sequence[i-2]

def test_fibonacci_generator_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Number of Fibonacci numbers must be non-negative"):
        fibonacci_generator(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(3.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator("5")

def test_fibonacci_generator_type_variety():
    """Ensure the function works with different integer types."""
    assert fibonacci_generator(int(5)) == [0, 1, 1, 2, 3]
    assert fibonacci_generator(True) == [0]  # bool is a subclass of int