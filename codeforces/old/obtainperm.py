n,m = map(int, input().split())
mtx = []
for _ in range(n):
    mtx.append(list(map(int,input().split())))

total = 0
for i in range(m):
    cnt = {}
    for j in range(n):
        if (mtx[j][i]-i-1)%m == 0:
            pos = (mtx[j][i]-1)//m
            if pos < n:
                c = (j-pos)%n
                cnt[c] = cnt.get(c,0)+1
    add = n
    for k,v in cnt.items():
        add = min(add, k+n-v)
    total+=add

print(total)
