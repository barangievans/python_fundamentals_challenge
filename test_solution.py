# Import functions from the solution files
from add_numbers import add_numbers
from is_even import is_even
from reverse_string import reverse_string
from count_vowels import count_vowels
from calculate_factorial import calculate_factorial
from apply_decorator import apply_decorator
from sort_by_age import sort_by_age
from merge_dicts import merge_dicts
from solution import Car

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("Python") == "nohtyP"

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOU") == 5

def test_calculate_factorial():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1

def test_apply_decorator():
    def sample_func():
        return "Hello"
    
    decorated_func = apply_decorator(sample_func)
    assert decorated_func() == "Hello"

def test_sort_by_age():
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    sorted_data = sort_by_age(data)
    assert sorted_data == [("Bob", 25), ("Alice", 30), ("Charlie", 35)]

def test_merge_dicts():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged_dict = merge_dicts(dict1, dict2)
    assert merged_dict == {"a": 1, "b": 5, "c": 4}

def test_car_class():
    car = Car("Honda", "Civic", 2022)
    assert car.make == "Honda"
    assert car.model == "Civic"
    assert car.year == 2022
    assert car.display_info() == "Make: Honda, Model: Civic, Year: 2022"

if __name__ == "__main__":
    test_add_numbers()
    test_is_even()
    test_reverse_string()
    test_count_vowels()
    test_calculate_factorial()
    test_apply_decorator()
    test_sort_by_age()
    test_merge_dicts()
    test_car_class()
    print("All tests passed!")
