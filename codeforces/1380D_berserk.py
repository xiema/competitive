from sys import stdin

n,m = map(int, stdin.readline().split())
x,k,y = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
fire = x < k*y

c,hi,limit = 0,False,b[0]
j = 0
M = 0
for i in range(n):
    if j < m and a[i] == b[j]:
        if hi:
            if c < k:
                M = -1
                break
            else:
                M += x
                c -= k
        if fire:
            M += x*(c//k)+y*(c%k)
        else:
            M += c*y
        j+=1
        if j<m:
            limit = max(b[j-1],b[j])
        else:
            limit = b[j-1]
        c,hi = 0,False
    else:
        c+=1
        if a[i] > limit:
            hi = True
else:
    if j < m or hi and c < k:
        M = -1
    else:
        if hi:
            M += x
            c -= k
        if fire:
            M += x*(c//k)+y*(c%k)
        else:
            M += c*y

print(M)
