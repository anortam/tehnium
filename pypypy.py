import random

def load_cities():
    f = open('cities.txt', 'r', encoding='utf-8')
    cities_list = [line.strip().lower() for line in f]
    f.close()
    return cities_list

def export_cities(city):
    f_answers = open('answers.txt', 'a', encoding='utf-8')
    f_answers.writelines(city + '\n')
    f_answers.close()

def get_last_char(city):
    city = city.lower()
    if city[-1] in ('ь' , 'ъ', 'ы'):
        return city[-2]
    return city[-1]

def validate_user_city(city, current_city, cities_list, used_cities):
    city = city.lower()
    if city in used_cities:
        return False
    elif city[0] != get_last_char(current_city):
        return False
    elif city not in cities_list:
        return False
    return True

def get_computer_city(city_user_last_char, cities_list, used_cities):#у всех аргументы добавила где использовала функцию?
    cities_starting_letter_list = [word for word in cities_list if word.startswith(city_user_last_char) and word not in used_cities]
    return random.choice(cities_starting_letter_list) if cities_starting_letter_list else None

def record_city(city, used_cities):
    export_cities(city)
    used_cities.append(city)

def game():
    open('answers.txt', 'w', encoding='utf-8').close()

    cities_list = load_cities()
    used_cities = []
    current_city = random.choice(cities_list)
    attempts = 5

    while True:
        print('Ход компьютера: ', current_city.title())
        record_city(current_city, used_cities)

        user_city = input('Введите город: ').lower().strip()
        last_char = get_last_char(user_city)

        # для читабельности лучше вынести в переменную или норм так и внести в иф?:
        # user_city_TrueFalse = validate_user_city(user_city, current_city, cities_list, used_cities)

        if validate_user_city(user_city, current_city, cities_list, used_cities):
            current_city = get_computer_city(last_char, cities_list, used_cities)
            record_city(user_city, used_cities)

            if current_city is None:
                print('Вы победили!')
                break

        else:
            attempts -= 1
            if attempts == 0:
                print('Вы проиграли!')
                break
            print('Неправильный город. Осталось попыток: ', attempts, 'из 5')
            #добавить, если нужно, чтобы при ошибке юзера комп менял свой выбор города и убрать, если не нужно
            current_city = get_computer_city(last_char, cities_list, used_cities)

game()