import requests

from scr.abc import Employer


class SuperJobAPI(Employer):
    """Класс для работы с сайтом superjob"""

    secret_key = "v3.r.137507897.7442de4e25a339834ba4ba48698f024e614b7679.9bcdfdef787ba2af71fef71ac60a6c78b451c32d"
    def __init__(self):
       pass
    def get_vacancies(self):
        secret_key = "v3.r.137507897.7442de4e25a339834ba4ba48698f024e614b7679.9bcdfdef787ba2af71fef71ac60a6c78b451c32d"
        catalogue_id = 48  # id каталога "Разработка, программирование"
        town_id = 4  # id города Москва
        vacancies_count = 100  # api запрещает запрашивать больше 100 вакансий
        keyword = 'Программист' #ключивое слово
        params = {'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': keyword}
        headers = {'X-Api-App-Id': secret_key}
        relative_url = 'vacancies/'
        self.response = requests.get('https://api.superjob.ru/2.0/%s' % relative_url,params=params, headers=headers).json()


    def __repr__(self):
        return self.response

