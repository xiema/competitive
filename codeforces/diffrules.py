from sys import stdin,stdout

t = int(stdin.readline().strip())
for _ in range(t):
    n,x,y = map(int, stdin.readline().split())
    if x > y:
        x,y = y,x
    a = max(0, (x-1) - max(0,(n-y-1)) + (1 if x!=y and n-y==0 else 0)) + 1
    b = n - max(0, (n-y)-(x-1))
    stdout.write("{} {}\n".format(a, b))
