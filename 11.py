# 11) Дан массив из N элементов в диапазоне [100;300].
# Сжать массив, оставив в нем только те элементы, сумма цифр которых четная.

array = []
for i in range(100,300):
    array.append(i)

for j in array:
    if j%2 == 0:
        print(j)