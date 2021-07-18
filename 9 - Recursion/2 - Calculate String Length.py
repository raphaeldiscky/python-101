'''
    1) Calculate String Length
        a. Iterative Approach
        b. Recursive Approach
'''


def iterative_str_len(input_str):
    # Iterative length calculation: O(n)
    input_str_len = 0
    for i in range(len(input_str)):
        input_str_len += 1
    return input_str_len


def recursive_str_len(input_str):
    # Recursive length calculation: O(n)
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])
    # input_str[1:] indicates that all the characters except at the 0th index are passed into the recursive call.


input_str = "LucidProgramming"

print(iterative_str_len(input_str))
print(recursive_str_len(input_str))
