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