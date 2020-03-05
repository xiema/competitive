from sys import stdin,stdout
t = int(stdin.readline().strip())
for _ in range(t):
    n,comp = stdin.readline().split()
    n = int(n)
    clist = []
    last,cnt = None,0
    lt = 0
    for i in range(len(comp)):
        if comp[i] == '<':
            lt+=1
        if last:
            if comp[i] != last:
                clist.append((last, cnt))
                cnt=0
        last = comp[i]
        cnt+=1
    else:
        clist.append((last, cnt))

    i,j = 0,0
    sht,lng = [],[]
    for c,v in clist:
        if c == '<':
            for x in range(i+1,i+v+1):
                lng.append(str(x))
            for x in range(lt-i-v+1,lt-i+1):
                sht.append(str(x))
            i+=v
        else:
            for _ in range(v):
                s = str(n-j)
                sht.append(s)
                lng.append(s)
                j+=1
    else:
        s = str(n-j)
        sht.append(s)
        lng.append(s)
    stdout.write("{}\n{}\n".format(' '.join(sht),' '.join(lng)))
