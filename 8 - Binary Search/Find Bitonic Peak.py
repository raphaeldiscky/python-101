'''
    bitonic peak: 1,2,3,4,5,4,3,2,1

    1) Naive Solution:
        - the element to the left of the peak element is less than the peak element
        - the element to the right of the peak element is less than the peak element
    2) Binary Search Solution:
        - if mid_left < midpoint value and midpoint value < mid_right,
          then the peak element should be to the right of the midpoint
        - discarding left side
'''


def find_highest_number(A):
    low = 0
    high = len(A)-1

    # require at least 3 elements for a bitonic sequence
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high)//2

        mid_left = A[mid-1] if mid - 1 > 0 else float("-inf")
        mid_right = A[mid+1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
    return None


# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))
