from sys import stdin, stdout

n = int(stdin.readline().strip())
friends = list(map(int, stdin.readline().split()))
friends.sort()
groups = []

occ_max, occ_min = 0, 0
start, end, possible_occ, count = friends[0],friends[0],0,0
prevsingle = None
occ = set()
for f in friends:
    if f > end+1:
        if possible_occ > 1:
            if start-1 not in occ:
                occ.add(start-1)
                occ_max+=1
            if end+1 not in occ:
                occ_max += 1
                occ.add(end+1)
        elif possible_occ > 0:
            groups.append((start, end))
        add = end-start+1
        occ_max += add

        if add == 1:
            if not prevsingle or start-prevsingle > 2:
                occ_min +=1
                prevsingle = end
        else:
            occ_min += add//3
            if add%3 == 1:
                if not prevsingle or start-prevsingle > 2:
                    prevsingle = end
                    occ_min +=1
            elif add%3 == 2:
                occ_min +=1
                if prevsingle and start-prevsingle == 2:
                    prevsingle = end

        end = start = f
        count = 1
        possible_occ = 0
    else:
        if end == f:
            count += 1
            if count > 1:
                possible_occ += 1
        else:
            count = 1
        end = f
else:
    if possible_occ > 1:
        if start-1 not in occ:
            occ.add(start-1)
            occ_max+=1
        if end+1 not in occ:
            occ_max += 1
            occ.add(end+1)
    elif possible_occ > 0:
        groups.append((start, end))
    add = end-start+1
    occ_max += add

    occ_min += add//3
    if add%3 == 1:
        if not prevsingle or start-prevsingle > 2:
            prevsingle = end
            occ_min +=1
    elif add%3 == 2:
        occ_min +=1
        if prevsingle and start-prevsingle == 2:
            prevsingle = end

for g in groups:
    if g[0]-1 not in occ:
        occ_max+=1
    elif g[1]+1 not in occ:
        occ_max+=1
        occ.add(g[1]+1)

stdout.write("{} {}".format(occ_min, occ_max))
