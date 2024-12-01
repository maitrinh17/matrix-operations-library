import numpy as np

def add_matrices(a, b):
    """
    Add two matrices element-wise.
    Args:
        a (list of list of int/float): First matrix.
        b (list of list of int/float): Second matrix.
    Returns:
        numpy.ndarray: The sum of the matrices.
    """
    try:
        return np.add(a, b)
    except ValueError:
        raise ValueError("Matrices must have the same dimensions for addition.")

def multiply_matrices(a, b):
    """
    Multiply two matrices.
    Args:
        a (list of list of int/float): First matrix.
        b (list of list of int/float): Second matrix.
    Returns:
        numpy.ndarray: The product of the matrices.
    """
    try:
        return np.dot(a, b)
    except ValueError:
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second.")

def transpose_matrix(a):
    """
    Transpose a matrix.
    Args:
        a (list of list of int/float): Matrix.
    Returns:
        numpy.ndarray: Transposed matrix.
    """
    return np.transpose(a)

def calculate_determinant(a):
    """
    Calculate the determinant of a square matrix.
    Args:
        a (list of list of int/float): Square matrix.
    Returns:
        float: Determinant of the matrix.
    """
    return round(np.linalg.det(np.array(a)), 2)

def eigenvalues_and_eigenvectors(a):
    """
    Calculate the eigenvalues and eigenvectors of a square matrix.
    Args:
        a (list of list of int/float): Square matrix.
    Returns:
        tuple: Eigenvalues and eigenvectors.
    """
    return np.linalg.eig(np.array(a))
