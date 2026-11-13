if __name__ == "__main__":
    month = int(input("Номер месяца: "))

    if month == 12 or month == 1 or month == 2:
        print("Зима")
    elif 3 <= month <= 5:
        print("Весна")
    elif 6 <= month <= 8:
        print("Лето")
    elif 9 <= month <= 11:
        print("Осень")
    else:
        print("Ошибка: номер месяца должен быть от 1 до 12")