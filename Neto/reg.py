import re


text = """регулярные выражения (их еще называют regexp, или regex) — это механизм для поиска и замены текста. В строке, файле, нескольких файлах... Их используют разработчики в коде приложения, тестировщики в автотестах, да просто при работе в командной строке!
Чем это лучше простого поиска? Тем, что позволяет задать шаблон. регулярные выражения
Например, на вход приходит дата рождения в формате ДД.ММ.ГГГГ. Вам надо передать ее дальше, но уже в формате ГГГГ-ММ-ДД. Как это сделать с помощью простого поиска? Вы же не знаете заранее, какая именно дата будет."""

#Поиск всех совпадений  
pattern = r"регуляр\w+"
result = re.findall(pattern, text)
print(result)

#Поиск одного совпадения
pattern = r"регуляр\w+"
idx = 0
while True:
  result = re.search(pattern, text[idx: ])
  if result == None:
    break
  print(result.group(), result.start(), result.end())
  idx = idx + result.end()

#Поиск одного совпадения 2
pattern = r"\w+"
result = re.match(pattern, text)
print(result)

#Флаги в RE
text = """регулярные выражения (их еще называют regexp, или regex) — это механизм для поиска и замены текста. В строке, файле, нескольких файлах... Их используют разработчики в коде приложения, тестировщики в автотестах, да просто при работе в командной строке!
Чем это лучше простого поиска? Тем, что позволяет задать шаблон. Регулярные выражения
Например, на вход приходит дата рождения в формате ДД.ММ.ГГГГ. РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯВам надо передать ее дальше, но уже в формате ГГГГ-ММ-ДД. Как это сделать с помощью простого поиска? Вы же не знаете заранее, какая именно дата будет."""

pattern = r"регулярн\w+ выражен\w+"
result = re.findall(pattern, text, re.IGNORECASE)
print(result, type(result))