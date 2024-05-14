# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
# Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friendlist(x):
  friends = []
  for i in list(x):
    if len(i) == 4:
      friends.append(i)
  return friends

print(friendlist(["Ryan", "Kieran", "Jason", "Yous"]))

def friendlist(x):
  return [i for i in x if len(i) == 4]

print(friendlist(["Ryan", "Kieran", "Jason", "Yous"]))
