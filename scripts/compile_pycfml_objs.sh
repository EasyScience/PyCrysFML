echo "- Entering build dir 'pycrysfml08_build'"
cd /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/pycrysfml08_build
echo "- Building fortran objects for PyCrysFML08:"
echo "  [ 20%] py_cfml_metrics.F90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/pycrysfml08_repo/src/py_cfml_metrics.F90 -I /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/include
echo "  [ 40%] py_cfml_profiles.F90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/pycrysfml08_repo/src/py_cfml_profiles.F90 -I /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/include
echo "  [ 60%] py_cfml_sxtal_geom.F90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/pycrysfml08_repo/src/py_cfml_sxtal_geom.F90 -I /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/include
echo "  [ 80%] powder_mod.F90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/pycrysfml08_repo/src/powder_mod.F90 -I /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/include
echo "  [100%] powder_mod_2.F90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/pycrysfml08_repo/src/powder_mod_2.F90 -I /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/include
echo "- Exiting build dir 'pycrysfml08_build'"
cd /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML
