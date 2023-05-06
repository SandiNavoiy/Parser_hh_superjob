import json
from json import JSONDecodeError
import pandas as pd


class Transform:
    """Класс для вывода файла с избранными вакансиями в различных форматах """

    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def printing(new_list):
        """Метод для построчного вывода списка"""
        for i in new_list:
            print(i)

    def to_txt(self):
        """Метод для сохранения вакансий в txt формате"""
        # Открываем json файл на чтение данных
        try:
            with open(self.file_name, 'r', encoding="utf8") as file:
                data_new = json.loads(file.read())
        except (FileNotFoundError, JSONDecodeError):
            print("Нет файла для выгрузки или он битый, создайте его")
        # Записываем данные в файл txt
        else:
            with open("favor.txt", 'w', encoding="utf8") as file:
                file.write(json.dumps(data_new, ensure_ascii=False))
            print(f"файл перезаписан в формате txt")

    def json_to_xls(self):
        """Сохранение вакансий в Excel формате, при помощи библиотеки pandas """
        try:
            data = pd.read_json(self.file_name)
        except (FileNotFoundError, JSONDecodeError):
            print("Нет файла для выгрузки или он битый, создайте его")
        else:
            data.to_excel("favor.xlsx", index=False)
            print("Файл xlsx выгружен")
