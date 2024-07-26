import argparse
import copy
import os
import numpy as np
from numpy.testing import assert_almost_equal

#import cfml_utilities
#import pycrysfml
#from pycrysfml import crysfml08lib
from pycrysfml import cfml_utilities


STUDY_DICT_PM3M = {
  "phases": [
    {
      "SrTiO3": {
        "_space_group_name_H-M_alt": "P m -3 m",
        "_cell_length_a": 3.9,
        "_cell_length_b": 3.9,
        "_cell_length_c": 3.9,
        "_cell_angle_alpha": 90,
        "_cell_angle_beta": 90,
        "_cell_angle_gamma": 90,
        "_atom_site": [
          {
            "_label": "Sr",
            "_type_symbol": "Sr",
            "_fract_x": 0.5,
            "_fract_y": 0.5,
            "_fract_z": 0.5,
            "_occupancy": 1,
            "_adp_type": "Biso",
            "_B_iso_or_equiv": 0.40
          },
          {
            "_label": "Ti",
            "_type_symbol": "Ti",
            "_fract_x": 0,
            "_fract_y": 0,
            "_fract_z": 0,
            "_occupancy": 1,
            "_adp_type": "Biso",
            "_B_iso_or_equiv": 0.50
          },
          {
            "_label": "O",
            "_type_symbol": "O",
            "_fract_x": 0.5,
            "_fract_y": 0,
            "_fract_z": 0,
            "_occupancy": 1,
            "_adp_type": "Biso",
            "_B_iso_or_equiv": 0.65
          }
        ]
      }
    }
  ],
  "experiments": [
    {
      "NPD": {
        "_diffrn_source": "nuclear reactor",
        "_diffrn_radiation_probe": "neutron",
        "_diffrn_radiation_wavelength": 1.27,
        "_pd_instr_resolution_u": 0.02,
        "_pd_instr_resolution_v": -0.02,
        "_pd_instr_resolution_w": 0.12,
        "_pd_instr_resolution_x": 0.0015,
        "_pd_instr_resolution_y": 0,
        "_pd_instr_reflex_asymmetry_p1": 0,
        "_pd_instr_reflex_asymmetry_p2": 0,
        "_pd_instr_reflex_asymmetry_p3": 0,
        "_pd_instr_reflex_asymmetry_p4": 0,
        "_pd_meas_2theta_offset": 0,
        "_pd_meas_2theta_range_min": 1,
        "_pd_meas_2theta_range_max": 140,
        "_pd_meas_2theta_range_inc": 0.05
      }
    }
  ]
}

# Help functions

def path_to_desired(file_name:str):
    return os.path.join(os.path.dirname(__file__), 'desired', file_name)

def compute_pattern(study_dict:dict):
    #_, y = crysfml08lib.f_powder_pattern_from_json(study_dict)  # returns x and y arrays
    _, y = cfml_utilities.powder_pattern_from_json(study_dict)  # returns x and y arrays
    return y

# Tests

# Workaround to set env variable CRYSFML_DB for all the tests below
# If running this with python instead of pytest, CRYSFML_DB is set automatically
# from the pycrysfml __init__.py, when importing pycrysfml
def test__crysfml_db_path():
    #os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(crysfml08lib.__file__), 'Databases')
    os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(cfml_utilities.__file__), 'Databases')
    actual = os.getenv('CRYSFML_DB', default='')
    desired = os.environ['CRYSFML_DB']
    assert desired == actual

def test__compute_pattern__SrTiO3_Pm3m(benchmark):
    study_dict = copy.deepcopy(STUDY_DICT_PM3M)
    norm = 120
    _, desired = np.loadtxt(path_to_desired('srtio3-pm3m-pattern_Nebil-ifort.xy'), unpack=True)
    desired = desired - 20.0  # remove background
    desired = np.roll(desired, -1)  # compensate for a 1-element horizontal shift in y data between old Nebil windows build and Andrew current gfortran build
    desired = desired / norm
    actual = benchmark(compute_pattern, study_dict)
    actual = actual / norm
    assert_almost_equal(desired, actual, decimal=0, verbose=True)

def test__compute_pattern__SrTiO3_Pnma(benchmark):
    study_dict = copy.deepcopy(STUDY_DICT_PM3M)
    study_dict['phases'][0]['SrTiO3']['_space_group_name_H-M_alt'] = 'P n m a'
    norm = 0.65
    desired = np.loadtxt(path_to_desired('srtio3-pnma-pattern_Andrew-ifort.y'), unpack=True)
    desired = desired - 20.0  # remove background
    desired = desired / norm
    actual = benchmark(compute_pattern, study_dict)
    actual = actual / norm
    assert_almost_equal(desired, actual, decimal=2, verbose=True)

# Debug

if __name__ == '__main__':
    print(f":::::: os.environ['CRYSFML_DB']: {os.environ['CRYSFML_DB']}")
    print(f':::::: os.getcwd(): {os.getcwd()}')
    test__compute_pattern__SrTiO3_Pm3m()
