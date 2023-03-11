# 12) Заполнить массив из 10 элементов случайными числами в интервале [0..4] и определить,
# есть ли в нем одинаковые соседние элементы.

array = []
while True:
    number = int(input("Number: "))
    if number >= 5 or number < 0:
        break
    else:
        array.append(number)
print(array)
for i in array:
    for j in array:
        if (j-1) == i or (j+1) == i:
            print("True")