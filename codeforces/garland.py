from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    r,g,b = map(int, stdin.readline().split())
    if max(r-g-b,g-r-b,b-r-g) < 2:
        stdout.write("Yes\n")
    else:
        stdout.write("No\n")
