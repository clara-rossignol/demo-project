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
    a=1.0
    b=0.1
    c=1.5
    d=0.75
    eq = LotkaVolterraModel.population_equilibrium(a=a, b=b, c=c, d=d)
    
    # Checking the first and second fixpoint:
    assert sum(np.abs(eq[0])) == 0  # equal to 0
    assert (eq[1] == (c / (d * b), a / b)).all()
    
def test_check_equilibrium():
    return_value = LotkaVolterraModel.check_equilibrium()
    assert return_value == None 
    
import sys 

def test_printoutput_checkeq(capsys): 
    ''' 
    Unit-test that check the print statements in LotkaVolterraModel.check_equilibrium()
    
    Notes: 
    ------
    Based on capture: https://docs.pytest.org/en/6.2.x/capture.html 
    '''
    LotkaVolterraModel.check_equilibrium()      # run check equlibrium and 
    captured = capsys.readouterr()              # capture the output
    
    first, second,_ = (captured.out).split('\n')      # separating different lines
    assert first == "[0. 0.]  is a fix point!"
    assert second == "[20. 10.]  is a fix point!"

def test_printoutput_checkeq_notfixpoint(capsys):
    
    # Overwrite dX_dt (with a different version so that equilibria are no longer fixpoints)
    def dX_dt(X, a=1.0, b=0.1, c=1.5, d=0.75):
        return np.array([a + X[0] - b * X[0] * X[1], -c * X[1] + d * b * X[0] * X[1]])

    LotkaVolterraModel.dX_dt = dX_dt
    LotkaVolterraModel.check_equilibrium()      # run check equlibrium and 
    captured = capsys.readouterr()              # capture the output
    
    first, second,_ = (captured.out).split('\n')      # separating different lines
    assert first == "[0. 0.]  is not a fix point!"
    assert second == "[20. 10.]  is not a fix point!"
    
def test_main(capsys):
    ''' Silly test that runs LVM.py as script.py '''
    import imp
    runpy = imp.load_source('__main__', 'LotkaVolterraModel.py')
    captured = capsys.readouterr()              # capture the output
    first, _ = (captured.out).split('\n')       # separating different lines
    assert first == "Starting doctests"