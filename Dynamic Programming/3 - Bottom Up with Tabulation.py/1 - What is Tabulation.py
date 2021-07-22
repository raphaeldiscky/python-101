'''
    - recursion is costly in terms of the stack memory and program execution
    - recursion = breaking down of a problem into subproblems until those subproblems were evaluated;
                  and when subproblems were evaluated, the main problem also evaluated.
    - bottom-up = solve subproblems first and then whenever the main problem requires answer to the subproblems,
                  we will return the answer we had already evaluated. 
    - tabulation = technique to store the results of evaluated subproblems in an array
'''


def factorial(n):
    # tabulation table of size n+1
    table = [0]*(n+1)
    # base case of 0! = 1
    table[0] = 1
    # iterate until n
    for i in range(1, n+1):
        # using answer to i-1th problem from tabulation to build answer for ith problem
        table[i] = table[i-1]*i
    # return answer; the nth factorial
    return table[n]


print(factorial(30))


def factorial_rec(n):
    if n == 0:  # base case
        return 1
    return n*factorial(n-1)


print(factorial_rec(30))
