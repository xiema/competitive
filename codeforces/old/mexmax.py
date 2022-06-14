from sys import stdin, stdout

q,x = map(int, stdin.readline().split())

d = {}
segs = {0 : 0}
lines = []
for _ in range(q):
    i = int(stdin.readline().strip())%x
    d[i] = d.get(i, i-x) + x
    segview = list(segs.keys())
    j = bisect(segview, d[i])
    if j > 0 and segs[segview[j-1]] == d[i]:
        segs[segview[j-1]] += 1
        i = j-1
    else:
        segs[d[i]] = d[i]+1
        i = d[i]
    if j < len(segview) and segs[i] == segview[j]:
        segs[i] = segs[segview[j]]
        del segs[segview[j]]
    lines.append("{}\n".format(segs[0]))

stdout.writelines(lines)
