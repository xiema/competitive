from sys import stdin,stdout

n = int(stdin.readline().strip())
lengths = list(map(int, stdin.readline().split()))

rem, total, dist = 0, 0, 0
for l in lengths:
    q,r = divmod(l,2)
    total += q
    if r:
        if rem and dist%2==0:
            total+=1
            rem = 0
            dist = 0
        else:
            rem = r
            dist = 0
    else:
        dist+=1

stdout.write("{}\n".format(total))
