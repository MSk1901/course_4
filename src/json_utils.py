import json
import os
from datetime import datetime

from .abs_classes import FileHandler


class JSONSaver(FileHandler):

    def __init__(self):
        """Инициализирует путь к файлу с вакансиями"""
        today = datetime.today().strftime("%d.%m.%Y")
        filename = f"{today}.json"

        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
        self.__path = path

    def add_vacancies(self, vacancies: list):
        """Добавляет вакансии в файл с вакансиями"""
        with open(self.__path, "a+") as file:
            data = file.read()
            if data:
                data = json.load(file)
                data += vacancies
            else:
                data = vacancies
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_vacancies_by_salary(self, salary: int):
        """Получет все вакансии с заданной зарплатой"""
        try:
            with open(self.__path) as file:
                vacancies = json.load(file)
                if not vacancies:
                    return "Вакансии не найдены"
                else:
                    return [x for x in vacancies if x["salary_from"] >= salary]
        except FileNotFoundError:
            raise FileNotFoundError("Файл с вакансиями не найден")

    def delete_vacancy(self, vacancy: dict):
        """Удаляет вакансию из файла с вакансиями"""
        try:
            with open(self.__path) as file:
                vacancies = json.load(file)
                if not vacancies:
                    return "Вакансии не найдены"
                elif vacancy not in vacancies:
                    return "Такой вакансии нет"
                else:
                    vacancies.remove(vacancy)
        except FileNotFoundError:
            raise FileNotFoundError("Файл с вакансиями не найден")
