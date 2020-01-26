class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print("Draw started")


class Pen(Stationery):
    def draw(self):
        print("Pen draw started")


class Pencil(Stationery):
    def draw(self):
        print(f"{self._title} draw started")


class Handle(Stationery):
    def draw(self):
        print("Handle draw started")


pen = Pen("A pen")
pen.draw()

pencil = Pencil("A pencil")
pencil.draw()

handle = Handle("A handle")
handle.draw()