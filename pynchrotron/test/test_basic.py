from pynchrotron import synchrotron_kernel
from pynchrotron.synchrotron_kernel import cheb_eval
from hypothesis import given
import hypothesis.strategies as st

import numpy as np


def test_cheb():


    data = np.array([1E-4,1E-2,1.])

    val = cheb_eval(data,2,-1,1,.1)

    np.testing.assert_almost_equal(val, -0.97895)
    

    

@given(st.floats(min_value=0) )
def test_synchrotron_kernel(val):

    synchrotron_kernel(val)
