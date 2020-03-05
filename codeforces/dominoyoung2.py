from sys import stdin,stdout

n = int(stdin.readline().strip())
alist = list(map(int,stdin.readline().split()))
k = max(alist)
total,odd,even = 0,0,0
for i,a in enumerate(alist):
    total += a//2
    if a%2:
        if i%2:
            odd+=1
        else:
            even+=1
total+=min(odd,even)
print(total)
