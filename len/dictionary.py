# pythons = {
#   'Chapman': 'Graham',
#   'Cleese': 'John',
#   'Idle': 'Eric',
#   'Jones': 'Terry',
#   'Palin': 'Michael',
# }

# pythons['Gilliam'] = 'Gerry'
# print(pythons)
# pythons['Gilliam'] = 'Terry'
# print(pythons)
# a = pythons['Chapman']
# print(a)
# b = pythons.get('Jones')
# print(b)
# all_keys = list(pythons.keys())
# print(all_keys)
# all_value = list(pythons.values())
# print(all_value)
# all_keys_values = list(pythons.items())
# print(all_keys_values)

# print(len(pythons))

# del(pythons['Cleese'])
# print(pythons)

# print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))
# s = set((1, 2, 3, 'eee'))
# print(s)
# s.add(5)
# print(s)
# s.remove('eee')
# print(s)

# furniture = set(('sofa', 'ottoman', 'table'))
# for i in furniture:
#   print(i)

# drinks = {
#   'martini': {'vodka', 'vermouth'},
#   'black russian': {'vodka', 'kahlua'},
#   'white russian': {'cream', 'kahlua', 'vodka'},
#   'manhattan': {'rye', 'vermouth', 'bitters'},
#   'screwdriver': {'orange juice', 'vodka'}
# }

e2f = {
  'dog': 'chien',
  'cat': 'chat',
  'walrus': 'morse',
}

for i, j in e2f.items():
  print(f"{i}/{j}")


f2e = {}
for i, j in e2f.items():
  f2e[j] = i

keys = set(e2f.keys())
# print(keys)

life = {
  'animals': {
    'cats': ['Henri', 'Grumpy', 'Lucy'],
    'octopi': {},
    'emus': {}
  },
  'plants': {},
  'other': {}
}

# print(life)
# print(life['animals']['cats'])

squares = {x: x**2 for x in range(10)}
print(squares)

odd = {x for x in range(10) if x % 2 != 0}
print(odd)

a = ('optimist', 'pessimist', 'troll')
b = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

c = dict(zip(a, b))
print(c)

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

movies = dict(zip(titles, plots))
print(movies)


