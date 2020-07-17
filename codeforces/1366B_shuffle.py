from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n,x,m = map(int, stdin.readline().split())
    a,b = x,x
    for _ in range(m):
        l,r = map(int, stdin.readline().split())
        if a >= l and a <= r:
            a = min(a,l)
        if b >= l and b <= r:
            b = max(b,r)
    stdout.write('{}\n'.format(b-a+1))
