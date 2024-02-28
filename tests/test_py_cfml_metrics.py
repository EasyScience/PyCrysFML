import os
import sys
import copy
import math
from deepdiff import DeepDiff
import numpy as np
from numpy.testing import assert_almost_equal

from pycrysfml08 import py_cfml_metrics

DI_CELL = {'fortran_type': 'cell_g_type',
           'cell': np.array([10., 10., 10.], dtype='f'),
           'scell': np.array([0., 0., 0.], dtype='f'),
           'ang': np.array([90., 90., 90.], dtype='f'),
           'sang': np.array([0., 0., 0.], dtype='f'),
           'vol': 1000.0, 'svol': 0.0,
           'rcell': np.array([0.1, 0.1, 0.1], dtype='f'),
           'rang': np.array([90., 90., 90.], dtype='f'),
           'rvol': 0.0010000000474974513,
           'gd': np.array([[100., 0., 0.], [0., 100., 0.], [0., 0., 100.]], dtype='f'),
           'gr': np.array([[0.010000001, 0., 0.], [0., 0.010000001, 0.], [0., 0., 0.010000001]], dtype='f'),
           'cr_orth_cel': np.array([[10., 0., 0.], [-0., 10., 0.], [0., 0., 10.]], dtype='f'),
           'orth_cr_cel': np.array([[0.1, -0., 0.], [ 0. ,  0.1, -0. ], [-0. , -0. ,  0.1]], dtype='f'),
           'bl_m': np.array([[ 0.1,  0. , -0. ], [-0. ,  0.1, -0. ], [ 0. , -0. ,  0.1]], dtype='f'),
           'inv_bl_m': np.array([[10., -0.,  0.], [ 0., 10.,  0.], [ 0.,  0., 10.]], dtype='f'),
           'cartype': 'CA'}

# Tests

def test_get_u_from_b():
    nd_b = np.array([1.5, 1.6, 1.7, 1.0, 1.1, 1.2], dtype='f')
    desired = np.array([0.019, 0.0203, 0.0215, 0.0127, 0.0139, 0.0152], dtype='f')
    code, message, actual = py_cfml_metrics.get_u_from_b(nd_b)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

def test_get_betas_from_biso():
    biso = 1.0
    di_cell = copy.deepcopy(DI_CELL)
    desired = np.array([0.0025, 0.0025, 0.0025, 0.0, 0.0, 0.0], dtype='f')
    code, message, actual = py_cfml_metrics.get_betas_from_biso(biso, di_cell)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

def test_set_crystal_cell():
    nd_abc = np.array([10.0, 10.0, 10.0], dtype='f')
    nd_albega = np.array([90.0, 90.0, 90.0], dtype='f')
    desired = copy.deepcopy(DI_CELL)
    code, message, actual = py_cfml_metrics.set_crystal_cell(nd_abc, nd_albega)
    assert code == 0
    assert message == ''
    for key in desired.keys():
        if isinstance(desired[key], np.ndarray):
            assert_almost_equal(desired[key], actual[key], decimal=4, verbose=True)
        else:
            assert desired[key] == actual[key]
