'''
    input:
        weights = [1, 2, 4, 6]
        prices = [4, 2, 4, 7]
        capacity =  7
    output:
        knapsack(weights, prices, capacity) = 11

    TOP DOWN approach:
        - subproblems are evaluated before the main problem
        - call is made to the main problem before the subproblem
'''


def solveKnapsack_rec(weights, prices, capacity, index):
    # simple recursion solution:
    # time complexity O(2^n)
    if capacity <= 0 or index >= len(weights):
        return 0
    # if weight at index-th position is greater than capacity, skip this object
    if weights[index] > capacity:
        return solveKnapsack_rec(weights, prices, capacity, index+1)
    # recursive call, either we can include the index-th object or we cannot,
    # we check both possibilities and return the most optimal one using max
    return max(prices[index] + solveKnapsack_rec(weights, prices, capacity - weights[index], index+1),
               solveKnapsack_rec(weights, prices, capacity, index+1))


def knapsack_rec(weights, prices, capacity):
    return solveKnapsack_rec(weights, prices, capacity, 0)


def solveKnapsack(weights, prices, capacity, index, memo):
    # DP solution:
    # time complexity O(C*n), C = capacity
    if capacity <= 0 or index >= len(weights):
        return 0
    # check for solution in memo table
    if (capacity, index) in memo:
        return memo[(capacity, index)]
    if weights[index] > capacity:
        # store result in memo table
        memo[(capacity, index)] = solveKnapsack(
            weights, prices, capacity, index+1, memo)
        return memo[(capacity, index)]

    memo[(capacity, index)] = max(prices[index]+solveKnapsack(weights, prices, capacity - weights[index], index+1, memo),
                                  solveKnapsack(weights, prices, capacity, index + 1, memo))
    return memo[(capacity, index)]


def knapsack(weights, prices, capacity):
    memo = {}
    return solveKnapsack(weights, prices, capacity, 0, memo)


print(knapsack([2, 1, 1, 3], [2, 8, 1, 10], 4))
