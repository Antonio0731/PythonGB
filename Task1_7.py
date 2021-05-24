list1 = [[1, 3, 5], [6, 9, 5], [9, 10, 12]]
list2 = [[15, 2, 8], [7, 10, 4], [31, 17, 2]]

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        list3 = []
        for i in range(len(self.list)):
            list3.append([])
            for j in range(len(self.list[0])):
                list3[i].append(self.list[i][j]+other.list[i][j])
        return '\n'.join(map(str,list3))

matrix_1 = Matrix(list1)
matrix_2 = Matrix(list2)
print(f"Matrix_1 \n{matrix_1}\n")
print(f"Matrix_2 \n{matrix_2}\n")
print(f"Sum \n{matrix_1+matrix_2}")