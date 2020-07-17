from sys import stdin

n = int(stdin.readline().strip())
alist = list(map(int,stdin.readline().split()))
blist = list(map(int,stdin.readline().split()))

pos = {}
for i in range(len(blist)):
    pos[blist[i]] = i

counts, ans = {}, 0
for i in range(len(alist)):
    d = (pos[alist[i]]-i)%n
    counts[d] = counts.get(d,0)+1
    ans = max(ans, counts[d])

print(ans)
