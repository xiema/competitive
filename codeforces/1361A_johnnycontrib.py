from sys import stdin

n,m = map(int, stdin.readline().split())
g = {}
for _ in range(m):
    a,b = map(int, stdin.readline().split())
    g.setdefault(a,set()).add(b)
    g.setdefault(b,set()).add(a)

tlist = list(map(int,stdin.readline().split()))

for v in g:
    
