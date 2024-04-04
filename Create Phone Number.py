# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in
# the form of a phone number.

def create_phone_number(numbers):
    # Проверяем, что входной массив содержит ровно 10 элементов
    if len(numbers) != 10:
        return "Массив должен содержать ровно 10 чисел"

    # Форматируем номер телефона в соответствии с требованиями
    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)

    return phone_number


# Пример использования
phone = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(phone)
#testd