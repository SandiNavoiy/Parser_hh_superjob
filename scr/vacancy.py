import json

from scr.abc import VacancyStorage
from scr.json_saver import JSONSaver


class Vacancy(VacancyStorage):
    """Класс работы с вакансиями"""

    def __init__(self):
        pass

    def read_file_favourites(self, file_name):
        """Просмотр файла с избранными вакансиями"""
        try:
            with open(file_name, 'r', encoding="utf8") as file:
                self.f = json.loads(file.read())
        except FileNotFoundError:
            JSONSaver.clean_file_favourites()

        return self.f

    def list_of_vacancy(self):
        """Метод сведения информации из 2-х json файлов в один список словарей"""
        number = 1
        self.new_list = []
        with open('hh.json', 'r', encoding="utf8") as file:
            data_new_hh = json.loads(file.read())
            for vacancy in data_new_hh["items"]:
                try:
                    self.new_list.append({
                        "number": number,
                        "name": vacancy["name"],
                        "city": vacancy["area"]["name"],
                        "experience": vacancy["experience"]["name"],
                        "salary_from": int(vacancy["salary"]["from"]),
                        "salary_to": vacancy["salary"]["to"],
                        "url": vacancy["alternate_url"]
                    })
                    number += 1

                except TypeError:
                    self.new_list.append({
                        "number": number,
                        "name": vacancy["name"],
                        "city": vacancy["area"]["name"],
                        "experience": vacancy["experience"]["name"],
                        "salary_from": 0,
                        "salary_to": 0,
                        "url": vacancy["alternate_url"]
                    })
                    number += 1
        with open('sj.json', 'r', encoding="utf8") as file:
            data_new_sj = json.loads(file.read())

            for vacancy in data_new_sj["objects"]:
                try:
                    self.new_list.append({
                        "number": number,
                        "name": vacancy["profession"],
                        "city": vacancy["client"]["town"]["title"],
                        "experience": vacancy["experience"]["title"],
                        "salary_from": int(vacancy["payment_from"]),
                        "salary_to": int(vacancy["payment_to"]),
                        "url": vacancy["link"]})
                    number += 1

                except (KeyError, TypeError):
                    self.new_list.append({
                        'number': number,
                        'name': vacancy['profession'],
                        'city': 'Адрес не указан',
                        'experience': vacancy['experience']['title'],
                        'salary_from': int(vacancy['payment_from']),
                        'salary_to': int(vacancy['payment_to']),
                        'url': vacancy['link']
                    })
                    number += 1

        return self.new_list

    def sorting(self):
        """Метод сортировки"""
        print("Выберите действие:")
        print("1 - сортировка по з/п, если з/п не указана то программа выводит ноль!")
        print("2 - сортировка по городу")
        print("3 - сортировка по названию вакансии")
        print("4 - сортировка по опыту")
        print("5 - сортировка по урл")
        print("Любое другое значение ввода- сортировка по порядковому номеру")
        choice = input("Введите значение---")
        if choice == "1":
            self.new_list_sort = sorted(self.new_list, key=lambda d: d['salary_from'], reverse=True)
        elif choice == "2":
            self.new_list_sort = sorted(self.new_list, key=lambda d: d['city'], reverse=False)
        elif choice == "3":
            self.new_list_sort = sorted(self.new_list, key=lambda d: d['name'], reverse=False)
        elif choice == "4":
            self.new_list_sort = sorted(self.new_list, key=lambda d: d['experience'], reverse=True)
        elif choice == "5":
            self.new_list_sort = sorted(self.new_list, key=lambda d: d['url'], reverse=True)
        else:
            self.new_list_sort = self.new_list

        return self.new_list_sort

    def top(self, top: int):
        """Выдача ТОП - количества вакансий"""
        n = 0
        self.new_top = []
        for i in self.new_list_sort:

            if n < top:
                self.new_top.append(i)
                n += 1
        return self.new_top

    def __gt__(self, other):
        """Метод больше"""
        if isinstance(other, Vacancy):
            if int(self.salary) > int(other.salary):
                return True
        return False

    def __ge__(self, other):
        """Метод больше или равно"""
        if isinstance(other, Vacancy):
            if int(self.salary) >= int(other.salary):
                return True
        return False

    def __lt__(self, other):
        """Метод меньше"""
        if isinstance(other, Vacancy):
            if int(self.salary) < int(other.salary):
                return True
        return False

    def __le__(self, other):
        """Метод меньше или равно"""
        if isinstance(other, Vacancy):
            if int(self.salary) <= int(other.salary):
                return True
        return False

    def get_vacancies(self, id):
        """Вывод вакансии по id"""
        temp_vac = []
        for line in self.new_list:
            if id == line["number"]:
                temp_vac.append(line)
        return temp_vac

    def get_salary(self, id):
        """Вывод з/п вакансии по id"""

        for line in self.new_list:
            if id == line["number"]:
                self.salary = int(line["salary_from"])
        return self.salary

    def found(self, job_title: str, url_job: str, payment, requirements: str, city: str):
        """Метод поиска по ключевым словам"""
        if not isinstance(job_title, str):
            raise ValueError('Параметр "job_title" должен быть строкой')
        self.job_title = job_title  # описание проффесии запроса

        if not isinstance(url_job, str):
            raise ValueError('Параметр "url_job" должен быть строкой')
        self.url_job = url_job  # урл запроса

        if not isinstance(payment, int):
            raise ValueError('Параметр "payment_range" должен быть числом')
        self.payment = payment  # уровень заработной платы

        if not isinstance(requirements, str):
            raise ValueError('Параметр "requirements" должен быть строкой')
        self.requirements = requirements  # требования

        if not isinstance(city, str):
            raise ValueError('Параметр "requirements" должен быть строкой')
        self.city = city  # город

        temp_vac = []
        for i in self.new_list:
            if self.job_title in i["name"] and self.url_job in i["url"] and self.payment > i[
                "salary_from"] and self.requirements in i["experience"] and self.city in i["city"]:
                temp_vac.append(i)

        if not temp_vac:
            return "Не найдено вакансий по заданным критериям"

        return temp_vac

class NotID(Exception):
    """Класс исключений"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Нет ID в списке.'

    def __str__(self):
        return self.message

class NegativeSalary(Exception):
    """Класс исключений - отрицательная з/п"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Залплата не может быть отрицательной.'

    def __str__(self):
        return self.message