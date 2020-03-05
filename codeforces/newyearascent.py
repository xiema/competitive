from sys import stdin,stdout

n = int(stdin.readline().strip())
seqmin, seqmax, asccount = [], [], 0
for _ in range(n):
    seq = list(map(int,stdin.readline().split()[1:]))
    imin,imax = -1,-1
    asc = False
    for i in seq:
        if imin < 0:
            imin = i
        else:
            if i > imin:
                asc = True
            imin = min(imin,i)
        if imax < 0:
            imax = i
        else:
            imax = max(imax,i)
    if asc:
        asccount+=1
    else:
        seqmin.append(imin)
        seqmax.append(imax)
seqmin.sort(reverse=True)
seqmax.sort(reverse=True)


total = asccount*n + (n-asccount)*asccount
i = 0
for imin in seqmin:
    while i<len(seqmax) and seqmax[i] > imin:
        i+=1
    total += i

stdout.write(str(total))
