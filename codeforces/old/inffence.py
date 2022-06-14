from sys import stdin,stdout
from math import ceil
t = int(stdin.readline().strip())
for _ in range(t):
    r,b,k = map(int, stdin.readline().split())
    if r > b:
        r,b = b,r
    if ceil((b-1)/r) < k:
        print("OBEY")
    else:
        print("REBEL")
