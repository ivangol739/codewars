import sys

#sys.stdin.readline()
# Чтение строки из стандартного ввода
line = sys.stdin.readline()

# # Вывод строки на экран
print("Прочитанная строка:", line)

# # Пример обработки символа новой строки
cleaned_line = line.strip()  # Удаление символа перевода строки
print("Очищенная строка:", cleaned_line)




# sys.stdin.readlines
# Чтение всех строк из стандартного ввода
lines = sys.stdin.readlines()

# Вывод количества прочитанных строк
print("Прочитано строк:", len(lines))

# # Вывод всех прочитанных строк
for i, line in enumerate(lines):
    print(f"Строка {i + 1}: {line}", end="")




#массив чисел -- map(int, input().split())
numbers = map(int, input().split())

# Преобразование в список (если нужно)
numbers_list = list(numbers)

# Вывод списка чисел
print(numbers_list)