s, p = int(input("введите Х: ")), int(input("Введите Y: "))
c = 0
for i in range(x + y):
    if c:
        break
    for j in range(x + y):
        if i + j == x and i * j == y:
            c = 1
            print(*sorted([i, j]))
            break
