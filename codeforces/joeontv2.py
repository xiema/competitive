n = int(input().strip())

seen = set()
sum = 1
for i in range(2,n+1):
    sum += 1/i

print(sum)
