from sys import stdin
from bisect import bisect

def maxlength(a, b, i, j):


t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    a = list(map(int,stdin.readline().split()))

    pos = {}
    for i in range(n):
        pos.setdefault(a[i], []).append(i)
