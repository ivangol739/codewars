def check_email(email: str) -> bool:
  if "@" in email and "." in email:
    if " " not in email:
      return True
    else: return False
  else:
    return False

# print(check_email('em@il.ru'))


def longest_film(film_1, film_2, film_3):
  films = [film_1, film_2, film_3]
  res = max(films)
  return res

# print(longest_film('Аладин', 'Мадагаскар', 'Бетховен'))


def string_slices(string: str):
  return string[2: len(string) - 2]

# print(string_slices('%%1gtfgeghethte1&#'))


from typing import List

def fio(initials: List[str]):
  return initials[0][0] + initials[1][0] + initials[2][0]

# print(fio(['Иванов', 'Иван', 'Иванович']))


def list_of_numbers(n: int):
  return list(range(1, n + 1))

# print(list_of_numbers(9))


def reverse(string: str):
  return string[::-1].lower()
print(reverse('Пусть старо как мир понтье корча порча привороG'))