'''
    Memoization: the act of storing results of costly function call, 
                 and retrieving them from the store when needed again to avoid re-evaluation.

                 *mostly using hastables
'''

memo = {}  # dictionary for Memoization


def fib(n):
    ''' reduce time complexity from O(2^n) to O(n) '''
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    elif n in memo:  # Check if result for n has already been evaluated
        return memo[n]  # return the result if it is available
    else:  # otherwise recursive step
        # store the result of n in memoization dictionary
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]  # return the value


print(fib(100))
