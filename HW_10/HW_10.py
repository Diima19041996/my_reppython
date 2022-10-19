# Задание:
# 1- Создать калькулятор
# 2- Обернуть в try\except
while True:
    try:
        a = float(input('Введите первое число '))
        b = input("Выполните действие ")
        c = float(input("Введите второе число "))
        if b == "+":
            print(a + c)
        elif b == "-":
            print(a - c)
        elif b == "*":
            print(a * c)
        try:
            if b == "/":
                print(a / c)

        except ZeroDivisionError:
            print("Деление на ноль невозможно, выбирите другое число")

    except ValueError:
        print("Необходимо вводить целочисленное значение")




