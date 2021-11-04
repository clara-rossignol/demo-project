import numpy as np


def dX_dt(X, a, b, c, d):
    """ Return the growth rate of fox and rabbit populations. """
    return np.array([a * X[0] - b * X[0] * X[1], -c * X[1] + d * b * X[0] * X[1]])

def d2X_dt2(X, a=1.0, b=.1, c=1.5, d=.75):
    """
    Compute the Jacobian matrix evaluated in X.

    Parameters
    ----------

    X : array
        Vector state of populations (rabbits, foxes)

    TODO: Parameters a,b,c,d

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


def population_equilibrium(a=1.0, b=.1, c=1.5, d=.75):
    """
    Returns equilibrium points of dX_dt, i.e. where groth rate is equal to zero.

    TODO: Parameters a,b,c,d
    """

    return np.zeros(2),np.array([c/(d*b),a/b])


def check_equilibrium(a=1.0, b=.1, c=1.5, d=.75):
    '''
    Checks if population_equilibrium returns fixpoints of dX_dt.

    TODO: Parameters a,b,c,d
    '''

    equilibria = population_equilibrium(a=a,b=b,c=c,d=d)
    for eq in equilibrium:
        if np.all(dX_df(eq,a=a,b=b,c=c,d=d)):
            print(eq, " is a fix point!")
        else:
            print(eq, " is not a fix point!")
