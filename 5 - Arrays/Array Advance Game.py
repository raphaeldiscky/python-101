'''
    1) Array Advance Game
        a. algorithm:
            - iterate through each entry in an array, A
            - track the furthest we can reach from entry (A[i]+i)
            - if for some i, we don't reach the end and that is the furthest we can reach, 
              then we can't reach the last index. Otherwise, the end is reached.
            - i: index processed. Furthest possible to advance from i:A[i] + i
'''


def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))
