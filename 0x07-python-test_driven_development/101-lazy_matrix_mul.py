#!/usr/bin/python3
""" numpy module """
import numpy as np


""" multiplicate matrix """


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.

    Raises:
        ValueError: If the matrices cannot be
        multiplied due to incompatible dimensions.
    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("Matrices cannot be multiplied: " + str(e))
