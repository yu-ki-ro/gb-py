# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

chislo = int(input("Введите целое число: "))
summ = 0
while (chislo != 0):
    summ = summ + chislo % 10
    chislo //= 10
print(f"Сумма цифр равна: {summ}")