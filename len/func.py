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

