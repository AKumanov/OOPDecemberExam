from abc import ABC, abstractmethod


class Car(ABC):
    _INVALID_SPEED_LIMIT_MESSAGE = None
    __MIN_ALLOWED_MODEL_SYMBOLS = 4

    _MIN_SPEED_LIMIT = None
    _MAX_SPEED_LIMIT = None

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @classmethod
    def __validate_model(cls, value):
        if not len(value) >= cls.__MIN_ALLOWED_MODEL_SYMBOLS:
            raise ValueError(f'Model {value} is less than 4 symbols!')

    # TODO: do the validation for the speed_limit - needs to have min and max values! -> DONE!

    @classmethod
    def __validate_speed_limit(cls, value):
        if cls._MIN_SPEED_LIMIT and value < cls._MIN_SPEED_LIMIT:
            raise ValueError(cls._INVALID_SPEED_LIMIT_MESSAGE)
        if cls._MAX_SPEED_LIMIT and value > cls._MAX_SPEED_LIMIT:
            raise ValueError(cls._INVALID_SPEED_LIMIT_MESSAGE)
        pass

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.__validate_speed_limit(value)
        self.__speed_limit = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__validate_model(value)
        self.__model = value
