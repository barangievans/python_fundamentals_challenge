def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries, summing up values for common keys.
    
    Args:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: The merged dictionary.
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
