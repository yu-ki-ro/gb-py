from random import randint

n = int(input("Ведите коллчиество монет: "))

monetki = []
for _ in range(n):
    monetki.append(randint(0,1))
print(monetki)
count_mon = 0
for _ in range(n):
    if monetki[_] < 1:
        count_mon += 1

if count_mon > n/2:
    for _ in range(n):
        if monetki[_] == 1:
            monetki[_] = 0
else:
    for _ in range(n):
        if monetki[_] == 0:
            monetki[_] = 1

print("нужно перевернуть: ", count_mon)
print(monetki)