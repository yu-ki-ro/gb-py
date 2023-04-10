n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    elem = int(input())
    set1.add(elem)

print("Введите элементы второго множества:")
for i in range(m):
    elem = int(input())
    set2.add(elem)

set3 = sorted(list(set1.intersection(set2)))

print("Элементы, встречающиеся в обоих множествах:", set3)
