import os
import sys
from numpy.testing import assert_allclose

sys.path.append(os.getcwd())  # to access tests/helpers.py
from tests.helpers import (dat_to_ndarray,
                           path_to_progs,
                           path_to_desired,
                           path_to_actual,
                           run_exe_with_args)


# Tests

def test__Bond_StrN__LiFePO4n():
    prog = 'Bond_StrN'
    input = 'LiFePO4n.cfl'
    output = 'LiFePO4n_sum.bvs'
    skip_begin = 3
    skip_end = 4
    usecols = (1, 2, 3, 4, 5, 6, 7)
    tol = 1e-02
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
    test__Bond_StrN__LiFePO4n()
