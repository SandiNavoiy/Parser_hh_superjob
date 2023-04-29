# сборник функций
from scr.headhunter import HeadHunterAPI
from scr.json_saver import JSONSaver
from scr.superjob import SuperJobAPI
from scr.vacancy import Vacancy


def welcome():
    """функция вывода приветствия"""
    print("                  Доброго времени суток")
    print("Вас приветсвует программа по поиску и отбору вакансий с сайтов:\n"
          "                        1. hh.ru\n"
          "                       2. superjob.ru")
    print("Далее будет представлено меню с возможными действиями")
    input("Нажмите любую клавишу для продолжения..................")


def interact_with_user():
    """
    Функция для взаимодействия с пользователем.
    :param vacancies: список вакансий.
    """
    json_saver = JSONSaver()
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    vacancy = Vacancy()

    while True:
        print("Выберите действие:")
        print("1 - Загрузить свежую информацию с hh.ru")
        print("2 - Загрузить свежую информацию с superjob.ru")
        print("3 - просмотр файла с избраными вакансиями")
        print("4 - вывод ваканисий с hh в упрошенном виде")
        print("5 - вывод ваканисий с superjob в упрошенном виде")
        print("7 - очистка файла (полная с избранными вакансиями)")
        print("8 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("9 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("10 - Выйти")


        choice = input("Введите значение---")

        if choice == "1":
            key_words = input("Введите ключевое слово поисков:   ")

            hh_vacancies = hh_api.get_vacancies(key_words)


        elif choice == "2":
            key_words = input("Введите ключевое слово поисков:    ")
            superjob_vacancies = superjob_api.get_vacancies(key_words)


        elif choice == "3":

            vacancy.read_file_favourites('favourites.json')

        elif choice == "4":

            vacancy.read_file_favourites('hh.json')
            vacancy.list_of_vacancy_hh()

        elif choice == "5":

            vacancy.read_file_favourites('sj.json')
            vacancy.list_of_vacancy_sj()



        elif choice == "7":

            json_saver.clean_file_favourites()

        elif choice == "8":
            vacancy.read_file_favourites('hh.json')

        elif choice == "9":
            vacancy.read_file_favourites('sj.json')



        elif choice == "10":
            print("--------------")
            print("Спасибо за обращение\n"
                  "До новых встреч!")
            print("--------------")
            break


        else:
            print("Введите правильное значение действий!!!!")
