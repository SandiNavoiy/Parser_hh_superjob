import json

from scr.abc import VacancyStorage


class JSONSaver(VacancyStorage):
    def __init__(self, filename = None):
        self.filename = filename
    def add_vacancy(self, id):
        with open("favourites.json", 'a'):
            pass

    def remove_vacancy(self, id):
        pass





    def clean_file_favourites(self):
        """очистка файла (полная с избраными вакансиями"""
        with open("favourites.json", 'w'):
            print("--------------")
            print("файл очищен")
            print("--------------")


