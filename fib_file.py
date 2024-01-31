def fib(n):
    f = [0]*n
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f

print(fib(5))
