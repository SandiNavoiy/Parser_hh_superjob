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
        try:
            if not isinstance(new_list, list):
                raise TypeError
        except TypeError:
            print('')
        else:
            for i in new_list:
                print(i)

    def to_txt(self):
        """Метод для сохранения вакансий в txt формате"""
        # Открываем json файл на чтение данных
        try:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                data_new = json.loads(file.read())
        # Ошибка при отсудствии файла
        except FileNotFoundError:
            print("Нет файла для выгрузки, создайте его")
        except JSONDecodeError:
            print("Файл  битый или пустой, создайте его заново")
        # Записываем данные в файл txt
        else:
            with open("favor.txt", 'w', encoding="utf-8") as file:
                file.write(json.dumps(data_new, ensure_ascii=False))
            print(f"файл перезаписан в формате txt")

    def json_to_xls(self):
        """Сохранение вакансий в Excel формате, при помощи библиотеки pandas """
        try:
            data = pd.read_json(self.file_name)
        # Ошибка при отсудствии файла
        except FileNotFoundError:
            print("Нет файла для выгрузки, создайте его")
        # Ошибка при другой кодировке
        except JSONDecodeError:
            print("Файл  битый, создайте его заново")
        # Ошибка при пустом файле
        except ValueError:
            print("Файл  пустой")
        else:
            data.to_excel("favor.xlsx", index=False)
            print("Файл xlsx выгружен")
