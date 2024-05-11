def lovefunc(flower1, flower2):
  love = None
  if flower1 % 2 == 0 and flower2 % 2 != 0:
    love = True
  elif flower1 % 2 != 0 and flower2 % 2 == 0:
    love = True
  else:
    love = False
  return love

print(lovefunc(5, 5))
