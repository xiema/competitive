import re, sys, collections

p_book = re.compile("\"([^\"]+)\" by (.+)")
p_cmd = re.compile("(\w+)( \"([^\"]+)\")?")

class Book():
    def __init__(self, title, author):
        self.key = (author, title)
        self.title = title
        self.author = author
        self.avail = True

if __name__ == "__main__":
    books = []
    while True:
        line = input()
        if line == "END":
            break
        books.append(Book(*p_book.match(line).group(1,2)))
    books.sort(key=lambda b: b.key)
    books_dict = collections.OrderedDict(zip((b.title for b in books), range(len(books))))

    lines = []
    books_return = []

    while True:
        cmd, title = p_cmd.match(input()).group(1,3)
        if cmd == "BORROW":
            i = books_dict[title]
            if books[i].avail:
                books[i].avail = False
            else:
                books_return.remove(i)
        elif cmd == "RETURN":
            books_return.append(books_dict[title])
        elif cmd == "SHELVE":
            books_return.sort()
            for i in books_return:
                books[i].avail = True
                first = True
                if i > 0:
                    for book in books[i-1::-1]:
                        if book.avail:
                            lines.append("Put \"{}\" after \"{}\"".format(books[i].title, book.title))
                            first = False
                            break
                if first:
                    lines.append("Put \"{}\" first".format(books[i].title))
            lines.append("END")
            books_return = []
        elif cmd == "END":
            break

    print('\n'.join(lines))
    path = sys.path[0] + "\\borrowers.out"
    with open(path, "w") as file:
        file.write("\n".join(lines))
