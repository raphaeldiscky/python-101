'''
    Anagram: 
        - "rail safety" = "fairy tales"
        - "roast beef" = "eat for BSE"

        - "William Shakespeare" = "I am a weakish speller"
        - "Madam Curie" = "Radium came"
'''

s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# requires O(nlogn) time (since any comparison based sorting algorithm)
print(sorted(s1) == sorted(s2))


def is_anagram(s1, s2):
    ht = {}

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:  # if all keys in ht have 0 values, then strings is anagram
        if ht[i] != 0:
            return False
    return True


print(is_anagram(s1, s2))
