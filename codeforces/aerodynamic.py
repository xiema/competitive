def get_slopes(v1,v2,v3):
    y1,x1 = (v2[1]-v1[1]),(v2[0]-v1[0])
    y2,x2 = (v3[1]-v2[1]),(v3[0]-v2[0])
    m1 = y1/x1
    m2 = y2/x2
    return (m1,m2,y1*y1+x1*x1,y2*y2+x2*x2)

n = int(input().strip())
b = False
if n%2==0:
    verts = []
    for _ in range(n):
        verts.append(tuple(map(int,input().split())))
    delta = []
    for i in range(n):
        j = (i+1)%n
        delta.append((abs(verts[j][0]-verts[i][0]),abs(verts[j][1]-verts[i][1])))
    b=True
    for i in range(n):
        j = (i+n//2)%n
        if delta[i] != delta[j]:
            b = False
            break

print(["NO","YES"][b])
