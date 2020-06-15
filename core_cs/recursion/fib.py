def fib(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return fib(value-1) + fib(value-2)


print(fib(10))
