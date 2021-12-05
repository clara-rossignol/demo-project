import numpy as np


class LVM:
    """ Simple LotkaVolterraClass with Euler Integration """

    def __init__(self, a=1.0, b=0.1, c=1.5, d=0.75, dt=0.1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.dt = dt

    def update(self, X):
        """ Forward Euler method update """
        return X + self.dt * np.array(
            [
                self.a * X[0] - self.b * X[0] * X[1],
                -self.c * X[1] + self.d * self.b * X[0] * X[1],
            ]
        )

    def dynamics(self, X0, num_iter, saver):
        X = X0  # initalize
        saver.store_iter(X, 0)
        for i in range(num_iter):
            X = self.update(X)
            saver.store_iter(X, self.dt * i)


class DataSaver:
    def __init__(self, instance=None):
        # self.a = LVM.a
        self.data = {"state_X": [], "state_T": []}
        if instance is not None:  # to store parameters with the result
            self.a = instance.a
            self.b = instance.b
            self.c = instance.c
            self.d = instance.d
            self.dt = instance.dt

    def reset(self):
        self.data = {"state_X": [], "state_T": []}

    def store_iter(self, X=None, T=None):
        if X is not None:
            self.data["state_X"].append(X.copy())
        if T is not None:
            self.data["state_T"].append(T)

    def get_data(self):
        return self.data

    def LyapunovFunction():
        # TODO: https://www.sciencedirect.com/science/article/pii/S1474667017354101
        raise NotImplementedError()


# Definition of parameters
a = 1.0  # natural growth rate of rabbits (prey)
b = 0.1  # natural dying rate of rabbits
c = 1.5  # natural dying rate of foxes
d = 0.75  # factor describing growth of foxes based on caught rabbits

numiter = 10000
dt = 15 * 1.0 / numiter

lvm = LVM(a, b, c, d, dt)
saver = DataSaver(lvm)

X0 = np.array([10, 5])  # initial conditions: 10 rabbits and 5 foxes
lvm.dynamics(X0, numiter, saver)

# You could also index saver.data['state_T']
T, Xeuler = saver.get_data()["state_T"], np.array(saver.get_data()["state_X"])
rabbits, foxes = Xeuler.T

# from Visualization import evolution
# evolution(tt, XX)

### Alternative method for solving the system
from scipy import integrate
from LotkaVolterraModel import dX_dt

t = np.linspace(0, 15, 1000)  # time
X0 = np.array([10, 5])  # initial conditions: 10 rabbits and 5 foxes
X, infodict = integrate.odeint(
    lambda x, _: dX_dt(x, a, b, c, d), X0, t, full_output=True
)
r, f = X.T

# Comparing the two methods (overlaid)

import matplotlib.pyplot as plt

fig1 = plt.figure()
plt.plot(T, rabbits, "r-", label="Rabbits")
plt.plot(T, foxes, "b-", label="Foxes")

plt.plot(t, r, "r--", label="Rabbits")
plt.plot(t, f, "b--", label="Foxes")

plt.grid()
plt.legend(loc="best")
plt.xlabel("time")
plt.ylabel("population")
plt.title("Evolution of fox and rabbit populations")

fig1.savefig("rabbits_and_foxes" + str(numiter) + ".png")


plt.show()
