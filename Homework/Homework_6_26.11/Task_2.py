class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_wight(self, weight, thikness):
        return self._length * self._width * weight * thikness / 1000


res = Road(4000, 15)
print(f"Вам понадобится {res.get_wight(20, 6)} т асфальта")