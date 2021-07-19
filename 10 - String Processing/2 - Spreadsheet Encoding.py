'''
    A = 1
    AA = 27

    314 -> 3.100 + 1.10 + 4.1 -> 3.10^2 + 1.10^1 + 4.10^0

    A = 1, B = 2, ...., Z = 26
    AA -> A.26^1 + A.26^0 -> 1.26^1 + 1.26^0 = 27
'''

# ord function python --> represents unicode character
print(ord('A'))
print(ord('B'))
print(ord('Z'))

print("\n")
print(ord('A') - ord('A') + 1)
print(ord('B') - ord('A') + 1)
print(ord('C') - ord('A') + 1)
print(ord('Z') - ord('A') + 1)


def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num += 26**count*(ord(s)-ord('A')+1)
        count -= 1
    return num


print("\n")
print(spreadsheet_encode_column("ZZ"))
