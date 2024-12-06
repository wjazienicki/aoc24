import pytest
from Day06.solution import part1, part2  # Import your solution functions
from utils.input_handler import *

@pytest.fixture
def test_input1():
    return "Day06/test.txt"

@pytest.fixture
def test_input2():
    return "Day06/test.txt"

def test_part1_example(test_input1):
    """Test part 1 with the example input and known output."""
    expected_output = 41  # Replace with the actual expected output for the example
    assert part1(test_input1) == expected_output

def test_part2_example(test_input2):
    """Test part 2 with the example input and known output."""
    expected_output = 6  # Replace with the actual expected output for the example
    assert part2(test_input2) == expected_output