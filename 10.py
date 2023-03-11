# 10) В одномерном массиве (заполнение массива случайными числами от -50 до 49)
# найти сумму отрицательных элементов. Если эта сумма меньше -100,
# то необходимо прибавить к ней минимальный положительный элемент.
# ////////////////////////////////////////////////////////////////////////////////

array = []
sum_negative_numbers = 0
plus_array = []
i = 0
while i < 8:
    number = int(input("Number: "))
    if -50 < number < 49:
        array.append(number)
    if number > 0:
        plus_array.append(number)
    i += 1
for n in array:
    if n < 0:
        sum_negative_numbers += n

if sum_negative_numbers < -100:
    sum_negative_numbers += max(plus_array)

print(f"сумму отрицательных элементов: {sum_negative_numbers}")

