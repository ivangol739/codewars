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