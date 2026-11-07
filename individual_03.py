
n = int(input("Введите целое неотрицательное число: "))
if n == 0:
    count = 1
    sum = 0
else:
    count = 0
    sum = 0
    while n > 0:
        digit = n % 10
        
        sum += digit
        
        count += 1
        
        n = n // 10

print("Количество цифр:", count)
print("Сумма цифр:", sum)