from sys import stdin,stdout

def f(n, m):
    if n==m:
        return (m, 0)
    if n<m:
        r = m%n
        return (m-r, r), (m+n-r, n-r)
    else:
        

t = int(stdin.readline().strip())
for _ in range(t):
    a,b,c = map(int, stdin.readline().split())

    m = c
