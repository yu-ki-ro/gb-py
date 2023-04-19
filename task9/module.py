
phone_book = []
start_phone_book = []

PATH = 'phonebook.txt'

def get_pb():
    global phone_book
    return phone_book

def load_file():
    global start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
        start_phone_book = phone_book.copy()

def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)

def search_contact(contact: dict):
    global phone_book
    for value in phone_book:
        if value['name'] == contact['name'] or value['phone'] == contact['phone'] or value['comment'] == contact['comment']:
            return value

def index_contact(contact: dict):
    global phone_book
    for value in phone_book:
        if value['name'] == contact['name'] or value['phone'] == contact['phone'] or value['comment'] == contact['comment']:
            return phone_book.index(value)


def change_contact(contact: dict, ind):
     global phone_book
     for value in phone_book:
         if contact['name'] != "" and value['name'] != contact['name']:
             phone_book[ind]['name'] = contact['name']
         if contact['phone'] != "" and value['phone'] != contact['phone']:
             phone_book[ind]['phone'] = contact['phone']
         if contact['comment'] != "" and value['comment'] != contact['comment']:
             phone_book[ind]['comment'] = contact['comment']


def del_contact(contact: dict):
    global phone_book
    for value in phone_book:
        if value['name'] == contact['name'] or value['phone'] == contact['phone'] or value['comment'] == contact['comment']:
            phone_book.pop(phone_book.index(value))



def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True
