import requests


class SuperJobAPI():
    """Класс для работы с сайтом superjob"""

    secret_key = "v3.r.137507897.7442de4e25a339834ba4ba48698f024e614b7679.9bcdfdef787ba2af71fef71ac60a6c78b451c32d"
    def __init__(self):
       pass
    def get_vacancies(self,keyword1):
        secret_key = "v3.r.137507897.7442de4e25a339834ba4ba48698f024e614b7679.9bcdfdef787ba2af71fef71ac60a6c78b451c32d"
        catalogue_id = 48  # id каталога "Разработка, программирование"
        town_id = 4  # id города Москва
        vacancies_count = 100  # api запрещает запрашивать больше 100 вакансий
        keyword = keyword1 #ключивое слово
        params = {'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': keyword}
        headers = {'X-Api-App-Id': secret_key}
        relative_url = 'vacancies/'
        self.response = requests.get('https://api.superjob.ru/2.0/%s' % relative_url,params=params, headers=headers).json()
        print(self.response)


    def __repr__(self):
        return self.response
superjob_api = SuperJobAPI()
key_words = "dxdgfxffh"
superjob_vacancies = superjob_api.get_vacancies(key_words)
print(repr(superjob_vacancies))