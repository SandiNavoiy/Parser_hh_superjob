# сборник функций
from scr.headhunter import HeadHunterAPI
from scr.json_saver import JSONSaver
from scr.superjob import SuperJobAPI
from scr.transform import Transform
from scr.vacancy import Vacancy


def welcome():
    """Функция вывода приветствия"""
    print("                  Доброго времени суток")
    print("Вас приветствует программа по поиску и отбору вакансий с сайтов:\n"
          "                        1. hh.ru\n"
          "                       2. superjob.ru")
    print("Далее будет представлено меню с возможными действиями")
    input("Нажмите любую клавишу для продолжения..................")


def interact_with_user():
    """Функция для взаимодействия с пользователем."""
    json_saver = JSONSaver("favor.json")
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    vacancy = Vacancy()
    transform = Transform("favor.json")
    vacancy.list_of_vacancy()

    while True:
        print("Выберите действие:")
        print("1 - Загрузить свежую информацию с hh.ru")
        print("2 - Загрузить свежую информацию с superjob.ru")
        print("3 - Просмотр файла с избранными вакансиями")
        print("4 - Вывод вакансий в упрошенном виде с сортировкой(настраемой)")
        print("5 - Добавление вакансии в избранное")
        print("6 - Удаление вакансии из избранного")
        print("7 - Очистка файла избранного (полная)")
        print("8 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("9 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("10 - Вывод  ТОП вакансий сортировкой(настраемой)")
        print("11 - Вывод  избраного в формате txt")
        print("12 - Вывод  избраного в формате xls")
        print("13 - Вывод  вакансии по id")
        print("14 - Поиск по вакансии по ключевым словам")
        print("15 - Сравенение вакансий по заработной плате")
        print("16 - Выйти")

        choice = input("Введите значение---")

        if choice == "1":
            key_words = input("Введите ключевое слово поисков:   ")
            hh_api.get_vacancies(key_words)
            vacancy.list_of_vacancy()


        elif choice == "2":
            key_words = input("Введите ключевое слово поисков:    ")
            superjob_api.get_vacancies(key_words)
            vacancy.list_of_vacancy()


        elif choice == "3":
            Transform.printing(vacancy.read_file_favourites('favor.json'))

        elif choice == "4":
            Transform.printing(vacancy.sorting())

        elif choice == "5":
            l = vacancy.list_of_vacancy()
            id_add = int(input("Введите id номер вакансии для добавление в избранное(для просмотра id выполните действие 4)"))
            json_saver.add_vacancy(id_add, vacancy.list_of_vacancy())


        elif choice == "6":
            id_del = int(input("Введите id номер вакансии для удаления из избранного (для просмотра id выполните действие 3)"))
            json_saver.remove_vacancy(id_del)


        elif choice == "7":

            json_saver.clean_file_favourites()

        elif choice == "8":
            print(vacancy.read_file_favourites('hh.json'))

        elif choice == "9":
            print(vacancy.read_file_favourites('sj.json'))

        elif choice == "10":
            top = int(input(" Введите количество вакансий для вывода"))
            try:
                if not isinstance(top, int):
                    raise ValueError('Параметр "top" должен быть числом')
            except ValueError as e:
                print(e)
            else:
                vacancy.sorting()
                Transform.printing(vacancy.top(top))
        elif choice == "11":
            transform.to_txt()
        elif choice == "12":
            transform.json_to_xls()

        elif choice == "13":
            id_vac = int(input(" Введите номер вакансии"))
            try:
                if not isinstance(id_vac, int):
                    raise ValueError('Параметр "id_vac" должен быть числом')
            except ValueError as e:
                print(e)
            else:
                vac1 = vacancy.get_vacancies(id_vac)
                print(vac1)

        elif choice == "14":
            print("Введите параметры ")
            job_title = input("Введите ключ к профессии")
            url_job = input("Введите ключ URL")
            payment = int(input("Введите уровень з/п"))
            requirements = input("Введите ключ к требованиям")
            city = input("Введите ключ к городу")
            vacancy.list_of_vacancy()
            print(vacancy.found(job_title, url_job, payment, requirements, city))


        elif choice == "15":
            id_vac1 = int(input(" Введите номер вакансии"))
            id_vac2 = int(input(" Введите номер вакансии"))
            try:
                if not isinstance(id_vac1, int) and not isinstance(id_vac2, int):
                    raise ValueError('Параметр "id_vac" должен быть числом')
            except ValueError as e:
                print(e)
            else:
                vac1 = vacancy.get_salary(id_vac1)
                vac2 = vacancy.get_salary(id_vac2)
                print(vac1)
                print(vac2)
                comparison(vac1, vac2)


        elif choice == "16":
            print("--------------")
            print("Спасибо за обращение\n"
                  "До новых встреч!")
            print("--------------")
            break


        else:
            print("Введите правильное значение действий!!!!")


def comparison(vac1, vac2):
    if vac1 > vac2:
        print("З/п первой вакансии больше")
    elif vac1 >= vac2:
        print("З/п первой вакансии больше или равна")
    elif vac1 < vac2:
        print("З/п первой вакансии меньше")
    elif vac1 < vac2:
        print("З/п первой вакансии меньше или равна")
