import os
import re
import filecmp
import time
import tomllib
import subprocess
from io import StringIO
import numpy as np
from numpy.testing import assert_array_equal, assert_almost_equal


# Help functions

def set_crysfml_db_path():
    """Sets the env variable 'CRYSFML_DB' as the path to the 'Databases' directory containing the file 'magnetic_data.txt'."""
    config_path = os.path.join(os.getcwd(), 'scripts.toml')
    with open(config_path, 'rb') as f:
        CONFIG = tomllib.load(f)
    repo_dir = CONFIG['cfml']['dir']['repo']
    src_dir = CONFIG['cfml']['dir']['repo-src']
    db_path = os.path.join(os.getcwd(), repo_dir, src_dir, 'Databases')
    os.environ['CRYSFML_DB'] = db_path

def change_cwd_to_tests():  # set current directory to be the directory of this script file
    """Changes the current directory to the directory of this script file."""
    os.chdir(os.path.dirname(__file__))

def dat_to_ndarray(file_name:str, skip_begin:int=3, skip_end:int=4):
    """Parses the file to extract an array of data and converts it to a numpy array."""
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

# Set up paths

os.system(f"echo '----- os.getcwd(): {os.getcwd()}'")
os.system(f'ls -l')

set_crysfml_db_path()
change_cwd_to_tests()

os.system(f"echo '----- os.getcwd(): {os.getcwd()}'")
os.system(f'ls -l')



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
    os.system(f"echo '----- ./Bond_StrN LiFePO4n.cfl'")
    os.system(f'./Bond_StrN LiFePO4n.cfl')
    time.sleep(1)

    os.system(f"echo '----- os.getcwd(): {os.getcwd()}'")
    os.system(f'ls -l')

    file_name = 'LiFePO4n_sum_desired.bvs'
    os.system(f"echo '----- file_name: {file_name}'")
    os.system(f"echo '----- os.path.abspath(file_name): {os.path.abspath(file_name)}'")

    # compare the actual output with the desired one
    desired = dat_to_ndarray(file_name)
    #actual = dat_to_ndarray('LiFePO4n_sum.bvs')
    #assert_array_equal(desired, actual, verbose=True)
