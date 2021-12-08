from LotkaVolterraClass import LVM, DataSaver

from LotkaVolterraModel import dX_dt

from scipy import integrate
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist 
import numpy as np

# Definition of parameters
a = 1.0  # natural growth rate of rabbits (prey)
b = 0.1  # natural dying rate of rabbits
c = 1.5  # natural dying rate of foxes
d = 0.75  # factor describing growth of foxes based on caught rabbits

numiter = 10000
dt = 1.0 / numiter

def test_sameresult():
    lvm = LVM(a, b, c, d, dt)
    saver = DataSaver(lvm)


    X0 = np.array([10, 5])  # initial conditions: 10 rabbits and 5 foxes
    lvm.dynamics(X0, numiter, saver)
    T, Xeuler = saver.get_data()["state_T"], np.array(saver.get_data()["state_X"])
    rabbits, foxes = Xeuler.T
    
    X, infodict = integrate.odeint(
        lambda x, _: dX_dt(x, a, b, c, d), X0,T, full_output=True
    )

    assert np.allclose(Xeuler , X,atol=1e-3)

    