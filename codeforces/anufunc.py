from sys import stdin,stdout
n = int(stdin.readline().strip())
alist = list(map(int,stdin.readline().split()))
cnt = {}
for a in alist:
    k=1
    while k<=a:
        if a&k:
            cnt.setdefault(k,[]).append(a)
        k*=2

mx = None
for k,v in sorted(list(cnt.items()),reverse=True):
    if len(v) == 1:
        mx = v[0]
        break

if mx:
    alist.remove(mx)
    alist.insert(0,mx)

stdout.write(' '.join([str(a) for a in alist]))
