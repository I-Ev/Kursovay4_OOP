import json
from Vacancia_class import Vacancy


def collect_hh_vacancies():
    with open('files/vacancies_HH.json', encoding='UTF-8') as file:
        data = json.load(file)
    vacancies_list =[]

    for vac in data['items']:
        vacancies_list.append(Vacancy(vac))
    return vacancies_list


# print(collect_hh_vacancies()[0])
# print('############################')
# print(repr(collect_hh_vacancies()[0]))