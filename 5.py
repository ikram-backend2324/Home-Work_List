# # 5) Дана квадратная матрица. Проверить, является ли она симметричной относительно
# #  главной диагонали.
# ////////////////////////////////////////////////////////////////////////////////

f_number = [[(input("First Number = "))], [(input("Second Number = "))]]
s_number = [[input("third Number = ")], [(input("Forth Number = "))]]

if f_number[-1][0] == s_number[0][0] and f_number[0][0] == s_number[-1][0]:
    print("True")
else:
    print("False")