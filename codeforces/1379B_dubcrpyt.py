from sys import stdin,stdout

def bs(s,e,ml,mr):
    i,j = s,e
    while True:
        n = mr//i
        na = n*i
        if na >= ml:
            return i
        if mr-na >= n:
            return i
        k = (i+j)//2
        if e*(mr//k) < ml:
            j = k
        else:
            i = k

t = int(stdin.readline().strip())

for _ in range(t):
    l,r,m = map(int, stdin.readline().split())
    ml,mr = m+l-r,m-l+r
    a = bs(l,r+1,ml,mr)
    d = m-(mr-mr%a)
    if d < 0:
        b,c = r+d,r
    else:
        b,c = l+d,l
    stdout.write('{} {} {}\n'.format(a,b,c))
