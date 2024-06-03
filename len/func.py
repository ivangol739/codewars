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

# ---

def answer():
  print(42)

def run_something(fuck):
  fuck()

run_something(answer)

def add_args(arg1, arg2):
  print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
  func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

#  ---
def outer(a, b):
  def inner(c, d):
    return c + d
  return inner (a, b)

print(outer(4, 7))

# ---

def knights2(saying):
  def inner2():
    return f"We are the knights who say: {saying}"
  return inner2

a = knights2('Duck')
print(a())
b = knights2('Hasenpfeffer')
print(b())

# ---

def edit_story(words, func):
  for word in words:
    print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
  return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')


def good(l):
  return l

print(good(['Harry', 'Ron', 'Hermione']))








