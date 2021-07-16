'''
    1) Intersection of Two Sorted Arrays
        A = [2, 3, 3, 5, 7, 11]
        B = [3, 3, 7, 15, 31]
        ~~
        intersection = [3,7]
'''

# one-line solution:
# A = [2, 3, 3, 5, 7, 11]
# B = [3, 3, 7, 15, 31]
# print(set(A).intersection(B))


def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:  # check if duplicate
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]
print(intersect_sorted_array(A, B))
