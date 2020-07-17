from sys import stdin

n = int(stdin.readline().strip())
s = stdin.readline().strip()
t = stdin.readline().strip()

lvl,M0,M1,prev = 0,0,0,None
for i in range(n):
    if s[i] == t[i]:
        continue
    if not prev:
        prev = s[i]
        lvl = 1
    elif s[i] == prev:
        lvl += 1
    else:
        lvl -= 1
        if lvl == 0:
            prev = None
    if prev == '0':
        M0 = max(M0,lvl)
    else:
        M1 = max(M1,lvl)

if lvl > 0:
    print(-1)
else:
    print(M0+M1)
