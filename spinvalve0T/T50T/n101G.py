# Magnetism example
# =================
#
# Magnetic structures can be anchored to the layer boundaries.
#
# Defining a magnetic model starts as usual.

from refl1d.names import *
from refl1d.probe import *

# We still need the nuclear structure, so define the materials.

LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)

# The materials are stacked as usual, but the layers with magnetism have
# an additional magnetism property specified.  This example use
# :class:`refl1d.magnetism.Magnetism` to define a flat magnetic layer with
# the given magnetic scattering length density *rhoM* and angle *thetaM*.
#
# The magnetism is anchored to the corresponding nuclear layer, and by
# default will have the same thickness and interface.   The magnetic interface
# can be shifted relative to the nuclear interface using *dead_below* and
# *dead_above*.  These can be negative, allowing the magnetism to extend
# beyond the nuclear layer.  The magnetic interface can also be varied
# independently by using *interface_above* and *interface_below* as in the
# example below.   Note that interface_below is ignored # in consecutive
# layers, much like the nuclear layers, for which the interface attribute
# indicates the interface above.  Using *extent=2*, the single magnetism
# definition can extend over two consecutive layers.
#
# The :class:`refl1d.magnetism.MagnetismTwist` allows you to define a magnetic
# layer whose values of theta and rho change linearly throughout the layer.
# There are additional magnetism types defined in :mod:`reflid.magnetism`.
# Note that the current definition of interface only transitions smoothly
# into and out of layers with constant magnetism.  This behaviour may change
# in newer releases.


Ftriple5Model = (STO (0, 1.5) 
                | LSMO (35.8999763551114, 0.991517161690633, magnetism=Magnetism(rhoM=1.19999935448565, thetaM=250)) | LNO(12.0976456838363, 0.999999082416319, magnetism=Magnetism(rhoM=0.35988727920024, thetaM=270)) 
                | LSMO (35.8999607635805, 0.999175920489308, magnetism=Magnetism(rhoM=1.19928447620729, thetaM=290)) | LNO(10.916900291373, 0.9997978369314, magnetism=Magnetism(rhoM=0.359995735700992, thetaM=270)) 
                | LSMO (35.8999102407187, 0.998563478223095, magnetism=Magnetism(rhoM=0.800047645372031, thetaM=250)) | LNO(10.9034319621133, 0.999656470600024, magnetism=Magnetism(rhoM=0.24016458987736, thetaM=270)) 
                | LSMO (35.8999962256821, 0.999868959773099, magnetism=Magnetism(rhoM=0.800438263427779, thetaM=290)) | LNO(10.9000804415887, 0.999839264340448, magnetism=Magnetism(rhoM=0.240104189851583, thetaM=270)) 
                | LSMO (35.8996855141303, 0.999919864658957, magnetism=Magnetism(rhoM=0.800261975838851, thetaM=250)) | LNO(10.9009823787915, 0.983972211557809, magnetism=Magnetism(rhoM=0.240000502704399, thetaM=270)) 
                | LSMO (35.8991583571373, 0.999906373186372, magnetism=Magnetism(rhoM=0.800000001495303, thetaM=290)) | LNO(3.65011617632097, 0.0945551225911317, magnetism=Magnetism(rhoM=0.240006446619767, thetaM=270)) 
                | LSMO (35.8990924710759, 0.999910204777874, magnetism=Magnetism(rhoM=0.800237079690324, thetaM=250)) | LNO(3.6515114081102, 0.999649877824892, magnetism=Magnetism(rhoM=0.240359082467019, thetaM=270)) 
                | LSMO (35.8980801338978, 0.999505157651077, magnetism=Magnetism(rhoM=0.800027783748864, thetaM=290)) | LNO(3.65027014866513, 0.997330674718383, magnetism=Magnetism(rhoM=0.240387492054324, thetaM=270)) 
                | LSMO (35.8995336479275, 0.990857273516943, magnetism=Magnetism(rhoM=0.800207063285033, thetaM=250)) | LNO(3.65002581675318, 0.97616260722089, magnetism=Magnetism(rhoM=0.240629521588475, thetaM=270)) 
                | LSMO (35.8998166208382, 0.167715882298592, magnetism=Magnetism(rhoM=0.800045205257954, thetaM=290)) | LNO(3.65186218808489, 0.995629872663096, magnetism=Magnetism(rhoM=0.240007333171385, thetaM=270)) 
                | LSMO (35.8997151614967, 0.999967444794469, magnetism=Magnetism(rhoM=0.800040558631474, thetaM=250)) | LNO(12.0954114128222, 0.999140742454424, magnetism=Magnetism(rhoM=0.240007682731784, thetaM=270)) 
                | LSMO (35.8994921298259, 0.996701647340918, magnetism=Magnetism(rhoM=0.800163252980095, thetaM=290)) | LNO(12.0999329014014, 0.999524722222122, magnetism=Magnetism(rhoM=0.240459978602768, thetaM=270)) 
                | LSMO (35.893521539501, 0.999602204637915, magnetism=Magnetism(rhoM=0.800144206991338, thetaM=250)) | LNO(12.0999195693942, 0.980382300305929, magnetism=Magnetism(rhoM=0.240051473205527, thetaM=270)) 
                | LSMO (35.8968441132639, 0.992620056061417, magnetism=Magnetism(rhoM=0.800027329735383, thetaM=290)) | LNO(12.0999770976278, 0.991720118175803, magnetism=Magnetism(rhoM=0.24013067318334, thetaM=270)) 
                | LSMO (35.8991979583523, 0.997051441367232, magnetism=Magnetism(rhoM=0.800011562986436, thetaM=250)) | LNO(12.0999770976278, 0.991720118175803, magnetism=Magnetism(rhoM=0.24013067318334, thetaM=270)) 
                | air)


# Define the fittable parameters as usual, including the magnetism attributes.

x = 1
while x < 31:
    
    #Ftriple5Model[x].thickness.pmp(5)
    #Ftriple5Model[x].interface.range(0,1)
    Ftriple5Model[x].magnetism.rhoM.pmp(20)
    Ftriple5Model[x].magnetism.thetaM.range(220, 320)
    x += 1

# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["n101Gc1.reflA", None, "n101Gc1.reflC", "n101Gc1.reflD"])

# We are going to compare the calculated reflectivity given two different
# step sizes on the profile.  Steps of *dz=0.3* are good enough for this
# example in that finer steps will not significantly change :math:`\chi^2`
# Steps of *dz=2* however are significantly different.  You can see the
# difference by looking at the spin asymmetry curves for the model rendered
# with *dz=2* and *dz=0.3* as we do below.  The reflectivity calculation time
# scales linearly with the step size, so you may want to use a large step
# size for your initial fits and a smaller step size later.  The *dA* parameter
# ought to give the best of both worlds, using a finer step size where the
# profile is changing quickly and coarser step size elsewhere, but it is
# currently broken and disabled below.

experiment = Experiment(probe=probe, sample=Ftriple5Model, dz=0.3, dA=None)
problem = FitProblem(experiment)
