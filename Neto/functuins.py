import math
from pprint import pprint
# 1

def discriminant(a, b, c):
  return b ** 2 - 4 * a * c


def solution(a, b, c):
  D = discriminant(a, b ,c)
  if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
  elif D == 0:
    x = -b / (2 * a)
    print(x)
  else:
    print("корней нет")

solution(1, 8, 15) 
solution(1, -13, 12)
solution(-4, 28, -49)
solution(1, 1, 1)

# 2
def vote(votes):
  set_count = {ch: 0 for ch in set(votes)}
  for i in votes:
    set_count[i] += 1
  return max(set_count, key=set_count.get)
  
  
  
# 3

# add — функция, которая добавит новый документ в каталог и перечень полок.
# В результате корректного выполнения задания будет выведен следующий результат:

# Аристарх Павлов
# 1
# Документ не найден
# 3
# Александр Пушкин
# Полки с таким документом не найдено

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
  for document in documents:
    if doc_number == document["number"]:
      return document["name"]
  return "Документ не найден"

def get_directory(doc_number):  
  for k, v in directories.items():
    if doc_number in v:
      return k
  return "Полки с таким документом не найдено"

def add(document_type, number, name, shelf_number):
  documents.append({"type": document_type, "number": number, "name": name})
  shelf_number_str = str(shelf_number)
  if shelf_number_str in directories:
    directories[shelf_number_str].append(number)
    return "Документ добавлен"
  else:
    return "Полки с таким документом не найдено"

if __name__ == '__main__':
  
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))