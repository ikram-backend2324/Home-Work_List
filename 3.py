# 3) Дан массив [1, 2, 3]. Сделайте из него массив [3, 2, 1].
#
numbers = [1, 2, 3]
result = []
for number in numbers:
    result.insert(0, number)

print(result)
