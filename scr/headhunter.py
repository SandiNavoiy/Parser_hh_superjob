import json

import requests

from scr.abc import Employer


class HeadHunterAPI(Employer):
    """Класс для работы с сайтом HeadHunter"""
    def __init__(self):
        pass


    def get_vacancies(self):
        #params = {
        #    'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
        #    'area': 1,  # Поиск ощуществляется по вакансиям города Москва
        #    'page': page,  # Индекс страницы поиска на HH
        #    'per_page': 100  # Кол-во вакансий на 1 странице
        #}
        # импортируем библиотеку request для работы с данными в сети
        # req = requests.get('https://api.hh.ru/areas')
        # data = req.content.decode()
        # req.close()
        # jsObj = json.loads(data)
        # print(jsObj)

        self.req = requests.get('https://api.hh.ru/vacancies').json()
        with open("hh.json", "w", encoding="utf-8") as f:
            json.dump(self.req, f, indent=2, ensure_ascii=False)

    def __repr__(self):
        return self.req





