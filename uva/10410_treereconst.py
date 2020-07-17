from sys import stdin,stdout

while True:
    line = stdin.readline().strip()
    if not line:
        break

    n = int(line)
    bfs = list(map(int,stdin.readline().split()))
    dfs = list(map(int,stdin.readline().split()))
    t = { i : set() for i in range(1,n+1) }
    m = { i : 0 for i in range(1,n+1) }

    for i in range(n):
        for j in range(i):
            if bfs[i] > m[bfs[j]]:
                t[bfs[j]].add(bfs[i])
                m[bfs[j]] = bfs[i]

    for i in m:
        m[i] = 0

    for i in range(n):
        for j in range(i):
            if dfs[i] in t[dfs[j]] and dfs[i] < m[dfs[j]]:
                t[dfs[j]].discard(dfs[i])
            else:
                m[dfs[j]] = dfs[i]
        for j in range(i+1,n):
            t[dfs[j]].discard(dfs[i])

    for i in range(1,n+1):
        stdout.write('{}: {}\n'.format(i, ' '.join(str(n) for n in t[i])))
