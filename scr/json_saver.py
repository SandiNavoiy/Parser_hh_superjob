import json
from json import JSONDecodeError

from scr.abc import VacancyStorage


class JSONSaver(VacancyStorage):
    def __init__(self, filename=None):
        self.filename = filename

    def add_vacancy(self, id, new_list):
        """метод добавления вакансии в избраное"""
        temp_favourites = []
        for line in new_list:
            if id == line["number"]:
                temp_favourites.append(line)
        with open("favourites.json", 'r', encoding="utf-8") as file:
            data_new = json.loads(file.read())
            for line in data_new:
                temp_favourites.append(line)

        with open("favourites.json", 'w', encoding="utf-8") as file:
            json.dump(temp_favourites, file, ensure_ascii=False)
        print(f"Вакансия {id} добавлена")

    def remove_vacancy(self, id):
        temp_favourites = []
        with open("favourites.json", 'r', encoding="utf8") as file:
            data_new = json.loads(file.read())

            for line in data_new:
                if id != line["number"]:
                    temp_favourites.append(line)

        with open("favourites.json", 'w') as file:
            json.dump(temp_favourites, file, indent=2, ensure_ascii=False)
        print(f"Вакансия {id} удалена")

    def clean_file_favourites(self):
        """очистка файла (полная с избраными вакансиями"""
        with open("favourites.json", 'w'):
            print("--------------")
            print("файл очищен")
            print("--------------")
