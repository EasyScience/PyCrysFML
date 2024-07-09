[![](http://github-actions.40ants.com/AndrewSazonov/TEST_PyCrysFML/matrix.svg)](https://github.com/AndrewSazonov/TEST_PyCrysFML/actions)

This is a repository for testing the build process of both the fortran crystallographic library [CrysFML2008](https://code.ill.fr/rodriguez-carvajal/CrysFML2008) and its python interface [PyCrysFML08](https://code.ill.fr/scientific-software/PyCrysFML08).

### Main steps

* Download the [CrysFML2008](https://code.ill.fr/rodriguez-carvajal/CrysFML2008) project (`nagfor` branch).
* Build the CrysFML2008 static library with the `gfortran`, `ifort/ifx` or `nagfor` fortran compiler.
* Build and run CrysFML2008 functional test programs.
* Download the [PyCrysFML08](https://code.ill.fr/scientific-software/PyCrysFML08) project (`master` branch).
* Build selected PyCrysFML08 modules with the `gfortran`, `ifort/ifx` or `nagfor` fortran compiler.
* Create the PyCrysFML08 python package and install PyCrysFML08 from it.
* Run the PyCrysFML08 unit tests.
* Run `powder_mod` form PyCrysFML08 to generate the powder diffraction pattern.

More details are in the [CI script](.github/workflows/main.yml).

### To run locally

* Create and activate a python environment (optional)

  ```
  $ python3.11 -m venv .venv
  $ source .venv/bin/activate 
  ```

* Upgrade the package installer for Python (optional)

  ```
  $ python -m pip install --upgrade pip
  ```
  
* Install Python dependences, including extras

  ```
  $ python -m pip install '.[ci,test]'
  ```

* Print possible options for creating job scripts

  ```
  $ python scripts.py --help 
  ```

* Create job scripts with default options

  ```
  $ python scripts.py
  ```

* Run all scripts in sequence

  ```
  $ scripts/main_script.sh
  ```
  
