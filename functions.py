import numpy as np


def dx_dt(X, a, b, c, d):
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
    """
    return np.array([a * X[0] - b * X[0] * X[1], -c * X[1] + d * b * X[0] * X[1]])
