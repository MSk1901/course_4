class Vacancy:

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, requirements: str):
        """Инициализирует вакансию"""
        self.__name = name
        self.__url = url

        if salary_from and isinstance(salary_from, (int, float)):
            self.__salary_from = salary_from
        elif isinstance(salary_from, str):
            self.__salary_from = int(salary_from)
        else:
            self.__salary_from = 0

        if salary_to and salary_to != 0 and isinstance(salary_from, (int, float)):
            self.__salary_to = salary_to
        elif isinstance(salary_to, str) and int(salary_to) > 0:
            self.__salary_to = int(salary_to)
        else:
            self.__salary_to = self.__salary_from

        self.__requirements = requirements

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def requirements(self):
        return self.__requirements

    def __str__(self):
        return f"""Название вакансии: {self.__name}
Ссылка на вакансию: {self.__url}
Зарплата от: {self.salary_from} рублей
Зарплата до: {self.salary_to} рублей
Требования: {self.requirements}"""

    def __gt__(self, other):
        """Сравнивает зарплату 'от' в вакансиях (>)"""
        if isinstance(other, Vacancy):
            return self.__salary_from > other.salary_from
        else:
            raise ValueError("Можно сравнивать только вакансии")

    def __ge__(self, other):
        """Сравнивает зарплату 'от' в вакансиях (>=)"""
        if isinstance(other, Vacancy):
            return self.__salary_from >= other.salary_from
        else:
            raise ValueError("Можно сравнивать только вакансии")

    def __eq__(self, other):
        """Сравнивает зарплату 'от' в вакансиях (==)"""
        if isinstance(other, Vacancy):
            return self.__salary_from == other.salary_from
        else:
            raise ValueError("Можно сравнивать только вакансии")

    @staticmethod
    def sort_by_salary(vacancies: list):
        """Сортирует вакансии по зарплате"""
        return sorted(vacancies, key=lambda x: x["salary_from"], reverse=True)

    @staticmethod
    def get_top_vacancies(vacancies: list, number: int):
        """Возвращает топ-N вакансий"""
        if len(vacancies) < number:
            return vacancies
        return vacancies[:number]
