from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Factory:
    def __init__(self):
        pass

    @staticmethod
    def create_car_by_type(car_type: str, model: str, speed_limit: int):
        if car_type == MuscleCar.__name__:
            return MuscleCar(model, speed_limit)
        if car_type == SportsCar.__name__:
            return SportsCar(model, speed_limit)
        return None

    @staticmethod
    def create_driver_by_name(driver_name: str):
        return Driver(driver_name)

    @staticmethod
    def create_race_by_name(race_name: str):
        return Race(race_name)
