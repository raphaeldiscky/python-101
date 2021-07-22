'''
    bottom-up: start from the base case, i.e., Fib(0) and Fib(1), and then build-up to the solution
'''


def fib(n):
    # time complexity O(n)
    # space complexity O(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    # table for tabulation
    table = [None]*(n+1)
    table[0] = 0  # base case 1, fib(0) = 0
    table[1] = 1  # base case 2, fib(1) = 1
    # filling up tabulation table starting from 2 and going upto n
    for i in range(2, n+1):
        # we have result of i-1 and i-2 available because these had been evaluated already
        table[i] = table[i-1] + table[i-2]
    # return the value of n
    return table[n]


print(fib(10000))
