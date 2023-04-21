import view
import text_fields as txt
from classes import Contact, PhoneBook



def start_pb():
    phonebook = PhoneBook('phonebook.txt')
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                phonebook.open_file()
                view.print_info(txt.load_succesful)
            case 2:
                phonebook.save_file()
                view.print_info(txt.save_complete)
            case 3:
                pb = phonebook.get()
                view.show_contacts(pb,txt.no_contact_or_file)
            case 4:
                contact = view.contact_fields()
                phonebook.add(contact)
                view.print_info(txt.new_contact_succesful)
            case 5:
                contact = view.contact_fields()
                contact = phonebook.find_contact(contact)
                view.show_contacts(contact,txt.search_cont)
            case 6:
                contact = phonebook.get()
                i = phonebook.find_contact(contact)
                contact2 = view.contact_fields()
                phonebook.edit_contact(i, contact2)
            case 7:
                contact = view.contact_fields()
                contact = phonebook.find_contact(contact)
                phonebook.remove(contact)
            case 8:
                if phonebook.save_on_exit():
                    if view.confirm(txt.is_changed):
                        phonebook.save_file()
                view.print_info(txt.bye_bye)
                exit()
