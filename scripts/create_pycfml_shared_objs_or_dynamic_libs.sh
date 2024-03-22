echo "- Entering build dir 'pycrysfml08_build'"
cd /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/pycrysfml08_build
echo "- Building fortran shared objs or dynamic libs for PyCrysFML08:"
echo "  [ 20%] py_cfml_metrics.o"
nagfor -Wl,-shared py_cfml_metrics.o -o py_cfml_metrics.so -L/Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/lib -lCrysFML08 `python3-config --ldflags --embed`
echo "  [ 40%] py_cfml_profiles.o"
nagfor -Wl,-shared py_cfml_profiles.o -o py_cfml_profiles.so -L/Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/lib -lCrysFML08 `python3-config --ldflags --embed`
echo "  [ 60%] py_cfml_sxtal_geom.o"
nagfor -Wl,-shared py_cfml_sxtal_geom.o -o py_cfml_sxtal_geom.so -L/Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/lib -lCrysFML08 `python3-config --ldflags --embed`
echo "  [ 80%] powder_mod.o"
nagfor -Wl,-shared powder_mod.o -o powder_mod.so -L/Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/lib -lCrysFML08 `python3-config --ldflags --embed`
echo "  [100%] powder_mod_2.o"
nagfor -Wl,-shared powder_mod_2.o -o powder_mod_2.so -L/Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_dist/lib -lCrysFML08 `python3-config --ldflags --embed`
echo "- Exiting build dir 'pycrysfml08_build'"
cd /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML
