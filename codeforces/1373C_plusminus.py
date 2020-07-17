from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    s = stdin.readline().strip()
    cur,res = 0,0
    for i in range(len(s)):
        if s[i] == '+':
            cur += 1
            res += 1
        elif cur > 0:
            cur -= 1
            res += 1
        else:
            res += i + 2
    stdout.write("{}\n".format(res))
