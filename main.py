import numpy as np
import time

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

def calcul_de_puissance_expo(M,n):
    i=1
    result = M
    while (i < n+1):
            i += 1
            result = np.dot(result,result)
    return result

def calcul_de_puissance(M,n):
    i=1
    result = M
    while (i < n):
        i += 1
        result = np.dot(M,M)
    return result


def puissance(M,n):
    
    if n==1 or n==0:
        return M

    elif np.log2(n).is_integer():
        k=np.log2(n)
        result = calcul_de_puissance_expo(M,k)
        return result

    elif n % 2 == 0:
        k=n/2
        result = puissance(M,k)
        return np.dot(result,result)
    
    else:
        k=n-1
        result = puissance(M,k)
        return np.dot(M,result)
    

def fib_mat(x):
    M = np.array([[1, 1], [1, 0]])
    M = M.astype('float64')
    fib= np.array([1, 0])
    result = np.dot(fib,puissance(M,x))
    return result[0]


n=input('Entrez votre numero :')
start_time = time.time()
print(f'Avec la methode d\'iteration : {fib_iter(int(n))}, avec un temps de : {(time.time() - start_time)*1000} miliseconds')
start_time = time.time()
print(f'Avec la methode reciproque : {fib_rec(int(n))}, avec un temps de : {(time.time() - start_time)*1000} miliseconds')
start_time = time.time()
print(f'Avec la methode matricielle : {fib_mat(int(n))}, avec un temps de : {(time.time() - start_time)*1000} milliseconds')
