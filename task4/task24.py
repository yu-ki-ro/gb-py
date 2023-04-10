n = int(input("Введите колличество кустов: "))
print("Введите урожайность через пробел")
a = list(map(int, input().split()))

berries = [a[i-1] + a[i] + a[(i+1) % n] for i in range(n)]

max_berries = max(berries)

print("Максимальный сбор", max_berries)
