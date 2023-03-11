# 2) Даны два массива: ['a', 'b', 'c'] и [1, 2, 3]. Объедините их вместе.

abc = ['a', 'b', 'c']
numbers = [1, 2, 3]
abc.extend(numbers)
print(abc)