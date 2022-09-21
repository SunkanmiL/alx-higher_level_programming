"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): The divisor
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix representing the result of the division
    """
if type(div) not in [int, float] or div != div or\
            abs(div) > 1.7976931348623158e+308:
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    if type(matrix) is list:
        new_matrix = [x[:] for x in matrix]
        for i in range(len(matrix)):
            if i <= len(matrix) - 2 and len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same" +
                                " size")
                return matrix
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in [int, float] or\
                        matrix[i][j] != matrix[i][j] or\
                        abs(matrix[i][j]) > 1.7976931348623158e+308:
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    " of integers/floats")
                    return matrix
                else:
                    new_matrix[i][j] = round(matrix[i][j] / div, 2)
    else:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
        return matrix

    return new_matrix
