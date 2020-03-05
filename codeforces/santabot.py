from sys import stdin, stdout
from math import sqrt


def xgcd (n, b):
    if n == 0:
        return b, 0, 1
    q,r = divmod(b,n)
    g,x,y = xgcd(r, n)
    return g, y-q*x, x

def invmod (n, b):
    g,x,_ = xgcd(n,b)
    if g!= 1:
        raise ArithmeticError
    return x%b

print(invmod(4,998244353))
