'''
 Non-Magnetic fitting for Triple 5 superlattice measure on Platypus in 1T field
Program: Refl1D Program

Version 0.1
Author Jackson Wong

Notes: This program doesn't account for any magnetic fitting.
Theoretically the 1T field will suppress any magnetic effects therefore only observing structure.
RhoM is fitted here but the canting is not.
'''

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
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2) 
                | air)

'''
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)
, magnetism=Magnetism(rhoM=0.3, thetaM=270)

# Define the fittable parameters as usual, including the magnetism attributes.

x = 1

while x < 30:
    Ftriple5Model[x].thickness.pmp(5)
    Ftriple5Model[x].interface.range(0,1)
    Ftriple5Model[x].magnetism.rhoM.pmp(20)
    
    x += 1
'''
x = 1

while x < 31:
    Ftriple5Model[x].thickness.pmp(5)
    Ftriple5Model[x].interface.range(0,1)
    x += 1

y = 1

while y < 31:
    Ftriple5Model[y].magnetism.rhoM.pmp(20)
    
    y += 2
# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["n101Gc1.reflA", None, None, "n101Gc1.reflD"])


experiment = Experiment(probe=probe, sample=Ftriple5Model, dz=0.3, dA=None)
problem = FitProblem(experiment)
