WATER_PER_KG = 30
WATER_PER_L = 1000

print("Здравствуйте, это программа по расчету ИМТ и нормы воды.")

# Запрос имени пользователя
user_name = input("Как Вас зовут? ")

# Запрос целочисленного возраста пользователя и обработка ошибок
while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        if user_age <= 0:
            print("Ошибка. Возраст не может быть отрицательным и нулем.")
        else:
            break
    except ValueError:
        print("Ошибка. Введите возраст цифрами!")

# Запрос целочисленного веса пользователя и обарботка ошибок
while True:
    try:
        user_weight = round(float(input("Каков Ваш вес в кг? "
                            "(Пример: 74.33) ")), 2)
        if user_weight <= 0:
            print("Ошибка. Вес не может быть отрицательным и нулем.")
        else:
            break
    except ValueError:
        print("Ошибка. Введите вес цифрами!")

# Запрос целочисленного роста пользователя и обарботка ошибок
while True:
    try:
        user_height = round(float(input("Каков Ваш рост в м? "
                            "(Пример: 1.83) ")), 2)
        if user_height <= 0:
            print("Ошибка. Рост не может быть отрицательным или нулем.")
        else:
            break
    except ValueError:
        print("Ошибка. Введите рост цифрами!")

# Расчет ИМТ пользователя
bmi = round((user_weight / (user_height ** 2)), 1)

# Расчет рекомендованнго объема воды
water_needed_ml = user_weight * WATER_PER_KG
water_needed_l = water_needed_ml / WATER_PER_L

print("\n", "-" * 30, "\n")
print(f"Отчет для пользователя: {user_name.title()} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Ваша рекомендуемая норма воды: {water_needed_l:.2f} л. в день")
print("Расчет окончен. Будьте здоровы!")
