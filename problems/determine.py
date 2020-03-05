from sys import stdin

vals = {}
n = None

def func (i, j):
    #print(i,j)
    if (i,j) in vals:
        return vals[(i,j)]
    if i >= j:
        r = 0
        if i < n:
            r += max([(func(k,1) + func(k,j)) for k in range(i+1,n+1)])
        if j > 1:
            r += max([(func(i,k) + func(n,k)) for k in range(1,j)])
        vals[(i,j)] = r
        return r
    else:
        r = max([(func(i,k) + func(k+1,j)) for k in range(i,j)])
        vals[(i,j)] = r
        return r

out = []
for line in stdin:
    n, a = map(int, line.split())
    vals = { (n,1) : a }
    out.append(str(func(1,n)))

print('\n'.join(out))
