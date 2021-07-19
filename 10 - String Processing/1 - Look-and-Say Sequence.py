'''
    1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... 

    - 1 -> one 1 -> 11
    - 11 -> two 1 -> 21
    - 21 -> one '2' one '1' -> 1211
    - 1211 -> one '1' one '2' two '1' -> 111221

    111221 is read off as "three 1s, two 2s, then one 1" or 312211.
'''


def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)


s = "1"
print(s)
n = 4
for i in range(n-1):
    s = next_number(s)
    print(s)
