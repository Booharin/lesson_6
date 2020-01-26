class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self._name = name
        self._surname = surname
        self.position = position
        self._salary = salary
        self._bonus = bonus

    @property
    def _income(self):
        return {
            "salary": self._salary,
            "bonus": self._bonus
        }


class Position(Worker):
    def get_full_name(self):
        try:
            print(f"{self._name} {self._surname}")
        except ValueError:
            print("Value error")

    def get_total_income(self):
        try:
            total = self._income["salary"] + self._income["bonus"]
            print(f"{total}")
        except ValueError:
            print("Value error")


position = Position("Rafael", "Ninja-turtle", "CEO", 10000, 5000)
position.get_full_name()
position.get_total_income()
