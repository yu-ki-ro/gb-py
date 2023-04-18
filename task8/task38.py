def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    with open("phonebook.txt", "a", encoding="utf-8") as f:
        f.write(f"{surname},{name},{patronymic},{phone}\n")
    print("Контакт добавлен в телефонный справочник.")
def search_contact():
    search_term = input("Введите фамилию, имя или отчество для поиска: ")
    with open("phonebook.txt", "r", encoding="utf-8") as f:
        for line in f:
            surname, name, patronymic, phone = line.strip().split(",")
            if search_term in [surname, name, patronymic]:
                print(f"{surname} {name} {patronymic}: {phone}")
def print_data():
    with open("phonebook.txt", "r", encoding="utf-8") as f1:
        for line in f1:
            print(line)
    print("Все данные отображены.")
def export_data():
    with open("phonebook.txt", "r", encoding="utf-8") as f1,  open("ex_phonebook.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line)
    print("Данные экспортированы в файл ex_phonebook.txt.")
def import_data():
    filename = input("Введите имя файла для импорта: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                surname, name, patronymic, phone = line.strip().split(",")
                with open("phonebook.txt", "a", encoding="utf-8") as f2:
                    f2.write(f"{surname},{name},{patronymic},{phone}\n")
        print("Данные импортированы в телефонный справочник.")
    except FileNotFoundError:
        print("Файл не найден.")

def change_data():
    search_term = input("Введите фамилию, имя или отчество для для изменения: ")
    with open("phonebook.txt", "r", encoding="utf-8") as fr:
        lines = fr.readlines()
        with open("phonebook.txt", "w", encoding="utf-8") as fw:
            for line in lines:
                surname, name, patronymic, phone = line.strip().split(",")
                if search_term in [surname, name, patronymic]:
                    print("Что меняем:")
                    print("1. Фамилию")
                    print("2. Имя")
                    print("3. Отчество")
                    print("4. Телефон")
                    choice = input()
                    if choice == "1":
                        surname = input("Введите фамилию: ")
                    elif choice == "2":
                        name = input("Введите имя: ")
                    elif choice == "3":
                        patronymic = input("Введите отчество: ")
                    elif choice == "4":
                        phone = input("Введите номер телефона: ")
                    fw.write(f"{surname},{name},{patronymic},{phone}\n")
                else:
                    fw.write(line)

def remove_data():
    search_term = input("Введите фамилию, имя или отчество для для удаления: ")
    with open("phonebook.txt", "r", encoding="utf-8") as fr:
        lines = fr.readlines()
        with open("phonebook.txt", "w", encoding="utf-8") as fw:
            for line in lines:
                surname, name, patronymic, phone = line.strip().split(",")
                if search_term in [surname, name, patronymic]:
                    print("Удалено")
                else:
                    fw.write(line)
def main():
    while True:
        print("Выберите действие:")
        print("1. Добавить контакт")
        print("2. Поиск контакта")
        print("3. Вывод данных")
        print("4. Импорт данных")
        print("5. Экспорт данных")
        print("6. Изменение данных")
        print("7. Удаление данных")
        print("8. Выход")
        choice = input()
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            print_data()
        elif choice == "4":
            import_data()
        elif choice == "5":
            export_data()
        elif choice == "6":
            change_data()
        elif choice == "7":
            remove_data()
        elif choice == "8":
            break
        else:
            print("Неверный выбор.")


if __name__ == '__main__':
    main()
