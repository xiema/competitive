from sys import stdin, stdout

n,m = map(int, stdin.readline().split())
leads = {}
for i in range(1,m+1):
    vs = list(map(int,stdin.readline().split()))
    base = vs[-1]
    for j in range(n-1):
        leads.setdefault(j, []).append((vs[j]-base, i))

ans = None
for llist in leads.values():
    llist.sort(reverse=True)
    lsum = 0
    idx = m
    for i,l in enumerate(llist):
        lsum += l[0]
        if lsum < 0:
            idx = i
            break
    if not ans or m-idx < len(ans):
        ans = llist[idx:]


stdout.write("{}\n".format(len(ans)))
stdout.write(' '.join(str(l[1]) for l in ans))
