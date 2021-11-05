import numpy as np


def dx_dt(X, a, b, c, d):
    """
    Functions to compute the growth rate of fox and rabbit populations.
    Parameters
    ----------
    X : array or tuple (prey_count, predator_count)
    a : natural growth rate of the prey
    b : natural dying rate of the prey
    c : natural growth rate of the predator
    d : natural dying rate of the predator

    Returns
    -------
    numpy array [prey_count, predator_count]
    """
    return np.array([a * X[0] - b * X[0] * X[1], -c * X[1] + d * b * X[0] * X[1]])
