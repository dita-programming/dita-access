class Laptop:
    def __init__(self, make=None, serial=None, member=None):
        self.__make = make
        self.__serial = serial
        self.__member = member

    @property
    def make(self):
        return self.__make

    @property
    def serial(self):
        return self.__serial

    @property
    def member(self):
        return self.__member

    @make.setter
    def make(self, val):
        self.__make = val.lower()

    @serial.setter
    def serial(self, val):
        self.__serial = val.lower()

    @member.setter
    def member(self, val):
        self.__member = val

    def get_details(self):
        details = (self.__make, self.__serial, self.__member)
        return details

    def has_details(self):
        if self.__make is None and self.__serial is None and self.__member is None:
            return False
        else:
            return True