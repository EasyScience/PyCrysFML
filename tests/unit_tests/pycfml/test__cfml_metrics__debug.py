import os
import sys
import copy
import math
import json
from deepdiff import DeepDiff
import numpy as np
from numpy.testing import assert_almost_equal


# Tests

def test__get_u_from_b__directly():
    try:
        from pycrysfml08 import crysfml08lib
    except ImportError as e:
        print(e)
        return
    nd_b = np.array([1.5, 1.6, 1.7, 1.0, 1.1, 1.2], dtype='f')
    desired = np.array([0.019, 0.0203, 0.0215, 0.0127, 0.0139, 0.0152], dtype='f')
    code, message, actual = crysfml08lib.f_get_u_from_b(nd_b)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

def test__get_u_from_b__pyapi():
    try:
        from pycrysfml08 import cfml_metrics
    except ImportError as e:
        print(e)
        return
    nd_b = np.array([1.5, 1.6, 1.7, 1.0, 1.1, 1.2], dtype='f')
    desired = np.array([0.019, 0.0203, 0.0215, 0.0127, 0.0139, 0.0152], dtype='f')
    code, message, actual = cfml_metrics.get_u_from_b(nd_b)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

# Debug

if __name__ == '__main__':
    pass
