import copy
import os
import numpy as np
from numpy.testing import assert_almost_equal
from pycrysfml import crysfml08lib
#from pycrysfml import cfml_utilities


os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(crysfml08lib.__file__), 'Databases')  # access to Databases/magnetic_data.txt

STUDY_DICT = {
  "phases": [
    {
      "SrTiO3": {
        #"_space_group_name_H-M_alt": "P m -3 m",
        "_space_group_name_H-M_alt": "P n m a",
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

def path_to_desired(file_name:str):
    return os.path.join(os.path.dirname(__file__), 'desired', file_name)

def phase_name_by_idx(study_dict:dict, phase_idx:int=0):
    return list(study_dict['phases'][phase_idx].keys())[phase_idx]

def space_group_by_phase_idx(study_dict:dict, phase_idx:int=0):
    phase_name = phase_name_by_idx(study_dict, phase_idx)
    return study_dict['phases'][phase_idx][phase_name]['_space_group_name_H-M_alt']

def set_space_group_by_phase_idx(study_dict:dict, phase_idx:int, space_group:str):
    phase_name = phase_name_by_idx(study_dict, phase_idx)
    study_dict['phases'][phase_idx][phase_name]['_space_group_name_H-M_alt'] = space_group

def compute_pattern(study_dict:dict):
    _, y = crysfml08lib.f_powder_pattern_from_json(study_dict)  # returns x and y arrays
    y = y.astype(np.float64)
    return y

#def compute_pattern_2(study_dict:dict):
#    return cfml_utilities.powder_pattern_from_json(study_dict)

# Tests

def _test__compute_pattern__SrTiO3_Pm3m():
    _, desired = np.loadtxt(path_to_desired('srtio3-pm3m-pattern_Nebil-ifort.xy'), unpack=True)
    desired = desired - 20.0  # remove background
    study_dict = copy.deepcopy(STUDY_DICT)
    set_space_group_by_phase_idx(study_dict, phase_idx=0, space_group='P m -3 m')
    pattern = compute_pattern(study_dict)
    actual = pattern.astype(np.float64)
    # compensate for a 1-element shift in y data between Nebil windows build and my gfortran build
    #desired = desired[1:]
    #actual = actual[:-1]
    assert_almost_equal(desired, actual, decimal=0, verbose=True)

def test__compute_pattern__SrTiO3_Pnma():
    desired = np.loadtxt(path_to_desired('srtio3-pmmm-pattern_Andrew-ifort.xy'), unpack=True)
    desired = desired - 20.0  # remove background
    study_dict = copy.deepcopy(STUDY_DICT)
    set_space_group_by_phase_idx(study_dict, phase_idx=0, space_group='P n m a')
    actual = compute_pattern(study_dict)
    assert_almost_equal(desired, actual, decimal=2, verbose=True)

# Debug

if __name__ == '__main__':
    test__compute_pattern__SrTiO3_Pnma()
