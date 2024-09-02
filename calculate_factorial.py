def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of n.
    """
    if n < 0:
        raise ValueError("The input must be a non-negative integer.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
