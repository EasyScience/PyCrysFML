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

def test__mol_tpcr__molecule_PPH3_Z():
    prog = 'mol_tpcr'
    input = 'molecule_PPH3_Z.cfl'
    output = 'molecule_PPH3_Z_fc.cfl'
    skip_begin = 7
    skip_end = 1
    usecols = (4, 5, 6, 7)
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
    test__mol_tpcr__molecule_PPH3_Z()
