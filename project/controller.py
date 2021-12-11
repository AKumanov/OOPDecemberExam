from project.factory import Factory


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __get_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def __get_free_car_by_type(self, car_type: str):
        car = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        if car:
            return car[-1]
        return None

    def __get_race_by_name(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def __is_car_model_in_cars_data(self, car_model):
        return car_model in [c.model for c in self.cars]

    def __is_driver_in_drivers_data(self, driver_name):
        return driver_name in [d.name for d in self.drivers]

    def __is_race_in_races_data(self, race_name: str):
        return race_name in [r.name for r in self.races]

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = Factory().create_car_by_type(car_type, model, speed_limit)
        if car:
            if self.__is_car_model_in_cars_data(model):
                raise Exception(f'Car {model} is already created!')
            self.cars.append(car)
            return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        if self.__is_driver_in_drivers_data(driver_name):
            raise Exception(f'Driver {driver_name} is already created!')
        driver = Factory().create_driver_by_name(driver_name)
        self.drivers.append(driver)
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        if self.__is_race_in_races_data(race_name):
            raise Exception(f'Race {race_name} is already created!')
        race = Factory().create_race_by_name(race_name)
        self.races.append(race)
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__get_driver_by_name(driver_name)
        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        found_car = self.__get_free_car_by_type(car_type)
        if not found_car:
            raise Exception(f'Car {car_type} could not be found!')

        if driver.car:
            old_car = driver.car
            driver.car = found_car
            found_car.is_taken = True
            old_car.is_taken = False
            return f'Driver {driver_name} changed his car from {old_car.model} to {found_car.model}.'
        else:
            found_car.is_taken = True
            driver.car = found_car
            return f'Driver {driver_name} chose the car {found_car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__get_race_by_name(race_name)
        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        driver = self.__get_driver_by_name(driver_name)
        if not driver:
            raise ValueError(f'Driver {driver_name} could not be found!')

        if not driver.car:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'

        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):
        race = self.__get_race_by_name(race_name)
        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if len(race.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        winners = sorted([d for d in race.drivers], key=lambda d: -d.car.speed_limit)[0:3]
        output = ''
        for winner in winners:
            winner.number_of_wins += 1
            output += f'Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n'

        return output.strip()


