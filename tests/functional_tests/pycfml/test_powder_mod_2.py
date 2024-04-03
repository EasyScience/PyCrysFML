import os
import sys
import math
import copy
import numpy as np
from deepdiff import DeepDiff
from numpy.testing import assert_almost_equal

from pycrysfml08 import powder_mod_2


os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(powder_mod_2.__file__), 'Databases')  # access to Databases/magnetic_data.txt

STUDY_DICT = {
  "phases": [
    {
      "SrTiO3": {
        "_space_group_name_H-M_alt": "P m -3 m",
        #"_space_group_name_H-M_alt": "P n m a",
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
        "_pd_meas_2theta_range_inc": 0.05,
        "_phase": [
          {
            "_label": "SrTiO3",
            "_scale": 1
          }
        ],
        "_pd_background": [
          {
            "_2theta": 1,
            "_intensity": 20
          },
          {
            "_2theta": 140,
            "_intensity": 20
          }
        ]
      }
    }
  ]
}

# Help functions

def phase_name_by_idx(study_dict:dict, phase_idx:int=0):
    return list(study_dict['phases'][phase_idx].keys())[phase_idx]

def space_group_by_phase_idx(study_dict:dict, phase_idx:int=0):
    phase_name = phase_name_by_idx(study_dict, phase_idx)
    return study_dict['phases'][phase_idx][phase_name]['_space_group_name_H-M_alt']

def set_space_group_by_phase_idx(study_dict:dict, phase_idx:int, space_group:str):
    phase_name = phase_name_by_idx(study_dict, phase_idx)
    study_dict['phases'][phase_idx][phase_name]['_space_group_name_H-M_alt'] = space_group

def compute_pattern(study_dict:dict):
    return powder_mod_2.simulation(study_dict)

def clean_after_compute(study_dict:dict):
    files = ['powder_pattern.dat', 'fort.77', f'{phase_name_by_idx(study_dict)}.powder']
    for f in files:
        try:
            os.remove(f)
        except:
            pass

# Tests

def test_magnetic_data_txt_exists():
    fpath = os.path.abspath(os.path.join(os.path.dirname(powder_mod_2.__file__), 'Databases', 'magnetic_data.txt'))
    assert os.path.isfile(fpath) == True

def test_phase_name_SrTiO3():
    assert phase_name_by_idx(STUDY_DICT, phase_idx=0) == 'SrTiO3'

def _test_space_group_Pm3m():
    assert space_group_by_phase_idx(STUDY_DICT, phase_idx=0) == 'P m -3 m'

def _test_set_space_group_Pm3m():
    new_study_dict = copy.deepcopy(STUDY_DICT)
    set_space_group_by_phase_idx(new_study_dict, phase_idx=0, space_group='P m -3 m')
    assert DeepDiff(STUDY_DICT, new_study_dict) == {}

def test_set_space_group_Pnma():
    new_study_dict = copy.deepcopy(STUDY_DICT)
    set_space_group_by_phase_idx(new_study_dict, phase_idx=0, space_group='P n m a')
    assert space_group_by_phase_idx(new_study_dict, phase_idx=0) == 'P n m a'

def _test_compute_pattern_SrTiO3_Pm3m():
    _, desired = np.loadtxt(os.path.join(os.path.dirname(__file__), 'srtio3-pm3m-pattern_Nebil-ifort.xy'), unpack=True)
    desired = desired - 20.0  # remove background
    study_dict = copy.deepcopy(STUDY_DICT)
    set_space_group_by_phase_idx(study_dict, phase_idx=0, space_group='P m -3 m')
    pattern = compute_pattern(study_dict)
    actual = pattern[0].astype(np.float64)
    # compensate for a 1-element shift in y data between Nebil windows build and my gfortran build
    desired = desired[1:]
    actual = actual[:-1]
    assert_almost_equal(desired, actual, decimal=0, verbose=True)

def test_compute_pattern_SrTiO3_Pnma():
    desired = np.loadtxt(os.path.join(os.path.dirname(__file__), 'srtio3-pmmm-pattern_Andrew-ifort.xy'), unpack=True)
    desired = desired - 20.0  # remove background
    study_dict = copy.deepcopy(STUDY_DICT)
    set_space_group_by_phase_idx(study_dict, phase_idx=0, space_group='P n m a')
    pattern = compute_pattern(study_dict)
    actual = pattern[0].astype(np.float64)
    assert_almost_equal(desired, actual, decimal=2, verbose=True)

# Debug

if __name__ == '__main__':
    np.set_printoptions(precision=5, threshold = np.inf)
    study_dict = copy.deepcopy(STUDY_DICT)

    #clean_after_compute(study_dict)
    study_dict["phases"][0]["SrTiO3"]["_space_group_name_H-M_alt"] = 'P m -3 m'
    ycalc = powder_mod_2.simulation(study_dict)
    print('::::: Y calculated (P m -3 m):', ycalc)

    study_dict["phases"][0]["SrTiO3"]["_space_group_name_H-M_alt"] = 'P n m a'
    ycalc = powder_mod_2.simulation(study_dict)
    print('::::: Y calculated (P n m a):', ycalc)
    #np.savetxt('ycalc.dat', ycalc, fmt='%12.6f')

    study_dict["phases"][0]["SrTiO3"]["_space_group_name_H-M_alt"] = 'I 4 3 2'
    ycalc = powder_mod_2.simulation(study_dict)
    print('::::: Y calculated (I 4 3 2):', ycalc)
    #np.savetxt('ycalc.dat', ycalc, fmt='%12.6f')
