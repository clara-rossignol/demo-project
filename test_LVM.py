import doctest
import LotkaVolterraModel
import numpy as np

def test_LotkaVolterraModel():
    ''' integrating the doctests in the pytest framework '''
    assert doctest.testmod(LotkaVolterraModel, raise_on_error=True)

def test_dX_dt():
    ''' a first example '''
    assert (LotkaVolterraModel.dX_dt(np.ones(2),1,0.1,1.5,.75) -  np.array([ 0.9  , -1.425])).all
    
def test_