def count_vowels(text):
    """
    Counts the number of vowels in the input string.
    
    Args:
    text (str): The string in which to count vowels.
    
    Returns:
    int: The count of vowels (a, e, i, o, u).
    """
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)
