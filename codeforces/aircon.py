from sys import stdin,stdout

def clamp(n, a,b):
    if n > a:
        return a
    elif n < b:
        return b
    return n

q = int(stdin.readline().strip())
for _ in range(q):
    n,m = map(int,stdin.readline().split())
    lo,hi,cur = m,m,0
    possible = True
    for _ in range(n):
        t,l,h = map(int,stdin.readline().split())
        if possible:
            a = t-cur
            b = -a
            lo += clamp(l-lo, a,b)
            hi += clamp(h-hi, a,b)
            if lo > h or hi < l:
                possible = False
            lo,hi = max(lo,l), min(hi,h)
            cur = t
    if possible:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
