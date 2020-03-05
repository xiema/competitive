from sys import stdin, stdout
from collections import namedtuple, deque

Solution = namedtuple("Solution", ['time', 'ans', 'count', 'limit'])

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
    ans = 0
    i = 0
    sols = deque([Solution(0,0,0,T+1)])

    default = (maxint, 0)
    while i < len(tests) and sols:

        t1,t2 = tests[i],default
        if i != len(tests)-1:
            t2 = tests[i+1]

        #print(i, t1, t2, time, ans, peek_time, ans2)

        if t1[1] < b:
            c = len(sols)
            for _ in range(c):
                sol = sols.popleft()
                _time = sol.time + t1[1]
                if _time < sol.limit:
                    _ans = sol.ans
                    _count = sol.count + 1
                    if _time < t2[0]:
                        _ans = _count
                        ans = max(ans, _ans)
                    sols.append(Solution(_time, _ans, _count, sol.limit))
                else:
                    ans = max(ans, sol.ans)


        else:
            c = len(sols)
            for _ in range(c):
                sol = sols.popleft()
                _count = sol.count
                _time = sol.time
                _ans = sol.ans
                _time += t1[1]
                if sol.time < t1[0]:
                    sols.append(Solution(sol.time, sol.ans, sol.count, min(sol.limit, t1[0])))
                if _time < sol.limit:
                    _count += 1
                    if _time < t2[0]:
                        _ans = _count
                        ans = max(ans, _ans)
                    sols.append(Solution(_time, _ans, _count, sol.limit))



        i+=1

    lines.append("{}\n".format(ans))

stdout.writelines(lines)
