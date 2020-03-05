out = []
while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    ints = list(map(int, input().split()))
    sets = ints[:]
    fitness = 0
    for i in ints:
        fitness = (fitness + i) % M
    for K in range(2,N+1):
        _fitness = 0
        _sum = sets[N-K+1]
        for i in range(N-K, -1, -1):
            _sum, sets[i] = (_sum + sets[i]) % M, (ints[i] * _sum) % M
            _fitness = (_fitness + sets[i]) % M
        if _fitness > fitness:
            fitness = _fitness

    out.append(str(fitness))

print('\n'.join(out))
