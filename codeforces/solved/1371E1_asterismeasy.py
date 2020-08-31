from sys import stdin


n,p = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
a.sort()
x = 0
aa = []
j=0
for i in range(n):
    if x+i < a[i]:
        x = a[i]-i
    if a[i]!=a[j]:
        aa.append((a[j], i-j))
        j=i
else:
    aa.append((a[j], n-j))

C = 2000
c,d = 0,0
for i in range(len(aa)):
    if aa[i][0] <= x:
        c+=aa[i][1]
    else:
        _d = aa[i][0]-x
        itv = _d-d
        d = _d
        c = c + aa[i][1] - itv
        if d+c >= p:
            C = min(C, p-1-c)
    if c>= p:
        C=-1
        break

print(C+1)
print(' '.join([str(ans) for ans in range(x,x+C+1)]))
