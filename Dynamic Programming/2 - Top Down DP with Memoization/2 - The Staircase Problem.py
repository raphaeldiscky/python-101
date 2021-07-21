'''
    1) The Staircase Problem
        input:
            n = 4 # the number of steps in the staircase
            m = 2 # number of steps covered in the biggest leap. Can jump between 1-m
        output:
            staircase(n,m) = 5
'''


def staircase_rec(n, m):
    # simple recursion solution:
    # time complexity O(m^n)
    if n == 0:
        return 1
    ways = 0
    for i in range(1, m+1):
        if i <= n:
            ways += staircase_rec(n-i, m)
    return ways


print(staircase_rec(4, 2))


def nthStair(n, m, memo):
    # DP solution:
    # time complexity O(nm)
    if n == 0:  # base case of when there is no stair
        return 1
    if n in memo:  # before recursive step check if result is memoized
        return memo[n]
    ways = 0
    # iterate over number of steps, we can take
    for i in range(1, m+1):
        # if steps remaining is samller than the jump step, skip
        if i <= n:
            # recursive call with n i units lesser where i is the number of steps taken here
            ways += nthStair(n-i, m, memo)
    # memoize result before returning
    memo[n] = ways
    return ways


def staircase(n, m):
    memo = {}
    return nthStair(n, m, memo)


print(staircase(100, 6))
