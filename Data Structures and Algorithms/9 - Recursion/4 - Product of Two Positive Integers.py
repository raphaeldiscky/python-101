def recursive_multiply(x, y):
    if x < y:
        # prevent "maximum recursion depth exceeded in comparison"
        # whenever the depth of the recursion tree exceeds a limit
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)


x = 500
y = 2000

print(x * y)
print(recursive_multiply(x, y))
