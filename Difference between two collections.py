a = ['a', 'a', 't', 'e', 'f', 'i', 'j']
b = ['t', 'g', 'g', 'i', 'k', 'f']

def diff(a, b):
  return sorted(set(a) ^ set(b))

print(diff(a, b))