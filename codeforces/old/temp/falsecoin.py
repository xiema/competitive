from sys import stdin

M = int(stdin.readline().strip())
for _ in range(M):
    N,K = map(int, stdin.readline().split())
    coins = set(i for i in range(1,N+1))
    for _ in range(K):
        p = list(map(int,stdin.readline().split()))
        c = p[0]
        pa,pb = p[1:1+c],p[1+c:]
        op = stdin.readline().strip()
        if op == '>':
            for p in pb:
                coins.discard(p)
        elif op == '<':
            for p in pa:
                coins.discard(p)
        elif op == '=':
            for p in pb:
                coins.discard(p)
            for p in pa:
                coins.discard(p)
    if len(coins) == 1:
        print(coins.pop())
    else:
        print(0)
