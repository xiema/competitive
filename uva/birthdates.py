class Person():
  def __init__(self, name, day, month, year):
    self.name = name
    self.day, self.month, self.year = day, month, year

  def __lt__(self, other):
    if self.year < other.year:
      return True
    if self.year == other.year and self.month < other.month:
      return True
    if self.year == other.year and self.month == other.month and self.day < other.day:
      return True
    return False

N = int(input())
p = []
for i in range(N):
  name,day,month,year = input().split()
  p.append(Person(name, int(day), int(month), int(year)))

p.sort()

print(p[-1].name)
print(p[0].name)
