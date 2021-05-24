class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.num // rows)]) + '\n' + "*" * (self.num % rows)

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        print("Sum:")
        return Cell(self.num + other.num)

    def __sub__(self, other):
        print("Вычитание:")
        return Cell(self.num - other.num) if self.num - other.num > 0 \
            else "Вычитание невозможно"

    def __mul__(self, other):
        print("Умножение:")
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        print("Целочисленное деление:")
        return Cell(self.num // other.num)

cell_1 = Cell(23)
cell_2 = Cell(18)
print(cell_1+cell_2)
print(cell_1-cell_2)
print(cell_1*cell_2)
print(cell_1//cell_2)
print(cell_1.make_order(5))

