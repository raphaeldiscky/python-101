'''
    a fixed point in an array A is an index i such taht A[i] is equal to i
    a. two facts:
        - the list is sorted
        - the list contains distinct elements
    b. algorithm:
        - if midpoint greater than its index, then element to the right will be greater than its index 
          and remove the right portion
'''


def find_fixed_point_linear(A):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
        return None


def find_fixed_point(A):
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    low = 0
    high = len(A)-1

    while low <= high:
        mid = (low + high)//2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]
print("Linear Approach")
print(A1)
print(find_fixed_point_linear(A1))
print(A2)
print(find_fixed_point_linear(A2))
print(A3)
print(find_fixed_point_linear(A3))

print("\nBinary Search Approach")
print(A1)
print(find_fixed_point(A1))
print(A2)
print(find_fixed_point(A2))
print(A3)
print(find_fixed_point(A3))
