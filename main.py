# Code adapted from https://scipy-cookbook.readthedocs.io/items/LoktaVolterraTutorial.html
import numpy as np
from scipy import integrate

# Definition of parameters
a = 1.        # natural growth rate of rabits (prey)
b = 0.1       # natural dying rate of rabbits
c = 1.5       # natural dyring rate of foxes
d = 0.75      # factor describing growth of foxes based on caught rabbits

def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return np.array([ a*X[0] -   b*X[0]*X[1] ,
                  -c*X[1] + d*b*X[0]*X[1] ])

t = np.linspace(0, 15,  1000)              # time
X0 = np.array([10, 5])                     # initials conditions: 10 rabbits and 5 foxes
X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)

print(X)
