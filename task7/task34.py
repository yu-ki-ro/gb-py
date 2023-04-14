def count_vowels(word):
    vowels = "аоуыэеёиюяАОУЫЭЕЁИЮЯ"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def check_rhythm(poem):
    words = poem.split()
    syllables = []
    for word in words:
        syllables.append(count_vowels(word))
        #print(syllables)
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
        #print(len(set(syllables)))
    else:
        return "Пам парам"


poem = input("Введите стихотворение: ")
print(check_rhythm(poem))