import numpy as np

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


def puissance(n):
    M = np.array([[1, 1], [1, 0]])
    i = 0
    result= 1
    if n==1 or n==0:
        return 1

    elif np.log2(n) is int:
        k=np.log2(n)
        while (i < k-1):
            i += 1
            M = np.dot(M,M)
        return M

    elif n % 2 == 0:
        k=n/2
        while (i < k+1):
            i += 1
            result = np.dot(M,result)
        return np.dot(result,result)
    else:
        k=n-1
        while (i < k+1):
            i+=1
            result = np.dot(M,result)
        return np.dot(M,result)
def fib_mat(x):
    M = np.array([[1, 1], [1, 0]])
    fib= np.array([0, 1])
    result = np.dot(fib,puissance(x))


    return result[1]


n=input('Please put your number:')
print(fib_iter(int(n)))
print(fib_rec(int(n)))
print(fib_mat(int(n)))
