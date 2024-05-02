count = 1
while count <= 5:
  print(count)
  count += 1

while True:
  stuff = input('String capitalizw [type q to quet]: ')
  if stuff == 'q':
    break
  
while True:
  value = input("Integer, please [q to quit]: ")
  if value == "q":
    break
  number = int(value)
  if number % 2 == 0:
    continue
  print(number, "squared is", number*number)


word = 'thud'
for letter in word:
  if letter == 'u':
    print(letter)


for i in range(1, 3):
    print('Первый цикл', i)
    for j in range(1, 5):
        print('Второй цикл', j)


# Используйте цикл for, чтобы вывести на экран значения списка [3, 2, 1, 0]
l = [3, 2, 1, 0]

for i in l:
  print(i)

# Присвойте значение 7 переменной guess_me и значение 1 переменной number.
# Напишите цикл while, который сравнивает переменные number и guess_me.
# Выведите строку 'too low', если значение переменной start меньше значения переменной guess_me. Если значение переменной number равно значению
# переменной guess_me, выведите строку 'found it!' и выйдите из цикла. Если
# значение переменной number больше значения переменной guess_me, выведите
# строку 'oops' и выйдите из цикла. Увеличьте значение переменной number на
# выходе из цикла.


guess_me = 7
number = 1

while number <= guess_me:
  if number < guess_me:
    print('to low')
  elif number == guess_me:
    print('found me')
  else:
    print('opps')
    break
  number += 1

# Присвойте значение 5 переменной guess_me. Используйте цикл for для того,
# чтобы проитерировать с помощью переменной number по диапазону range(10).
# Если значение переменной number меньше, чем значение guess_me, выведите
# на экран сообщение 'too low'. Если оно равно значению guess_me — выведите
# сообщение 'found it!', а затем выйдите из цикла. Если значение переменной
# number больше, чем guess_me, выведите на экран сообщение 'oops' и выйдите
# из цикла.

guess_me = 5
for number in range(10):
  if number < guess_me:
    print('to low')
  elif number == guess_me:
    print('found it')
    break
  else:
    print('opps')
    break