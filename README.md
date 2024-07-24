## About

This is a repository for creating a python library **pycrysfml** based on the new automatically generated Python API for the crystallographic library CrysFML2008 (Fortran 2008) from https://code.ill.fr/scientific-software/CrysFML2008.

## CI status

### Status of CI jobs 'build' and 'tests'

| Platform / Compiler       | gfortran | ifx         | ifort         | nagfor     |
| ------------------------- | -------- | ----------- | ------------- | ---------- |
| Windows 10                | ✅       | ❌1        | ✅           | ⚙️ Testing |
| Ubuntu 22.04              | ✅       | ✅          | ✅           | ⚙️ Testing |
| macOS 12 (Intel)          | ✅       | Unsupported | ❌2         | ⚙️ Testing |
| macOS 14 (Apple Silicone) | ✅       | Unsupported | Unsupported   | ⚙️ Testing |

* ❌1 - Failed at the **Run pyCFML functional tests** step (**'tests'** job):

```
tests\functional_tests\pyCFML\...\test__powder_pattern_from_json.py . [ 33%]
Windows fatal exception: access violation

Current thread 0x0000068c (most recent call first):

...

scripts/run_pycfml_functional_tests_no_benchmarks.sh:
line 2:  1359 Segmentation fault
```
* ❌2 - Failed at the **Build pyCFML shared obj / dynamic library** step (**'build'** job):

```
Undefined symbols for architecture x86_64:
  "_cfml_kvec_symmetry_mp_inlat_", referenced from:
      _cfml_kvec_symmetry_mp_latsym_ in libCrysFML08.a(ksym_auxsub.o)
  "_cfml_kvec_symmetry_mp_ltr_", referenced from:
      _cfml_kvec_symmetry_mp_latsym_ in libCrysFML08.a(ksym_auxsub.o)
  "_cfml_kvec_symmetry_mp_nlat_", referenced from:
      _cfml_kvec_symmetry_mp_latsym_ in libCrysFML08.a(ksym_auxsub.o)
ld: symbol(s) not found for architecture x86_64
```

## Installing

### Standard installation

The pycrysfml python package is currently in beta testing, with pre-releases being published on our own PyPi server. To test it, please install it using the PIP package manager with additional option as shown below.

* Create and activate a python environment (_optional_)

  ***macOS and Linux***

  ```
  python3.11 -m venv .venv
  source .venv/bin/activate
  ```

  ***Windows***

  ```
  python3.11 -m venv .venv
  .venv\Scripts\activate
  ```

* Upgrade the package installer for Python (_optional_)

  ```
  pip install --upgrade pip
  ```

* Install pycrysfml using a link to our own online repository

  ```
  pip install pycrysfml --extra-index-url https://easyscience.github.io/pypi/
  ```

### Installation from source

If the standard installation doesn't work for you, try building pycrysfml locally and installing it from the generated Python wheel.

* Create and activate a python environment (_optional_)

  ***macOS and Linux***

  ```
  python3.11 -m venv .venv
  source .venv/bin/activate
  ```

  ***Windows***

  ```
  python3.11 -m venv .venv
  .venv\Scripts\activate
  ```

* Upgrade the package installer for Python (_optional_)

  ```
  pip install --upgrade pip
  ```

* Install Python dependences, including extras (ci and test)

  ```
  pip install '.[ci,test]'
  ```

* Print possible options for creating job scripts (_optional_)

  ```
  python pybuild.py --help
  ```

* Create job scripts with default options

  ```
  python pybuild.py --create-scripts
  ```

* Print some build-specific variables (_optional_)

  ```
  scripts/print_build_variables.sh
  ```

* Create CFML and pyCFML directories

  ```
  scripts/create_cfml_repo_dir.sh
  scripts/create_cfml_build_dir.sh
  scripts/create_cfml_dist_dir.sh
  scripts/create_pycfml_src_dir.sh
  scripts/create_pycfml_build_dir.sh
  scripts/create_pycfml_dist_dir.sh
  ```

* Download CFML repository

  ```
  scripts/download_cfml_repo.sh
  ```

* Build CFML modules

  ```
  scripts/rename_global_deps_file.sh
  scripts/build_cfml_modules_obj.sh
  scripts/delete_renamed_global_deps_file.sh
  ```

* Build CFML static library

  ```
  scripts/build_cfml_static_lib.sh
  ```

* Make CFML distribution

  ```
  scripts/move_built_to_cfml_dist.sh
  ```

* Build und run CFML functional test programs

  ```
  scripts/build_cfml_test_programs.sh
  scripts/copy_cfml_test_programs_to_tests_dir.sh
  scripts/run_cfml_functional_tests_no_benchmarks.sh
  ```

* Create pyCFML source code

  ```
  scripts/create_pycfml_src.sh
  ```

* Build pyCFML modules

  ```
  scripts/build_pycfml_modules_obj.sh
  ```

* Build pyCFML shared obj / dynamic library

  ```
  scripts/build_pycfml_lib_obj.sh
  scripts/build_pycfml_shared_obj_or_dynamic_lib.sh
  ```

* Make pyCFML distribution

  ```
  scripts/copy_built_to_pycfml_dist.sh
  scripts/change_runpath_for_built_pycfml.sh
  scripts/copy_extra_libs_to_pycfml_dist.sh
  scripts/copy_py_api_files_to_pycfml_dist.sh
  scripts/copy_init_file_to_pycfml_dist.sh
  scripts/copy_cfml_databases_to_pycfml_dist.sh
  ```

* Create Python package wheel of pyCFML

  ```
  scripts/validate_pyproject_toml.sh
  scripts/create_pycfml_python_wheel.sh
  scripts/rename_pycfml_python_wheel.sh
  ```

* Install pyCFML from Python package wheel (with dev extras)

  ```
  scripts/install_pycfml_from_wheel.sh
  ```

* Run pyCFML unit tests

  ```
  scripts/run_pycfml_unit_tests.sh
  ```

* Run pyCFML functional tests

  ```
  scripts/run_pycfml_functional_tests_no_benchmarks.sh
  ```

## How to use

### Compute the powder diffraction pattern

Here is the simplest example of using pycrysfml to calculate a powder diffraction pattern from a Python dictionary, which contains a description of the crystallographic phase as well as parameters related to the instrument and experiment. 

```
from pycrysfml import cfml_utilities

EXAMPLE = {
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

if __name__ == '__main__':
    x, y = cfml_utilities.powder_pattern_from_json(EXAMPLE)

```

More features will be added as the project develops.


