import os
import sys
import math
from numpy.testing import assert_almost_equal

from pycrysfml08 import py_cfml_profiles

# Tests

def test_exponential():
    a = 1.0
    x = 1.5
    desired = a * math.exp(-a * x)
    code, message, actual = py_cfml_profiles.exponential(x, a)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=3, verbose=True)
