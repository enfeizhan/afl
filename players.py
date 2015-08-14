# define players class
from datetime import date


class Player(object):
    def __init__(
            self,
            first_name='Matthew',
            middle_name='Harley',
            surname='Priddis',
            dob=date(1985, 3, 21),
            height=185,
            weight=86,
            position='Midfielder',
            club='West Coast',
            afl_debut=date(2006, 1, 1),
            ):
        self.first_name = first_name
        self.middle_name = middle_name
        self.surname = surname
        self.dob = dob
        self.height = height
        self.weight = weight
        self.position = position
        self.club = club
        self.afl_debut = afl_debut

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        assert isinstance(first_name, str),\
            'First name must be of a string type!\n'
        self.__first_name = first_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        assert isinstance(surname, str), 'Surname must be of a string type!\n'
        self.__surname = surname

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        assert isinstance(dob, date), 'DOB must be a datetime.date type.\n'
        self.__dob = dob
        self.age = (date.today() - dob).days // 365.25

    @property
    def afl_debut(self):
        return self.__afl_debut

    @afl_debut.setter
    def afl_debut(self, afl_debut):
        assert isinstance(afl_debut, date),\
            'afl_debut must be a datetime.date type.\n'
        self.__afl_debut = afl_debut
        self.afl_age = (date.today() - self.afl_debut).days // 365.25

    def __repr__(self):
        return self.first_name + ' ' + self.surname
