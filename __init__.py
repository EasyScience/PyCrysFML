import os
import sys


CURRENT_PATH = os.path.dirname(__file__)


# Add current path to system path
sys.path.append(CURRENT_PATH)

# Set en variable CRYSFML_DB to be the path to the Databases directory
os.environ['CRYSFML_DB'] = os.path.join(CURRENT_PATH, 'Databases')
