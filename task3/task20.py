ball_1 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'н', 'о', 'р', 'с', 'т']
ball_2 = ['d', 'g', 'д', 'к', 'л', 'м', 'п', 'у']
ball_3 = ['b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я']
ball_4 = ['f', 'g', 'v', 'w', 'y', 'й', 'ы']
ball_5 = ['k', 'ж', 'з', 'х', 'ц', 'ч']
ball_8 = ['j', 'x' , 'ш', 'э', 'ю']
ball_10 = ['q', 'z', 'ф', 'щ', 'ъ']

slovo = input("Введите любое слово: ")
summ = 0
for _ in range(len(slovo)):
    if slovo[_] in ball_1:
        summ += 1
    elif slovo[_] in ball_2:
        summ += 2
    elif slovo[_] in ball_3:
        summ += 3
    elif slovo[_] in ball_4:
        summ =+ 4
    elif slovo[_] in ball_5:
        summ =+ 5
    elif slovo[_] in ball_8:
        summ =+ 8
    elif slovo[_] in ball_10:
        summ =+ 10

print(summ)
