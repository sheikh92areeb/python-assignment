def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

result = factorial(6)

print(result)