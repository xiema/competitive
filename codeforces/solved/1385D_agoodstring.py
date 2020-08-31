from sys import stdin,stdout
from collections import Counter

t = int(stdin.readline().strip())

next = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(25):
    next[alpha[i]] = alpha[i+1]

for _ in range(t):
    n = int(stdin.readline().strip())
    s = stdin.readline().strip()

    C = {}
    def count(i,l):
        if l == 1:
            cnt = Counter()
            cnt[s[i]]+=1
        else:
            ll = l//2
            cnt = count(i,ll)+count(i+ll,ll)
        C[(i,i+l)] = cnt
        return cnt
    count(0,n)

    def solve(i,j,c):
        if j-i == 1 or c=='z':
            return j-i-C[(i,j)][c]
        l = (j-i)//2
        a1 = l-C[(i,i+l)][c] + solve(i+l,j,next[c])
        a2 = l-C[(i+l,j)][c] + solve(i,i+l,next[c])
        return min(a1,a2)

    ans = solve(0,n,'a')

    stdout.write('{}\n'.format(ans))
