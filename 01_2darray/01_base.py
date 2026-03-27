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


def main():
    m1 = Matrix([[1, 0, 2], [-1, 3, 1]])
    print(transpose(m1))
    print()

    matrix_to_sum = Matrix((2, 3), 1)
    print(m1 + matrix_to_sum)
    print()

    matrix_to_mul = Matrix([[3, 1], [2, 1], [1, 0]])
    print(m1 * matrix_to_mul)
    print()


main()
