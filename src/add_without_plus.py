def add_without_plus(a, b):
    """
    Add two integers without using the '+' operator.
    
    Uses bitwise operations to perform addition:
    - XOR (^) handles addition without carry
    - AND (&) and left shift (<<) handle the carry
    
    Args:
        a (int): First integer to add
        b (int): Second integer to add
    
    Returns:
        int: Sum of a and b
    
    Raises:
        TypeError: If inputs are not integers
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both arguments must be integers")
    
    # Handle signed numbers
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    # Continue until there's no carry
    while b != 0:
        # Calculate sum without carry using XOR
        sum_without_carry = a ^ b
        
        # Calculate carry using AND and left shift
        carry = (a & b) << 1
        
        # Update a and b
        a = sum_without_carry
        b = carry
        
        # Prevent integer overflow
        a = a & ((1 << 32) - 1)
        if a > MAX_INT:
            a -= 2**32
    
    return a