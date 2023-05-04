    def get_data_by_id(self, element):
        """"""
        LinkedList.to_list(self)
        for i in self.new_list:
            if i['id'] == element:
                return i
        raise NotID()


class NotID(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Нет ID в списке.'

    def __str__(self):
        return self.message




   @classmethod
    def instantiate_from_csv(cls):
        """Открытие файла csv"""
        cls.all = []
        if not os.path.exists(cls.file_mame):
            raise FileNotFoundError('Отсутствует файл item.csv')

        with open(os.path.join(cls.file_mame), 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) != 3:
                    raise InstantiateCSVError("Файл item.csv поврежден")
                name = row[0]
                price = int(row[1])
                quantity = int(row[2])
                cls(name, price, quantity)

    #      raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(number):
        """ Статическая функция (метод) преобразования строкового представления числа в целое число"""
        return_number = float(number)
        return int(return_number)

    def __add__(self, other):
        """Метод сложения количества"""
        if not isinstance(other, Item):
            raise Exception("Складывать можно только наследников класса Item.")
        elif not isinstance(self, Item):
            raise Exception("Складывать можно только наследников класса Item.")

        return self.quantity + other.quantity