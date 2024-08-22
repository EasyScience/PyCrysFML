import os
import sys
from numpy.testing import assert_allclose

sys.path.append(os.getcwd())  # to access tests/helpers.py
from tests.helpers import (dat_to_ndarray,
                           path_to_progs,
                           path_to_desired,
                           path_to_actual,
                           run_exe_with_args,
                           set_crysfml_db)


# Tests

def test__Simple_calc_powder__SrTiO3s():
    prog = 'Simple_calc_powder'
    input = 'SrTiO3s.cfl'
    output = 'SrTiO3s.dat'
    skip_begin = 2
    skip_end = 1
    usecols = (0, 1, 2, 3, 4, 5, 6, 7)
    tol = 1e-03
    set_crysfml_db()
    run_exe_with_args(path_to_progs(prog),
                      args=f'{path_to_actual(input)}')
    desired = dat_to_ndarray(path_to_desired(output),
                             skip_begin=skip_begin,
                             skip_end=skip_end,
                             usecols=usecols)
    actual = dat_to_ndarray(path_to_actual(output),
                            skip_begin=skip_begin,
                            skip_end=skip_end,
                            usecols=usecols)
    assert_allclose(desired,
                    actual,
                    rtol=tol,
                    verbose=True)

def test__Simple_calc_powder__ponsin():
    prog = 'Simple_calc_powder'
    input = 'ponsin.cfl'
    output = 'if_ponsin.dat'
    skip_begin = 2
    skip_end = 1
    usecols = (0, 1, 2, 3, 4, 5, 6, 7)
    tol = 1e-03
    set_crysfml_db()
    run_exe_with_args(path_to_progs(prog),
                      args=f'{path_to_actual(input)}')
    desired = dat_to_ndarray(path_to_desired(output),
                             skip_begin=skip_begin,
                             skip_end=skip_end,
                             usecols=usecols)
    actual = dat_to_ndarray(path_to_actual(output),
                            skip_begin=skip_begin,
                            skip_end=skip_end,
                            usecols=usecols)
    assert_allclose(desired,
                    actual,
                    rtol=tol,
                    verbose=True)

# Debug

if __name__ == '__main__':
    test__Simple_calc_powder__SrTiO3s()
