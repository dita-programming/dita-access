from abc import ABCMeta, abstractmethod


class ValidatorFactory:
    def __init__(self, mbr_dao, lpt_dao, log_dao, mbr, lpt):
        self.__mbr_dao = mbr_dao
        self.__lpt_dao = lpt_dao
        self.__log_dao = log_dao
        self.__mbr = mbr
        self.__lpt = lpt

    def get_validator(self, val):
        if val is None:
            return None

        if val.lower() == "sign in":
            return SignInValidator(self.__mbr_dao, self.__lpt_dao, self.__log_dao, self.__mbr, self.__lpt)
        elif val.lower() == "sign out":
            return SignOutValidator(self.__mbr_dao, self.__log_dao, self.__mbr)
        else:
            return None


class BaseValidator(metaclass=ABCMeta):
    def __init__(self):
        self._mbr_val = None
        self._lpt_val = None
        self._log_dao = None
        self._mbr = None
        self._lpt = None
        self._msg = None
        self._msg_details = None

    def _is_member_in(self):
        members = [obj.member for obj in self._log_dao.get_incomplete_objects()]

        for member in members:
            if member.get_details() == self._mbr.get_details():
                return True

        return False

    @abstractmethod
    def validate(self):
        pass

    @property
    def message(self):
        msg = (self._msg, self._msg_details)
        return msg


class SignInValidator(BaseValidator):
    def __init__(self, mbr_dao, lpt_dao, log_dao, mbr, lpt):
        super(SignInValidator, self).__init__()
        self._mbr_val = MemberValidator(mbr_dao, mbr)
        self._lpt_val = LaptopValidator(lpt_dao, lpt)
        self._log_dao = log_dao
        self._mbr = mbr
        self._lpt = lpt
        self.__no_laptop_checked = False

    def validate(self):
        # Check whether member exists
        if not self._mbr_val.check_object_exists():
            self._msg = "Unregistered Member"
            self._msg_details = "Member not registered!"
            return False

        # Check whether member has already signed in
        if self._is_member_in():
            self._msg = "Member in"
            self._msg = "Member has already signed in!".format(self._mbr.id)
            return False

        if not self.__no_laptop_checked:
            # Check whether laptop exists
            if not self._lpt_val.check_object_exists():
                self._msg = "Unregistered Laptop"
                self._msg_details = "Laptop not registered!"
                return False
            else:
                # Check whether laptop is registered to the right member

                if self._mbr.id != self._lpt.member.id:
                    self._msg = "Duplicate Laptop"
                    self._msg_details = "Laptop registered to another member!"
                    return False

        self._msg = "Welcome"
        self._msg_details = "Welcome {}!".format(self._mbr.name.split()[0].title())
        return True

    @property
    def no_laptop_checked(self):
        return self.__no_laptop_checked

    @no_laptop_checked.setter
    def no_laptop_checked(self, bool):
        self.__no_laptop_checked = bool


class SignOutValidator(BaseValidator):
    def __init__(self, mbr_dao, log_dao, mbr):
        super(SignOutValidator, self).__init__()
        self._mbr_val = MemberValidator(mbr_dao, mbr)
        self._log_dao = log_dao
        self._mbr = mbr

    def validate(self):
        # Check whether member has already signed in
        if not self._is_member_in():
            self._msg = "Member not in"
            self._msg_details = "Member hasn't signed in!"
            return False

        self._msg = "Goodbye"
        self._msg_details = "Goodbye {}!".format(self._mbr.name.split()[0].title())
        return True


class BaseObjectValidator(metaclass=ABCMeta):
    def __init(self, dao=None, obj=None):
        self._dao = dao
        self._obj = obj

    @abstractmethod
    def check_object_exists(self):
        pass


class MemberValidator(BaseObjectValidator):
    def __init__(self, dao, obj):
        super(MemberValidator, self).__init__()
        self._dao = dao
        self._obj = obj

    def check_object_exists(self):
        return self._dao.get_object(self._obj.id).has_details()


class LaptopValidator(BaseObjectValidator):
    def __init__(self, dao, obj):
        super(LaptopValidator, self).__init__()
        self._dao = dao
        self._obj = obj

    def check_object_exists(self):
        return self._dao.get_object(self._obj.serial).has_details()


class LogItemValidator(BaseObjectValidator):
    def __init__(self, dao, obj):
        super(LogItemValidator, self).__init__()
        self._dao = dao
        self._obj = obj

    def check_object_exists(self):
        pass

    def get_members_in(self):
        members_in = []
        log_items = self._dao.get_objects()

        if log_items:
            members_in = [item.member for item in log_items if item.time_out is None]

        return members_in