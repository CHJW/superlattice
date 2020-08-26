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


Nine3Nine1 = (STO (0, 1.5) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1.3, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | air)


# Define the fittable parameters as usual, including the magnetism attributes.

x = 1
while x < 31:
    
    Nine3Nine1[x].thickness.pmp(10)
    Nine3Nine1[x].interface.range(0.5,1.5)
    Nine3Nine1[x].magnetism.rhoM.pmp(20)
    Nine3Nine1[x].magnetism.thetaM.range(220, 320)
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

experiment = Experiment(probe=probe, sample=Nine3Nine1, dz=0.3, dA=None)
problem = FitProblem(experiment)
