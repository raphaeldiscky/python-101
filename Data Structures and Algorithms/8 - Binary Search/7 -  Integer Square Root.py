'''
    - takes a non-negative integer, k
    - return the largest integer whose square is less than or equal to specified integer k

    input = 300
    output = 17

    (17)^2 = 289 < 300
    (18)^2 = 324 > 300
    so the number 17 is the correct response

    input = 12
    output = 3

    (1)^2 = 1
    (2)^2 = 4
    (3)^2 = 9
    (4)^2 = 16
'''


def integer_square_root(k):
    # time complexity = O(k)
    low = 0
    high = k

    while low <= high:
        mid = (low + high)//2
        mid_squared = mid*mid
        print("low: " + str(low) + " high: " + str(high) +
              " mid_squared: " + str(mid_squared))

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


k = 12
print(integer_square_root(k))
