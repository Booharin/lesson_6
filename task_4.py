class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def turn(self, direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f"Speed: {self._speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Speed: {self._speed}")
        try:
            if self._speed > 60:
                print("You go really fast!")
        except ValueError:
            print("Value error")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Speed: {self._speed}")
        try:
            if self._speed > 40:
                print("You go really fast!")
        except ValueError:
            print("Value error")


class PoliceCar(Car):
    pass


town_car = TownCar(60, "blue", "Mercedes", False)
town_car.go()
town_car.show_speed()

sport_car = SportCar(100, "red", "Lamborghini", False)
sport_car.go()
sport_car.turn("left")

work_car = WorkCar(50, "yellow", "Ford", False)
work_car.go()
work_car.show_speed()
work_car.stop()

police = PoliceCar(70, "white", "Gaz", True)
police.go()
police.show_speed()
police.turn("right")
police.stop()
