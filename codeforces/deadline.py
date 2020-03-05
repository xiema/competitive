from sys import stdin,stdout

def compute(x,d):
    return x + (d//(x+1)) + (d%(x+1)>0)

def check(n,d):
    i,j = 0,n-1
    if compute(i,d) <= n or compute(j,d) <= n:
        return True
    p1,p2 = i+d/(i+1),j+d/(j+1)
    while i < j:
        if j-i <= 3:
            for x in range(i+1,j):
                if compute(x,d) <= n:
                    return True
            return False
        _s = (j-i)//3
        x,y = i+_s,j-_s
        if compute(x,d) <= n or compute(y,d) <= n:
            return True
        p3,p4 = x+d/(x+1),y+d/(y+1)
        if p1 > p2:
            if p3 > p2 and p4 > p2:
                return False
            if p3 > p4:
                i,p1 = x,p3
            else:
                j,p2 = y,p4
        else:
            if p3 > p1 and p4 > p1:
                return False
            if p3 > p4:
                i,p1 = x,p3
            else:
                j,p2 = y,p4
    return False


t = int(stdin.readline().strip())

for _ in range(t):
    n,d = map(int, stdin.readline().split())
    if check(n,d):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
