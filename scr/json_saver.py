# Реализация класса JSONSaver
import json
from json import JSONDecodeError
from scr.abc import JsonSave


class JSONSaver(JsonSave):
    """Класс сохранения вакансий в файл и его изменения"""

    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, id, new_list):
        """Метод добавления вакансии в избранное"""
        temp_favourites = []
        # Прогоняем список на наличие в нем нужного id
        for line in new_list:
            if id == line["number"]:
                temp_favourites.append(line)
        # Отработка исключения в случае битого файла или пустого
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                data_new = json.loads(file.read())
        except (FileNotFoundError, JSONDecodeError):
            print("Файл избранных вакансий пустой или отсудствует")
            with open(self.filename, 'w', encoding="utf8"):
                pass
        else:
            for line in data_new:
                temp_favourites.append(line)
        # Записываем вакансию в файл
            with open(self.filename, 'w', encoding="utf-8") as file:
                json.dump(temp_favourites, file, ensure_ascii=False)
            print(f"Вакансия {id} добавлена")

    def remove_vacancy(self, id):
        """Метод удаления вакансии, провевека наличия вакансии в принципе обходится самой реалиацией"""
        temp_favourites = []
        # Идея в том, чтобы прогнать файл избраного и при нахождении того что нужно удалить
        # просто не добавлять его в новый временый список, который перезаписываем в файл избранного,
        # в принципе в таком варианте валидация ввода на наличия не имеет смысла
        try:
            with open(self.filename, 'r', encoding="utf8") as file:
                data_new = json.loads(file.read())
        except (FileNotFoundError, JSONDecodeError):
            print("нет  файла  с избраными вакансиями или он битый, создайте его")
        else:
            for line in data_new:
                if id != line["number"]:
                    temp_favourites.append(line)
        with open(self.filename, 'w') as file:
            json.dump(temp_favourites, file, indent=2, ensure_ascii=False)
        print(f"Вакансия {id} удалена")

    def clean_file_favourites(self):
        """Очистка файла (полная с избранными вакансиями)"""
        with open(self.filename, 'w', encoding="utf8"):
            print("--------------")
            print("файл очищен")
            print("--------------")
