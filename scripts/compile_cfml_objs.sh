echo "- Entering build dir 'crysfml08_build'"
cd /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_build
echo "- Building fortran objects for CrysFML2008:"
echo "  [  0%] Forpy.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/Forpy.f90
echo "  [  1%] CFML_Degree_Trigonometric.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Degree_Trigonometric.f90
echo "  [  1%] CFML_GlobalDeps_MacOS_GFOR.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_GlobalDeps_MacOS_GFOR.f90
echo "  [  1%] CFML_FFT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_FFT.f90
echo "  [  1%] FFT_Gen.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_FFT/FFT_Gen.f90
echo "  [  2%] FFT_Convol.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_FFT/FFT_Convol.f90
echo "  [  2%] CFML_Maths.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths.f90
echo "  [  2%] Math_Diagonalize_GEN.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Diagonalize_GEN.f90
echo "  [  2%] Math_Equal_Vector.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Equal_Vector.f90
echo "  [  3%] Math_Determinant.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Determinant.f90
echo "  [  3%] Math_Co_Prime.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Co_Prime.f90
echo "  [  3%] Math_Cross_Product.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Cross_Product.f90
echo "  [  4%] Math_Debye.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Debye.f90
echo "  [  4%] Math_Co_Linear.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Co_Linear.f90
echo "  [  4%] Math_Erfc_Der.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Erfc_Der.f90
echo "  [  4%] Math_Diagonalize_SH.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Diagonalize_SH.f90
echo "  [  5%] Math_Factorial.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Factorial.f90
echo "  [  5%] Math_Equal_Matrix.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Equal_Matrix.f90
echo "  [  5%] Math_Inverse_Matrix.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Inverse_Matrix.f90
echo "  [  5%] Math_Is_Diagonal_Matrix.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Is_Diagonal_Matrix.f90
echo "  [  6%] Math_Equal_Vector.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Equal_Vector.f90
echo "  [  6%] Math_Determinant.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Determinant.f90
echo "  [  6%] Math_PolynomialFit.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_PolynomialFit.f90
echo "  [  7%] Math_Lower_Triangular.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Lower_Triangular.f90
echo "  [  7%] Math_Is_Null_Vector.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Is_Null_Vector.f90
echo "  [  7%] Math_Norm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Norm.f90
echo "  [  7%] Math_Locate.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Locate.f90
echo "  [  8%] Math_Tensor_Product.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Tensor_Product.f90
echo "  [  8%] Math_Linear_Dependent.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Linear_Dependent.f90
echo "  [  8%] Math_Polyhedron_Volume.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Polyhedron_Volume.f90
echo "  [  8%] Math_Resolv_System.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Resolv_System.f90
echo "  [  9%] Math_SistCoord_Changes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_SistCoord_Changes.f90
echo "  [  9%] Math_Rotation_Axes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Rotation_Axes.f90
echo "  [  9%] Math_Modulo_Lat.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Modulo_Lat.f90
echo "  [ 10%] Math_Negligible.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Negligible.f90
echo "  [ 10%] Math_Trace.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Trace.f90
echo "  [ 10%] Math_Scalar.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Scalar.f90
echo "  [ 10%] Math_Outerprod.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Outerprod.f90
echo "  [ 11%] Math_Smoothing_Interpol.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Smoothing_Interpol.f90
echo "  [ 11%] Math_Zbelong.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Zbelong.f90
echo "  [ 11%] Math_Spher_Harm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Spher_Harm.f90
echo "  [ 11%] Math_Pgcd.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Pgcd.f90
echo "  [ 12%] Math_Mat_Cross.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Mat_Cross.f90
echo "  [ 12%] Math_Poly_Legendre.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Poly_Legendre.f90
echo "  [ 12%] Math_Upper_Triangular.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Upper_Triangular.f90
echo "  [ 12%] Math_Points_In_Line2D.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Points_In_Line2D.f90
echo "  [ 13%] Math_RowEchelon.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_RowEchelon.f90
echo "  [ 13%] Math_Swap.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Swap.f90
echo "  [ 13%] Math_Rank.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Rank.f90
echo "  [ 14%] Math_Sort.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maths/Math_Sort.f90
echo "  [ 14%] CFML_ExtinCorr.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_ExtinCorr.f90
echo "  [ 14%] Ext_BeckerCoppens.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_ExtinCorr/Ext_BeckerCoppens.f90
echo "  [ 14%] Ext_FlippingRatios.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_ExtinCorr/Ext_FlippingRatios.f90
echo "  [ 15%] Ext_ShelxCorr.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_ExtinCorr/Ext_ShelxCorr.f90
echo "  [ 15%] CFML_Random.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random.f90
echo "  [ 15%] Random_Beta_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_Beta_Sm.f90
echo "  [ 15%] Random_Binomial_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_Binomial_Sm.f90
echo "  [ 16%] Random_VonMises_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_VonMises_Sm.f90
echo "  [ 16%] Random_InvGauss_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_InvGauss_Sm.f90
echo "  [ 16%] Random_Poisson_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_Poisson_Sm.f90
echo "  [ 17%] Random_Gamma_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_Gamma_Sm.f90
echo "  [ 17%] Random_Normal_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_Normal_Sm.f90
echo "  [ 17%] Random_Cauchy_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_Cauchy_Sm.f90
echo "  [ 17%] Random_T_Sm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Random/Random_T_Sm.f90
echo "  [ 18%] CFML_Messages.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Messages.f90
echo "  [ 18%] Con_Print_Message.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Messages/Con_Print_Message.f90
echo "  [ 18%] Con_Info_Message.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Messages/Con_Info_Message.f90
echo "  [ 18%] Con_Err_Message.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Messages/Con_Err_Message.f90
echo "  [ 19%] Con_Write_ScrollMsg.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Messages/Con_Write_ScrollMsg.f90
echo "  [ 19%] Con_Wait_Message.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Messages/Con_Wait_Message.f90
echo "  [ 19%] CFML_Strings.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Strings.f90
echo "  [ 20%] StringFullp.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Strings/StringFullp.f90
echo "  [ 20%] StringNum.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Strings/StringNum.f90
echo "  [ 20%] StringReadKey.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Strings/StringReadKey.f90
echo "  [ 20%] StringTools.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Strings/StringTools.f90
echo "  [ 21%] CFML_Rational.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational.f90
echo "  [ 21%] RAT_constructor.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_constructor.f90
echo "  [ 21%] RAT_generic.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_generic.f90
echo "  [ 21%] RAT_is_integer.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_is_integer.f90
echo "  [ 22%] RAT_assignment.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_assignment.f90
echo "  [ 22%] RAT_operator_add.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_add.f90
echo "  [ 22%] RAT_operator_eq.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_eq.f90
echo "  [ 23%] RAT_operator_ge.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_ge.f90
echo "  [ 23%] RAT_Equal_rational.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_Equal_rational.f90
echo "  [ 23%] RAT_operator_divisor.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_divisor.f90
echo "  [ 23%] RAT_operator_gt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_gt.f90
echo "  [ 24%] RAT_operator_le.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_le.f90
echo "  [ 24%] RAT_operator_minus.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_minus.f90
echo "  [ 24%] RAT_rowechelon.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_rowechelon.f90
echo "  [ 24%] RAT_operator_lt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_lt.f90
echo "  [ 25%] RAT_overloads.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_overloads.f90
echo "  [ 25%] RAT_operator_multiply.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_multiply.f90
echo "  [ 25%] RAT_operator_neq.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Rational/RAT_operator_neq.f90
echo "  [ 26%] CFML_SuperSpace_Database.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SuperSpace_Database.f90
echo "  [ 26%] CFML_Magnetic_Database.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Magnetic_Database.f90
echo "  [ 26%] CFML_BVS_Tables.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_BVS_Tables.f90
echo "  [ 26%] CFML_Scattering_Tables.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Scattering_Tables.f90
echo "  [ 27%] CFML_Bonds_Tables.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Bonds_Tables.f90
echo "  [ 27%] CFML_Symmetry_Tables.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Symmetry_Tables.f90
echo "  [ 27%] Tab_Del_BVST.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Del_BVST.f90
echo "  [ 27%] Tab_Set_BVST.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Set_BVST.f90
echo "  [ 28%] Tab_Set_ScatterT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Set_ScatterT.f90
echo "  [ 28%] Tab_Get_ScatterT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Get_ScatterT.f90
echo "  [ 28%] Tab_Del_ScatterT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Del_ScatterT.f90
echo "  [ 29%] Tab_Get_SpgT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Get_SpgT.f90
echo "  [ 29%] Tab_Del_SpgT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Del_SpgT.f90
echo "  [ 29%] Tab_Set_SpgT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Set_SpgT.f90
echo "  [ 29%] Tab_Get_SpgSymbols.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Get_SpgSymbols.f90
echo "  [ 30%] Tab_Get_BondsT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Get_BondsT.f90
echo "  [ 30%] Tab_Del_BondsT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Del_BondsT.f90
echo "  [ 30%] Tab_Set_BondsT.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Set_BondsT.f90
echo "  [ 30%] Tab_Allocating_SuperSpaceDBase.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Allocating_SuperSpaceDBase.f90
echo "  [ 31%] Tab_Read_SSG_DBase.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Read_SSG_DBase.f90
echo "  [ 31%] Tab_Allocating_MagneticDBase.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Allocating_MagneticDBase.f90
echo "  [ 31%] Tab_Read_MagneticDBase.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Tables/Tab_Read_MagneticDBase.f90
echo "  [ 32%] CFML_Profiles.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles.f90
echo "  [ 32%] Profile_BacktoBack.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_BacktoBack.f90
echo "  [ 32%] Profile_Exponential.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_Exponential.f90
echo "  [ 32%] Profile_Finger.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_Finger.f90
echo "  [ 33%] Profile_Gaussian.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_Gaussian.f90
echo "  [ 33%] Profile_Init_ProfVal.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_Init_ProfVal.f90
echo "  [ 33%] Profile_IkedaCarpenter.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_IkedaCarpenter.f90
echo "  [ 33%] Profile_TCHpVoigt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_TCHpVoigt.f90
echo "  [ 34%] Profile_Hat.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_Hat.f90
echo "  [ 34%] Profile_PseudoVoigt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_PseudoVoigt.f90
echo "  [ 34%] Profile_Lorentzian.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_Lorentzian.f90
echo "  [ 35%] Profile_TOF_Jorgensen.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_TOF_Jorgensen.f90
echo "  [ 35%] Profile_TOF_Jorg_Vondreele.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_TOF_Jorg_Vondreele.f90
echo "  [ 35%] Profile_TOF_Carpenter.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Profiles/Profile_TOF_Carpenter.f90
echo "  [ 35%] CFML_Optimization_LSQ.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_LSQ.f90
echo "  [ 36%] OPT_LSQ_LevebergMarquardt_AnalyDer.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_LSQ/OPT_LSQ_LevebergMarquardt_AnalyDer.f90
echo "  [ 36%] OPT_LSQ_Marquardt_Fit.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_LSQ/OPT_LSQ_Marquardt_Fit.f90
echo "  [ 36%] OPT_LSQ_Output.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_LSQ/OPT_LSQ_Output.f90
echo "  [ 36%] OPT_LSQ_LevebergMarquardt_NumDer.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_LSQ/OPT_LSQ_LevebergMarquardt_NumDer.f90
echo "  [ 37%] CFML_Optimization.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization.f90
echo "  [ 37%] OPT_Global_Csendes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization/OPT_Global_Csendes.f90
echo "  [ 37%] OPT_Cg_Quasi_Newton.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization/OPT_Cg_Quasi_Newton.f90
echo "  [ 38%] OPT_Local_Optim.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization/OPT_Local_Optim.f90
echo "  [ 38%] OPT_Simplex.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization/OPT_Simplex.f90
echo "  [ 38%] CFML_Simulated_Annealing.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Simulated_Annealing.f90
echo "  [ 38%] CFML_Diffpatt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Diffpatt.f90
echo "  [ 39%] DiffP_ReadPatt_ILL.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_ILL.f90
echo "  [ 39%] DiffP_ReadPatt_CIF.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_CIF.f90
echo "  [ 39%] DiffP_FWHM_Peak.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_FWHM_Peak.f90
echo "  [ 39%] DiffP_BackgPatt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_BackgPatt.f90
echo "  [ 40%] DiffP_ReadPatt_LLB.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_LLB.f90
echo "  [ 40%] DiffP_NoisyPoints.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_NoisyPoints.f90
echo "  [ 40%] DiffP_ReadPatt_GSAS.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_GSAS.f90
echo "  [ 40%] DiffP_ReadPatt_ISIS.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_ISIS.f90
echo "  [ 41%] DiffP_ReadPatt_NLS.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_NLS.f90
echo "  [ 41%] DiffP_ReadPatt_PAN.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_PAN.f90
echo "  [ 41%] DiffP_ReadPatt_FREE.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_FREE.f90
echo "  [ 42%] DiffP_ReadPatt_PSI.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_PSI.f90
echo "  [ 42%] DiffP_ReadPatt_Socabim.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_Socabim.f90
echo "  [ 42%] DiffP_ReadPatt_TimeVar.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_TimeVar.f90
echo "  [ 42%] DiffP_ReadPatt_XYSIG.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatt_XYSIG.f90
echo "  [ 43%] DiffP_WritePatterns.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_WritePatterns.f90
echo "  [ 43%] DiffP_ReadPatterns.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_DiffPatt/DiffP_ReadPatterns.f90
echo "  [ 43%] CFML_Metrics.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Metrics.f90
echo "  [ 43%] Metrics_Tensor.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Metrics/Metrics_Tensor.f90
echo "  [ 44%] Metrics_Gen.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Metrics/Metrics_Gen.f90
echo "  [ 44%] Metrics_ThConver.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Metrics/Metrics_ThConver.f90
echo "  [ 44%] Metrics_IO.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Metrics/Metrics_IO.f90
echo "  [ 45%] Metrics_NiggliCell.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Metrics/Metrics_NiggliCell.f90
echo "  [ 45%] SAnn_General.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_SAnn/SAnn_General.f90
echo "  [ 45%] SAnn_LocalOpt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_SAnn/SAnn_LocalOpt.f90
echo "  [ 45%] SAnn_MultiConf.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_SAnn/SAnn_MultiConf.f90
echo "  [ 46%] SAnn_SetnCheck.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_SAnn/SAnn_SetnCheck.f90
echo "  [ 46%] SAnn_inout.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Optimization_SAnn/SAnn_inout.f90
echo "  [ 46%] CFML_EoS.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS.f90
echo "  [ 46%] EoS_Calc.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_Calc.f90
echo "  [ 47%] EoS_CopyEDat.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_CopyEDat.f90
echo "  [ 47%] EoS_Get_APL.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_Get_APL.f90
echo "  [ 47%] EoS_Get_HeatCap.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_Get_HeatCap.f90
echo "  [ 48%] EoS_CellPar.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_CellPar.f90
echo "  [ 48%] EoS_PrincipalEoS.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_PrincipalEoS.f90
echo "  [ 48%] Eos_Allocate.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Allocate.f90
echo "  [ 48%] EoS_Transform_ESD.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_Transform_ESD.f90
echo "  [ 49%] EoS_ModDir.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_ModDir.f90
echo "  [ 49%] Eos_DerivPartial.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_DerivPartial.f90
echo "  [ 49%] EoS_Get_Tensor.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_Get_Tensor.f90
echo "  [ 49%] Eos_Get_Bulk.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Get_Bulk.f90
echo "  [ 50%] Eos_Checks.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Checks.f90
echo "  [ 50%] EoS_Get_Angle.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_Get_Angle.f90
echo "  [ 50%] Eos_AlphaCalc.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_AlphaCalc.f90
echo "  [ 51%] Eos_Conlev.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Conlev.f90
echo "  [ 51%] Eos_FfCalc.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_FfCalc.f90
echo "  [ 51%] EoS_LinEoS_Allowed.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/EoS_LinEoS_Allowed.f90
echo "  [ 51%] Eos_Get_Pressure.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Get_Pressure.f90
echo "  [ 52%] Eos_Get_Temperature.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Get_Temperature.f90
echo "  [ 52%] Eos_Get_Tait.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Get_Tait.f90
echo "  [ 52%] Eos_Gruneisen.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Gruneisen.f90
echo "  [ 52%] Eos_NormPressure.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_NormPressure.f90
echo "  [ 53%] Eos_Set.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Set.f90
echo "  [ 53%] Eos_Get_Properties.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Get_Properties.f90
echo "  [ 53%] Eos_Read.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Read.f90
echo "  [ 54%] Eos_Get_Volume.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Get_Volume.f90
echo "  [ 54%] Eos_PVT_Table.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_PVT_Table.f90
echo "  [ 54%] Eos_Get_Transition.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Get_Transition.f90
echo "  [ 54%] Eos_Init.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Init.f90
echo "  [ 55%] Eos_K_Cal.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_K_Cal.f90
echo "  [ 55%] Eos_Pthermal.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Pthermal.f90
echo "  [ 55%] Eos_Strain.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Strain.f90
echo "  [ 55%] Eos_Write.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_Write.f90
echo "  [ 56%] Eos_dKdTCalc.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EoS/Eos_dKdTCalc.f90
echo "  [ 56%] CFML_gSpaceGroups.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups.f90
echo "  [ 56%] gS_Allocate_Opers.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Allocate_Opers.f90
echo "  [ 57%] gS_Allocate_SpaceG.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Allocate_SpaceG.f90
echo "  [ 57%] gS_ApplySO.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_ApplySO.f90
echo "  [ 57%] gS_Get_Cosets.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Cosets.f90
echo "  [ 57%] gS_CheckGener.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_CheckGener.f90
echo "  [ 58%] gS_Get_CrystalSys.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_CrystalSys.f90
echo "  [ 58%] gS_Get_GenerStr.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_GenerStr.f90
echo "  [ 58%] gS_Get_Dimension.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Dimension.f90
echo "  [ 58%] gS_Get_Generators.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Generators.f90
echo "  [ 59%] gS_Get_Hall_Gener.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Hall_Gener.f90
echo "  [ 59%] gS_Get_HM_Standard.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_HM_Standard.f90
echo "  [ 59%] gS_Get_LattType.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_LattType.f90
echo "  [ 60%] gS_Get_OriginShift.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_OriginShift.f90
echo "  [ 60%] gS_Is_LattCentring.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Is_LattCentring.f90
echo "  [ 60%] gS_Get_X_Matrix.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_X_Matrix.f90
echo "  [ 60%] gS_Is_InversionCentre.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Is_InversionCentre.f90
echo "  [ 61%] gS_Get_Oper_Symb.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Oper_Symb.f90
echo "  [ 61%] gS_Reorder_Oper.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Reorder_Oper.f90
echo "  [ 61%] gS_Smallest_IntegralVec.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Smallest_IntegralVec.f90
echo "  [ 61%] gS_Identify_Groups.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Identify_Groups.f90
echo "  [ 62%] gS_Get_Mult_OPTable.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Mult_OPTable.f90
echo "  [ 62%] gS_Get_Orb_Stabilizer_Constr.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Orb_Stabilizer_Constr.f90
echo "  [ 62%] gS_Get_PseudoStdBase.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_PseudoStdBase.f90
echo "  [ 62%] gS_Match_Spg3D.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Match_Spg3D.f90
echo "  [ 63%] gS_Get_Mat_Symb.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Mat_Symb.f90
echo "  [ 63%] gS_Get_Symb_Mat.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Symb_Mat.f90
echo "  [ 63%] gS_Set_SpaceG.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Set_SpaceG.f90
echo "  [ 64%] gS_Inverse_OP.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Inverse_OP.f90
echo "  [ 64%] gS_Get_LauePG.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_LauePG.f90
echo "  [ 64%] gS_Get_SubGrp.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_SubGrp.f90
echo "  [ 64%] gS_Init_Procedures.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Init_Procedures.f90
echo "  [ 65%] gS_Match_Shubnikov_Grp.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Match_Shubnikov_Grp.f90
echo "  [ 65%] gS_Get_Rotations.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Rotations.f90
echo "  [ 65%] gS_Get_Ops_Gener.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Ops_Gener.f90
echo "  [ 65%] gS_Spg_Const_VGen.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Spg_Const_VGen.f90
echo "  [ 66%] gS_Rational_RedTraslation.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Rational_RedTraslation.f90
echo "  [ 66%] gS_Get_Symb_Oper.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Get_Symb_Oper.f90
echo "  [ 66%] gS_operator_equal.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_operator_equal.f90
echo "  [ 67%] gS_Sort_Operator.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Sort_Operator.f90
echo "  [ 67%] gS_operator_mult.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_operator_mult.f90
echo "  [ 67%] gS_Write_SpaceG.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Write_SpaceG.f90
echo "  [ 67%] gS_Is_Antilattice.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Is_Antilattice.f90
echo "  [ 68%] gS_Spg_Const_Str.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Spg_Const_Str.f90
echo "  [ 68%] gS_Symm_Symbols.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_Symm_Symbols.f90
echo "  [ 68%] gS_OnePrimeOp.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_gSpaceGroups/gS_OnePrimeOp.f90
echo "  [ 68%] CFML_BckPeaks.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_BckPeaks.f90
echo "  [ 69%] CFML_ILL_Instrm_Data.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_ILL_Instrm_Data.f90
echo "  [ 69%] CFML_Atoms.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms.f90
echo "  [ 69%] Atm_ExtendList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms/Atm_ExtendList.f90
echo "  [ 70%] Atm_ChangeList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms/Atm_ChangeList.f90
echo "  [ 70%] Atm_Allocating_Atoms.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms/Atm_Allocating_Atoms.f90
echo "  [ 70%] Atm_PointList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms/Atm_PointList.f90
echo "  [ 70%] Atm_RW_Bin_AtmList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms/Atm_RW_Bin_AtmList.f90
echo "  [ 71%] Atm_Write_AtmList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms/Atm_Write_AtmList.f90
echo "  [ 71%] Atm_SymmetryConstraints.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Atoms/Atm_SymmetryConstraints.f90
echo "  [ 71%] CFML_Propagation_Vectors.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Propagation_Vectors.f90
echo "  [ 71%] CFML_Reflections.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections.f90
echo "  [ 72%] Refl_H_Convent.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_H_Convent.f90
echo "  [ 72%] Refl_AsymUnit.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_AsymUnit.f90
echo "  [ 72%] Refl_Generate.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_Generate.f90
echo "  [ 73%] Refl_H_EquivList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_H_EquivList.f90
echo "  [ 73%] Refl_H_Equal.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_H_Equal.f90
echo "  [ 73%] Refl_Conditions.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_Conditions.f90
echo "  [ 73%] Refl_H_Equiv.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_H_Equiv.f90
echo "  [ 74%] Refl_H_S.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_H_S.f90
echo "  [ 74%] Refl_H_Absent.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_H_Absent.f90
echo "  [ 74%] Refl_MaxNum.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_MaxNum.f90
echo "  [ 74%] Refl_Write_List.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_Write_List.f90
echo "  [ 75%] Refl_UnitaryVec.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_UnitaryVec.f90
echo "  [ 75%] Refl_Init_RefList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_Init_RefList.f90
echo "  [ 75%] Refl_H_Mult.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Reflections/Refl_H_Mult.f90
echo "  [ 76%] CFML_Structure_Factors.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Structure_Factors.f90
echo "  [ 76%] SF_AtomicFactors.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Structure_Factors/SF_AtomicFactors.f90
echo "  [ 76%] SF_Calculations.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Structure_Factors/SF_Calculations.f90
echo "  [ 76%] SF_Scattering_Species.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Structure_Factors/SF_Scattering_Species.f90
echo "  [ 77%] SF_Initialize.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Structure_Factors/SF_Initialize.f90
echo "  [ 77%] SF_Write_SF.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Structure_Factors/SF_Write_SF.f90
echo "  [ 77%] SF_Create_Tables.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Structure_Factors/SF_Create_Tables.f90
echo "  [ 77%] CFML_Geom.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Geom.f90
echo "  [ 78%] Geom_Angles.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Geom/Geom_Angles.f90
echo "  [ 78%] Geom_Allocations.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Geom/Geom_Allocations.f90
echo "  [ 78%] Geom_Matrices.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Geom/Geom_Matrices.f90
echo "  [ 79%] Geom_Coordination.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Geom/Geom_Coordination.f90
echo "  [ 79%] Geom_Orbits.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Geom/Geom_Orbits.f90
echo "  [ 79%] Geom_Distances.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Geom/Geom_Distances.f90
echo "  [ 79%] CFML_kvec_Symmetry.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_kvec_Symmetry.f90
echo "  [ 80%] ksym_auxsub.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_kvec_Symmetry/ksym_auxsub.f90
echo "  [ 80%] ksym_init.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_kvec_Symmetry/ksym_init.f90
echo "  [ 80%] ksym_functions.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_kvec_Symmetry/ksym_functions.f90
echo "  [ 80%] ksym_suscept.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_kvec_Symmetry/ksym_suscept.f90
echo "  [ 81%] ksym_read.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_kvec_Symmetry/ksym_read.f90
echo "  [ 81%] ksym_write.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_kvec_Symmetry/ksym_write.f90
echo "  [ 81%] CFML_Maps.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maps.f90
echo "  [ 82%] Maps_Mapping.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maps/Maps_Mapping.f90
echo "  [ 82%] Maps_MarchingCubes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maps/Maps_MarchingCubes.f90
echo "  [ 82%] Maps_Percolation.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Maps/Maps_Percolation.f90
echo "  [ 82%] CFML_Molecules.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules.f90
echo "  [ 83%] Mol_Formula.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_Formula.f90
echo "  [ 83%] Mol_Cartesian_to.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_Cartesian_to.f90
echo "  [ 83%] Mol_Fractional_to.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_Fractional_to.f90
echo "  [ 83%] Mol_IndexList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_IndexList.f90
echo "  [ 84%] Mol_Orientation.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_Orientation.f90
echo "  [ 84%] Mol_Initialize.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_Initialize.f90
echo "  [ 84%] Mol_WriteInfo.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_WriteInfo.f90
echo "  [ 85%] Mol_Spherical_to.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_Spherical_to.f90
echo "  [ 85%] Mol_ReadInfo.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_ReadInfo.f90
echo "  [ 85%] Mol_ZMatrix_to.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_ZMatrix_to.f90
echo "  [ 85%] Mol_to_AtList.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Molecules/Mol_to_AtList.f90
echo "  [ 86%] CFML_Keywords_Code_Parser.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser.f90
echo "  [ 86%] KWC_FillCodes_Gen.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_FillCodes_Gen.f90
echo "  [ 86%] KWC_Allocation.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_Allocation.f90
echo "  [ 86%] KWC_Deletion.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_Deletion.f90
echo "  [ 87%] KWC_WriteRefCodes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_WriteRefCodes.f90
echo "  [ 87%] KWC_FillCodes_MolX.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_FillCodes_MolX.f90
echo "  [ 87%] KWC_FillCodes_FAtm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_FillCodes_FAtm.f90
echo "  [ 88%] KWC_SplitOperations.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_SplitOperations.f90
echo "  [ 88%] KWC_GetConCodes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_GetConCodes.f90
echo "  [ 88%] KWC_VStateToAtomPar.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_VStateToAtomPar.f90
echo "  [ 88%] KWC_ReadCodes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_ReadCodes.f90
echo "  [ 89%] KWC_GetRestrCodes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_GetRestrCodes.f90
echo "  [ 89%] KWC_RefCodes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Keywords_Code_Parser/KWC_RefCodes.f90
echo "  [ 89%] CFML_IOForm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm.f90
echo "  [ 89%] Format_GEN.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm/Format_GEN.f90
echo "  [ 90%] Format_MCIF.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm/Format_MCIF.f90
echo "  [ 90%] Format_Blocks.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm/Format_Blocks.f90
echo "  [ 90%] Format_CIF.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm/Format_CIF.f90
echo "  [ 90%] Format_CFL.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm/Format_CFL.f90
echo "  [ 91%] Format_FST.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm/Format_FST.f90
echo "  [ 91%] Format_SHX.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_IOForm/Format_SHX.f90
echo "  [ 91%] CFML_KeyCodes.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes.f90
echo "  [ 92%] KeyCod_VecRef.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_VecRef.f90
echo "  [ 92%] KeyCod_RGB.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_RGB.f90
echo "  [ 92%] KeyCod_Atm.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_Atm.f90
echo "  [ 92%] KeyCod_Patt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_Patt.f90
echo "  [ 93%] KeyCod_GenPar.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_GenPar.f90
echo "  [ 93%] keyCod_Phas.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/keyCod_Phas.f90
echo "  [ 93%] KeyCod_WriteInfo.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_WriteInfo.f90
echo "  [ 93%] KeyCod_Restraints.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_Restraints.f90
echo "  [ 94%] KeyCod_Molec.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_KeyCodes/KeyCod_Molec.f90
echo "  [ 94%] CFML_Python.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python.f90
echo "  [ 94%] Python_Common.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python/Python_Common.f90
echo "  [ 95%] Python_Atoms.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python/Python_Atoms.f90
echo "  [ 95%] Python_DiffPatt.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python/Python_DiffPatt.f90
echo "  [ 95%] Python_Metrics.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python/Python_Metrics.f90
echo "  [ 95%] Python_Reflections.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python/Python_Reflections.f90
echo "  [ 96%] Python_gSpaceGroups.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python/Python_gSpaceGroups.f90
echo "  [ 96%] Python_Ndarray.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Python/Python_Ndarray.f90
echo "  [ 96%] CFML_VTK.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_VTK.f90
echo "  [ 96%] VTK_Scan_Utils.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_VTK/VTK_Scan_Utils.f90
echo "  [ 97%] CFML_SXTAL_Geom.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SXTAL_Geom.f90
echo "  [ 97%] SXTAL_Angles.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SXTAL_Geom/SXTAL_Angles.f90
echo "  [ 97%] SXTAL_IO.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SXTAL_Geom/SXTAL_IO.f90
echo "  [ 98%] SXTAL_Matx_Zvect.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SXTAL_Geom/SXTAL_Matx_Zvect.f90
echo "  [ 98%] SXTAL_PSD.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SXTAL_Geom/SXTAL_PSD.f90
echo "  [ 98%] SXTAL_FlatCone.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SXTAL_Geom/SXTAL_FlatCone.f90
echo "  [ 98%] SXTAL_UB.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_SXTAL_Geom/SXTAL_UB.f90
echo "  [ 99%] CFML_Export_VTK.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_Export_VTK.f90
echo "  [ 99%] CFML_EnBVS.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EnBVS.f90
echo "  [ 99%] EnBVS_CostF.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EnBVS/EnBVS_CostF.f90
echo "  [ 99%] EnBVS_Energy.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EnBVS/EnBVS_Energy.f90
echo "  [100%] EnBVS_Maps.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EnBVS/EnBVS_Maps.f90
echo "  [100%] EnBVS_SetTab.f90"
nagfor -colour -f2008 -fpp -PIC -quiet -w=all  -c /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML/crysfml08_repo/Src/CFML_EnBVS/EnBVS_SetTab.f90
echo "- Exiting build dir 'crysfml08_build'"
cd /Users/andrewsazonov/Development/github.com/AndrewSazonov/TEST_PyCrysFML
