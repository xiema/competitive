from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n,m = map(int,stdin.readline().split())
    M = []
    for _ in range(n):
        M.append(list(map(int,stdin.readline().split())))

    counts = {}
    for i in range(n):
        for j in range(m):
            k = i+j
            counts[k] = counts.get(k,0)+M[i][j]

    ans = 0
    s,e,c,d = 0,m+n-2,2,2*min(m,n)
    while s < e:
        a = counts[s]+counts[e]
        ans += min(a,c-a)
        s,e,c = s+1,e-1,min(d,c+2)

    stdout.write('{}\n'.format(ans))
