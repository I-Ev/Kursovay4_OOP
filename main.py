import json
from abc import ABC, abstractmethod
import requests


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text, location, salary):
        self.search_text = search_text
        self.location = location
        self.salary = salary


class HhVacancyAPI(AbstractVacancyAPI):

    def get_vacancies(self, search_text: str, location: str = '1', salary: float = None):
        """Возвращает список вакансий с HH.ru и записывает в json файл"""
        # описание API на вакансии - https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies
        HH_URL = "https://api.hh.ru/vacancies"
        params = {
            'area': location,
            'text': search_text,
            'period': 30,
            'per_page': 20,
            'salary': salary
        }
        response = requests.get(HH_URL, params=params).json()

        with open("vacancies_HH.json", "w", encoding="utf-8") as file:
            json.dump(response, file, indent=4, ensure_ascii=False)


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


class SuperJobVacancyAPI(AbstractVacancyAPI):
    def get_vacancies(self, search_text, location, salary):
        pass


class Vacancy:
    def __init__(self, vacancy_api):
        self.vacancy_api = vacancy_api
        self.name = None
        self.salary = None
        self.url = None
        self.description = None

    def __str__(self):
        return f"{self.name} {self.url}"

    def __repr__(self):
        return f"{self.__class__} ({self.name} {self.salary} {self.url})"

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return TypeError("Нельзя сравнить с другими объектами")

    def __gt__(self, other):
        return self.salary > other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary


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
    user_text= input('Введите ключевые слова для поиска вакансий\n')
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


if __name__ == "__main__":

    user_platform = get_platform_from_user()
    user_region = get_region_from_user()
    user_region_id = user_region['id']
    user_region_name = user_region['name']
    user_text = get_text_from_user()
    user_salary = get_salary_from_user()
    show_summary_from_user(user_platform, user_region_name, user_text, user_salary)
    if user_platform == 'HeadHunter.ru':
        pass
    else:
        pass

    # vakansy = HhVacancyAPI()
    # vakansy_HH.get_vacancies('Pytnon', '1124', 50000)
    # vakansy_HH.get_russian_areas()
