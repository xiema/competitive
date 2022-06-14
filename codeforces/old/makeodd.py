from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    ints = list(map(int, stdin.readline().split()))
    seen = set()
    count = 0
    for i in ints:
        if i in seen:
            continue
        while i not in seen and i%2==0:
            seen.add(i)
            i=i//2
            count+=1
    stdout.write("{}\n".format(count))
