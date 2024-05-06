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
# cheeses = ['brie', 'gjetost', 'havarti']

# for chees in cheeses:
#   if chees.startswith('x'):
#     print("I won't eat anything that starts with 'x'")
#     break
#   else:
#     print(chees)

years_list = [1996, 1997, 1998, 1999, 2000]
things = ["mozzarella", "cinderella", "salmonella"]

things[1] = things[1].capitalize()
print(things)
# print(years_list[3])
# print(max(years_list))
things[0] = things[0].upper()
print(things)
del(things[2])
print(things)

surprice = ['Groucho', 'Chico', 'Harpo']
new_surprice = surprice[-1][0].lower() + surprice[-1][1:]
print(new_surprice)
new_surprice = surprice[-1][-1].upper() + surprice[-1][-2:0:-1] + surprice[-1][0].lower()
print(new_surprice)

even = []

for i in range(2, 10, 2):
  even.append(i)

print(even)


start1 = ["fee", "fie", "foe"]

rhymes = [
  ("flop", "get a mop"),
  ("fope", "turn the rope"),
  ("fa", "get your ma"),
  ("fudge", "call the judge"),
  ("fat", "pet the cat"),
  ("fog", "walk the dog"),
  ("fun", "say we're done"),
]

start2 = "Someone better"

for first, second in rhymes:
  for word in start1:
    print(word.capitalize() + '!', end=' ')
  print(first.capitalize() + '!')

  print(start2, end=' ')
  print(second + '.')