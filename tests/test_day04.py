import pytest
from Day04.solution import part1, part2  # Import your solution functions
from utils.input_handler import *

@pytest.fixture
def test_input1():
    return "Day04/test.txt"

@pytest.fixture
def test_input2():
    return "Day04/test.txt"

def test_part1_example(test_input1):
    """Test part 1 with the example input and known output."""
    expected_output = 18  # Replace with the actual expected output for the example
    assert part1(test_input1) == expected_output

def test_part2_example(test_input2):
    """Test part 2 with the example input and known output."""
    expected_output = 9  # Replace with the actual expected output for the example
    assert part2(test_input2) == expected_output
