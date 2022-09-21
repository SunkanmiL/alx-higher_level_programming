#!/usr/bin/python3
"""This script defines a function that multiplies 2 matrices by using Numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix
    Args:
        m_a (list): First matrix
        m_b (list): second matrix
    Returns:
        The result of multiply m_a by m_b
    """
    return (np.matmul(m_a, m_b)
