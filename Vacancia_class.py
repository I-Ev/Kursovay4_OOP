class Vacancy:
    def __init__(self, json_data):
        self.name = json_data['name']
        self.city = json_data['area']['name']
        self.employer_name = json_data['employer']['name']
        self.url = json_data['alternate_url']
        self.description = json_data['snippet']['responsibility']
        self.requirement = json_data['snippet']['requirement']
        # блок с зарплатой
        if json_data['salary'] is None:
            self.__salary_to = None
            self.__salary_from = None
            self.salary_info = False
        else:
            self.salary_info = True
            if json_data['salary']['from'] is None:
                self.__salary_from = None
            else:
                self.__salary_from = json_data['salary']['from']
            if json_data['salary']['to'] is None:
                self.__salary_to = None
            else:
                self.__salary_to = json_data['salary']['to']




    def __str__(self):
        return f"{self.name} в компанию {self.employer_name} в городе {self.city}"

    def __repr__(self):
        return f"{self.__class__} (self.name= {self.name}, self.city= {self.city}, " \
               f"self.salary_from= {self.__salary_from}, self.salary_to= {self.__salary_to}, " \
               f"self.salary_info= {self.salary_info}, " \
               f"self.eployer_name= {self.employer_name}, self.url= {self.url}" \
               f"self.description= {self.description}, self.requirement= {self.requirement} "
    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    # def __lt__(self, other):
    #     if isinstance(other, Vacancy):
    #         return self.salary < other.salary
    #     return TypeError("Нельзя сравнить с другими объектами")
    #
    # def __gt__(self, other):
    #     return self.salary > other.salary
    #
    # def __le__(self, other):
    #     return self.salary <= other.salary
    #
    # def __ge__(self, other):
    #     return self.salary >= other.salary
