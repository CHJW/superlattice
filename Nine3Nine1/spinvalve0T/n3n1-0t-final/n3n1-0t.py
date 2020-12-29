'''
 Magnetic fitting for 9-3/9-1 superlattice measure on Platypus in 0T field
Program: Refl1D Program

Version 0.1

Structure values are taken from 0T fitting.
Canting of the magnetic layers are done in this program.
Canting is defined with reference to LNO layer.
ThetaM 270 is set for LNO and LSMO is canted above and below it. 
Based on original paper canting between LSMO layers can go as high as 110 degrees.
Magnetism twist needs to be added to LNO layer, LSMO is presumed uniform.
'''


from refl1d.names import *
from refl1d.probe import *

# Material definition. rho is calculated. May need some fitting.
#LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
#LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
#STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)
LNO = Material(formula='LaNiO3', name = 'LaNiO3', density=7.06209, fitby='bulk_density')
LSMO = Material(formula='LaSrMnO3', name = 'LaSrMnO3', density=6.58148, fitby='bulk_density')
STO = Material(formula='SrTiO3', name = 'SrTiO3', density=5.11, fitby='bulk_density')

#Need to add magnetic twist to LNO layers


Nine3Nine1 = (STO (0,5.89162) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(4.52885, 1.89032, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(4.52885, 1.89032, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(4.52885, 1.89032, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(4.52885, 1.89032, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(4.52885, 1.89032, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(4.52885, 1.89032, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(4.52885, 1.89032, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (34.1234, 4.08768,magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.6286, 2.2015, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | air)


# Define the fittable parameters as usual, including the magnetism attributes.

#Substrate fittings
Nine3Nine1[0].interface.range(0.5,10)

#LSMO Fittings
x = 1
while x < 31:
    Nine3Nine1[x].material.density.pmp(5)
    Nine3Nine1[x].thickness.pmp(15)
    Nine3Nine1[x].interface.range(0.5,10)
    Nine3Nine1[x].magnetism.rhoM.pmp(10)
    Nine3Nine1[x].magnetism.thetaM.range(0,359)
    x += 2

#LNO fittings
y = 2
while y < 31:
    Nine3Nine1[y].material.density.pmp(5)
    Nine3Nine1[y].thickness.pmp(15)
    Nine3Nine1[y].interface.range(0.5,10)
    Nine3Nine1[y].magnetism.rhoM[0].pmp(5)
    Nine3Nine1[y].magnetism.rhoM[1].pmp(5)
    Nine3Nine1[y].magnetism.thetaM[0].range(0,359)
    Nine3Nine1[y].magnetism.thetaM[1].range(0,359) 
    y += 2

# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["n3n1-0t.reflA", None, "n3n1-0t.reflC", "n3n1-0t.reflD"])

experiment = Experiment(probe=probe, sample=Nine3Nine1, dz=0.3, dA=None)
problem = FitProblem(experiment)