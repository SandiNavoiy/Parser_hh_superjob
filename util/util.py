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
    print("В случае первого использования програмы или удаления файлов hh.json и sj.json\n"
          "необходимо загрузить данные хотя бы с одного из сайтов!")
    input("Нажмите любую клавишу для продолжения..................")


def interact_with_user():
    """Функция для взаимодействия с пользователем."""
    # Инициируем обьекты классов для работы
    json_saver = JSONSaver("favor.json")
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    vacancy = Vacancy()
    transform = Transform("favor.json")
    vacancy.list_of_vacancy()

    while True:
        # Запускаем бесконечный цикл для работы меню
        print("Выберите действие:")
        print("1 - Загрузить свежую информацию с hh.ru")
        print("2 - Загрузить свежую информацию с superjob.ru")
        print("3 - Просмотр файла с избранными вакансиями")
        print("4 - Вывод вакансий в упрошенном виде с сортировкой")
        print("5 - Добавление вакансии в избранное")
        print("6 - Удаление вакансии из избранного")
        print("7 - Очистка файла избранного (полная)")
        print("8 - Вывод  ТОП вакансий сортировкой")
        print("9 - Вывод  избранного в формате txt")
        print("10 - Вывод  избранного в формате xls")
        print("11 - Вывод  вакансии по id")
        print("12 - Поиск по вакансии по ключевым словам")
        print("13 - Сравнение вакансий по заработной плате")
        print("14 - Выйти")
        choice = input("Введите значение---")
        # Непосредствено работы меню выбора
        if choice == "1":
            # Загружаем информацию с hh
            key_words = input("Введите ключевое слово поисков:   ")
            hh_api.get_vacancies(key_words)
            # Сразу формируем список вакансий для работы,
            # чтобы не прописывать в дальнейшем в каждом варианте
            vacancy.list_of_vacancy()

        elif choice == "2":
            # Загружаем информацию с sj
            key_words = input("Введите ключевое слово поисков:    ")
            superjob_api.get_vacancies(key_words)
            # Сразу формируем список вакансий для работы,
            # чтобы не прописывать в дальнейшем в каждом варианте
            vacancy.list_of_vacancy()

        elif choice == "3":
            # Вывод файла с избранным
            transform.printing(vacancy.read_file_favourites('favor.json'))

        elif choice == "4":
            # Вывод вакансий в упрошенном виде с сортировкой
            transform.printing(vacancy.sorting())

        elif choice == "5":
            # Добавление вакансии в избранное
            try:
                id_add = int(input(
                    "Введите id номер вакансии для добавление в избранное(для просмотра id выполните действие 4):  "))
                # В связи с тем что выгруз с каждого сайта ограничен 100 вакансий,
                # суммарно не более 200 отсекаем неверные значения ввода специальным исключением
                if id_add <= 0 or id_add > 201:
                    raise NotID
            # Валидация числа ввода
            except ValueError as e:
                print(f"{e} Параметр id_add должен быть целым числом")
            except NotID:
                print(NotID())
            else:
                json_saver.add_vacancy(id_add, vacancy.list_of_vacancy())

        elif choice == "6":
            # Удаление вакансии из избранного
            try:
                id_del = int(input(
                    "Введите id номер вакансии для удаления из избранного (для просмотра id выполните действие 3): "))
                # В связи с тем что выгруз с каждого сайта ограничен 100 вакансий,
                # суммарно не более 200 отсекаем неверные значения ввода специальным исключением
                if id_del <= 0 or id_del > 201:
                    raise NotID
            # Валидация числа ввода
            except ValueError as e:
                print(f"{e} Параметр id_del должен быть целым числом")
            except NotID:
                print(NotID())
            else:
                json_saver.remove_vacancy(id_del)

        elif choice == "7":
            # Очистка файла избранного (полная)
            json_saver.clean_file_favourites()

        elif choice == "8":
            # Вывод ТОП вакансий сортировкой
            # Валидация числа ввода
            try:
                top = int(input(" Введите количество вакансий для вывода:  "))
                if top <= 0 or top > 201:
                    raise NotID
            except ValueError as e:
                print(f"{e} Параметр top должен быть целым числом")
            except NotID:
                print("Валидные значения от 1 до 200")

            else:
                vacancy.sorting()
                transform.printing(vacancy.top(top))

        elif choice == "9":
            # Вывод избранного в формате txt
            transform.to_txt()

        elif choice == "10":
            # Вывод избранного в формате xls
            transform.json_to_xls()

        elif choice == "11":
            # Вывод вакансии по id
            # В связи с тем что выгруз с каждого сайта ограничен 100 вакансий,
            # суммарно не более 200 отсекаем неверные значения ввода специальным исключением
            try:
                id_vac = int(input(" Введите номер вакансии:  "))
                if id_vac <= 0 or id_vac > 201:
                    raise NotID
            # Валидация числа ввода
            except ValueError as e:
                print(f"{e} Параметр id_vac должен быть целым числом")
            except NotID:
                print(NotID())
            else:
                vac1 = vacancy.get_vacancies(id_vac)
                if vac1 == []:
                    print("Вакансии не загружены в программу")
                else:
                    print(vac1)

        elif choice == "12":
            # Поиск по вакансии по ключевым словам
            print("Введите параметры")
            job_title = input("Введите ключ к профессии:  ")
            url_job = input("Введите ключ URL:  ")
            # Валидация проводится только по значению залплаты, потому что input
            # по документации выдает значение в формате строки
            # и она не может быть отрицательной(хотя может:)),
            # используется рукописное исключение NegativeSalary
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

        elif choice == "13":
            # Сравнение вакансий по заработной плате
            # В связи с тем что выгруз с каждого сайта ограничен 100 вакансий,
            # суммарно не более 200 отсекаем неверные значения ввода специальным исключением
            try:
                id_vac1 = int(input(" Введите номер вакансии"))
                id_vac2 = int(input(" Введите номер вакансии"))
                if id_vac1 <= 0 or id_vac1 > 201:
                    raise NotID
                if id_vac2 <= 0 or id_vac2 > 201:
                    raise NotID
            except ValueError as e:
                print(f"{e} Параметр id_vac1, id_vac1 должны быть целыми числами")
            except NotID:
                print(NotID())
            else:
                try:
                    vac1 = vacancy.get_salary(id_vac1)
                    vac2 = vacancy.get_salary(id_vac2)
                except AttributeError:
                    print("Данные не загружены")
                else:
                    print(f" з/п первой вакансии = {vac1}")
                    print(f" з/п второй вакансии = {vac2}")
                    # Дополнительная функция сравнения
                    comparison(vac1, vac2)

        elif choice == "14":
            # Выход
            print("--------------")
            print("Спасибо за обращение\n"
                  "До новых встреч!")
            print("--------------")
            break

        else:
            print("Введите правильное значение действий!!!!")


def comparison(vac1, vac2):
    """ Функция реализации сравнения атрибутов класса, вынес чтобы совсем не загромождать"""
    if vac1 > vac2:
        print("З/п первой вакансии больше")
    elif vac1 < vac2:
        print("З/п первой вакансии меньше")
    else:
        print("Залплаты равны")
