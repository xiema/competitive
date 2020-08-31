from sys import stdin

w,l = map(int, stdin.readline().split())
a = [0] + list(map(int, stdin.readline().split()))

c = [0 for _ in range(w)]
i,j = 1,1
C = 0
while j <= l:
    c[j] = a[j]
    a[j] = 0
    j+=1

while i < w:
    while j<w and a[j]==0:
        j+=1
    if j-i > l:
        i+=1
        continue
    if j==w:
        C+=c[i]
        c[i]=0
    else:
        d = min(c[i],a[j])
        c[i]-=d
        a[j]-=d
        c[j]+=d
    if c[i]==0:
        i+=1

print(C)
