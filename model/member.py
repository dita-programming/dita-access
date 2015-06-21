class Member:
    def __init__(self, id_no=None, name=None):
        self.__name = name
        self.__id = id_no

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @name.setter
    def name(self, val):
        self.__name = val.lower()

    @id.setter
    def id(self, val):
        self.__id = val.lower()

    def get_details(self):
        details = (self.__id, self.__name)
        return details

    def has_details(self):
        if self.__name is None and self.__id is None:
            return False
        else:
            return True


