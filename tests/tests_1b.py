"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_addition():
    assert simple_calculator("add", 5, 3) == 8          # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0         # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0          # Test for zero addition

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0   # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5    # Test for zero minuend

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4   # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0   # Test for multiplication by zero

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2     # Test for negative and positive number
    assert simple_calculator("divide", 5, 2) == 2.5     # Test for division resulting in float

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)               # Test division by zero

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation
        
# Additional Personally added edge case tests

# Test to see if booleans are treated as they should be like 1 is for True and 0 is for False 
def testBooleanInputs():
    assert simple_calculator("add", 10, True) == 11
    assert simple_calculator("multiply", 10, False) == 0
    
# Test for Mixed Input types like on being decimal and an other being an integer
def testMixedInputTypes():
    assert simple_calculator("add", 10, 2.5) == 12.5
    assert simple_calculator("subtract", 100.5, 3) == 97.5

# One of the basic tests of making sure that input is valid and there is no mistake
def testInvalidInputs():
    with pytest.raises(TypeError):
        simple_calculator("add", [1, 2], 3)
    with pytest.raises(TypeError):
        simple_calculator("subtract", None, 5) 

# Test for the specific types of Mistakes like does it handle string input and does handle numbers inputted as strings
def testStringMistakes():
    with pytest.raises(TypeError):
        simple_calculator("add", "C", "$")
    with pytest.raises(TypeError):
        simple_calculator("multiply", "10", 5)

if __name__ == "__main__":
    pytest.main()