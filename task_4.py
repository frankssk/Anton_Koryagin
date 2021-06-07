class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('Машина поехала')

    @staticmethod
    def stop():
        print('Машина остановилась')

    @staticmethod
    def turn_to_the(direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости.')


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    town_car = TownCar(90, 'red', 'lada', False)
    town_car.go()
    town_car.show_speed()
    town_car.turn_to_the('право')
    print('\n')
    police_car = PoliceCar(90, 'bleak', 'bugatti', True)
    police_car.go()
    police_car.show_speed()
    police_car.turn_to_the('право')
    print('\n')
    sport_car = SportCar(90, 'blue', 'jiguli', False)
    sport_car.go()
    sport_car.show_speed()
    sport_car.turn_to_the('право')
    print('\n')
    work_car = WorkCar(90, 'green', 'mazda', False)
    work_car.go()
    work_car.show_speed()
    work_car.turn_to_the('право')
