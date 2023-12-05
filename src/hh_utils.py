import requests

from .abs_classes import JobsParser


class HeadHunterAPI(JobsParser):

    def get_vacancies(self, keyword: str):
        """Осуществляет поиск вакансий по ключевому слову и сохраняет вакансии в список"""
        vacancies_list = []

        try:
            for i in range(20):
                url = "https://api.hh.ru/vacancies"
                params = {"text": keyword, "count": 100, "page": 0, "only_with_salary": "true"}
                response = requests.get(url, params=params)
                data = response.json()
                vacancies = data["items"]

                for j in range(len(vacancies)):

                    salary_from = vacancies[j]["salary"]["from"]
                    if not salary_from:
                        salary_from = 0

                    salary_to = vacancies[j]["salary"]["to"]
                    if not salary_to:
                        salary_to = 0

                    vacancy = {"name": vacancies[j]["name"],
                               "url": vacancies[j]["url"],
                               "salary_from": salary_from,
                               "salary_to": salary_to,
                               "requirements": vacancies[j]["snippet"].get("requirement", "")}
                    vacancies_list.append(vacancy)
            return vacancies_list

        except (requests.exceptions.HTTPError, ValueError, KeyError) as e:
            raise Exception(e)
