import os
import sys
import math
import numpy as np
from numpy.testing import assert_almost_equal

from pycrysfml08 import py_cfml_sxtal_geom

# Tests


def test__z1frmd():
    wavelength = 1.49
    # angles in degrees
    chi = 5.0
    phi = 1.5
    gamma = 10.0
    omega = 15.0
    nu = 20.0

    desired = np.array([0.09877002, -0.01742656,  0.23901892], dtype='f')
    code, message, actual = py_cfml_sxtal_geom.z1frmd(wavelength, chi, phi, gamma, omega, nu)
    assert code == 0
    assert message == ''
    assert_almost_equal(actual, desired, decimal=3, verbose=True)


def test__z1frnb():
    wave = 1.49
    ga = 10.000
    om = 15.000
    nu = 20.000
    desired = np.array([0.119, -0.02, 0.23], dtype='f')
    code, message, actual = py_cfml_sxtal_geom.z1frnb(wave, ga, om, nu)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=3, verbose=True)
