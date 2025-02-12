import pytest

# import the functions to test
from running_avg        import running_average  
from median_arrays      import median_number_array
from bracket_validation import validate_brackets, is_valid_bracket_sequence
from interval_merging   import merge_intervals  

def test_running_average_valid(capfd):
    """
    tests running_average with a valid list of numbers.
    captures printed output and compares it to expected output.
    """

    numbers = [0.5, 3.0, 7.5, 14.0, 22.5, 33.0, 45.5, 60.0, 76.5, 95.0, 115.5, 138.0, 162.5, 189.0, 217.5, 248.0, 280.5, 315.0, 351.5]
    
    expected_output = [
    "Current number: 0.50, Running average: 0.50",
    "Current number: 3.00, Running average: 1.75",
    "Current number: 7.50, Running average: 3.67",
    "Current number: 14.00, Running average: 6.25",
    "Current number: 22.50, Running average: 9.50",
    "Current number: 33.00, Running average: 13.42",
    "Current number: 45.50, Running average: 18.00",
    "Current number: 60.00, Running average: 23.25",
    "Current number: 76.50, Running average: 29.17",
    "Current number: 95.00, Running average: 35.75",
    "Current number: 115.50, Running average: 43.00",
    "Current number: 138.00, Running average: 50.92",
    "Current number: 162.50, Running average: 59.50",
    "Current number: 189.00, Running average: 68.75",
    "Current number: 217.50, Running average: 78.67",
    "Current number: 248.00, Running average: 89.25",
    "Current number: 280.50, Running average: 100.50",
    "Current number: 315.00, Running average: 112.42",
    "Current number: 351.50, Running average: 125.00"]
    
    # run function and get output and split it into a list line by line
    running_average(numbers)  
    aux    = capfd.readouterr().out
    output = [line for line in aux.split("\n") if line.strip()]  # remove empty lines
    
    # validate the output line by line
    assert output == expected_output

def test_running_average_empty():
    """tests running_average with an empty list (should raise valueerror)."""

    with pytest.raises(ValueError, match = "Input list cannot be empty."):
        running_average([])

def test_running_average_non_numeric():

    """tests running_average with non-numeric values (should raise valueerror)."""

    with pytest.raises(ValueError, match = "All elements in the list must be integers or floats."):
        running_average([1, "two", 3.0])

def test_median_number_array():
    """
    tests median_number_array with different cases.
    """

    # test with provided example
    assert median_number_array([4, 2, 1], [2, 5], [7, 6]) == 4

    # test with an odd number of elements
    assert median_number_array([10, 2, 8], [3, 6])        == 6

    # test with an even number of elements
    assert median_number_array([1, 3, 5], [2, 4, 6])      == 3.5

    # test with negative numbers
    assert median_number_array([-5, -10, 0], [10, 5])     == 0

    # test with a single list
    assert median_number_array([1, 2, 3, 4, 5])           == 3

    # test with a single value
    assert median_number_array([7])                       == 7

    # test with duplicate values
    assert median_number_array([2, 2, 2], [2, 2])         == 2

    # test with an empty array 
    with pytest.raises(ValueError):
        median_number_array([])

    # test with invalid values like strings 
    with pytest.raises(ValueError):
        median_number_array([1904, 2025, "benfica"], [123, 456])

# test for valid intervals that merge
def test_merge_intervals_good():
    assert merge_intervals([[2, 4], [2, 5], [3, 6], [9, 11]]) == [[2, 6], [9, 11]]
    assert merge_intervals([[1, 3], [2, 4], [3, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 10], [2, 6], [7, 8], [9, 15]]) == [[1, 15]]
    assert merge_intervals([[1, 3], [4, 6], [7, 10]]) == [[1, 3], [4, 6], [7, 10]]

# test for an empty list
def test_merge_intervals_empty():
    assert merge_intervals([]) == []

# test intervals where start > end
def test_merge_intervals_invalid_start_end():
    with pytest.raises(ValueError):
        merge_intervals([[5, 4]])
    
    with pytest.raises(ValueError):
        merge_intervals([[10, 8], [2, 6]])

# test for invalid input 
def test_merge_intervals_invalid_input_type():
    
    # not a list of intervals
    with pytest.raises(ValueError):
        merge_intervals([5, 4])  
    
    # non-numeric values
    with pytest.raises(ValueError):
        merge_intervals([['Benfica', 4], [2, 6]])  

    # non-integer or float start
    with pytest.raises(ValueError):
        merge_intervals([['1', 4], [2, 6]])  
    
    # list with only one value instead of two
    with pytest.raises(ValueError):
        merge_intervals([[2, 4], [1]])  

# test for single interval
def test_merge_intervals_single_interval():
    assert merge_intervals([[1, 5]]) == [[1, 5]]
    assert merge_intervals([[10, 10]]) == [[10, 10]]

# test the bracket_validation but only is_valid_bracket_sequence function since the other is a simple if statement that returns a string message
def test_is_valid_bracket_sequence():
    """
    tests is_valid_bracket_sequence with different cases.
    """

    # test valid cases
    assert is_valid_bracket_sequence("{[BENFICA 1904]}") == True
    assert is_valid_bracket_sequence("[{Benfica}]")      == True
    assert is_valid_bracket_sequence("{[()]}")           == True
    assert is_valid_bracket_sequence("[[]]")             == True
    assert is_valid_bracket_sequence("{[]()[]}")         == True
    assert is_valid_bracket_sequence("")                 == True  # empty string is considered valid

    # test invalid cases
    assert is_valid_bracket_sequence("{[benfica 1904}")  == False  # missing closing bracket
    assert is_valid_bracket_sequence("[{benfica}]")      == True   # correct
    assert is_valid_bracket_sequence("{[())}")           == False  # incorrect order of brackets
    assert is_valid_bracket_sequence("{[}")              == False  # unmatched opening bracket
    assert is_valid_bracket_sequence("[{]")              == False  # mismatched brackets

    # test cases with only opening or closing brackets
    assert is_valid_bracket_sequence("{[{") == False  # only opening brackets
    assert is_valid_bracket_sequence("}])") == False  # only closing brackets
