[![](http://github-actions.40ants.com/AndrewSazonov/TEST_PyCrysFML/matrix.svg)](https://github.com/AndrewSazonov/TEST_PyCrysFML/actions)

This is a repository for testing the build process of both the fortran crystallographic library [CrysFML2008](https://code.ill.fr/rodriguez-carvajal/CrysFML2008) and its python interface [PyCrysFML08](https://code.ill.fr/scientific-software/PyCrysFML08).

### Build matrix

| Platform / Compiler       | gfortran | ifx | ifort | nagfor |
| ------------------------- | -------- | --- | ----- | ------ |
| Windows                   | +        | +   | +     |        |
| Ubuntu 22.04              | +        | +   | +     |        |
| macOS 12 (Intel)          | +        | N/A | +     |        |
| macOS 14 (Apple Silicone) | +        | N/A | N/A   | LOCAL  |



### Main steps

* Download the [CrysFML2008](https://code.ill.fr/rodriguez-carvajal/CrysFML2008) project (`nagfor` branch).
* Build the CrysFML2008 static library with the `gfortran`, `ifort/ifx` or `nagfor` fortran compiler.
* Build and run CrysFML2008 functional test programs.
* Download the [PyCrysFML08](https://code.ill.fr/scientific-software/PyCrysFML08) project (`master` branch).
* Build selected PyCrysFML08 modules with the `gfortran`, `ifort/ifx` or `nagfor` fortran compiler.
* Create the PyCrysFML08 python package and install PyCrysFML08 from it.
* Run the PyCrysFML08 unit tests.
* Run `powder_mod` from PyCrysFML08 to generate the powder diffraction pattern.

More details are in the [CI script](.github/workflows/main.yml).

### To run locally

* Create and activate a python environment (_optional_)

  ```
  $ python3.11 -m venv .venv
  $ source .venv/bin/activate 
  ```

* Upgrade the package installer for Python (_optional_)

  ```
  $ python -m pip install --upgrade pip
  ```
  
* Install Python dependences, including extras

  ```
  $ python -m pip install '.[ci,test]'
  ```

* Print possible options for creating job scripts (_optional_)

  ```
  $ python scripts.py --help 
  ```

* Create job scripts with default options

  ```
  $ python scripts.py
  ```

* Print some build-specific variables (_optional_)

  ```
  $ scripts/print_build_variables.sh
  ```

* Run all scripts in sequence

  ```
  $ scripts/main_script.sh
  ```
  
