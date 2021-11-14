import doctest
import LotkaVolterraModel
import numpy as np


def test_LotkaVolterraModel():
    """ integrating the doctests in the pytest framework """
    assert doctest.testmod(LotkaVolterraModel, raise_on_error=True)


def test_dX_dt():
    """ a first example """
    assert (
        LotkaVolterraModel.dX_dt(np.ones(2), 1, 0.1, 1.5, 0.75)
        - np.array([0.9, -1.425])
    ).all


def test_growth():
    state = np.array([13.0, 12.0])
    growth = LotkaVolterraModel.dX_dt(state, a=1.0, b=0.3, c=1.5, d=0.1)
    assert (growth == np.array([-33.8, -13.32])).all()


def test_jacobian():
    jac = LotkaVolterraModel.d2X_dt2(np.zeros(2), a=2, b=0.3, c=1.2, d=0.4)
    target_jac = np.array([[2.0, -0.0], [0.0, -1.2]])
    assert (jac == target_jac).all()

def test_equilibria():
    eq = LotkaVolterraModel.population_equilibrium(a=1.0, b=0.1, c=1.5, d=0.75)
    assert sum(eq[0])==0 # equal to 0