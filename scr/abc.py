from abc import ABC, abstractmethod

class Employer(ABC):
    """Абстрактный класс для работы с API сайтов"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass



class VacancyStorage(ABC):
    """Абстрактный класс для классов работы с данными вакансий"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **kwargs):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy):
        pass





