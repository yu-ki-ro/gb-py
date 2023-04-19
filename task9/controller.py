import view
import module
import text_fields as txt



def start_pb():
    while True:
        choice = view.main_menu()
        print(choice)
        match choice:
            case 1:
                module.load_file()
                view.print_info(txt.load_succesful)
            case 2:
                module.save_file()
                view.print_info(txt.save_complete)
            case 3:
                pb = module.get_pb()
                view.show_contacts(pb,txt.no_contact_or_file)
            case 4:
                contact = view.contact_fields()
                module.add_contact(contact)
                view.print_info(txt.new_contact_succesful)
            case 5:
                contact = view.contact_fields()
                contact = module.search_contact(contact)
                view.show_contacts(contact,txt.search_cont)
            case 6:
                contact = view.change_contact()
                i = module.index_contact(contact)
                contact2 = view.contact_fields()
                module.change_contact(contact2, i)
            case 7:
                contact = view.contact_fields()
                contact = module.search_contact(contact)
                module.del_contact(contact)
            case 8:
                if module.exit_pb():
                    if view.confirm(txt.is_changed):
                        module.save_file()
                view.print_info(txt.bye_bye)
                exit()
