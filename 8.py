# 8) Требуется заполнить массив числами,
# которые вводит пользователь, и вычислить их сумму.
# Если пользователь вводит ноль или превышен размер массива,
# то запросы на ввод должны прекратиться.

array = []

n = 0
while n <= 8:
    number = int(input("Number = "))
    array += str(number)
    n += 1
    if number == '0':
        break
print(array)