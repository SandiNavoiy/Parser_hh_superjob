# сборник функций

def interact_with_user(vacancies):
    """
    Функция для взаимодействия с пользователем.
    :param vacancies: список вакансий.
    """
    while True:
        print("Выберите действие:")
        print("1 - Показать все вакансии")
        print("2 - Добавить вакансию")
        print("3 - Фильтровать вакансии")
        print("4 - Удалить вакансию")
        print("5 - Выйти")

        choice = input()

        if choice == "1":
            for vacancy in vacancies:
                print(vacancy)
        elif choice == "2":
            title = input("Введите название вакансии: ")
            link = input("Введите ссылку на вакансию: ")
            salary = input("Введите зарплату: ")
            description = input("Введите описание вакансии: ")
            new_vacancy = Vacancy(title, link, salary, description)
            vacancies.append(new_vacancy)
            print("Вакансия успешно добавлена!")
        elif choice == "3":
            print("Выберите тип фильтрации:")
            print("1 - Фильтровать по зарплате")
            print("2 - Фильтровать по ключевым словам в описании")

            filter_choice = input()

            if filter_choice == "1":
                salary_range = input("Введите диапазон зарплаты через дефис (например, 50000-100000): ")
                min_salary, max_salary = salary_range.split("-")
                filtered_vacancies = list(filter(lambda v: v.salary and (int(min_salary.replace(" ", "")) <= v.salary <= int(max_salary.replace(" ", ""))), vacancies))
            elif filter_choice == "2":
                keywords = input("Введите ключевые слова через запятую: ")
                keywords_list = [kw.strip() for kw in keywords.split(",")]
                filtered_vacancies = list(filter(lambda v: any([kw in v.description.lower() for kw in keywords_list]), vacancies))

            for vacancy in filtered_vacancies:
                print(vacancy)
        elif choice == "4":
            link = input("Введите ссылку на вакансию, которую нужно удалить: ")
            vacancies = list(filter(lambda v: v.link != link, vacancies))
            print("Вакансия успешно удалена!")
        elif choice == "5":
            break