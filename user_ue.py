from create_db import add_user, update_user, exit, delete_user, all_workers


while True:
    say_1 = input('Выберите действие:\n(Д)обавить\n(У)далить\n(О)бновить\n(Е)ыход\n(В)се сотрудники\n')

    if say_1 == 'Д':
        f_name = input("Ведите имя сотрудника ")
        l_name = input('Введите фамилию сотрудника ')
        phone = input("Введите номер сотрудника ")
        email = input("Введите email сотрудника ")
        add_user(f_name, l_name, phone, email)
    if say_1 == 'О':
        fix1 = input("Что нужно заменить? ")
        fix2 = input("На что надо заменить? ")
        fix3 = input("У кого надо заменить? ")
        update_user(fix1, fix2, fix3)
    if say_1 == 'У':
        del1 = input("Какого сотрудника нкжно удалить? ")
        delete_user(del1)
    if say_1 == 'В':
        all_workers()
        
    if say_1 == 'Е':
        exit()
        break
        
