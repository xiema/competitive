from sys import stdin,stdout

memo = {1 : 1}
def f(n):
    if n in memo:
        return memo[n]
    q,c = [n],1
    while n!=1:
        if n%2:
            n = 3*n+1
        else:
            n//=2
        if n in memo:
            c+=memo[n]
            break
        else:
            q.append(n)
            c+=1
    for n in q:
        memo[n] = c
        c-=1
    return memo[q[0]]

while True:
    line = stdin.readline()
    if not line:
        break

    i,j = map(int, line.split())
    l = 0
    for n in range(min(i,j),max(i,j)+1):
        l = max(l, f(n))
    stdout.write('{} {} {}\n'.format(i,j,l))
