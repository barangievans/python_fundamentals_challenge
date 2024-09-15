# Python Fundamentals Code Challenge

## Overview

This repository contains solutions to a Python fundamentals code challenge. It includes functions, decorators, sorting, merging dictionaries, and object-oriented programming examples.

## Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Python Fundamentals - Phase 3 Code Challenge
Overview
This repository contains the solutions for the Python Fundamentals Phase 3 Code Challenge. The purpose of this assessment is to evaluate your understanding of basic Python concepts including data structures, functions, decorators, sequences, sets, dictionaries, and object-oriented programming.

Instructions
Clone the Repository

To get started, clone the repository to your local machine:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Setup Environment

This project does not require any external libraries. Ensure you have Python 3.x installed on your machine.

Run the Code

The solutions are designed to be run in the Python interpreter. You can test each function individually by calling them from the Python shell or writing test scripts.

Example:

bash
Copy code
python
>>> from solution import add_numbers
>>> add_numbers(3, 5)
8
Functions and Classes
Here is a summary of the provided functions and classes:

add_numbers(num1, num2)

Description: Returns the sum of two numbers.
Parameters: num1 (int or float), num2 (int or float)
Returns: Sum of num1 and num2
is_even(number)

Description: Checks if a number is even.
Parameters: number (int)
Returns: True if the number is even, otherwise False
reverse_string(text)

Description: Returns the reversed version of the input string.
Parameters: text (str)
Returns: Reversed text
count_vowels(text)

Description: Counts the number of vowels in a string (case-insensitive).
Parameters: text (str)
Returns: Number of vowels in text
calculate_factorial(n)

Description: Returns the factorial of a non-negative integer.
Parameters: n (int, non-negative)
Returns: Factorial of n
apply_decorator(func)

Description: Applies a decorator that prints "Decorator Applied" before calling the original function.
Parameters: func (callable)
Returns: Decorated function
sort_by_age(list_of_tuples)

Description: Sorts a list of tuples by the age value in ascending order.
Parameters: list_of_tuples (list of tuples, each containing a name and an age)
Returns: Sorted list of tuples
merge_dicts(dict1, dict2)

Description: Merges two dictionaries, summing values for any common keys.
Parameters: dict1 (dict), dict2 (dict)
Returns: Merged dictionary
Car Class

Description: Represents a car with attributes make, model, and year.
Attributes: make (str), model (str), year (int)
Methods:
display_info(): Prints the car's make, model, and year
Code Quality
Comments: Each function and class is commented to explain its purpose and usage.
Naming Conventions: Functions and variables are named descriptively and consistently.
Data Structures: Efficient use of Python's built-in data structures is demonstrated.
Testing
To verify the functionality of each component, you can write and run individual test cases. Here is an example of a simple test script for the add_numbers function:

python
Copy code
from solution import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

test_add_numbers()
print("All tests passed!")
Submission
Push Your Code: Ensure all code is pushed to the private repository.
Submit the URL: Provide the URL of the private repository for assessment.
Rubric