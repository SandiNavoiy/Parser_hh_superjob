# сборник функций
from scr.headhunter import HeadHunterAPI
from scr.json_saver import JSONSaver
from scr.superjob import SuperJobAPI


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
    while True:
        print("Выберите действие:")
        print("1 - Загрузить свежую информацию с hh.ru")
        print("2 - Загрузить свежую информацию с superjob.ru")
        print("3 - -")
        print("4 - -")
        print("5 - очистка файла (полная с избранными вакансиями")
        print("6 - Выйти")

        choice = input()

        if choice == "1":
            key_words = input("Введите ключевое слово поисков")
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies()


        elif choice == "2":
            key_words = input("Введите ключевое слово поисков")
            superjob_api = SuperJobAPI()
            superjob_vacancies = superjob_api.get_vacancies()



        elif choice == "5":
            clean = JSONSaver()
            clean.clean_file_favourites()



        elif choice == "6":
            print("--------------")
            print("Спасибо за обращение\n"
                  "До новых встреч!")
            print("--------------")
            break


        else:
            print("Введите правильное значение действий!!!!")
