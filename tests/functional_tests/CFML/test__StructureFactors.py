import os
import sys
import re
import filecmp
import time
import toml
import subprocess
import platform
import numpy as np
from io import StringIO
from pathlib import Path
from numpy.testing import assert_array_equal, assert_almost_equal, assert_allclose


################
# Help functions
################

def set_crysfml_db_path():
    """Sets the env variable 'CRYSFML_DB' as the path to the 'Databases' directory containing the file 'magnetic_data.txt'."""
    default = os.path.join(os.getcwd(), '..', '..', '..')
    project_dir = os.getenv('GITHUB_WORKSPACE', default=default)  # locally do: export GITHUB_WORKSPACE=`pwd`
    config_path = os.path.join(project_dir, 'scripts.toml')
    with open(config_path, 'r') as f:
        CONFIG = toml.load(f)
    db_relpath = CONFIG['cfml']['dir']['repo-database']
    db_abspath = os.path.join(project_dir, db_relpath)
    db_dir_relpath = os.path.dirname(db_abspath)
    db_dir_abspath = os.path.abspath(db_dir_relpath)
    os.environ['CRYSFML_DB'] = db_dir_abspath

def change_cwd_to_tests():
    """Changes the current directory to the directory of this script file."""
    os.chdir(os.path.dirname(__file__))

def run_exe_with_args(file_name:str, args:str=''):
    """Runs the executable with optional arguments."""
    if platform.system() == 'Windows':
        file_name = f'{file_name}.exe'
    exe_path = os.path.join(os.getcwd(), file_name)
    cmd = f'{exe_path} {args}'
    os.system(cmd)

def dat_to_ndarray(file_name:str, skip_lines:int=0):
    """Parses the file to extract an array of data and converts it to a numpy array."""
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()  # reads into list removing end-of-line symbols
    del lines[:skip_lines]  # deletes requested number of first lines
    joined = ' '.join(lines)  # joins into single string
    stripped = joined.strip()  # removes leading and trailing whitespaces
    splitted = re.split(r'\s{2,}', stripped)  # splits back into list ignoring single whitespaces
    array = np.array(splitted, dtype=np.float32)  # converts list of string numbers into numpy array of floats
    return array

#######
# Tests
#######

def test__Calc_Sfac__mfe_sfac():
    run_exe_with_args('Calc_Sfac', args='mfe_sfac.cfl 1.0')
    desired = dat_to_ndarray('SrTiO3s_desired.dat', skip_lines=2)
    actual = dat_to_ndarray('SrTiO3s.dat', skip_lines=2)
    assert_allclose(desired, actual, rtol=1e-03, verbose=True)

def test__Calc_Sfac__mfe_msfac():
    run_exe_with_args('Calc_Sfac', args='mfe_msfac.cfl 1.0')
    desired = dat_to_ndarray('SrTiO3s_desired.dat', skip_lines=2)
    actual = dat_to_ndarray('SrTiO3s.dat', skip_lines=2)
    assert_allclose(desired, actual, rtol=1e-03, verbose=True)

#######
# Debug
#######

if __name__ == '__main__':
    test__Calc_Sfac__mfe_sfac()
