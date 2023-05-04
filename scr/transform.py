import json

import pandas as pd


class Transform:
    """Класс для вывода файла и избраными вакансиями в различных форматах """

    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def printing(new_list):
        """Функция для построчного вывода списка"""
        for i in new_list:
            print(i)

    def to_txt(self):
        """Метод cброса вакансии в txt"""

        with open(self.file_name, 'r', encoding="utf8") as file:
            data_new = json.loads(file.read())

        with open("favor.txt", 'w', encoding="utf8") as file:
            file.write(json.dumps(data_new, ensure_ascii=False))
        print(f"файл перезаписан в формате txt")

    def json_to_xls(self):
        """Сохранение вакансий в Эксель формате"""
        data = pd.read_json(self.file_name)
        data.to_excel("favor.xlsx", index=False)
        print("Файл xlsx выгружен")
