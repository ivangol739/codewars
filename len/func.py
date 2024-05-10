def do_nothing():
  pass

do_nothing()

# ---

def do_make_a_sound():
  print('quack')

do_make_a_sound()

# ---

def echo(anything):
  return anything + ' ' + anything

print(echo('Rumplestiltskin'))

# ---

def commentary(color):
  if color == 'red':
    return 'Its a tomato.'
  elif color == 'green':
    return 'Its a green pepper.'
  elif color == 'purple':
    return 'I dont know what it is, but only bees can see it.'
  else:
    return  "I've never heard of the color " + color + "."
  
print(commentary('red'))

# ---
def menu(wine, entree, dessert):
  return {'wine': wine, 'entree': entree, 'dessert': dessert}

# print(menu('chardonnay', 'chicken', 'cake'))
print(menu(dessert = '1', wine = "3", entree = '2'))

# ---

def buggy(arg, result=[]):
  result.append(arg)
  print(result)

buggy('a')
buggy('b')

# ---

def nonbuggy(arg, result=None):
  if result==None:
    result = []
  result.append(arg)
  print(result)

nonbuggy('a')
nonbuggy('b')

#  ---

def final_price (*prices, discount=1):
  return [price - price * discount / 100 for price in prices]

print(final_price(100, 200, 300, discount=5))

# ---

def print_kwargs(**kwargs):
  print('Keyword arguments:', kwargs)

print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')






