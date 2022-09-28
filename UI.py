import Work1 as w1
import Work2 as w2
 
def choice():
    while True:
        text = input('Выберите действие с запсью: 1 - просмотр, 2 - добавление, 3 - экспорт, 4 - импорт, 5 - выйти из программы: ')
        if text == '1':
            w1.view_data()
        elif text == '2':
            w1.get_info()
            w1.write_data()
        elif text == '3':
            w2.export_data()
        elif text == '4':
            imp_file = "'" + input('Сохраните файл в текущей папке в формате .txt и введите имя файла: ') + '.txt' + "'"
            print(f'Подтвердите имя файла: {imp_file}')
            w2.import_data(imp_file)
        elif text == '5':
            break
        else:
            print('Введена некорректная команда.')

choice()