def button_click():
    menu = view.menu()
    choice = view.control_menu()
    if choice:
        go_to = {
            '1': function.add,
            '2': function.delete,
            '3': function.view_contakt,
            '4': function.find_contakt_surname,
            '5': function.import_,
            '6': function.exit,
            '7': function.export
        }
        go_to[menu]()


button_click()
 