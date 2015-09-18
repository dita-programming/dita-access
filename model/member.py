class Member:
    def __init__(self, id_no=None, name=None):
        self.__name = name
        self.__id = id_no
        self.__image = None
        self.__laptops = []

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def image(self):
        return self.__image

    @name.setter
    def name(self, val):
        self.__name = val.lower()

    @id.setter
    def id(self, val):
        self.__id = val.lower()

    @image.setter
    def image(self, image):
        self.__image = image

    def get_details(self):
        details = (self.__id, self.__name)
        return details

    def has_details(self):
        if self.__name is None and self.__id is None:
            return False
        else:
            return True


