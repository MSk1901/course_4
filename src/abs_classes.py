from abc import ABC, abstractmethod


class JobsParser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass


class FileHandler(ABC):

    @abstractmethod
    def add_vacancies(self, vacancies: list):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary: int):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: dict):
        pass
