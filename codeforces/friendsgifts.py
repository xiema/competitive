from sys import stdin, stdout

n = int(stdin.readline().strip())
flist = list(map(int, stdin.readline().split()))
avail = set([i for i in range(1,n+1)])
unpaired = set()
for i,v in enumerate(flist):
    if v:
        avail.remove(v)
    else:
        unpaired.add(i+1)

dupl = unpaired.intersection(avail)
if dupl:
    if len(dupl) > 1:
        avail -= dupl
        unpaired -= dupl
        f1 = first = dupl.pop()
        while dupl:
            f2 = dupl.pop()
            flist[f1-1] = f2
            f1 = f2
        flist[f1-1] = first
    else:
        f1, other = dupl.pop(), None
        for f2 in avail:
            if f1 != f2:
                other = flist[f1-1] = f2
                break
        avail.remove(other)
        unpaired.remove(f1)

for f1 in unpaired:
    f2 = avail.pop()
    flist[f1-1] = f2

stdout.write(' '.join(map(str, flist)))
