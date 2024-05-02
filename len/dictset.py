# a = list()
# print(a)

# a = list('cat')
# print(a)

# a = ('cat', 'dog')
# b = list(a)
# print(a)

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# others = ['Gummo', 'Karl']

# marxes.extend(others)
# print(marxes)

# newstr = ', '.join(marxes)
# print(newstr)

# Итерация по списку
cheeses = ['brie', 'gjetost', 'havarti']

for chees in cheeses:
  if chees.startswith('x'):
    print("I won't eat anything that starts with 'x'")
    break
  el