def summ(a, b):
    if a < 0 or b < 0:
        return print("Есть отрицательное число")
    else:
        return a + b

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(summ(a, b))
