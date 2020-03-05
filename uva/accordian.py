class Card():
    def __init__(self, f, s):
        self.face, self.suit = f, s

    def __repr__(self):
        return self.face + self.suit

def match(s1, s2):
    return s1[-1].face == s2[-1].face or s1[-1].suit == s2[-1].suit

def move(s1, s2):
    s2.append(s1.pop())

def display(cards):
    l = len(cards)
    p = " ".join(str(len(s)) for s in cards)
    if (l > 1):
        print("{} piles remaining: {}".format(l,p))
    else:
        print("{} pile remaining: {}".format(l,p))

if __name__ == "__main__":
    while True:
        cards = []
        for i in range(2):
            for c in input().split():
                if c == "#": exit()
                cards.append([Card(c[0],c[1])])
        i = 0
        while (i < len(cards)):
            if (i >= 3):
                if match(cards[i], cards[i-3]):
                    move(cards[i], cards[i-3])
                    if len(cards[i]) == 0:
                        del cards[i]
                    i-=3
                    continue
            if (i >= 1):
                if match(cards[i], cards[i-1]):
                    move(cards[i], cards[i-1])
                    if len(cards[i]) == 0:
                        del cards[i]
                    i-=1
                    continue
            i+=1

        display(cards)

"""
    algorithm

    for each case
        store inputs as stacks of 1 card in a list
        set card stack position cur = 0
        while cur <= last stack position
            if cur-3 >= 0, and cur and cur-3 top cards match
                move top card at cur to cur-3
                if cur stack is empty, remove from list
                set cur = cur-3
                continue loop
            if cur-1 >= 0, and cur and cur-1 top cards match
                move top card at cur to cur-1
                if cur stack is empty, remove from list
                set cur = cur-1
                continue loop
            no matches, set cur = cur+1, continue loop
        print the final arrangement of cards

"""
