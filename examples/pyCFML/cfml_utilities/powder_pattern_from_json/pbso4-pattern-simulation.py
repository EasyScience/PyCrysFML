import matplotlib.pyplot as plt
from pycrysfml import cfml_utilities

EXAMPLE = {
   "phases":[
      {
         "pbso4":{
            "_space_group_name_H-M_alt":"P n m a",
            "_cell_length_a":8.47793,
            "_cell_length_b":5.39682,
            "_cell_length_c":6.9581,
            "_cell_angle_alpha":90.0,
            "_cell_angle_beta":90.0,
            "_cell_angle_gamma":90.0,
            "_atom_site":[
               {
                  "_label":"Pb",
                  "_type_symbol":"Pb",
                  "_fract_x":0.18724,
                  "_fract_y":0.25,
                  "_fract_z":0.16615,
                  "_occupancy":1.0,
                  "_adp_type":"Biso",
                  "_B_iso_or_equiv":0.5
               },
               {
                  "_label":"S",
                  "_type_symbol":"S",
                  "_fract_x":0.06434,
                  "_fract_y":0.25,
                  "_fract_z":0.68261,
                  "_occupancy":1.0,
                  "_adp_type":"Biso",
                  "_B_iso_or_equiv":0.5
               },
               {
                  "_label":"O1",
                  "_type_symbol":"O",
                  "_fract_x":0.9079,
                  "_fract_y":0.25,
                  "_fract_z":0.59598,
                  "_occupancy":1.0,
                  "_adp_type":"Biso",
                  "_B_iso_or_equiv":0.5
               },
               {
                  "_label":"O2",
                  "_type_symbol":"O",
                  "_fract_x":0.1926,
                  "_fract_y":0.25,
                  "_fract_z":0.54171,
                  "_occupancy":1.0,
                  "_adp_type":"Biso",
                  "_B_iso_or_equiv":0.5
               },
               {
                  "_label":"O3",
                  "_type_symbol":"O",
                  "_fract_x":0.08043,
                  "_fract_y":0.02893,
                  "_fract_z":0.80734,
                  "_occupancy":1.0,
                  "_adp_type":"Biso",
                  "_B_iso_or_equiv":0.5
               }
            ]
         }
      }
   ],
   "experiments":[
      {
         "pd":{
            "_diffrn_radiation_probe":"neutron",
            "_diffrn_radiation_wavelength":1.912,
            "_pd_instr_resolution_u":0.12205,
            "_pd_instr_resolution_v":-0.33588,
            "_pd_instr_resolution_w":0.2838,
            "_pd_instr_resolution_x":0.14871,
            "_pd_instr_resolution_y":0.0,
            "_pd_meas_2theta_range_min":10.0,
            "_pd_meas_2theta_range_max":140.00,
            "_pd_meas_2theta_range_inc":0.05,
            "_pd_meas_2theta_offset":-0.138,
         }
      }
   ]
}

if __name__ == '__main__':
    x, y = cfml_utilities.powder_pattern_from_json(EXAMPLE)
    plt.plot(x, y)
    plt.show()
