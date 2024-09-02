def sort_by_age(list_of_tuples):
    """
    Sorts a list of tuples by age in ascending order.
    
    Args:
    list_of_tuples (list of tuples): Each tuple contains (name, age).
    
    Returns:
    list of tuples: The sorted list of tuples.
    """
    return sorted(list_of_tuples, key=lambda x: x[1])
