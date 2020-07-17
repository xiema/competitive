from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())

for _ in range(n):
    s = stdin.readline().strip()
    stk = deque()
    correct = True
    for c in s:
        if c == '(' or c == '[':
            stk.append(c)
            continue
        if not stk:
            correct = False
            break
        if stk[-1] == '(' and c == ')' or stk[-1] == '[' and c == ']':
            stk.pop()
            continue
        correct = False
        break
    if correct and not stk:
        stdout.write('Yes\n')
    else:
        stdout.write('No\n')
