import math
x = float(input("Введите x: "))

if x < -1 or x > 1:
    print("Ошибка: x должен быть от -1 до 1")
else:
    k = 0
    a = math.pi * x**3 / 6
    s = a
    count = 1

    while count < 1000:
        b = a * (-math.pi**2 * x**4 * (4*k + 3)) / (
            4 * (2*k + 2) * (2*k + 3) * (4*k + 7)
        )

        if abs(b) <= 1e-10:
            break

        k += 1
        a = b
        s += a
        count += 1

    else:
        print("Не достигнута нужная точность")

    if count < 1000:
        print("Результат:", round(s, 10))
        print("Количество членов:", count)