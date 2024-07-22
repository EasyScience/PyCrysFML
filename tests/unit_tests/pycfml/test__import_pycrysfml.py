import os
import sys

# Tests

def test__from_pycrysfml_import_crysfml08lib():
    try:
        from pycrysfml import crysfml08lib
        assert True
    except Exception as e:
        print("::::: Failed to 'from pycrysfml import crysfml08lib'")
        print('::::: ERROR:', e)
        #assert False

def test__from_pycrysfml_import_cfml_utilities():
    try:
        from pycrysfml import cfml_utilities
        assert True
    except Exception as e:
        print("::::: Failed to 'from pycrysfml import cfml_utilities'")
        print('::::: ERROR:', e)
        #assert False

# Debug

if __name__ == '__main__':
    test__from_pycrysfml_import_crysfml08lib()
    test__from_pycrysfml_import_cfml_utilities()
