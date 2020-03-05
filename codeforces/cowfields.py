from sys import stdin,stdout
from collections import deque
n,m,k = map(int,stdin.readline().split())
alist = list(map(int,stdin.readline().split()))
cnx = {}
for _ in range(m):
    x,y = map(int,stdin.readline().split())
    cnx.setdefault(x,[]).append(y)
    cnx.setdefault(y,[]).append(x)

visited = [False for _ in range(n+1)]
next = deque([[1]])
short = None
path = []
scan = set(alist)
while not short or len(path) < k:
    p = next.popleft()
    v1 = p[-1]
    if visited[v1]:
        continue
    if v1 == n:
        short = p
    if v1 in scan:
        path.append((v1, p.copy()))
    visited[v1] = True
    for v2 in cnx[v1]:
        if not visited[v2]:
            pp = p.copy()
            pp.append(v2)
            next.append(pp)
fpos = {v : i for i,v in enumerate(short)}
fdist = {}
for a,p in path:
    d = 0
    for v in reversed(p):
        if v in fpos:
            fdist[a]=(fpos[v],d)
            break
        elif v in fdist:
            fdist[a]=(fdist[v][0],fdist[v][1]+d)
            break
        d+=1

#flist = sorted(fdist.values())
flist = list(fdist.values())
#print(flist)
i,j=0,1
hi = flist[i][1]+flist[j][1]-(flist[j][0]-flist[i][0])
for k in range(2,len(flist)):
    d1 = flist[i][1]+flist[k][1]-(flist[k][0]-flist[i][0])
    d2 = flist[j][1]+flist[k][1]-(flist[k][0]-flist[j][0])
    if d1>d2:
        if d1>=hi:
            j,hi=k,d1
    else:
        if d2>=hi:
            i,j,hi = j,k,d2
    #print(f1,f2,d)
    hi = d if not hi else max(hi,d)

#print(short,hi)
stdout.write(str(min(0,hi+1)+len(short)-1))
