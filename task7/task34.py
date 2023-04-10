def count_vowels(word):
    """
    Функция для подсчета количества гласных букв в слове
    """
    vowels = "aeiouyAEIOUY"  # гласные буквы в английском языке
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


def check_rhythm(poem):
    """
    Функция для проверки ритма в стихотворении
    """
    words = poem.split()  # разделение стихотворения на слова
    syllables = []  # список количества слогов в каждом слове
    for word in words:
        syllables.append(count_vowels(word))
    if len(set(syllables)) == 1:  # проверка, что все слова имеют одинаковое количество слогов
        return "Парам пам-пам"
    else:
        return "Пам парам"


poem = input("Введите стихотворение: ")
print(check_rhythm(poem))
#