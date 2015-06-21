class LogItem:
    def __init__(self, mbr=None, time_in=None, time_out=None):
        self.__mbr = mbr
        self.__time_in = time_in
        self.__time_out = time_out

    @property
    def member(self):
        return self.__mbr

    @property
    def time_in(self):
        return self.__time_in

    @property
    def time_out(self):
        return self.__time_out

    @member.setter
    def member(self, mbr):
        self.__mbr = mbr

    @time_in.setter
    def time_in(self, time_in):
        self.__time_in = time_in

    @time_out.setter
    def time_out(self, time_out):
        self.__time_out = time_out

    def get_details(self):
        details = (self.__member, self.__time_in, self.__time_out)
        return details

    def has_details(self):
        if self.__mbr is None and self.__time_in is None:
            return False
        else:
            return True