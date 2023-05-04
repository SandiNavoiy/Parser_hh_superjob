# сборник функций
from scr.headhunter import HeadHunterAPI
from scr.json_saver import JSONSaver
from scr.superjob import SuperJobAPI
from scr.transform import Transform
from scr.vacancy import Vacancy, NotID, NegativeSalary


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
        print("4 - Вывод вакансий в упрошенном виде с сортировкой")
        print("5 - Добавление вакансии в избранное")
        print("6 - Удаление вакансии из избранного")
        print("7 - Очистка файла избранного (полная)")
        print("8 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("9 - Просмотр файла загрузки с API superjob, формат json (служебная функция)")
        print("10 - Вывод  ТОП вакансий сортировкой")
        print("11 - Вывод  избранного в формате txt")
        print("12 - Вывод  избранного в формате xls")
        print("13 - Вывод  вакансии по id")
        print("14 - Поиск по вакансии по ключевым словам")
        print("15 - Сравнение вакансий по заработной плате")
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
            try:
                id_add = int(input("Введите id номер вакансии для добавление в избранное(для просмотра id выполните действие 4):  "))
                if id_add < 0 or id_add > 201:
                    raise NotID
            except ValueError as e:
                print(f"{e} Параметр id_add должен быть целым числом")
            except NotID:
                print(NotID())
            else:
                json_saver.add_vacancy(id_add, vacancy.list_of_vacancy())


        elif choice == "6":
            try:
                id_del = int(input("Введите id номер вакансии для удаления из избранного (для просмотра id выполните действие 3): "))
                if id_del < 0 or id_del > 201:
                    raise NotID
            except ValueError as e:
                print(f"{e} Параметр id_del должен быть целым числом")
            except NotID:
                print(NotID())
            else:
                json_saver.remove_vacancy(id_del)


        elif choice == "7":

            json_saver.clean_file_favourites()

        elif choice == "8":
            print(vacancy.read_file_favourites('hh.json'))

        elif choice == "9":
            print(vacancy.read_file_favourites('sj.json'))

        elif choice == "10":
            try:
                top = int(input(" Введите количество вакансий для вывода:  "))
            except ValueError as e:
                print(f"{e} Параметр top должен быть целым числом")
            else:
                vacancy.sorting()
                Transform.printing(vacancy.top(top))

        elif choice == "11":
            transform.to_txt()

        elif choice == "12":
            transform.json_to_xls()

        elif choice == "13":
            try:
                id_vac = int(input(" Введите номер вакансии:  "))
                if id_vac < 0 or id_vac > 201:
                    raise NotID
            except ValueError as e:
                print(f"{e} Параметр id_vac должен быть целым числом")
            except NotID:
                print(NotID())
            else:
                vac1 = vacancy.get_vacancies(id_vac)
                print(vac1)

        elif choice == "14":
            print("Введите параметры")
            job_title = input("Введите ключ к профессии:  ")
            url_job = input("Введите ключ URL:  ")
            try:
                payment = int(input("Введите уровень з/п:  "))
                if payment < 0:
                    raise NegativeSalary
            except ValueError as e:
                print(f"{e} Параметр payment должен быть целым числом")
                payment = 0
            except NegativeSalary as e:
                print(NegativeSalary())
                payment = 0
            requirements = input("Введите ключ к требованиям:  ")
            city = input("Введите ключ к городу:  ")
            print(vacancy.found(job_title, url_job, payment, requirements, city))


        elif choice == "15":
            try:
                id_vac1 = int(input(" Введите номер вакансии"))
                id_vac2 = int(input(" Введите номер вакансии"))
                if id_vac1 < 0 or id_vac1 > 201:
                    raise NotID
                if id_vac2 < 0 or id_vac2 > 201:
                    raise NotID

            except ValueError as e:
                print(f"{e} Параметр id_vac1, id_vac1 должны быть целыми числами")
            except NotID:
                print(NotID())
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
