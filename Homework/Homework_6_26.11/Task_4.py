class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('GO!')

    def stop(self):
        print('STOP!')

    def turn(self, direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Speed limit exceeded!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Speed limit exceeded!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town = TownCar(70, 'white', 'Town')
sport = SportCar(130, 'red', 'Sport')
work = WorkCar(55, 'yellow', 'Work')
police = PoliceCar(100, 'blue', 'Police')

town.show_speed()
work.show_speed()

work.speed = 39
work.show_speed()

sport.turn('Right')