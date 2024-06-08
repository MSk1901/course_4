from .hh_utils import HeadHunterAPI
from .json_utils import JSONSaver
from .sj_utils import SuperJobAPI
from .vacancy import Vacancy

hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()

js_saver = JSONSaver()


def user_interaction():
    platforms = int(input("""Выберите платформу, на которой будем искать вакансии:
1 - HeadHunter
2 - SuperJob
3 - Обе
"""))
    while platforms not in [1, 2, 3]:
        platforms = int(input("""Вы ввели некорректное значение. Введите 1, 2 или 3.
1 - HeadHunter
2 - SuperJob
3 - Обе
"""))
    user_query = input("Введите запрос: ")

    needs_sorting = input("Сортировать вакансии по зарплатам? (Да/Нет): ")
    while needs_sorting.lower().strip() not in ["да", "нет"]:
        needs_sorting = input("Введите Да или Нет: ")
    if needs_sorting == "да":
        needs_sorting = True
    else:
        needs_sorting = False

    top = input("""Вывести определенное количество вакансий?
Введите цифру, сколько вакансий вывести или 0, если нужно вывести все: """)
    while not top.isdigit():
        top = input("Введите цифру, сколько вакансий вывести или 0, если нужно вывести все: ")

    print("\nСобираем информацию...")
    if platforms == 1:
        vacancies = hh_api.get_vacancies(user_query)
    elif platforms == 2:
        vacancies = sj_api.get_vacancies(user_query)
    else:
        vacancies = hh_api.get_vacancies(user_query) + sj_api.get_vacancies(user_query)

    js_saver.add_vacancies(vacancies)

    if needs_sorting:
        vacancies = Vacancy.sort_by_salary(vacancies)

    if bool(int(top)):
        vacancies = Vacancy.get_top_vacancies(vacancies, int(top))

    for vacancy in vacancies:
        vacancy_ = (
            Vacancy(vacancy["name"], vacancy["url"],
                    vacancy["salary_from"], vacancy["salary_to"], vacancy["requirements"]))
        print(f"\n{vacancy_}")
