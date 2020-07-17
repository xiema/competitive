from sys import stdin,stdout
from collections import Counter

t = int(stdin.readline().strip())

for _ in range(t):
    n,k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    r = Counter()
    for i in range(n):
        r[k - a[i]%k] +=1

    c = 0
    for i in r:
        if i == k:
            continue
        c = max(c, i + k*(r[i]-1) + 1)

    stdout.write('{}\n'.format(c))
