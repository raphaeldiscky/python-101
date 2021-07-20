'''
    - Palindrome: A word or phrase that is the same forwards and backward.
    - Permutation: A rearrangement of letters.

    tacocat --> every character has a duplicate in this odd-length string except the one char at the middle
'''


def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = {}

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:  # it implies that there is more than one char which has an odd number of occurences
            return False
    return True


palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))
