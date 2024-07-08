import os
import sys
import re
import filecmp
import time
import tomllib
import subprocess
import platform
import numpy as np
from numpy.testing import assert_allclose, assert_almost_equal


# Help functions

def set_crysfml_db_path():
    """Sets the env variable 'CRYSFML_DB' as the path to the 'Databases' directory containing the file 'magnetic_data.txt'."""
    default = os.path.join(os.getcwd(), '..', '..', '..')
    project_dir = os.getenv('GITHUB_WORKSPACE', default=default)  # locally do: export GITHUB_WORKSPACE=`pwd`
    config_path = os.path.join(project_dir, 'scripts.toml')
    with open(config_path, 'rb') as f:
        CONFIG = tomllib.load(f)
    repo_dir = CONFIG['cfml']['dir']['repo']
    src_dir = CONFIG['cfml']['dir']['repo-src']
    db_path = os.path.join(project_dir, repo_dir, src_dir, 'Databases')
    os.environ['CRYSFML_DB'] = db_path

def change_cwd_to_tests():
    """Changes the current directory to the directory of this script file."""
    os.chdir(os.path.dirname(__file__))

def run_exe_with_args(file_name:str, args:str=''):
    """Runs the executable with optional arguments."""
    if platform.system() == 'Windows':
        file_name = f'{file_name}.exe'
    file_name = os.path.abspath(file_name)
    cmd = f'{file_name}'
    if args:
        cmd = f'{file_name} {args}'
    #os.system(f"echo '::::: {cmd}'")
    os.system(f'{cmd}')
    time.sleep(2)

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

# Set up paths

change_cwd_to_tests()
set_crysfml_db_path()

# Tests

def test__Simple_calc_powder__SrTiO3s(benchmark):
    @benchmark
    def bench():
        run_exe_with_args('Simple_calc_powder', args='SrTiO3s.cfl')
    desired = dat_to_ndarray('SrTiO3s_desired.dat', skip_lines=2)
    actual = dat_to_ndarray('SrTiO3s.dat', skip_lines=2)
    assert_allclose(desired, actual, rtol=1e-03, verbose=True)

def test__Simple_calc_powder__ponsin(benchmark):
    @benchmark
    def bench():
        run_exe_with_args('Simple_calc_powder', args='ponsin.cfl')
    desired = dat_to_ndarray('if_ponsin_desired.dat', skip_lines=2)
    actual = dat_to_ndarray('if_ponsin.dat', skip_lines=2)
    assert_allclose(desired, actual, rtol=1e-03, verbose=True)

# Debug

if __name__ == '__main__':
    test__Simple_calc_powder__SrTiO3s()
