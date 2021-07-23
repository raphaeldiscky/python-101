'''
    input:
        bills = [10, 20]
        amount = 30
    output:
        countways([10, 20], 30) = 2

        two ways to represent $30:
            - 3 bills of $10
            - 1 bill of $20 and 1 bill of $10
'''


def countways_rec_(bills, amount, maximum):
    '''
        Solution 1: simple recursion
            n = length of bills, amount = C
            time complexity O(n^C)
    '''
    if amount == 0:
        return 1
    ways = 0
    for bill in bills:
        # to avoid repetition of similar sequences, use bills smaller than maximum
        if bill <= maximum and amount - bill >= 0:
            # notice how bill becomes maximum in recursive call
            ways += countways_rec_(bills, amount-bill, bill)
    return ways


def countways_rec(bills, amount):
    return countways_rec_(bills, amount, max(bills))


print(countways_rec([1, 2, 5], 5))


def countways_topdown_(bills, amount, maximum, memo):
    '''
        Solution 2: top-down approach
            time complexity O(Cn)
            space complexity O(Cn)
    '''
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if (amount, maximum) in memo:
        return memo[(amount, maximum)]
    ways = 0
    for bill in bills:
        # to avoid repetition of similar sequences, use bills smaller than maximum
        if bill <= maximum:
            ways += countways_topdown_(bills, amount-bill, bill, memo)
    memo[(amount, maximum)] = ways
    return ways


def countways_topdown(bills, amount):
    memo = {}
    return countways_topdown_(bills, amount, max(bills), memo)


print(countways_topdown([1, 2, 5], 5))


def countways_bottomup(bills, amount):
    '''
        Solution 3: bottom-up approach
            time complexity O(Cn)
            space complexity O(Cn)
    '''
    if amount <= 0:
        return 0
    dp = [[1 for _ in range(len(bills))] for _ in range(amount + 1)]
    for amt in range(1, amount+1):
        for j in range(len(bills)):
            bill = bills[j]
            if amt - bill >= 0:
                x = dp[amt - bill][j]
            else:
                x = 0
            if j >= 1:
                y = dp[amt][j-1]
            else:
                y = 0
            dp[amt][j] = x + y
    return dp[amount][len(bills)-1]


print(countways_bottomup([1, 2, 5], 5))


def countways_bottomup_optimized(bills, amount):
    '''
        Solution 4: bottom-up optimized
            time complexity O(Cn)
            space complexity O(C)
    '''
    dp = [1 for _ in range(amount + 1)]
    for j in range(len(bills)):
        thiscol = [1 for _ in range(amount + 1)]
        for amt in range(1, amount + 1):
            bill = bills[j]
            if amt - bill >= 0:
                x = thiscol[amt - bill]
            else:
                x = 0
            if j >= 1:
                y = dp[amt]
            else:
                y = 0
            thiscol[amt] = x + y
        dp = thiscol
    return dp[amount]


print(countways_bottomup_optimized([1, 2, 5], 5))
