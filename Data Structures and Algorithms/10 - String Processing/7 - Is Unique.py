'''
    1) Is Unique
        a. Solution 1
        b. Solution 2
        c. Solution 3

    abCDefGh -> is_unique() -> True
    nonunique -> is_unique() -> False
'''


def is_unique_1(input_str):
    d = {}
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True


def is_unique_2(input_str):
    # set(input_str) converts input_str into a set by removing all duplicates
    return len(set(input_str)) == len(input_str)


def is_unique_3(input_str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


unique_str = "AbCDefG"
non_unique_str = "non UniqueSTR"

print("Unique String")
print(unique_str)
print("Non-Unique String")
print(non_unique_str, "\n")

print("Solution 1 where input string is unique string")
print(is_unique_1(unique_str))
print("Solution 1 where input string is non-unique string")
print(is_unique_1(non_unique_str), "\n")


print("Solution 2 where input string is unique string")
print(is_unique_2(unique_str))
print("Solution 2 where input string is non-unique string")
print(is_unique_2(non_unique_str), "\n")

print("Solution 3 where input string is unique string")
print(is_unique_3(unique_str))
print("Solution 3 where input string is non-unique string")
print(is_unique_3(non_unique_str))
