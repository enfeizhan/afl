"""
define team class
"""

class Team(object):
    """
    Class Team.
    """
    def __init__(self, name):
        assert type(name) == str, 'Team name must be a string!'
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class Lineup(Team):

