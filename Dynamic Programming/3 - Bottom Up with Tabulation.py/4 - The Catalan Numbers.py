'''
    C4 = C0C3 + C1C2 + C2C1 + C3C0
    catalan nums: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862

    input:
        n = 4
    output:
        catalan(4) = 14
        catalan(6) = 132
'''


def catalan_rec(n):
    '''
        Solution 1: simple recursion
            time complexity O(n!)
    '''
    if n == 0:  # C(0) = 1
        return 1
    sum = 0
    # iterate from 1...n to evaluate: C(0)*C(n-1) + C(1)*C(n-2) ... + C(n-1)*C(0)
    for i in range(n):
        sum += (catalan_rec(i)*catalan_rec(n-1-i))  # C(i)*C(n-1-i)
    return sum


print(catalan_rec(4))


def catalan_memo(n, memo):
    '''
        Solutin 2: top-down approach
            time complexity O(n^2)
            space complexity O(n)
    '''
    if n == 0:
        return 1
    elif n in memo:
        return memo[n]
    sum = 0
    # iterate from 1...n to evaluate: C(0)*C(n-1) + C(1)*C(n-2) ... + C(n-1)*C(0)
    for i in range(n):
        sum += (catalan_memo(i, memo) *
                catalan_memo(n-1-i, memo))  # C(i)*C(n-1-i)
    memo[n] = sum
    return memo[n]


def catalan_topdown(n):
    memo = {}
    return catalan_memo(n, memo)


print(catalan_topdown(400))


def catalan_bottomup(n):
    '''
        Solution 3: bottom-up approach
        time complexity O(n^2)
        space complexity O(n)
    '''
    table = [None]*(n+1)
    table[0] = 1
    for i in range(1, n+1):
        table[i] = 0
        # iterate from 0 to i; according to formula of catalan i.e. C0*Ci + C1*Ci-1 + ... Ci*C0
        for j in range(i):
            table[i] += (table[j]*table[i-j-1])  # C(j) * C(i-j-1)
    return table[n]


print(catalan_bottomup(1000))
