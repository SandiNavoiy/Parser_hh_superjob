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


    def list_of_vacancy_hh(self):
        with open('hh.json', 'r', encoding="utf8") as file:
            json.load(file)
            number_hh = 1
            new_list_hh = []
            for vacancy in file:
                new_list_hh.append({
                    'number': number_hh,
                    'name': vacancy['name'],
                    'city': vacancy['area']['name'],
                    'experience': vacancy['experience']['name'],
                    'salary_from': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to'],
                    'url': vacancy['alternate_url']
                })
                number_hh += 1
        print(new_list_hh)

    def list_of_vacancy_sj(self):
        new_list_sj = []
        number_sj = 1
        for vacancy in self.f['objects']:
            new_list_sj.append({
                    'number': number_sj,
                    'name': vacancy['profession'],
                    'city': vacancy['client']['town']['title'],
                    'experience': vacancy['experience']['title'],
                    'salary_from': vacancy['payment_from'],
                    'salary_to': vacancy['payment_to'],
                    'url': vacancy['link']})
            number_sj += 1
        return new_list_sj


