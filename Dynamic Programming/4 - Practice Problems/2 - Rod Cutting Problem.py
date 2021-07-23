'''
    input:
        n = 4
        prices = [2,3,7,8]
    output:
        rodCutting(n, prices) = 9
'''


def rodCutting_rec(n, prices):
    '''
        Solution 1: simple recursion
            time complexity O(2^N)
    '''
    if n < 0:
        return 0
    max_val = 0
    for i in range(1, n+1):
        max_val = max(max_val, prices[i-1] + rodCutting_rec(n-i, prices))
    return max_val


print(rodCutting_rec(3, [3, 7, 8]))


def rodCutting_topdown_(n, prices, memo):
    '''
        Solution 2: top-down approach
            time complexity O(n^2)
            space complexity O(n)
    '''
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    max_val = 0
    for i in range(1, n+1):
        max_val = max(max_val, prices[i-1] +
                      rodCutting_topdown_(n-i, prices, memo))
    memo[n] = max_val
    return memo[n]


def rodCutting_topdown(n, prices):
    memo = {}
    return rodCutting_topdown_(n, prices, memo)


print(rodCutting_topdown(3, [3, 7, 8]))


def rodCutting_bottomup(n, prices):
    '''
        Solution 3: bottom-up approach
            time complexity O(n^2)
            space complexity O(n)
    '''
    # create a dp array the size of (n+1)
    dp = [0 for _ in range(n+1)]
    # startiing from rod of length 1, find optimal answer to all subproblems
    for i in range(1, n+1):
        max_val = 0
        # for a rod of length i, we can find what cuts give max answer since we have answer to all smaller cuts
        for j in range(i):
            max_val = max(max_val, prices[j] + dp[i-j-1])
        dp[i] = max_val
    return dp[n]


print(rodCutting_bottomup(3, [3, 7, 8]))
