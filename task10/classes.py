class Contact:

    def __init__(self, name: str, phone: str, comment: str = ''):
        self.name = name
        self.phone = phone
        self.comment = comment

    def cnt_to_str(self):
        return f'{self.name};{self.phone};{self.comment}'

    def __str__(self):
        return f'{self.name} | {self.phone} | {self.comment}'


    def edit(self, name: str, phone: str, comment: str):
        self.name = name if name else self.name
        self.phone = phone if phone else  self.phone
        self.comment = comment if comment else self.comment

class PhoneBook:

    def __init__(self, path: str):
        self.path = path
        self.phone_book: list[Contact] = []
        self.original_book: list[Contact] = []
        self.if_changed = False


    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            self.phone_book.append(Contact(contact[0], contact[1], contact[2]))
        self.original_book = self.phone_book.copy()
        self.if_changed = False

    def save_file(self):
        save_book = []
        for contact in self.phone_book:
            save_book.append(contact.cnt_to_str())
        data = '\n'.join(save_book)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.original_book = self.phone_book.copy()

    def get(self):
        return self.phone_book

    def add(self, new_contact: Contact) -> None:
        self.phone_book.append(new_contact)
        self.if_changed = True

    def find_contact(self, word: str) -> list[Contact]:
        result = []
        for contact in self.phone_book:
            if word in contact.cnt_to_str():
                result.append(contact)
        return result

    def edit_contact(self, edited_contact: tuple[int, Contact]) -> None:
        index, new = edited_contact
        self.phone_book[index - 1].edit(new.name, new.phone, new.comment)
        self.if_changed = True


    def remove(self, index: int) -> str:
        deleted_element = self.phone_book.pop(index - 1)
        self.if_changed = True
        return deleted_element.name

    def save_on_exit(self) -> bool:
        return self.if_changed
