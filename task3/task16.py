from random import randint

n = int(input("введите n: "))
num_list = []
for _ in range(n):
    num_list.append(_+1)

x = int(input("введите x: "))
x_count = 0
for _ in range(n):
    if num_list[_] == x:
        x_count =+ 1

print(x_count)

print(num_list[:])