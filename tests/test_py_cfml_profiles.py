import os
import sys
import math
from numpy.testing import assert_almost_equal

from pycrysfml08 import py_cfml_profiles

# Tests

def test_back_to_back_exp():
    alpha = 0.1
    beta = 0.3
    x = 1.0
    N = 0.5*alpha*beta/(alpha+beta)
    # output of back_to_back_exp for a positive and a negative value of x
    desired = [N * math.exp(-beta * x), N * math.exp(alpha * (-x))]
    # x > 0
    code, message, actual_x_pos = py_cfml_profiles.back_to_back_exp(x, alpha, beta)
    assert code == 0
    assert message == ''
    code, message, actual_x_neg = py_cfml_profiles.back_to_back_exp(-x, alpha, beta)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, [actual_x_pos, actual_x_neg], decimal=8, verbose=True)


def test_exponential():
    a = 1.0
    x = 1.5
    desired = a * math.exp(-a * x)
    code, message, actual = py_cfml_profiles.exponential(x, a)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=3, verbose=True)


def test_gaussian():
    x = 1.5
    H = 1.0
    desired = 2 * math.sqrt(math.log(2) / math.pi) / H * math.exp(- 4 * math.log(2) * (x / H)**2)
    code, message, actual = py_cfml_profiles.gaussian(x, H)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=8, verbose=True)


def test_hat():
    # Width and amplitude of hat function
    width = 0.33
    half_width = width / 2
    ampl_hat = 1.0 / width

    # Negative value outside of hat function
    x_neg_out = -0.3
    desired = 0
    code, message, actual = py_cfml_profiles.hat(x_neg_out, width)
    assert code == 0
    assert message == ''
    assert desired == actual

    # Negative value at boundary
    x_neg_boundary = -half_width
    desired = ampl_hat
    code, message, actual = py_cfml_profiles.hat(x_neg_boundary, width)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=6, verbose=True)

    # Negative value within range of hat function
    x_neg_in = -0.1
    desired = ampl_hat
    code, message, actual = py_cfml_profiles.hat(x_neg_in, width)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=6, verbose=True)

    # Value of 0
    x_zero = 0.0
    desired = ampl_hat
    code, message, actual = py_cfml_profiles.hat(x_zero, width)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=6, verbose=True)

    # Positive value within range of hat function
    x_pos_in = 0.1
    desired = ampl_hat
    code, message, actual = py_cfml_profiles.hat(x_pos_in, width)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=6, verbose=True)

    # Positive value at boundary
    x_pos_boundary = half_width
    desired = ampl_hat
    code, message, actual = py_cfml_profiles.hat(x_pos_boundary, width)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=6, verbose=True)

    # Positive value outside of hat function
    x_pos_out = 0.3
    desired = 0
    code, message, actual = py_cfml_profiles.hat(x_pos_out, width)
    assert code == 0
    assert message == ''
    assert desired == actual


def test_ikeda_carpenter():
    x = 1.0
    alpha = 2.0
    beta = 3.0
    r = 4.0
    exb = math.exp(-beta * x)
    exa = math.exp(-alpha * x)
    poly = 1.0 + (1.0 + 0.5 * (alpha - beta) * x) * (alpha - beta) * x
    desired = 0.5 * alpha ** 3 * (
            (1.0 - r) * x**2 * exa
            + 2.0 * r * beta * (exb - exa * poly) / (alpha - beta) ** 3
    )

    code, message, actual = py_cfml_profiles.ikeda_carpenter(x, alpha, beta, r)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=7, verbose=True)

    # If x < 0, the function should return 0
    x = 0.0
    desired = 0.0
    code, message, actual = py_cfml_profiles.ikeda_carpenter(x, alpha, beta, r)
    assert code == 0
    assert message == ''
    assert desired == actual


def test_lorentzian():
    x = 1.0
    H = 1.0

    al = 2.0 / math.pi / H
    bl = 4.0 / (H * H)
    desired = al / (1.0 + bl * x * x)
    code, message, actual = py_cfml_profiles.lorentzian(x, H)

    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=8, verbose=True)


def test_pseudovoigt():
    x = 1.0
    H = 1.5
    eta = 0.9
    desired = eta * py_cfml_profiles.lorentzian(x, H)[2] \
              + (1 - eta) * py_cfml_profiles.gaussian(x, H)[2]

    code, message, actual = py_cfml_profiles.pseudovoigt(x, H, eta)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=8, verbose=True)


def test_split_pseudovoigt():
    H1 = 1.0
    H2 = 1.0
    eta1 = 0.5
    eta2 = 0.5

    # TODO check where the terms in norm_coeff come from
    norm_coeff = 0.25 * H1 * (eta1 * 1.0126586 + 2.128934) \
                 + 0.25 * H2 * (eta2 * 1.0126586 + 2.128934)

    # Test for negative x
    x = -1.0
    gauss = math.exp(-4.0 * math.log(2.0) * (x / H1)**2)
    lor = 1.0 / (1.0 + 4.0 * (x / H1) ** 2)
    desired = (eta1 * lor + (1.0 - eta1) * gauss) / norm_coeff

    code, message, actual = py_cfml_profiles.split_pseudovoigt(x, H1, H2, eta1, eta2)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=8, verbose=True)

    # Test for positive x
    x = 1.0
    gauss = math.exp(-4.0 * math.log(2.0) * (x / H2)**2)
    lor = 1.0 / (1.0 + 4.0 * (x / H2) ** 2)
    desired = (eta2 * lor + (1.0 - eta2) * gauss) / norm_coeff
    code, message, actual = py_cfml_profiles.split_pseudovoigt(x, H1, H2, eta1, eta2)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=8, verbose=True)


def test_tch_pvoigt():
    """ Test for Thompson-Cox-Hastings pseudo-Voigt profile """
    x = 1.0
    Hg = 2.0
    Hl = 3.0
    # Coefficients of polynomials giving expression of FWHM as function of powers of Hg**(5-n)Hl**n,
    # n=1..5. See Thompson et al, Acta Cryst. 20, 79 (1987) for details
    o1 = 2.69269
    o2 = 2.42843
    o3 = 4.47163
    o4 = 0.07842
    # Coefficients of polynomials giving expression of eta as function of powers of (Hl/FWHM)**n,
    # n=1..3
    e1 = 1.36603
    e2 = 0.47719
    e3 = 0.11116

    H = abs(Hg ** 5 + o1 * Hg ** 4 * Hl
            + o2 * Hg ** 3 * Hl ** 2
            + o3 * Hg ** 2 * Hl ** 3 + o4 * Hg * Hl ** 4 + Hl ** 5) ** 0.2

    r = Hl / H
    eta = max(1.0e-06, r * (e1 - (e2 + e3 * r) * r))

    gauss = 2.0 * math.sqrt(math.log(2.)/math.pi) / H * math.exp(-4.0 * math.log(2.0) * (x/H)**2)
    lor = 2.0 / math.pi / H / (1.0 + 4.0 * (x/H)**2)
    desired = eta * lor + (1.0 - eta) * gauss

    code, message, actual = py_cfml_profiles.tch_pvoigt(x, Hg, Hl)
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=8, verbose=True)
