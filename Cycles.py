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


todo_list = [
    ["Разобрать почту", 1],
    ["Обзвонить клиентов", 2],
    ["Запланировать дела на завтра", 0.6],
    ["Сделать презентацию", 3],
    ["Созвон с командой", 0.5]
]


def solve(to_d0: list, workday: float = 8):
  work_time = 0.0
  for i in todo_list:
    work_time += i[1]
  return workday - work_time
print(solve(todo_list))


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

result = ""

if len(boys) == len(girls):
  boys.sort()
  girls.sort()
  for p in zip(boys, girls):
    result += f"{p[0]} и {p[1]}, "
  result = result[:-2]
else:
  result = 'Кто-то может остаться без пары!'

print(result)


phrases = [
           "нажал кабан на баклажан",
           "дом как комод",
           "рвал дед лавр",
           "азот калий и лактоза",
           "а собака боса",
           "тонет енот",
           "карман мрак",
           "пуст суп"
]

def solve(phrases: list):
    result = []
    for phrase in phrases: # пройдите циклом по всем фразам
      new_phrase = phrase.replace(" ", "")
      if new_phrase == new_phrase[::-1]:
        result.append(phrase)
    return result

print(solve(phrases))