def decorator_func(func):
    """
    A decorator that prints 'Decorator Applied' before calling the function.
    
    Args:
    func (function): The function to decorate.
    
    Returns:
    function: The decorated function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """
    Applies a decorator to the given function.
    
    Args:
    func (function): The function to apply the decorator to.
    
    Returns:
    function: The decorated function.
    """
    return decorator_func(func)
