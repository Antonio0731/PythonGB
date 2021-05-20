class Stationary:
    def __init__(self, title = "Прибор для рисования"):
        self.title = title
    def draw(self):
        print(f"Запуск зарисовки {self.title}")

class Pen(Stationary):
    def draw(self):
        print(f"Запуск зарисовки, используя {self.title} ручку")

class Pencil(Stationary):
    def draw(self):
        print(f"Запуск зарисовки, используя {self.title} карандаш")

class Handle(Stationary):
    def draw(self):
        print(f"Запуск зарисовки, используя {self.title} маркер")


a = Stationary()
a.draw()

pen = Pen("Erich Krause")
pen.draw()

pencil = Pencil("Faber-Castell")
pencil.draw()

handle = Handle("Copic")
handle.draw()