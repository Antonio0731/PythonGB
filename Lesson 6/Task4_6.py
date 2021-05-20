class Car:
    def __init__(self, name, color, speed, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Машина: {self.name}, Цвет: {self.color}, Полицейская? {self.is_police}")
    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {'направо' if direction == 1 else 'налево'}")

    def show_speed(self):
        return f"Машина {self.name} едет со скоростью {self.speed} км/ч"

class TownCar(Car):
    def show_speed(self):
        return f"Машина {self.name} едет со скоростью {self.speed} км/ч, немедленно снизить скорость!"\
            if self.speed > 60 else f"Машина {self.name} едет со скоростью {self.speed} км/ч"

class WorkCar(Car):
    def show_speed(self):
        return f"Машина {self.name} едет со скоростью {self.speed} км/ч, немедленно снизить скорость!"\
            if self.speed > 40 else f"Машина {self.name} едет со скоростью {self.speed} км/ч"

class SportCar(Car):
    def show_speed(self):
        return f"Машина {self.name} едет со скоростью {self.speed} км/ч, немедленно набрать скорость!"\
            if self.speed < 50 else f"Машина {self.name} едет со скоростью {self.speed} км/ч"

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar('Chevrolet', 'желтый', 80)
town_car.go()
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()
print()

work_car = WorkCar('Nissan', 'красный', 50)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.stop()
print()

sport_car = SportCar('Ferrari', 'красный', 40)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

police_car = PoliceCar('Ford','белый', 100)
police_car.go()
police_car.turn(0)
print(police_car.show_speed())
police_car.stop()
print()
