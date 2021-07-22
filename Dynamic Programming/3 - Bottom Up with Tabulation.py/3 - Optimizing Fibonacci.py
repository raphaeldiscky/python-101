'''
    - reduce space complexity from O(n) to O(1)
    - so, if we maintain only two previous numbers and keep updating them as we go along, we will be able to get 
      nth fibonacci number without keeping a table of size n
'''


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    secondLast = 0
    last = 1
    current = None
    for i in range(1, n):
        # storing ith fibonacci in current by summing up i-1th and i-2th fibonacci
        current = secondLast + last
        secondLast = last  # updating for next iteration
        last = current
    return current


print(fib(6))
