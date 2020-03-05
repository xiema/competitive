from sys import stdin, stdout
from math import ceil

maxint = int(1e9)

m = int(stdin.readline().strip())
lines = []

for case in range(m):
    #print("***{}***".format(case))
    n,T,a,b = map(int, stdin.readline().split())
    diff = list(map(int,stdin.readline().split()))
    mand = list(map(int,stdin.readline().split()))
    tests = []
    for i,v in enumerate(diff):
        if v==0:
            tests.append((mand[i], a))
        else:
            tests.append((mand[i], b))
    tests.sort()

    time = 0
    ans1,ans2 = -1,-1
    peek_time, peek_prev = 0, tests[0][0]
    i = 0
    while True:
        if i == len(tests):
            break


        t1,t2 = tests[i],None
        if i != len(tests)-1:
            t2 = tests[i+1]

        #print(i, t1, t2, time, ans, peek_time, ans2)

        if t1[1] < b:
            _time = peek_time + t1[1]
            if _time <= T:
                if _time < peek_prev:
                    ans2 += 1
            peek_time = _time


        _time = time + t1[1]
        if _time <= T:
            if not t2 or _time < t2[0]:
                ans1 = i
                if t
                peek_time = _time
                if t2:
                    peek_prev = t2[0]
        time = _time

        i+=1

        if time >= T and peek_time > T:
            break

    lines.append("{}\n".format(max(ans1,ans2)+1))

stdout.writelines(lines)
