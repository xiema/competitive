from sys import stdin,stdout
from math import

T = int(stdin.readline().strip())

for _ in range(T):
    h,c,t = map(int, stdin.readline().split())
    a = (h+c)/2
    i,j = 3,ceil((t-a)/h)
    while i!=j:
        k = (i+j)//2
        if
