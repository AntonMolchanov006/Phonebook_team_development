# создаём метод, который будет предлагать пользователю выбрать из меню,
# по какому сценарию будет работать программа.


# Приветствие
# Описание...

# меню:
# 0. Показать все записи
# 1. Найти номер телефона по фамилии (вылает все совпадения или пишет, что нет такого)
# 2. Найти номер телефона по имени (вылает все совпадения или пишет, что нет такого)
# 3. Поиск по номеру телефона
# 4. Добавить запись в телефонную книгу
# 5. Изменить существующую запись
# 6. Удалить запись
# 7. Закрыть программу


# - выводит меню
# - спрашивает у пользователя
# - пользователь ввел данные (переменная), сравнение через elif
# - обращается к методу импорт из DP

# - Выберите имя

# import data_provider

import data_generation
import data_provider


def ls_menu() -> int:
    print('1. Показать все записи.')
    print('2. Найти номер по фамилии.')
    print('3. Найти номер по имени.')
    print('4. Поиск по номеру телефона.')
    print('5. Добавить новую запись.')
    print('6. Изменить существующую запись.')
    print('7. Удалить запись.')
    print('8. Закрыть программу.')
    n = int(input('Выберите пункт из меню'))
    return n


def user_choice(n) -> str:
    if n == 1:
        print(data_generation)
        ls_menu()
    elif n == 2:
        search = input('Введите фамилию: ')
        ls_menu()
    elif n == 3:
        search = input('Введите имя: ')
        ls_menu()
    elif n == 4:
        search = input('Введите номер  телефона: ')
        ls_menu()
    elif n == 5:
        data_provider.add()  #добавить метод добавления новой записи из CRUD
        ls_menu()
    elif n == 6:
        print('1. Найти номер по фамилии.')
        print('2. Найти номер по имени.')
        print('3. Поиск по номеру телефона.')
        change = input('Введите номер пункта: ')
        if change == 1:
            search1 = input('Введите фамилию.')
        elif change == 2:
            search1 = input('Введите имя')
        elif change == 3:
            search1 = input('Введите номер телефона')
        
    elif n == 7:
        print('1. Найти номер по фамилии.')
        print('2. Найти номер по имени.')
        print('3. Поиск по номеру телефона.')
        deleting = input('Введите номер пункта: ')
        if deleting == 1:
            search2 = input('Введите фамилию.')
        elif deleting == 2:
            search2 = input('Введите имя')
        elif deleting == 3:
            search2 = input('Введите номер телефона')
    else:
        file.close()
    return search

# def find(user_choice(n)):
    # делаем срез по таблице и выдаем необходимые данные Инне.
