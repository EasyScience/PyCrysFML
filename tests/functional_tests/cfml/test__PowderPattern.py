import os
import re
import filecmp
import time
import subprocess
import numpy as np
from numpy.testing import assert_allclose, assert_almost_equal

from pycrysfml08 import powder_mod


os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(powder_mod.__file__), 'Databases')  # access to Databases/magnetic_data.txt
os.chdir(os.path.dirname(__file__))  # set current directory to be the directory of this script file

# Help functions

def dat_to_ndarray(file_name:str, skip_lines:int=0):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()  # reads into list removing end-of-line symbols
    del lines[:skip_lines]  # deletes requested number of first lines
    joined = ' '.join(lines)  # joins into single string
    stripped = joined.strip()  # removes leading and trailing whitespaces
    splitted = re.split(r'\s{2,}', stripped)  # splits back into list ignoring single whitespaces
    array = np.array(splitted, dtype=np.float32)  # converts list of string numbers into numpy array of floats
    return array

# Tests

def test__Simple_calc_powder__SrTiO3s():
    # run fortran program to produce the actual output
    os.system(f'./Simple_calc_powder SrTiO3s.cfl')
    time.sleep(1)
    # compare the actual output with the desired one
    desired = dat_to_ndarray('SrTiO3s_desired.dat', skip_lines=2)
    actual = dat_to_ndarray('SrTiO3s.dat', skip_lines=2)
    assert_allclose(desired, actual, rtol=1e-03, verbose=True)

def test__Simple_calc_powder__ponsin():
    # run fortran program to produce the actual output
    os.system(f'./Simple_calc_powder ponsin.cfl')
    time.sleep(1)
    # compare the actual output with the desired one
    desired = dat_to_ndarray('if_ponsin_desired.dat', skip_lines=2)
    actual = dat_to_ndarray('if_ponsin.dat', skip_lines=2)
    assert_allclose(desired, actual, rtol=1e-03, verbose=True)

# Debug

if __name__ == '__main__':
    os.system(f'./Simple_calc_powder SrTiO3s.cfl')
