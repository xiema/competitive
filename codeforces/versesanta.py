from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, s = map(int, stdin.readline().split())
    verses = list(map(int, stdin.readline().split()))
    _max, _maxi, _sum = 0, 0, 0
    ans = 0
    for i, v in enumerate(verses):
        if v > _max:
            _max, _maxi = v, i
        _sum += v
        if _sum > s:
            ans = _maxi + 1
            break
    stdout.write("{}\n".format(ans))
