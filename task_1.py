from termcolor import cprint
from time import sleep


class TrafficLight:
    def __init__(self):
        self._color = "green"
        self._count = 0

    def traffic_go(self):
        if self._count == 0 and self._color == "green":
            print()
            cprint('   ', 'green', 'on_red')
            self._color = "red"
        elif self._count % 7 == 0 and self._color == "red":
            cprint('   ', 'green', 'on_yellow')
            self._color = "yellow"
        elif self._count % 9 == 0 and self._color == "yellow":
            cprint('   ', 'green', 'on_green')
            self._color = "green"
        self._count += 1

        if self._count == 13:
            self._count = 0

    def running(self):
        while True:
            sleep(1)
            self.traffic_go()


traffic = TrafficLight()
traffic.running()
