# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)


def is_identity_matrix(matrix):
    for i in range(0, len(matrix)):
       for j in range(0, len(matrix)):
           if i == j and matrix[i][j] != 1:
                return False
           elif i != j and matrix[i][j] != 0:
                return False
    return True
