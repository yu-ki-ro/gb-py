a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = []
for i in range(n):
    progression.append(a1 + i * d)

print("Элементы прогрессии:", progression)
