from sys import stdin, stdout

n, sx, sy = map(int, stdin.readline().split())
counts = {(1, 0) : 0, (-1, 0) : 0, (0, 1) : 0, (0, -1) : 0}
for _ in range(n):
    x,y = map(int, stdin.readline().split())
    if x > sx:
        counts[(1, 0)]+=1
    elif x < sx:
        counts[(-1, 0)]+=1
    if y > sy:
        counts[(0, 1)]+=1
    elif y < sy:
        counts[(0, -1)]+=1

maxcount, ans = 0, None
for d,v in counts.items():
    if v > maxcount:
        maxcount, ans = v, d

stdout.write("{}\n{} {}".format(maxcount, sx+ans[0], sy+ans[1]))
