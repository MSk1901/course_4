import os

import requests
from dotenv import load_dotenv

from .abs_classes import JobsParser


class SuperJobAPI(JobsParser):

    def __init__(self):
        load_dotenv()
        self.headers = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}

    def get_vacancies(self, keyword: str):
        """Осуществляет поиск вакансий по ключевому слову и сохраняет вакансии в список"""
        vacancies_list = []
        try:
            for i in range(5):
                params = {"keyword": keyword, "count": 100, "page": i, "payment_from": 1, "currency": "rub"}
                url = "https://api.superjob.ru/2.0/vacancies/"
                response = requests.get(url, headers=self.headers, params=params)
                data = response.json()

                vacancies = data["objects"]

                for j in range(len(vacancies)):

                    salary_from = vacancies[j]["payment_from"]
                    if not salary_from:
                        salary_from = 0

                    salary_to = vacancies[j]["payment_to"]
                    if not salary_to:
                        salary_to = 0

                    vacancy = {"name": vacancies[j]["profession"],
                               "url": vacancies[j]["link"],
                               "salary_from": salary_from,
                               "salary_to": salary_to,
                               "requirements": vacancies[j]["candidat"]}
                    vacancies_list.append(vacancy)
            return vacancies_list

        except (requests.exceptions.HTTPError, ValueError, KeyError) as e:
            raise Exception(e)
