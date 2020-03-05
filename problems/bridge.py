import sys

if __name__ == "__main__":
    C = int(input())
    all = []
    for i in range(C):
        input()
        P = int(input())
        people = []
        for j in range(P):
            people.append(int(input()))

        if P == 1:
            all.append("{0}\n{0}".format(people[0]))
            continue

        people.sort()
        out = []
        time = 0
        p1, p2 = people[0], people[1]
        j = P-1

        s1 = "{0} {1}\n{0}\n{2} {3}\n{1}"
        s2 = "{0} {1}\n{0}\n{0} {2}\n{0}"

        while True:
            if j == 2:
                out.append("{0} {1}\n{0}\n{0} {2}".format(people[0], people[1], people[2]))
                time += people[0] + people[1] + people[2]
                break
            elif j == 1:
                out.append("{0} {1}".format(people[0], people[1]))
                time += people[1]
                break

            p3, p4 = people[j-1], people[j]
            t1, t2 = p2 + p1 + p4 + p2, p3 + p1 + p4 + p1
            if t1 < t2:
                time += t1
                out.append(s1.format(p1,p2,p3,p4))
            else:
                time += t2
                out.append(s2.format(p1,p3,p4))
            j -= 2

        all.append("{}\n".format(time) + "\n".join(out))

    print("\n\n".join(all))
    #with open(sys.path[0] + "\\bridge.out", 'w') as file:
        #file.write("\n\n".join(all))
