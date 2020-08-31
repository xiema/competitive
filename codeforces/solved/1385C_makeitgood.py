from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().split()))

    ans = 0
    b = False
    for i in range(n-2,-1,-1):
        if not b:
            if a[i] < a[i+1]:
                b = True
        else:
            if a[i] > a[i+1]:
                ans = i+1
                break

    stdout.write('{}\n'.format(ans))
