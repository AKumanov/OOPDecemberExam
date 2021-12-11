from project.common import validate_string


class Race:
    __INVALID_NAME_MESSAGE = 'Name cannot be an empty string!'

    def __init__(self, name: str):
        self.name = name
        self.drivers = []

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
