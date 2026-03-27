# skończone


class Matrix:
    def __init__(self, matrix, values=0):

        if isinstance(matrix, tuple):  # (rows, cols)
            self.__matrix = [
                [values for i in range(matrix[1])] for j in range(matrix[0])
            ]

            self.__size = matrix
        else:
            self.__matrix = matrix
            self.__size = (len(matrix), len(matrix[0]))

    def __add__(self, other):
        if isinstance(other, Matrix) and (self.__size == other.size()):
            res_matrix = Matrix(self.__size)
            for row in range(self.__size[0]):
                for col in range(self.__size[1]):
                    res_matrix[row][col] = (
                        self.__matrix[row][col] + other.__matrix[row][col]
                    )
            return res_matrix
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Matrix) and (self.__size[1] == other.size()[0]):

            rows_a = self.__size[0]
            cols_a = self.__size[1]
            cols_b = other.size()[1]
            res_matrix = Matrix((rows_a, cols_b))

            for row in range(rows_a):
                for col in range(cols_b):
                    res_matrix[row][col] = sum(
                        self.__matrix[row][k] * other.get_matrix()[k][col]
                        for k in range(cols_a)
                    )
            return res_matrix
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Matrix) and (self.__size == other.size()):
            return True if (self.__matrix == other.get_matrix()) else False
        return NotImplemented

    def __getitem__(self, index):
        return self.__matrix[index]

    def __str__(self):

        row_str = [f"| {row} |" for row in self.__matrix]
        return "\n".join(row_str)

    def __setitem__(self, index, value):  # potrzebne do zmiany kolejności wierszy
        self.__matrix[index] = value

    def size(self):
        return self.__size

    def get_matrix(self):
        return self.__matrix


def transpose(matrix):
    if isinstance(matrix, Matrix):
        rows_a = matrix.size()[0]
        cols_a = matrix.size()[1]
        res_matrix = Matrix((cols_a, rows_a))
        for row in range(rows_a):
            for col in range(cols_a):
                res_matrix[col][row] = matrix[row][col]

        return res_matrix


def chio(orig_matrix):
    matrix = orig_matrix  # referencja bezpieczna, bo jeśli a11_el!=0 to jedynie odczytuję matrix, nie zmieniam
    if isinstance(matrix, Matrix) and (matrix.size()[0] == matrix.size()[1]):
        n = matrix.size()[0]
        a11_el = matrix[0][0]  # zakładam, że pierwszy element nie będzie zerem
        sign = 1
        if a11_el == 0:
            matrix = Matrix(
                orig_matrix.get_matrix().copy()
            )  # do bezpiecznej zmiany kolejności wierszy, płytka kopia wystarczy, bo nie będę zmieniał elementów w wierszach
            idx = 1

            while idx < n:
                if matrix[idx][0] != 0:
                    matrix[0], matrix[idx] = matrix[idx], matrix[0]
                    sign = -1
                    a11_el = matrix[0][0]
                    break
                idx += 1
            if a11_el == 0:
                return 0  # jeśli cała kolumna wynosi zero to det = 0

        if n <= 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return det
        else:
            b_matrix = Matrix((n - 1, n - 1), 0)
            for row in range(n - 1):
                for col in range(n - 1):
                    b_matrix[row][col] = (
                        a11_el * matrix[row + 1][col + 1]
                        - matrix[row + 1][0] * matrix[0][col + 1]
                    )  # elementy macierzy b to wartości wyznaczników mniejszych macierzy 2x2
            return sign * (1 / (a11_el ** (n - 2))) * chio(b_matrix)


def main():
    m1 = Matrix([[1, 2, 3], [-1, 1, 0], [1, 5, 1]])
    print(chio(m1))

    m2 = Matrix(
        [
            [5, 1, 1, 2, 3],
            [4, 2, 1, 7, 3],
            [2, 1, 2, 4, 7],
            [9, 1, 0, 7, 0],
            [1, 4, 7, 2, 2],
        ]
    )
    print(chio(m2))

    m3 = Matrix(
        [
            [0, 1, 1, 2, 3],
            [4, 2, 1, 7, 3],
            [2, 1, 2, 4, 7],
            [9, 1, 0, 7, 0],
            [1, 4, 7, 2, 2],
        ]
    )
    print(chio(m3))

    m4 = Matrix(
        [
            [0, 1, 1, 2, 3],
            [0, 2, 1, 7, 3],
            [0, 1, 2, 4, 7],
            [0, 1, 0, 7, 0],
            [0, 4, 7, 2, 2],
        ]
    )
    print(chio(m4))

    m5 = Matrix(
        [
            [0, 0, 0, 0, 0],
            [4, 2, 1, 7, 3],
            [2, 1, 2, 4, 7],
            [9, 1, 0, 7, 0],
            [1, 4, 7, 2, 2],
        ]
    )
    print(chio(m5))


main()
