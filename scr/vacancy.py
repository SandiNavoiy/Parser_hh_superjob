from scr.abc import VacancyStorage


class Vacancy(VacancyStorage):
    def __init__(self, job_title: str,url_job, payment_range, requirements:str):
        self.job_title = job_title  #описание проффесии запроса
        self.url_job = url_job #урл запроса
        self.payment_range = payment_range #уровень заработной платы(диапазон)
        self.requirements = requirements  #требования


    def __init__(self):
        pass
    def add_vacancy(self, vacancy):
        pass

    def get_vacancies(self, **kwargs):
        pass

    def remove_vacancy(self, vacancy):
        pass



