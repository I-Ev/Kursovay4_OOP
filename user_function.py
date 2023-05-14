import json

import requests


def get_hh_russian_areas():
    """Получаем список доступных в HH.ru регионов России для поиска и записываем в json
            в виде словаря"""
    response = requests.get("https://api.hh.ru/areas").json()

    russian_areas = {}
    for country in response:
        if country['name'] == 'Россия':
            i = 1
            for areas in country['areas']:
                areas_info = {'id': areas['id'], 'name': areas['name']}
                russian_areas[i] = areas_info
                i += 1
    return russian_areas
    # with open('hh_russian_areas.json', 'w', encoding='UTF-8') as file:
    #     json.dump(russian_areas, file, indent=4, ensure_ascii=False)


def get_platform_from_user() -> str:
    while True:
        user_platform = int(input("\n#########################"
                                  "\nДля поиска вакансий выберите ресурс:\n"
                                  "[1] - HeadHunter.ru\n"
                                  "[2] - SuperJob.ru\n"
                                  "или нажмите [0] для выхода\n")
                            )
        if user_platform == 0:
            exit()
        elif user_platform == 1:
            user_platform = 'HeadHunter.ru'
            break
        elif user_platform == 2:
            user_platform = 'SuperJob.ru'
            break
        else:
            print("Введите правильную команду")
    return user_platform


def get_region_from_user() -> dict:
    """ Получает список регионов по API, выводит список пользователю и возвращает ID
    выбранного региона"""
    regions = get_hh_russian_areas()
    while True:
        print('\nВведите номер региона, в котором будем искать вакансии\n'
              'Для выбора доступны следующие регионы:')
        for key, value in regions.items():
            print(f"[{key}] - {value['name']}")
        print("или нажмите [0] для выхода\n ")
        user_region = int(input())
        if user_region == 0:
            print("##########[ Выход из программы ]##########\n")
            exit()
        elif user_region in regions:
            break
        else:
            print('Введите корректную команду')

    return regions[(user_region)]


def get_text_from_user() -> str:
    user_text = input('Введите ключевые слова для поиска вакансий\n')
    return str(user_text)


def get_salary_from_user():
    while True:
        user_input = input("Введите размер зарплаты для поиска ИЛИ оставьте поле пустым\n")
        if user_input == "":
            return None
        try:
            user_salary = int(user_input)
            return user_salary
        except ValueError:
            print("Введите корректное значение или оставьте поле пустым")


def show_summary_from_user(platform, region, text, salary):
    if salary is None:
        salary = "____"
    print(f"Отлично, все данные получены\n"
          f"Ищем на [{platform}] по региону [{region}] "
          f"по ключевым словам [{text}] c зарплатой от [{salary}] ")


def adaptation_hh_salary(data):
    """ Принимает на вход информацию о зарплате из вакансии и возвращает
    обработанный читаемый формат """
    # если dict с зарплатой пустой
    if data is None:
        return f'Не указана'

    # если заполнены оба параметра От/До
    if data['from'] and data['to']:
        return f"от {data['from']} до {data['to']} {data['currency']}"

    # далее обрабатываем кейс если 1 параметр От/До не указан
    if data['from'] is None or data['to'] is None:
        if data['from'] is None:
            return f"до {data['to']} {data['currency']}"
        else:
            return f"от {data['from']} {data['currency']}"


def show_vacancies():
    with open('files/vacancies_HH.json', encoding='UTF-8') as file:
        vacancies = json.load(file)
    if len(vacancies['items']) == 0:
        print("Вакансий по данным критериям не найдено")
        return None
    print(f"\n#############################\n"
          f"Найдено вакансий - [{vacancies['found']}]\n"
          f"#############################\n")
    i = 1
    for vacancy in vacancies['items']:
        salary = adaptation_hh_salary(vacancy['salary'])
        print(f"[{i} из {vacancies['found']}] - {vacancy['name']} в {vacancy['employer']['name']},\n"
              f"зарплата: {salary}\n"
              f"требования: - {vacancy['snippet']['requirement']}\n"
              f"описание: {vacancy['snippet']['responsibility']}\n"
              f"ссылка на вакансию: {vacancy['alternate_url']}\n")
        i += 1
        user_input = input('Нажмите любую кнопку для продолжения или 0 для выхода \n')
        try:
            if int(user_input) == 0:
                print("Вы успешно вышли из программы")
                return None
        except:
            continue
    print('Это все результаты поиска')



