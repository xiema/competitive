from sys import stdin,stdout

s = stdin.readline().strip()
segs = []

cur,count = s[0],0
for c in s:
    if cur == c:
        count+=1
    else:
        segs.append((cur,count))
        cur,count = c,1
else:
    segs.append((cur,count))

l = len(segs)
ans = False
if l%2:
    if segs[l//2][1] >= 2:
        i,j = l//2-1,l//2+1
        ans = True
        while i>=0:
            if segs[i][0] == segs[j][0] and segs[i][1]+segs[j][1] >= 3:
                i-=1
                j+=1
                continue
            ans=False
            break

if ans:
    stdout.write("{}\n".format(segs[l//2][1]+1))
else:
    stdout.write("0\n")
