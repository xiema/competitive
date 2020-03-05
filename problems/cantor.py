from decimal import *
import sys

CantorTable = { 0 : True, 1 : True}

def IsCantor (i):
    if i not in CantorTable:
        j = i * 3
        if j >= 2:
            CantorTable[i] = True
            CantorTable[i] = IsCantor(j-2)
        elif j < 1:
            CantorTable[i] = True
            CantorTable[i] = IsCantor(j)
        else:
            return False
    return CantorTable[i]


if __name__ == "__main__":
    out = []
    while True:
        s = input()
        if s == "END":
            break
        if IsCantor(Decimal(s)):
            out.append("MEMBER")
        else:
            out.append("NON-MEMBER")
    print("\n".join(out))
    #with open(sys.path[0] + "\\cantor.out", "w") as file:
    #    file.write("\n".join(out))
