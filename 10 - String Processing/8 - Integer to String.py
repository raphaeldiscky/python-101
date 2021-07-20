'''
    ord() -> returns an integer which represents the Unicode
    chr() -> opposite of ord()

    ord('0') = 48
    ord('1') = ord('0') + 1 = 48 + 1 = 49 
    ord('2') = ord('0') + 2 = 48 + 2 = 50 

    chr(ord('0')) = chr(48) = '0' 
    chr(ord('0') + 1) = chr(48 + 1) = chr(49) = '1' 
    chr(ord('0') + 2) = chr(48 + 2) = chr(50) = '2' 
'''


def int_to_str(input_int):
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    if input_int == 0:
        output_str.append('0')
    else:
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str


input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))
