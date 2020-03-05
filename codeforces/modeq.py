from sys import stdin, stdout
from collections import deque

n,m = map(int, stdin.readline().split())
alist = list(map(int, stdin.readline().split()))
blist = list(map(int, stdin.readline().split()))



bcounts = {}
for b in blist:
    bcounts[b] = bcounts.get(b, 0) + 1

bcount2i = {}
for i,c in bcounts.items():
    bcount2i.setdefault(c, []).append(i)

acounts = {}
for a in alist:
    acounts[a] = acounts.get(a, 0) + 1

acount2i = {}
for i,c in acounts.items():
    acount2i.setdefault(c, []).append(i)

minc, minalist = None, None
for c,alist in acount2i.items():
    if not minc or len(alist) < len(minalist):
        minc,minalist = c,alist

a = minalist[0]
minbs = deque(bcount2i[minc])

ans = 0
while True:
    b = minbs.popleft()
    if b < a:
        minbs.append(b+m)
        continue
    diff = b-a
    found = True
    for oa,c in acounts.items():
        if bcounts.get((oa+diff)%m, -1) != c:
            found = False
            break
    if found:
        ans = diff
        break

stdout.write("{}".format(ans))
