import importlib.metadata
import os
import platform
import sys


# Set package version
__version__ = importlib.metadata.version("pycrysfml")

# Add current path to system path
sys.path.append(os.path.dirname(__file__))

# Set environment variable CRYSFML_DB to be the path to the Databases directory
os.environ['CRYSFML_DB'] = os.path.join(os.path.dirname(__file__), 'Databases')

# Fix path to Python
if platform.system() == 'Darwin':  # macOS
    import sysconfig
    python_tag = sysconfig.get_config_var('py_version_short')
    old_path = f'/Library/Frameworks/Python.framework/Versions/{python_tag}/Python'
    new_path = f'`python3-config --prefix`/Python'
    if old_path != new_path:
        import subprocess
        lib_name = 'crysfml08lib.so'
        lib_path = os.path.join(os.path.dirname(__file__), lib_name)
        cmd = f'otool -L {lib_path}'
        p = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        result = p.stdout
        if old_path in result:
            cmd = f'install_name_tool -change {old_path} {new_path} {lib_path}'
            p = subprocess.run(cmd, shell=True, text=True, capture_output=True)
            #result = p.stdout
            #print(result)
            #cmd = f'otool -L {lib_path}'
            #p = subprocess.run(cmd, shell=True, text=True, capture_output=True)
            #result = p.stdout
            #print(result)
