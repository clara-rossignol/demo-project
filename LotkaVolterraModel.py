"""
Module containing simulation code of the Lotka Volterra model.

Adapted from:
https://github.com/scipy/scipy-cookbook/blob/master/ipython/LotkaVolterraTutorial.ipynb

"""

import numpy as np


def dX_dt(X, a=1.0, b=0.1, c=1.5, d=0.75):
    """
    Computes the growth rate of fox and rabbit populations based on system state (X) and parameters (a,b,c,d)

    Parameters
    ----------
    X : array or tuple
        [prey_count, predator_count]
    a : float, optional
        natural growth rate of the prey (rabbit)
    b : float, optional
        natural dying rate of the prey
    c : float, optional
        natural growth rate of the predator (fox)
    d : float, optional
        natural dying rate of the predator

    Returns
    -------
    numpy array
        [change of prey_count, change of predator_count]
        
    Examples
    -------
    >>> dX_dt(np.ones(2),1,0.1,1.5,.75)
    array([ 0.9  , -1.425])
    >>> dX_dt(np.zeros(2),1,0.1,1.5,.75)        # zero is a fixpoint
    array([0., 0.])
    """
    if np.size(X) > 2:
        raise ValueError("X has only two dimensions!")

    return np.array([a * X[0] - b * X[0] * X[1], -c * X[1] + d * b * X[0] * X[1]])


def d2X_dt2(X, a=1.0, b=0.1, c=1.5, d=0.75):
    """
    Compute the Jacobian matrix evaluated at X.

    Parameters
    ----------

    X : array
        Vector state of populations (rabbits, foxes)
    a : float, optional
        natural growth rate of the prey (rabbit)
    b : float, optional
        natural dying rate of the prey
    c : float, optional
        natural growth rate of the predator (fox)
    d : float, optional
        natural dying rate of the predator

    Returns
    -------
    numpy array, shape (2, 2)
        Array containing Jacobian of dX_dt


    Example
    -------
    Jacobian at [0, 0] for 0 rabbits and 0 foxes for default parameters
    >>> d2X_dt2(np.zeros(2))
    array([[ 1. , -0. ],
           [ 0. , -1.5]])
    >>> d2X_dt2(np.zeros(2),a=2,b=.3,c=1.2,d=0.4)
    array([[ 2. , -0. ],
           [ 0. , -1.2]])
    """
    return np.array([[a - b * X[1], -b * X[0]], [b * d * X[1], -c + b * d * X[0]]])


def population_equilibrium(a=1.0, b=0.1, c=1.5, d=0.75):
    """
    Returns equilibrium points of dX_dt, i.e. where growth rate is equal to zero.

    Parameters
    ----------

    a : float, optional
        natural growth rate of the prey (rabbit)
    b : float, optional
        natural dying rate of the prey
    c : float, optional
        natural growth rate of the predator (fox)
    d : float, optional
        natural dying rate of the predator

    Returns
    -------
    list
        List of points with dX_dt = 0.

    Examples
    -------
    >>> population_equilibrium()
    (array([0., 0.]), array([20., 10.]))
    >>> population_equilibrium(1,0.1,1.5,.2)   
    (array([0., 0.]), array([75., 10.]))
    """
    return np.zeros(2), np.array([c / (d * b), a / b])


def check_equilibrium(a=1.0, b=0.1, c=1.5, d=0.75):
    """
    Checks if population_equilibrium returns fixpoints of dX_dt.

    Parameters
    ----------

    a : float, optional
        natural growth rate of the prey (rabbit)
    b : float, optional
        natural dying rate of the prey
    c : float, optional
        natural growth rate of the predator (fox)
    d : float, optional
        natural dying rate of the predator

    """

    equilibria = population_equilibrium(a=a, b=b, c=c, d=d)
    for eq in equilibria:
        if np.all(dX_dt(eq, a=a, b=b, c=c, d=d) == np.zeros(2)):
            print(eq, " is a fix point!")
        else:
            print(eq, " is not a fix point!")


if __name__ == "__main__":
    import doctest

    print("Starting doctests")  # not required!
    doctest.testmod()
