def running_average(numbers):
    """
    Computes and prints the running average of a list of numbers.

    Args:
        numbers (List[float] or List[int]): A list of numerical values.

    Output:
        Prints the current number and the running average at each step.

    The running average is calculated as:
        average = (sum of all numbers seen so far) / (count of numbers seen so far)

    Raises:
        ValueError: If the input list is empty or contains non-numeric values.

    Time Complexity:  O(n), where n is the number of elements in the list.
    Space Complexity: O(1), since we only use a few variables (total, index, number).
    """

    # Check if the list is empty
    if not numbers:
        raise ValueError( "Input list cannot be empty." )

    # Check if all elements are integers or floats
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError( "All elements in the list must be integers or floats." )

    # Initialize total sum to zero
    total = 0

    # Iterate over the list, keeping track of index and number
    for index, number in enumerate(numbers):
        total  += number                         # Update the cumulative sum
        average = round(total / (index + 1), 2)  # Compute the running average
        print(f"Current number: {number:.2f}, Running average: {average:.2f}") # Output the result rounding the average to 2 decimal places 
        print() 
