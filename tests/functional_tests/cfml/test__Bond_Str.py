import os
import re
import filecmp
import time
import subprocess
from io import StringIO
import numpy as np
from numpy.testing import assert_array_equal, assert_almost_equal

from pycrysfml08 import powder_mod


os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(powder_mod.__file__), 'Databases')  # access to Databases/magnetic_data.txt
os.chdir(os.path.dirname(__file__))  # set current directory to be the directory of this script file

# Help functions

def dat_to_ndarray(file_name:str, skip_begin:int=3, skip_end:int=4):
    with open(file_name, 'r') as file:
        lines = file.readlines()  # reads into list
    del lines[:skip_begin]  # deletes requested number of first lines
    del lines[len(lines)-skip_end:]  # deletes requested number of last lines
    lines = [l.replace('(',' ').replace(')', ' ') for l in lines]  # replace brackets with spaces
    joined = '\n'.join(lines)  # joins into single string
    array = np.loadtxt(StringIO(joined),  # converts string to ndarray
                       dtype={ 'names':   ('Atom', 'Coord', 'D_aver', 'D_aver_Sigm', 'Distort', 'Valence', 'BVSum', 'BVSum_Sigma'),
                               'formats': ('S2',   'f4',    'f4',     'i4',          'f8',      'f4',      'f4',    'i4'         ) })
    return array

# Tests

def test__Bond_StrN():
    # run fortran program to produce the actual output
    os.system(f'./Bond_StrN LiFePO4n.cfl')
    time.sleep(1)
    # compare the actual output with the desired one
    desired = dat_to_ndarray('LiFePO4n_sum_desired.bvs')
    actual = dat_to_ndarray('LiFePO4n_sum.bvs')
    assert_array_equal(desired, actual, verbose=True)

# Debug

if __name__ == '__main__':
    # run fortran program to produce the actual output
    os.system(f'./Bond_StrN LiFePO4n.cfl')
    time.sleep(1)
    # compare the actual output with the desired one
    desired = dat_to_ndarray('LiFePO4n_sum_desired.bvs')
    actual = dat_to_ndarray('LiFePO4n_sum.bvs')
    assert_array_equal(desired, actual, verbose=True)
