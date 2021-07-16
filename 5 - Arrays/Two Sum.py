'''
    1) Two Sum Problem
        a. Solution 1: Brute-force
        b. Solution 2: Hash table
        c. Solution 3
'''


def two_sum_brute_force(A, target):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A, target))
target = 20
print(two_sum_brute_force(A, target))


def two_sum_hash_table(A, target):
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    ht = {}
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]  # A[i] = value, target-A[i] = key
            # print("A["+str(target-A[i])+"]:", A[i])
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_hash_table(A, target))


# assume array is sorted
def two_sum(A, target):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum(A, target))
