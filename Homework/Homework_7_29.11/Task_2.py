from abc import ABC, abstractmethod


class Clothers(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothers):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothers):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumption(self, list_suits):
        a = 0
        for suit in list_suits:
            a += suit.consumption
        return a


coat = Coat(52)
costume = Suit(1.55)
costume_2 = Suit(1.87)
costume_3 = Suit(1.90)
costume_4 = Suit(2.03)
list_costumes = [costume, costume_2, costume_3, costume_4]
print(coat.consumption)
print(costume.consumption)
print(costume.sum_consumption(list_costumes))
