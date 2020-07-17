from sys import stdin,stdout
from collections import deque

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    alist = stdin.readline().split()

    if len(alist) == 1 or int(alist[0]) < int(alist[-1]):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
