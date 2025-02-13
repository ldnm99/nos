import sys
import ast

def median_number_array(*arrays):
    """
    Computes the median of multiple numeric arrays combined.
    This function does not use built-in median (from statistics) or chain (from itertools) to explicitly demonstrate sorting and median logic.

    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(n) since all values are stored in a list.
    """
    
    # creates empty list to store all numbers in the arrays
    numbers = []

    # checks if all elements in the arrays are integers or floats
    for array in arrays:
        if not all( isinstance(x, (int, float)) for x in array):
            raise ValueError("All elements in the arrays must be integers or floats.")
        
        # extends the list of numbers with the values in each array
        numbers.extend(array)

    # if numbers list is empty raise an error
    if not numbers:
        raise ValueError("The input arrays contain no valid numbers.")

    # sorts all values in ascending order
    numbers.sort()
    
    # n is the number of values in the list
    n = len(numbers)

    if n % 2 == 1:  # if number of values is odd, the median is the middle value
        return numbers[n // 2]
    else:           # if number of values is even,the median is the average of the two middle values
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a list of numeric arrays.")
        sys.exit(1)

    try:
        input_arrays = ast.literal_eval(sys.argv[1])  # parse the input as a list
        if not isinstance(input_arrays, list) or not all(isinstance(arr, list) for arr in input_arrays):
            raise ValueError("Input must be a list of numeric arrays.")
        median = median_number_array(*input_arrays)
        print("Median:", median)
    except (ValueError, SyntaxError):
        print("Invalid input. Please provide a valid list of numeric arrays.")