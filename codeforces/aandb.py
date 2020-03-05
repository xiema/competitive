from sys import stdin, stdout
t = int(stdin.readline().strip())

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    diff = abs(a-b)
    ans, cur = 0, 0
    while cur < diff or (cur-diff)%2 == 1:
        ans += 1
        cur += ans

    stdout.write("{}\n".format(ans))
