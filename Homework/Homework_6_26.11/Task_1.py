from time import sleep


class TrafficLight:
    colors = ('red', 'yellow', 'green')
    duration = (7, 2, 6)

    def __init__(self):
        self.__color = 'green'

    def running(self):
        while True:
            for elem in self.colors:
                self.__color = elem
                print(self.__color)
                sleep(self.duration[self.colors.index(self.__color)])


traffic_light = TrafficLight()
traffic_light.running()
