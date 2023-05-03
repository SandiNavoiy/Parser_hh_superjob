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
        print("3 - Просмотр файла с избраными вакансиями")
        print("4 - Вывод ваканисий в упрошенном виде с сортировкой(настраемой)")
        print("5 - Добавление вакансии в избраное")
        print("6 - Удаление вакансии из избраного")
        print("7 - Очистка файла избранного (полная)")
        print("8 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("9 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("11 - Вывод  ТОП ваканисий сортировкой(настраемой)")
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

            vacancy.list_of_vacancy()
            printing(vacancy.sorting())

        elif choice == "5":
            l = vacancy.list_of_vacancy()
            id_add = input("введите id номер вакансии для добавление в избраное(для просмотра id выполните действие 4)")
            json_saver.add_vacancy(id_add, l)


        elif choice == "6":
            vacancy.list_of_vacancy()
            id_del = input("введите id номер вакансии для удаления из избраного (для просмотра id выполните действие 3)")
            json_saver.remove_vacancy(id_del)



        elif choice == "7":

            json_saver.clean_file_favourites()

        elif choice == "8":
            print(vacancy.read_file_favourites('hh.json'))

        elif choice == "9":
            print(vacancy.read_file_favourites('sj.json'))

        elif choice == "11":
            top = int(input(" Введите количесво вакансий для вывода"))
            try:
                if not isinstance(top, int):
                    raise ValueError('Параметр "top" должен быть числом')
            except ValueError as e:
                print(e)
            else:
                vacancy.list_of_vacancy()
                vacancy.sorting()
                printing(vacancy.top(top))




        elif choice == "10":
            print("--------------")
            print("Спасибо за обращение\n"
                  "До новых встреч!")
            print("--------------")
            break


        else:
            print("Введите правильное значение действий!!!!")


def printing(new_list):
    """функция для посторочного вывода списка"""
    for i in new_list:
        print(i)
