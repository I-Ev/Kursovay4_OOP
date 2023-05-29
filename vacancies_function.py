import json
from Vacancia_class import VacancyHH, VacancySJ


def collect_hh_vacancies():
    with open('files/vacancies_HH.json', encoding='UTF-8') as file:
        data = json.load(file)
    vacancies_list = []

    for vac in data['items']:
        vacancies_list.append(VacancyHH(vac))

    succsess_message(len(vacancies_list))
    return vacancies_list


def collect_sj_vacancies():
    with open('files/vacancies_SJ.json', encoding='UTF-8') as file:
        data = json.load(file)
    vacancies_list = []

    for vac in data['objects']:
        vacancies_list.append(VacancySJ(vac))
        # print(f'{vac["profession"]}: {vac["client"]}')

    succsess_message(len(vacancies_list))
    return vacancies_list


def succsess_message(count):
    if count == 0:
        pass
    else:
        print(
            f'\n------Инициализация экземпляров класса "Вакансия" выполнена успешна, создано [{count}] экземпляров------\n')
