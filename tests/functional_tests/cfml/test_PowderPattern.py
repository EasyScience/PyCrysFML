import os
import filecmp
import time
import subprocess

from pycrysfml08 import powder_mod


os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(powder_mod.__file__), 'Databases')  # access to Databases/magnetic_data.txt
os.chdir(os.path.dirname(__file__))  # set current directory to be the directory of this script file


# Tests

def _test__Simple_calc_powder__SrTiO3s():
    # run fortran program to produce the actual output
    os.system(f'./Simple_calc_powder SrTiO3s.cfl')
    # compare the actual output with the desired one
    with open('SrTiO3s_desired.dat', 'r') as file:
        desired = file.read()
    with open('SrTiO3s.dat', 'r') as file:
        actual = file.read()
    assert actual == desired

def _test__Simple_calc_powder__ponsin():
    # run fortran program to produce the actual output
    os.system(f'./Simple_calc_powder ponsin.cfl')
    # compare the actual output with the desired one
    with open('if_ponsin_desired.dat', 'r') as file:
        desired = file.read()
    with open('if_ponsin.dat', 'r') as file:
        actual = file.read()
    assert actual == desired

def test__Simple_calc_powder__SrTiO3s():
    # run fortran program to produce the actual output
    os.system(f'./Simple_calc_powder SrTiO3s.cfl')
    time.sleep(1)
    # compare the actual output with the desired one
    cmp = filecmp.cmp('SrTiO3s.dat', 'SrTiO3s_desired.dat')
    assert cmp == True

def test__Simple_calc_powder__ponsin():
    # run fortran program to produce the actual output
    os.system(f'./Simple_calc_powder ponsin.cfl')
    time.sleep(1)
    # compare the actual output with the desired one
    cmp = filecmp.cmp('if_ponsin.dat', 'if_ponsin_desired.dat')
    assert cmp == True
