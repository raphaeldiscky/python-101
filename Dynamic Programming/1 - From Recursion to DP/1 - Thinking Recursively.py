def countChar(str, char):
    '''
        1 - You catered to the base case when the string is empty
        2 - You did computation for one step and passed the rest of the work to the recursive call.
            Here computation is simply checking if the first character of the string str is character char or not.
    '''
    if len(str) <= 0:
        return -1
    if str[0] == char:
        return 1 + countChar(str[1:], char)
    else:
        return countChar(str[1:], char)


str = "abacada"
char = 'a'
print(countChar(str, char))


def fib(n):
    '''
        fib(0) = 0 -> base case
        fib(1) = 1 -> base case
        fib(n) = fib(n-1) + fib(n-2) -> recursive step

        exponential time complexity for fibo -> O(2^n) 
    '''
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    else:  # recursive step
        return fib(n-1) + fib(n-2)


print(fib(10))
