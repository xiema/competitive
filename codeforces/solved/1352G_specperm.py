from sys import stdin,stdout

t = int(stdin.readline().strip())

p = [
    [3,1,5,2,4],
    [3,1,5,2,4,6],
    [3,1,5,2,6,4,7],
    [3,1,5,2,6,8,4,7],
    [3,1,5,2,6,8,4,7,9]
]

for _ in range(t):
    n = int(stdin.readline().strip())
    a = 0
    A = []
    if n <= 3:
        stdout.write('-1\n')
        continue
    if n == 4:
        stdout.write('3 1 4 2\n')
        continue
    for _ in range(n//5-1):
        for d in p[0]:
            A.append(str(a+d))
        a += 5
    for d in p[n%5]:
        A.append(str(a+d))

    stdout.write(' '.join(A) + '\n')
