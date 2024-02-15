def is_parentheses_balanced(s):
    """
    This function checks if all the open-parentheses in the string have
    corresponding close-parentheses.
    """
    # Dictionary to hold the pairs of parentheses
    parentheses = {'(': ')', '[': ']', '{': '}'}
    
    # Initialize an empty stack
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If the character is an open parenthesis, push it onto the stack
        if char in parentheses:
            stack.append(char)
        # If the character is a close parenthesis
        elif char in parentheses.values():
            # If the stack is empty or the top of the stack doesn't match
            if not stack or parentheses[stack.pop()] != char:
                return False
    
    # If the stack is empty, all parentheses are properly matched
    return not stack

# Test the function with the provided examples
example1 = "I { love [ the {rains}()] }"
example2 = "I { love [ the {rains ] (}"

# Output results
is_balanced_example1 = is_parentheses_balanced(example1)
is_balanced_example2 = is_parentheses_balanced(example2)

# (is_balanced_example1, is_balanced_example2)
print(is_balanced_example1, is_balanced_example2)
