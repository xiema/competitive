from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))

    pairs = {}
    i,j = 0,n-1
    while i < (n-1)/2:
        pairs[(a[i],a[j])] = pairs.get((a[i],a[j]),0) + 1
        i,j = i+1,j-1

    ans = 'yes\n'
    i,j = 0,n-1
    while i < (n-1)/2:
        if (b[i],b[j]) in pairs and pairs[(b[i],b[j])] > 0:
            pairs[(b[i],b[j])] -= 1
        elif (b[j],b[i]) in pairs and pairs[(b[j],b[i])] > 0:
            pairs[(b[j],b[i])] -= 1
        else:
            ans = 'no\n'
            break
        i,j = i+1,j-1

    if n%2 and a[(n-1)//2] != b[(n-1)//2]:
        ans = 'no\n'

    stdout.write(ans)
