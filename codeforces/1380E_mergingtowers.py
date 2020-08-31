from sys import stdin,stdout

n,m = map(int, stdin.readline().split())
t = list(map(int, stdin.readline().split()))
T = [[] for _ in range(m+1)]
Ti = [i for i in range(m+1)]
L = [0 for _ in range(m+1)]
C = 0
for i in range(n):
    if i > 0 and t[i] != t[i-1]:
        C+=1
    T[t[i]].append(i)
    L[t[i]]+=1

stdout.write('{}\n'.format(C))

for _ in range(m-1):
    a,b = map(int, stdin.readline().split())
    if L[b] > L[a]:
        for i in T[a]:
            if i>0 and Ti[t[i-1]] == b:
                C-=1
            if i<n-1 and Ti[t[i+1]] == b:
                C-=1
    else:
        for i in T[b]:
            if i>0 and Ti[t[i-1]] == a:
                C-=1
            if i<n-1 and Ti[t[i+1]] == a:
                C-=1
    Ti[b] = Ti[a]
    L[a] += L[b]

    stdout.write('{}\n'.format(C))
