# define players class


class Player(object):
    def __init__(self, first_name, surname):
        assert type(first_name) == str,\
            'First name must be of a string type!\n'
        assert type(surname) == str,\
            'Surname must be of a string type!\n'
        self.first_name = first_name 
        self.surname = surname
    def get_first_name(self):
        return self.first_name
    def get_surname(self):
        return self.surname
    def get_name(self):
        return self.first_name + ' ' + self.surname
    def __str__(self):
        return self.first_name + ' ' + self.surname
    def __repr__(self):
        return self.first_name + ' ' + self.surname
