def is_valid_bracket_sequence(s: str) -> bool:
    """
    Checks if a given string contains a valid sequence of brackets.

    Args:
        s (str): The input string containing brackets.

    Returns:
        bool: True if the bracket sequence is valid, False otherwise.

    A valid bracket sequence means:
    - Every opening bracket ('(', '{', '[') has a corresponding closing bracket (')', '}', ']').
    - Brackets are closed in the correct order.
    - Nested brackets are properly balanced.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(n) in the worst case (when all brackets are open).
    """

    # Stack to track opening brackets
    stack = []

    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the string
    for char in s:
        # If it's an opening bracket,
        if char in bracket_map.values():   
            stack.append(char)          # push it onto the stack
        
        # If it's a closing bracket
        elif char in bracket_map.keys(): 
            if not stack or bracket_map[char] != stack.pop():  # Check if the stack is empty or if the last opened bracket doesn't match
                return False

    # If the stack is empty at the end, all brackets were properly matched
    return not stack


def validate_brackets(s: str) -> None:
    """
    Validates the bracket sequence in a given string and prints the result.

    Args:
        s (str): The input string containing brackets.

    Output:
        Prints whether the bracket sequence is valid or not.
    """
    
    if is_valid_bracket_sequence(s):
        print("The string is valid.")
    else:
        print("Error: The string contains invalid brackets.")

