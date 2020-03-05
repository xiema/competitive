from array import array

n,m = map(int,input().split())
msgs = list(map(int,input().split()))

seen = set()
for msg in msgs:
    seen.add(msg)

cur = [i for i in range(n,0,-1)]
states = [array('I', cur)]
c = n
for msg in msgs:
    cur.remove(msg)
    cur.append(msg)
    states.append(array('I',cur[:c]))
    c-=1

maxpos = {}
i,j = m,0
while j < n:
    #print(i,j)
    if states[i][j] not in maxpos:
        maxpos[states[i][j]] = n-j
    i -= 1
    if i < 0:
        j += 1
        i = m-j

lines = []
for i in range(1,n+1):
    a = 1 if i in seen else i
    b = maxpos[i]
    lines.append("{} {}\n".format(a,b))

print(''.join(lines))
