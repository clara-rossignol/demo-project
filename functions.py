import numpy as np


def dX_dt(X, a, b, c, d):
    """ Return the growth rate of fox and rabbit populations. """
    return np.array([a * X[0] - b * X[0] * X[1], -c * X[1] + d * b * X[0] * X[1]])
