# сборник функций
from scr.headhunter import HeadHunterAPI
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
        print("3 - Добавить вакансию")
        print("4 - Фильтровать вакансии")
        print("5 - Удалить вакансию")
        print("6 - Выйти")

        choice = input()

        if choice == "1":
            key_words = input("Введите кючевое слово поисков")
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies()


        elif choice == "2":
            key_words = input("Введите кючевое слово поисков")
            superjob_api = SuperJobAPI()
            superjob_vacancies = superjob_api.get_vacancies()
        elif choice == "4":

            superjob_api = SuperJobAPI()
            superjob_vacancies = superjob_api.get_vacancies()

        elif choice == "5":
            print("Спасибо за работу\n"
                  "До новых встреч!")
            break
        else:
            print("Введите правильное замения действий!!!!")
