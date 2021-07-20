'''
    - determines the index of the smallest element of the cyclically shifted array
    - cyclically shifted = array that possible to shift its entries cyclically so that it becomes sorted

    A = [4, 5, 6, 7, 1, 2, 3]

    all the possible cyclic shifs of an array:
    [2, 3, 4, 5, 6, 7, 1]
    [3, 4, 5, 6, 7, 1, 2]
    [4, 5, 6, 7, 1, 2, 3]
    [5, 6, 7, 1, 2, 3, 4]
    [6, 7, 1, 2, 3, 4, 5]
    [7, 1, 2, 3, 4, 5, 6]
'''


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high)//2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low
