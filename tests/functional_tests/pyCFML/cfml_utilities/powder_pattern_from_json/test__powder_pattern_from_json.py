import os
from pycrysfml import crysfml08lib

os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(crysfml08lib.__file__), 'Databases')  # access to Databases/magnetic_data.txt

PHASE_CIF = os.path.join(os.path.dirname(__file__), 'phases', '19023_Ca1Li2O4Si1_Tetragonal_121.cif')

JSON = {
  "cif": PHASE_CIF,
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
            "_label": "CIFCODE",
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

# Debug

if __name__ == '__main__':
    print(f':::::: Calculating diffraction pattern for: {os.path.basename(PHASE_CIF)}')
    x, y = crysfml08lib.f_powder_pattern_from_json(JSON)
    print(f':::::: Resulted y-array: {y}')
