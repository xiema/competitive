from sys import stdin,stdout
from bisect import bisect

t = int(stdin.readline().strip())
for _ in range(t):
    n,p,k = map(int, stdin.readline().split())
    goods = list(map(int, stdin.readline().split()))
    goods.sort()
    sum = [0 for i in range(k)]
    c = k
    total = 0
    for i,v in enumerate(goods):
        sum[i%k]+=v
        if sum[i%k] > p:
            c-=1
            total = i
            if c == 0:
                break
    stdout.write("{}\n".format(total))
