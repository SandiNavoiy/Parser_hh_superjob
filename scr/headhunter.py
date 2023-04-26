import json

import requests

from scr.abc import Employer


class HeadHunterAPI(Employer):
    """Класс для работы с сайтом HeadHunter"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self):
        # params = {
        #    'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
        #    'area': 1,  # Поиск ощуществляется по вакансиям города Москва
        #    'page': page,  # Индекс страницы поиска на HH
        #    'per_page': 100  # Кол-во вакансий на 1 странице
        # }

        try:
            self.req = requests.get(self.url).json()

        except requests.exceptions.RequestException as e:
            print(f"Нет соединения, ошибка{e}. СМЕНИ РЕГИОН VPN!! ")
        else:
            with open("hh.json", "w", encoding="utf-8") as f:
                json.dump(self.req, f, indent=2, ensure_ascii=False)

    def __repr__(self):
        return self.req
