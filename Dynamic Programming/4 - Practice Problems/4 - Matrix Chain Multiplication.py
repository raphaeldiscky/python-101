'''
    input:
        dims = [3,3,2,1]
    output:
        MinMultplications([3,3,2,1]) = 15
'''


def min_bottomup_rec_(dims, i, j):
    '''
        Solution 1: simple recursion
            time complexity O(n2^n)
    '''
    if j-i <= 2:
        return 0
    minimum = float("inf")
    for k in range(i+1, j-1):
        minimum = min(minimum, min_bottomup_rec_(dims, i, k+1) + min_bottomup_rec_(dims, k, j) +
                      dims[i] * dims[j-1] * dims[k])
    return minimum


def min_bottomup_rec(dims):
    return min_bottomup_rec_(dims, 0, len(dims))


print(min_bottomup_rec([3, 3, 2, 1, 2]))


def min_topdown_(dims, i, j, memo):
    '''
        Solution 2: top-down approach
            time complexity O(n^3)
            space complexity O(n^2)
    '''
    if j-i <= 2:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    minimum = float("inf")
    for k in range(i+1, j-1):
        minimum = min(minimum, min_topdown_(dims, i, k+1, memo) + min_topdown_(dims, k, j, memo) +
                      dims[i]*dims[j-1]*dims[k])
    memo[(i, j)] = minimum
    return minimum


def min_topdown(dims):
    memo = {}
    return min_topdown_(dims, 0, len(dims), memo)


print(min_topdown([3, 3, 2, 1, 2]))


def min_bottomup(dims):
    '''
        Solution 3: bottom-up approach
            time complexity O(n^3)
            space complexity O(n^3)
    '''
    dp = [[0 for _ in range(len(dims))] for _ in range(len(dims))]

    for l in range(2, len(dims)):
        for i in range(1, len(dims)-l+1):
            j = i + l - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                temp = dp[i][k] + dp[k+1][j] + dims[i-1]*dims[k]*dims[j]
                if temp < dp[i][j]:
                    dp[i][j] = temp
    return dp[1][-1]


print(min_bottomup([3, 3, 2, 1, 2]))
