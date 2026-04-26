def greet(name):
    """
    Greet a person by name.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def add(a, b):
    """
    Add two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of a and b
    """
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print("This is a new feature added to the myfeature.py file.")