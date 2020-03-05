from math import ceil
from collections import Counter

s = input().strip()
cnt = Counter()
slen = len(s)
sub = [[] for _ in range(slen)]
for i in range(slen):
    #arithmetic seq begin chars
    for itv in range(i+1,slen-i):
        sub[itv].append(s[i])
    cnt[s[i]] += 1
    for itv in range(1,i+1):
        substr = sub[itv][i%itv] + s[i]
        for j in range(len(substr)-1):
            cnt[substr[j:]] += 1
        sub[itv][i%itv] = substr
print(max(cnt.values()))
