'''
    Dynamic programming solution

    Prerequisites:
        - optimal substructure = optimal solution to a problem can be built using the optimal solutions to that
                                 problems's subproblems.

            permutations("abc") uses optimal output of permutations("ab")

        - overlapping subproblems = dp is all about avoiding recomputations.

            permutations("abcd") makes call to permutations("abc") and permutations("abd"), both pf which will
            use result of permutations("ab")

        * problem depending on subproblems does not mean an optimal substructure
'''
calculated = {}


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n in calculated:
        return calculated[n]
    else:
        calculated[n] = fib(n-1) + fib(n-2)
        return calculated[n]


print(fib(10))
