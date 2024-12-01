import unittest
import numpy as np
from matrix_operations import (
    add_matrices,
    multiply_matrices,
    transpose_matrix,
    calculate_determinant,
    eigenvalues_and_eigenvectors,
)

class TestMatrixOperations(unittest.TestCase):

    def test_add_matrices(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = np.array([[6, 8], [10, 12]])
        np.testing.assert_array_equal(add_matrices(a, b), expected)

    def test_multiply_matrices(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(multiply_matrices(a, b), expected)

    def test_calculate_determinant(self):
        a = [[1, 2], [3, 4]]
        self.assertEqual(calculate_determinant(a), -2.0)

if __name__ == "__main__":
    unittest.main()
