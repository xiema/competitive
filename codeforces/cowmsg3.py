from collections import Counter

s = input().strip()
cnt = Counter()
cnt2 = Counter()

for c in s:
    cnt[c]+=1
mx = max(cnt.values())
for c in s:
    cnt[c]-=1
    for d,v in cnt.items():
        cnt2[c+d]+=v

print(max(mx,max(cnt2.values())))
