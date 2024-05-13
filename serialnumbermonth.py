def check_month(month: int):
  if 0 < month < 3 or month == 12:
    result = 'Зима'
  elif 2 < month < 6:
    result = 'Весна'
  elif 5 < month < 9:
    result = 'Лето'
  elif 8 < month < 12:
    result = 'Осень'
  else:
    result = 'Некорректный номер месяца'
  return result


if __name__ == '__main__':
    season = check_month(1)
    assert season == 'Зима', "Ответ должен быть Зима"
    print(f"1 месяц время года: {season}")
    season = check_month(4)
    assert season == 'Весна', "Ответ должен быть Весна"
    print(f"4 месяц время года: {season}")
    season = check_month(18)
    assert season == "Некорректный номер месяца", "Ответ должен быть 'Некорректный номер месяца'"
    print(f"18 месяц: {season}")