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
        total  += number                    # Update the cumulative sum
        average = total / (index + 1)       # Compute the running average
        print(f"Current number: {number}, Running average: {average:.2f}") # Output the result rounding the average to 2 decimal places 
        print() 

def main():
    # Example usage
    numbers = [0.5, 3.0, 7.5, 14.0, 22.5, 33.0, 45.5, 60.0, 76.5, 95.0, 115.5, 138.0, 
      162.5, 189.0, 217.5, 248.0, 280.5, 315.0, 351.5]
    running_average(numbers)

if __name__ == "__main__":
    main()
