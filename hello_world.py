#!/usr/bin/env python3
"""
A simple Python script demonstrating basic functionality.
"""

def greet(name):
    """
    Greet a person by name.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to the repository."

def main():
    """
    Main function to run the script.
    """
    print("=" * 50)
    print("Python Script Example")
    print("=" * 50)
    
    # Greet the user
    message = greet("GitHub User")
    print(message)
    
    # Demonstrate some basic Python features
    numbers = [1, 2, 3, 4, 5]
    print(f"\nSum of {numbers}: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    
    print("\nScript completed successfully!")

if __name__ == "__main__":
    main()