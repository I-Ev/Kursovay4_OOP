import json
from abc import ABC, abstractmethod
import os
import requests


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text, location, salary):
        self.search_text = search_text
        self.location = location
        self.salary = salary


class HhVacancyAPI(AbstractVacancyAPI):

    def get_vacancies(self, search_text: str, location: str = '1', salary: float = None):
        """Возвращает список вакансий по критериям с HH.ru и записывает в json файл"""
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

        # проверяем наличие папки files и создаем ее если не нашли
        if not os.path.exists('files'):
            os.mkdir('files')

        # записываем в файл найденные вакансии
        with open("files/vacancies_HH.json", "w", encoding="utf-8") as file:
            json.dump(response, file, indent=4, ensure_ascii=False)


class SuperJobVacancyAPI(AbstractVacancyAPI):
    def get_vacancies(self, search_text, location, salary):
        pass