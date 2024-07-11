import os
import sys
import copy
import math
import json
from deepdiff import DeepDiff
import numpy as np
from numpy.testing import assert_almost_equal

from pycrysfml08 import crysfml08lib

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

def test__get_u_from_b():
    nd_b = np.array([1.5, 1.6, 1.7, 1.0, 1.1, 1.2], dtype='f')
    desired = np.array([0.019, 0.0203, 0.0215, 0.0127, 0.0139, 0.0152], dtype='f')
    code, message, actual = crysfml08lib.f_get_u_from_b(nd_b)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

def test__get_betas_from_biso():
    biso = 1.0
    di_cell = copy.deepcopy(DI_CELL)
    desired = np.array([0.0025, 0.0025, 0.0025, 0.0, 0.0, 0.0], dtype='f')
    code, message, actual = crysfml08lib.f_get_betas_from_biso(biso, di_cell)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

def test__get_betas_from_u():
    u = np.array([0.0127, 0.0127, 0.0127, 0.0, 0.0, 0.0], dtype='f')
    di_cell = copy.deepcopy(DI_CELL)
    desired = np.array([0.0025, 0.0025, 0.0025, 0.0, 0.0, 0.0], dtype='f')
    code, message, actual = crysfml08lib.f_get_betas_from_u(u, di_cell)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

def test__get_u_from_betas():
    betas = np.array([0.0025, 0.0025, 0.0025, 0.0, 0.0, 0.0], dtype='f')
    di_cell = copy.deepcopy(DI_CELL)
    desired = np.array([0.0127, 0.0127, 0.0127, 0.0, 0.0, 0.0], dtype='f')
    code, message, actual = crysfml08lib.f_get_u_from_betas(betas, di_cell)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)

def test__set_crystal_cell():
    nd_abc = np.array([10.0, 10.0, 10.0], dtype='f')
    nd_albega = np.array([90.0, 90.0, 90.0], dtype='f')
    desired = copy.deepcopy(DI_CELL)
    code, message, actual = crysfml08lib.f_set_crystal_cell(nd_abc, nd_albega)
    assert code == 0
    assert message == ''
    for key in desired.keys():
        if isinstance(desired[key], np.ndarray):
            assert_almost_equal(desired[key], actual[key], decimal=4, verbose=True)
        else:
            assert desired[key] == actual[key]

def test__get_twofold_axes():
    desired = {
        'fortran_type': 'twofold_axes_type',
        'ntwo': 9,
        'tol': 1.0,
        'caxes': np.array([[0., 0., 10., 0., 10., 0., 10., 10., 10., 0., 0., 0.],
                           [10., 0., 0., 10., 10., 10., 0., 0., -10., 0., 0., 0.],
                           [0., 10., 0., -10., 0., 10., 10., -10., 0., 0., 0., 0.]],
                           dtype=np.float32),
        'dtwofold': np.array([[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                              [1, 0, 0, 1, 1, 1, 0, 0, -1, 0, 0, 0],
                              [0, 1, 0, -1, 0, 1, 1, -1, 0, 0, 0, 0]],
                              dtype=np.int32),
        'rtwofold': np.array([[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                              [1, 0, 0, 1, 1, 1, 0, 0, -1, 0, 0, 0],
                              [0, 1, 0, -1, 0, 1, 1, -1, 0, 0, 0, 0]],
                              dtype=np.int32),
        'dot': np.array([1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0], dtype=np.int32),
        'cross': np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                           dtype=np.float32),
        'maxes': np.array([10., 10., 10.,
                           14.142136, 14.142136, 14.142136,
                           14.142136, 14.142136, 14.142136,
                           0., 0., 0.],
                           dtype=np.float32),
        'a': np.array([10., -0., 0.], dtype=np.float32),
        'b': np.array([0., 10., 0.], dtype=np.float32),
        'c': np.array([0., 0., 10.], dtype=np.float32)}
    code, message, actual = crysfml08lib.f_get_twofold_axes(DI_CELL, 1.0)
    assert code == 0
    assert message == ''
    for key in desired.keys():
        if isinstance(desired[key], np.ndarray):
            assert_almost_equal(desired[key], actual[key], decimal=4, verbose=True)
        else:
            assert desired[key] == actual[key]

def _test__get_conventional_cell():
    di_cell = copy.deepcopy(DI_CELL)
    desired = {
        'fortran_type': 'twofold_axes_type',
        'ntwo': 9,
        'tol': 10.0,
        'caxes': np.array([[0., 0., 10., 0., 10., 0., 10., 10., 10., 0., 0., 0.],
                           [10., 0., 0., 10., 10., 10., 0., 0., -10., 0., 0., 0.],
                           [0., 10., 0., -10., 0., 10., 10., -10., 0., 0., 0., 0.]],
                          dtype=np.float32),
        'dtwofold': np.array([[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                              [1, 0, 0, 1, 1, 1, 0, 0, -1, 0, 0, 0],
                              [0,  1, 0, -1, 0, 1, 1, -1, 0, 0, 0, 0]],
                             dtype=np.int32),
        'rtwofold': np.array([[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                              [1, 0, 0, 1, 1, 1, 0, 0, -1, 0, 0, 0],
                              [0, 1, 0, -1, 0, 1, 1, -1, 0, 0, 0, 0]],
                             dtype=np.int32),
        'dot': np.array([1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0], dtype=np.int32),
        'cross': np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=np.float32),
        'maxes': np.array([10., 10., 10.,
                           14.142136, 14.142136, 14.142136,
                           14.142136, 14.142136, 14.142136,
                           0., 0., 0.],
                          dtype=np.float32),
        'a': np.array([10., -0., 0.], dtype=np.float32),
        'b': np.array([0., 10., 0.], dtype=np.float32),
        'c': np.array([0., 0., 10.], dtype=np.float32)}

    code, message, actual = crysfml08lib.f_get_twofold_axes(di_cell, 10.0)
    assert code == 0
    assert message == ''
    assert DeepDiff(desired, actual) == {}

# Debug

if __name__ == '__main__':
    desired = {'fortran_type': 'twofold_axes_type',
               'ntwo': 9,
               'tol': 1.0,
               'caxes': np.array([[0., 0., 10., 0., 10., 0., 10., 10., 10., 0., 0., 0.],
                                  [10., 0., 0., 10., 10., 10., 0., 0., -10., 0., 0., 0.],
                                  [0., 10., 0., -10., 0., 10., 10., -10., 0., 0., 0., 0.]],
                                 dtype=np.float32),
               'dtwofold': np.array([[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                                     [1, 0, 0, 1, 1, 1, 0, 0, -1, 0, 0, 0],
                                     [0, 1, 0, -1, 0, 1, 1, -1, 0, 0, 0, 0]],
                                    dtype=np.int32),
               'rtwofold': np.array([[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                                     [1, 0, 0, 1, 1, 1, 0, 0, -1, 0, 0, 0],
                                     [0, 1, 0, -1, 0, 1, 1, -1, 0, 0, 0, 0]],
                                    dtype=np.int32),
               'dot': np.array([1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0], dtype=np.int32),
               'cross': np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                 dtype=np.float32),
               'maxes': np.array([10., 10., 10.,
                                  14.142136, 14.142136, 14.142136,
                                  14.142136, 14.142136, 14.142136,
                                  0., 0., 0.],
                                 dtype=np.float32),
               'a': np.array([10., -0., 0.], dtype=np.float32),
               'b': np.array([0., 10., 0.], dtype=np.float32),
               'c': np.array([0., 0., 10.], dtype=np.float32)}
    print('DESIRED:')
    #print(json.dumps(desired, indent=4))
    print(desired)
    print()
    di_cell = copy.deepcopy(DI_CELL)
    code, message, actual = crysfml08lib.f_get_twofold_axes(di_cell, 1.0)
    print(f'CODE: {code}')
    print(f'MESSAGE: {message}')
    print('ACTUAL:')
    #print(json.dumps(actual, indent=4))
    print(actual)
