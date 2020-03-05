from sys import stdin, stdout

n = int(stdin.readline().strip())
a = list(map(int, stdin.readline().split()))

c,i,j,prev = 0,-1,1,a[0]
ans = 0
while j < n:
    if a[j] > a[j-1]:
        j+=1
    else:
        ans = max(ans, c+j-i-1)
        if i==-1 or a[i] >= a[i+1]:
            c = j-i-1
        c=j-i-1
        i=j
    i+=1
else:
    ans = max(ans, ca+cb)

stdout.write("{}".format(ans))
