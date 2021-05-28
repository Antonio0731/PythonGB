class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

number_1 = input("Введите делитель: ")
number_2 = input("Введите делимое: ")

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
    if number_2 == 0:
        raise OwnError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {number_1 / number_2}")