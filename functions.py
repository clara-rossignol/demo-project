import numpy as np


def dX_dt(X, a, b, c, d):
    """ Return the growth rate of fox and rabbit populations. """
    return np.array([a * X[0] - b * X[0] * X[1], -c * X[1] + d * b * X[0] * X[1]])

a = 1.0  # natural growth rate of rabbits (prey)
b = 0.1  # natural dying rate of rabbits
c = 1.5  # natural dying rate of foxes
d = 0.75  # factor describing growth of foxes based on caught rabbits

def d2X_dt2(X, a=1.0, b=.1, c=1.5, d=.75):
    """
    Compute the Jacobian matrix evaluated in X.

    Parameters
    ----------

    X : array
        Vector state of populations (rabbits, foxes)

    Returns
    -------
    y : array, shape (2, 2)
        Array containing Jacobian of dX_dt


    Example
    -------
    Jacobian at [0, 0] for 0 rabbits and 0 foxes.
    >>> jacobian = d2X_dt2(np.zeros(2))

    """
    return np.array([[a -b*X[1],   -b*X[0]     ],
                    [b*d*X[1] ,   -c +b*d*X[0]] ])
