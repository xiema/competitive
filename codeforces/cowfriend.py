from sys import stdin,stdout
t = int(stdin.readline().strip())
for _ in range(t):
    n,x = map(int,stdin.readline().split())
    alist = set(map(int,stdin.readline().split()))
    mx = 0
    cnt = x+x
    for a in alist:
        mx = max(a,mx)
        if x%a==0:
            cnt = min(x//a,cnt)
    c = max(0,x//mx - 1)
    x -= c*mx
    if x in alist:
        c += 1
    else:
        c += 2
    cnt = min(c,cnt)
    stdout.write("{}\n".format(cnt))
