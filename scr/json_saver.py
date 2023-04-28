import json

from scr.abc import VacancyStorage


class JSONSaver(VacancyStorage):
    def __init__(self, filename):
        self.filename = filename
    def add_vacancy(self, vacancy):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(vars(vacancy), ensure_ascii=False) + "\n")

    def get_vacancies(self, **kwargs):
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                vacancy_data = json.loads(line)
                vacancy = Vacancy(**vacancy_data)
                yield vacancy

    def remove_vacancy(self, vacancy):
        with  open(self.filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

    with open(self.filename, "w", encoding="utf-8") as f:
        for line in lines:
            vacancy_data = json.loads(line)
            if vacancy_data != vars(vacancy):

    def clean_file_favourites(self):
        """очистка файла (полная с избраными вакансиями"""
        with open(path, 'w'):
            print("файл очищен")


