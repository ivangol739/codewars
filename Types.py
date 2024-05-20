def check_email(email: str) -> bool:
  if "@" in email and "." in email:
    if " " not in email:
      return True
    else: return False
  else:
    return False

print(check_email('em@il.ru'))



def longest_film(film_1, film_2, film_3):
  films = [film_1, film_2, film_3]
  res = max(films)
  return res

print(longest_film('Аладин', 'Мадагаскар', 'Бетховен'))