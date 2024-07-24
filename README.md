This is a repository for creating a python library **pycrysfml** based on the new automatically generated Python API for the crystallographic library CrysFML2008 (Fortran 2008) from https://code.ill.fr/scientific-software/CrysFML2008.

### Build and test jobs

| Platform / Compiler       | gfortran | ifx         | ifort         | nagfor     |
| ------------------------- | -------- | ----------- | ------------- | ---------- |
| Windows 10                | ✅       | ❌1        | ✅           | ⚙️ Testing |
| Ubuntu 22.04              | ✅       | ✅          | ✅           | ⚙️ Testing | 
| macOS 12 (Intel)          | ✅       | Unsupported | ❌2         | ⚙️ Testing |
| macOS 14 (Apple Silicone) | ✅       | Unsupported | Unsupported   | ⚙️ Testing |

* ❌1 Failed at the _:::::: Running unit tests from 'tests/functional_tests/pyCFML'_ step (tests job):

```
tests\functional_tests\pyCFML\cfml_utilities\powder_pattern_from_json\test__powder_pattern_from_json.py . [ 33%]
Windows fatal exception: access violation

Current thread 0x0000068c (most recent call first):

...

scripts/run_pycfml_functional_tests_no_benchmarks.sh: line 2:  1359 Segmentation fault
```
* ❌2 Failed at the _:::::: Building fortran shared obj or dynamic lib 'crysfml08lib.so'_ step (build job):

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

### Local build

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
  python scripts.py --help
  ```

* Create job scripts with default options

  ```
  python scripts.py
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
