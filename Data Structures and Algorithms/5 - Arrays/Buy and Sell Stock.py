'''
    1) Buy and Sell Stock
        profit = selling price - buying price
        a. Solution 1: brute force
        b. Solution 2: tracking min price
'''


def buy_and_sell_once_brute(A):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    max_profit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            # print('i:', i)
            # print('j:', j)
            if A[j]-A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_once_brute(A))


def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit


print(buy_and_sell_once(A))
