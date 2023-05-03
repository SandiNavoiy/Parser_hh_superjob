import json
from json import JSONDecodeError

from scr.abc import VacancyStorage, JsonSave


class JSONSaver(JsonSave):
    def __init__(self, filename=None):
        self.filename = filename

    def add_vacancy(self, id, new_list):
        """Метод добавления вакансии в избраное"""
        temp_favourites = []
        for line in new_list:
            if id == line["number"]:
                temp_favourites.append(line)
        try:
            with open("favor.json", 'r', encoding="utf-8") as file:
                data_new = json.loads(file.read())
        except JSONDecodeError:
            print("Файл избранных вакансий пустой")
        else:
            for line in data_new:
                temp_favourites.append(line)

        with open("favor.json", 'w', encoding="utf-8") as file:
            json.dump(temp_favourites, file)
        print(f"Вакансия {id} добавлена")

    def remove_vacancy(self, id):
        """Метод удаления вакансии"""
        temp_favourites = []
        with open("favor.json", 'r', encoding="utf8") as file:
            data_new = json.loads(file.read())

            for line in data_new:
                if id != line["number"]:
                    temp_favourites.append(line)

        with open("favor.json", 'w') as file:
            json.dump(temp_favourites, file, indent=2, ensure_ascii=False)
        print(f"Вакансия {id} удалена")

    def clean_file_favourites(self):
        """Очистка файла (полная с избранными вакансиями)"""
        with open("favor.json", 'w', encoding="utf8"):
            print("--------------")
            print("файл очищен")
            print("--------------")
