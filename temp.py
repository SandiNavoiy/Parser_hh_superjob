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






    def __add__(self, other):
        """Метод сложения количества"""
        if not isinstance(other, Item):
            raise Exception("Складывать можно только наследников класса Item.")
        elif not isinstance(self, Item):
            raise Exception("Складывать можно только наследников класса Item.")

        return self.quantity + other.quantity