from sys import stdin,stdout

M = int(stdin.readline().strip())
for m in range(M):
    line = stdin.readline().split()
    if not line:
        line = stdin.readline().split()
    N,K = map(int,line)
    lt = set([i for i in range(1,N+1)])
    gt = lt.copy()
    for _ in range(K):
        line = list(map(int,stdin.readline().split()))
        p = line[0]
        comp = stdin.readline().strip()
        if comp == '<':
            lt &= set(line[1:1+p])
            gt &= set(line[1+p:])
        elif comp == '>':
            gt &= set(line[1:1+p])
            lt &= set(line[1+p:])
        elif comp == '=':
            gt -= set(line[1:])
            lt -= set(line[1:])

    ans = 0
    if len(lt) <= 1 and len(gt) <= 1:
        if not gt:
            ans = lt.pop()
        elif not lt:
            ans = gt.pop()
        else:
            ans = lt.pop()
            if ans != gt.pop():
                ans = 0
    stdout.write("{}\n".format(ans))


    if m!=M-1:
        stdout.write('\n')
