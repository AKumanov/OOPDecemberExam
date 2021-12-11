from project.common import validate_string


class Driver:
    __INVALID_NAME_MESSAGE = 'Name should contain at least one character!'

    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @classmethod
    def __validate_name(cls, value):
        if not validate_string(value):
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value
