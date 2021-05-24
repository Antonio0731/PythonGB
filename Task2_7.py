from abc import ABC, abstractmethod

class Clothes(ABC):
    res = 0

    def __init__(self, par):
        self.par = par

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.res += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        result = Clothes.res
        Clothes.res = 0
        return f"{result}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.par / 6.5) + 0.5

class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.par + 0.3) / 100)

a = Coat(48)
b = Costume(184)
print(a+a+a+a+b+b+b+b)