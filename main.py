def fib_rec(x):

    if x == 0 or x == 1:
        return 1
    else:
        return fib_rec(x-1)+fib_rec(x-2)

def fib_iter(x):
    if x == 0 or x == 1:
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, x+1):
            c = a + b
            a = b
            b = c
        return c


n=input()
print(fib_iter(int(n)))
print(fib_rec(int(n)))