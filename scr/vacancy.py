import json

from scr.abc import VacancyStorage


class Vacancy(VacancyStorage):
    def __init__(self, job_title: str = None, url_job: str = None, payment_range = None, requirements: str = None):
        if isinstance(job_title, str):
            raise ValueError('Параметр "job_title" должен быть строкой')
        self.job_title = job_title  # описание проффесии запроса

        if isinstance(url_job, str):
            raise ValueError('Параметр "url_job" должен быть строкой')
        self.url_job = url_job  # урл запроса

        if isinstance(payment_range, str):
            raise ValueError('Параметр "payment_range" должен быть строкой')
        self.payment_range = payment_range  # уровень заработной платы(диапазон)

        if isinstance(requirements, str):
            raise ValueError('Параметр "requirements" должен быть строкой')
        self.requirements = requirements  # требования

    def read_file_favourites(self, file_name):
        """просмотр файла с избраными вакансиями"""
        with open(file_name, 'r', encoding="utf8") as file:
            self.f = file.read()
        return self.f


    def list_of_vacancy(self):
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
                        "salary_from": vacancy["payment_from"],
                        "salary_to": vacancy["payment_to"],
                        "url": vacancy["link"]})
                    number += 1

                except (KeyError, TypeError):
                    self.new_list.append({
                        'number': number,
                        'name': vacancy['profession'],
                        'city': 'Адрес не указан',
                        'experience': vacancy['experience']['title'],
                        'salary_from': vacancy['payment_from'],
                        'salary_to': vacancy['payment_to'],
                        'url': vacancy['link']
                    })
                    number += 1

        return self.new_list


    def sorting(self):
        """сортировка hh"""
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
        n = 0
        self.new_top = []
        while n <= top:
            for i in self.new_list_sort:
                self.new_top.append(i)
                n += 1
        return self.new_top

