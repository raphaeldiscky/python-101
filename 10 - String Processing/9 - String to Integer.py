'''
    "123" -> 123
    "-12332" -> -12332
    "554" -> 554

    123 -> 1.10^2 + 2.10^1 + 3.10^0 -> 100 + 20 + 3 = 123
'''


def str_to_int(input_str):
    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str)-(i+1))
        digit = ord(input_str[i]) - ord('0')  # string to int
        output_int += place*digit

    if is_negative:
        return -1*output_int
    else:
        return output_int


s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))
