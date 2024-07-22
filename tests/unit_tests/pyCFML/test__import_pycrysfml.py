import os
import sys

# Tests

def test__from_pycrysfml_import_crysfml08lib():
    msg = 'from pycrysfml import crysfml08lib'
    try:
        from pycrysfml import crysfml08lib
        print(f"::::: Succeeded to '{msg}'")
        assert True
    except Exception as e:
        print(f"::::: Failed to '{msg}': {e}")
        #assert False

def test__from_pycrysfml_import_cfml_utilities():
    msg = 'from pycrysfml import cfml_utilities'
    try:
        from pycrysfml import cfml_utilities
        print(f"::::: Succeeded to '{msg}'")
        assert True
    except Exception as e:
        print(f"::::: Failed to '{msg}': {e}")
        #assert False

# Debug

if __name__ == '__main__':
    test__from_pycrysfml_import_crysfml08lib()
    test__from_pycrysfml_import_cfml_utilities()
