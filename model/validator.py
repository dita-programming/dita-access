from abc import ABCMeta, abstractmethod

from model.do import Log, Member, Laptop


class ValidatorFactory:
    def __init__(self, mbr, lpt):
        self.__mbr = mbr
        self.__lpt = lpt

    def get_validator(self, val):
        if val is None:
            return None

        if val.lower() == "sign in":
            return SignInValidator(self.__mbr, self.__lpt)
        elif val.lower() == "sign out":
            return SignOutValidator(self.__mbr)
        else:
            return None


class BaseValidator(metaclass=ABCMeta):
    def __init__(self):
        self._mbr = None
        self._lpt = None
        self._msg = None
        self._msg_details = None

    def _is_member_in(self):
        members = Log.get_members_in()
        for member in members:
            if member == self._mbr:
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
    def __init__(self, mbr, lpt):
        super(SignInValidator, self).__init__()
        self._mbr = mbr
        self._lpt = lpt
        self.__no_laptop_checked = False

    def validate(self):
        # Check whether member exists
        print("pass")
        if self._mbr is None:
            self._msg = "Unregistered Member"
            self._msg_details = "Member not registered!"
            print("pass1")
            return False

        # Check whether member has already signed in
        if self._is_member_in():
            print("pass2")
            self._msg = "Member in"
            self._msg = "Member has already signed in!"
            return False

        if not self.__no_laptop_checked:
            # Check whether laptop exists
            print("pass3")

            if self._lpt is None:
                self._msg = "Unregistered Laptop"
                self._msg_details = "Laptop not registered!"
                return False
            else:
                # Check whether laptop is registered to the right member

                if self._mbr.id_no != self._lpt.owner.id_no:
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
    def __init__(self, mbr):
        super(SignOutValidator, self).__init__()
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