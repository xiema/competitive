from math import ceil
from collections import Counter

s = input().strip()
cnt = Counter()
slen = len(s)
sub = [[] for _ in range(slen)]

def count (s):
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            cnt[s[i:j]]+=1

for c in s:
    cnt[c]+=1

print(cnt)

count(s)

for itv in range(2,slen):
    slist = [[] for _ in range(itv)]
    for i,c in enumerate(s):
        slist[i%itv].append(c)
    for clist in slist:
        count(''.join(clist))
#print(cnt)
mx = max(cnt.values())
for ss in cnt:
    if cnt[ss] == mx:
        print(ss)
print(mx)
