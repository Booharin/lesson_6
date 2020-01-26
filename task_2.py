class Road:
    def __init__(self, length, width, depth):
        self._length = length
        self._width = width
        self._depth = depth

    def get_mass(self):
        print(f"mass = {self._length * self._width * 25 * self._depth}")


road = Road(1000, 30, 5)
road.get_mass()