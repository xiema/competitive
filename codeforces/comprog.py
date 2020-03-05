n = int(input().strip())

for _ in range(n):
    x = input().strip()
    z,e = False,False
    if int(x)%3==0:
        i=0
        while i<len(x) and (not z or not e):
            if not z and x[i]=='0':
                z = True
                i+=1
                continue
            if int(x[i])%2==0:
                e = True
            i+=1
    if z and e:
        print("red")
    else:
        print("cyan")
