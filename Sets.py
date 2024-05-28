from pprint import pprint

# 1
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

# В этот список будут добавляться словари-курсы
courses_list = []
# Допишите код, который генерирует словарь-курс с тремя ключами: "title", "mentors", "duration"
for i in zip(courses, mentors, durations):
	course_dict = {"title": i[0], "mentors": i[1], "duration": i[2]}
	courses_list.append(course_dict)

# Найдите самое маленькое и самое большое значение длительности курса
# Подсказка: используйте функции min и max для списка durations
min = min(durations)
max = max(durations)

# Как видите, в duration встречаются одинаковые длительности курса. Допишите код, который это учитывает
# Подсказка 1: найдите индексы, по которым в списке durations встречается самое маленькое и самое большое значение
# Подсказка 2: не забудьте, что индекс можно удобно получить функцией enumerate
maxes = []
minis = []
for idx, i in enumerate(durations):
	if i == max:
		maxes.append(idx)
	elif i == min:
		minis.append(idx)

# Соберите все названия самых коротких и самых длинных курсов
# Так как курсов с одной длительностью может быть больше одного,
# создайте список названий самых коротких (courses_min) и самых длинных (courses_max) курсов
courses_min = []
courses_max = []
for id in minis:
	courses_min.append(courses_list[id]['title']) # Допишите код, который берёт по id нужный курс из courses_list и получает название курса из ключа "title"
for id in maxes:
	courses_max.append(courses_list[id]['title']) # По аналогии допишите такой же код для курсов максимальной длительности


# Допишите конструкцию вывода результата. Можете использовать string.join()
# print(f"Самый короткий курс(ы): {', '.join(courses_min)} - {min} месяца(ев)")
# print(f"Самый длинный курс(ы): {', '.join(courses_max)} - {max} месяца(ев)")

# 2

# Наводим порядок: упорядочиваем курсы по продолжительности

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

# С этого момента начинается выполнение задания 2
# На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

# Отсортируйте курсы по длительности (ключ duration), но при этом сохраните порядковый номер каждого курса из courses_list
# Самое простое — создать новый словарь durations_dict с ключом — duration и значением — исходным номером курса в courses_list
# Но у нас могут быть курсы с одинаковой длительностью, поэтому значение словаря — это список индексов, а не одно значение
durations_dict = {}

# Допишите код цикла так, чтобы в нём вы получали id курса. Подсказка: помните о функции enumerate
for id, i in enumerate(courses_list):
  key = i.get('duration') # Получите значение из ключа duration

  if key not in durations_dict:
    durations_dict[key] = []
  durations_dict[key].append(id)
	# Допишите код ниже, который добавляет в словарь durations_dict по ключу key значения — id



# Отсортируем словарь по ключам. Этот код уже готов, ничего менять не нужно
# Здесь мы получаем пары ключ-значение в виде кортежа, и функция sorted выполняет сортировку по первым значениям кортежа — ключам
durations_dict = dict(sorted(durations_dict.items()))


# Выведите курсы, отсортированные по длительности
# Допишите код цикла так, чтобы в нём вы получали из durations_dict ключи и значения
for key, value in durations_dict.items():
  for idx in value:
    course = courses_list[idx]['title']
	# Допишите код, который проходит по всему списку значений и выводит на экран текст вида «название курса — длительность
    # print(f'{course} - {key} месяцев')


# 3


 #  этом задании вы сделаете мини-анализ данных. Вам нужно проверить, зависят ли друг от друга продолжительность курса и количество преподавателей на этом курсе.
# Если отсортировать курсы по продолжительности и по количеству преподавателей и окажется, что курсы идут в одном и том же порядке, значит связь есть. Если порядок будет разный – значит связи нет.
# Для сравнения используйте не названия курсов, а их порядковые номера в списке courses_list.
# Для сравнения сделайте пары [длительность, индекс] и [количество преподавателей, индекс] и сортируйте по ним.

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)
 
# С этого момента начинается выполнение задания 3.
# На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

# Подсказка: если связь между продолжительностью курсов и количеством преподавателей есть,
# то после сортировки курсов по длительности и по количеству преподавателей курсы должны идти в одном и том же порядке
# Проверьте себя: в этом задании курсы будут идти в таком порядке:
# ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"] - по продолжительности,
# ["Python-разработчик с нуля", "Frontend-разработчик с нуля", "Fullstack-разработчик на Python", "Java-разработчик с нуля"] - по количеству преподавателей
# То есть ваш скрипт должен вывести "Связи нет", т.к. порядок оказался разным

# Подсказка 1: для сравнения используйте не названия курсов, а их порядковые номера в списке courses_list
# Подсказка 2: для сравнения сделайте пары [duration, index] и [mentors_count, index]
# Допишите код ниже, который добавляет эти пары в список duration_index и mcount_index соответственно:
duration_index = []
mcount_index = []
for index, course in enumerate(courses_list):
  duration_index.append([course['duration'], index])
  mcount_index.append([len(course['mentors']), index]) 
  
duration_index.sort()
mcount_index.sort()

indexes_d = []
indexes_m = []

# Допишите код ниже:
for i in duration_index:
	indexes_d.append(i[1])

for i in mcount_index:
  indexes_m.append(i[1])

# Сравните два получившихся списка индексов. Если они равны, то есть индексы идут в одинаковом порядке,
# выведите "Связь есть", если не равны - выведите "Связи нет" и ниже - номера курсов по длительности, а потом - по количеству преподавателей
# Допишите код ниже:

print("Связь есть" if indexes_m == indexes_d else "Связи нет")
print(f"Порядок курсов по длительности: {indexes_d}")
print(f"Порядок курсов по количеству преподавателей: {indexes_m}")