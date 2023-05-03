import json
from json import JSONDecodeError

from scr.abc import VacancyStorage


class JSONSaver(VacancyStorage):
    def __init__(self, filename = None):
        self.filename = filename
    def add_vacancy(self, id, new_list):

        with open("favourites.json", 'a', encoding="utf-8") as file:
            new_list = json.loads(file.read())

            for line in new_list:
                if line['number'] == id:
                    file.write(line)
        file.close()



    def remove_vacancy(self, id):
        temp_favourites = []
        with open("favourites.json", 'r') as file:
            data_new = json.loads(file.read())
            try:
                for line in data_new:
                    if line['number'] != id:
                        temp_favourites.append(line)
            except (KeyError, JSONDecodeError) as e:
                print(e)
        with open("favourites.json", 'w') as file:
            json.dump(temp_favourites, file, indent=2, ensure_ascii=False)

    def clean_file_favourites(self):
        """очистка файла (полная с избраными вакансиями"""
        with open("favourites.json", 'w'):
            print("--------------")
            print("файл очищен")
            print("--------------")


