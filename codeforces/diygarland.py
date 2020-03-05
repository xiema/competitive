from sys import stdin, stdout
from bisect import insort_right

n = int(stdin.readline().strip())
rank = list(map(int, stdin.readline().split()))
root = rank[0]

rank_dict = {}
for r in rank:
    rank_dict[r] = rank_dict.get(r, 0) + 1

lamps = []
for i in range(1,n+1):
    if i not in rank_dict:
        lamps.append((i, i))
        rank_dict[i] = 0

stdout.write("{}\n".format(root))
possible = True
aux = set()
for r in reversed(rank):
    idx, found = None, False
    for i,l in enumerate(lamps):
        if l[1] != r:
            if rank_dict[l[1]] == 0:
                idx = i
                found = True
                break
    if not found:
        possible = False
        break
    stdout.write("{} {}\n".format(r, lamps[idx][1]))
    rank_dict[r] -= 1
    imp = lamps[idx][0]
    del lamps[idx]
    if r not in aux:
        insort_right(lamps, (max(imp, r), r), idx)
        lamps.sort()
        aux.add(r)
