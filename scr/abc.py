from abc import ABC, abstractmethod

class Employer(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass
