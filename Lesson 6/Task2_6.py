class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def total_mass(self, m = 25, thick = 0.005):
        main = m * thick * self._length * self._width
        return f"Масса асфальта, необходимая для покрытия дорожного полотна, равна {round(main)} тонн"

result = Road(int(input("Введите предполагаемую длину дороги в метрах: ")),int(input("Введите предполагаемую ширину дороги в метрах: ")))
print(result.total_mass())