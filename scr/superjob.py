import json

import requests

from scr.abc import Employer


class SuperJobAPI(Employer):
    """Класс для работы с сайтом superjob"""

    def __init__(self):
        self.__secret_key = "v3.r.137507897.7442de4e25a339834ba4ba48698f024e614b7679.9bcdfdef787ba2af71fef71ac60a6c78b451c32d"
        self.__url = 'https://api.superjob.ru/2.0/%s'

    def get_vacancies(self, keyword):
        catalogue_id = 48  # id каталога "Разработка, программирование"
        #town_id = 4  # id города Москва

        vacancies_count = 100  # api запрещает запрашивать больше 100 вакансий
        self.keyword = keyword  # ключивое слово
        params = {'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': self.keyword}
        headers = {'X-Api-App-Id': self.__secret_key}
        relative_url = 'vacancies/'
        try:
            self.response = requests.get(self.__url % relative_url, params=params,
                                         headers=headers).json()

        except requests.exceptions.RequestException as e:
            print(f"Нет соединения, ошибка{e}. СМЕНИ РЕГИОН VPN!! ")
        else:
            print("Информация с superjob.ru успешно загружена")
            with open("sj.json", "w", encoding="utf-8") as f:
                json.dump(self.response, f, indent=2, ensure_ascii=False)

    def __repr__(self):
        return self.response
