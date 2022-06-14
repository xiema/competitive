from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())
chars = {}
for _ in range(n):
    s = stdin.readline().strip()
    base = set([c for c in s])
    for c in s:
        chars.setdefault(c,set()).update(base)
seen = set(chars.keys())
count = 0
while seen:
    c = seen.pop()
    next = deque([c])
    while next:
        c = next.popleft()
        for cc in chars[c]:
            if cc in seen:
                seen.remove(cc)
                next.append(cc)
    count+=1

stdout.write("{}\n".format(count))
