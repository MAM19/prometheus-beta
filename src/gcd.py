def euclidean_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    The Euclidean algorithm is an efficient method to find the largest positive integer 
    that divides both input numbers without a remainder.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is negative
        TypeError: If inputs are not integers
    
    Examples:
        >>> euclidean_gcd(48, 18)
        6
        >>> euclidean_gcd(54, 24)
        6
        >>> euclidean_gcd(0, 5)
        5
        >>> euclidean_gcd(5, 0)
        5
    """
    # Type checking
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Negative input validation
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle special case where one number is 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Main Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a