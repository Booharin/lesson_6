from termcolor import cprint
from time import sleep


class TrafficLight:
    def __init__(self, param_1=7, param_2=2, param_3=4):
        self._color = "green"
        self._count = 0
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3

    def traffic_go(self):
        if self._count == 0 and self._color == "green":
            print()
            cprint('   ', 'green', 'on_red')
            self._color = "red"
        elif self._count % self.param_1 == 0 and self._color == "red":
            cprint('   ', 'green', 'on_yellow')
            self._color = "yellow"
        elif self._count % (self.param_1 + self.param_2) == 0 and self._color == "yellow":
            cprint('   ', 'green', 'on_green')
            self._color = "green"
        self._count += 1

        if self._count == self.param_1 + self.param_2 + self.param_3:
            self._count = 0

    def running(self):
        while True:
            sleep(1)
            self.traffic_go()


traffic = TrafficLight(7, 2, 4)
traffic.running()
