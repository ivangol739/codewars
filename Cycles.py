def solve(receipts: list):
  result = [i for i in receipts[2::3]]
  return result, len(result)

# print(solve([123, 145, 346, 246, 235, 166, 112, 351, 342]))

hare_distance = [8, 5, 3, 2, 0, 1, 1, 9]
turtle_distance = [3, 3, 3, 3, 3, 3, 3]

def solve(hare_distance, turtle_distance):
  hare_all = 0
  for i in hare_distance:
    hare_all += i
  turtle_all = 0
  for j in turtle_distance:
    turtle_all += j
  if hare_all > turtle_all:
    result = 'заяц'
  elif turtle_all > hare_all:
    result = 'черепаха'
  else:
    result = 'одинаково'
  return result

print(solve(hare_distance, turtle_distance))