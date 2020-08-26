'''
 Magnetic fitting for 9-3/9-1 superlattice measure on Platypus in 0T field
Program: Refl1D Program

Version 0.1
Author Jackson Wong

Quick fit of all parameters. 
This fit would need a lot of additional time/steps. 
This was a test if all labels were sucessfully converted.
'''


from refl1d.names import *
from refl1d.probe import *

# Material definition. rho is calculated. May need some fitting.

LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)

#Need to add magnetic twist to LNO layers


Nine3Nine1 = (STO (0, 1.5) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(3.86, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(3.86, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(3.86, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(3.86, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(3.86, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(3.86, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(3.86, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | LSMO (35.9, 1, magnetism=MagnetismTwist(rhoM=[1.3, 1.3], thetaM=[270,270])) | LNO(11.5, 1, magnetism=MagnetismTwist(rhoM=[0.3, 0.3], thetaM=[270, 270])) 
                | air)


# Define the fittable parameters as usual, including the magnetism attributes.

x = 1
while x < 31:
    
    Nine3Nine1[x].thickness.pmp(10)
    Nine3Nine1[x].interface.range(0,5)
    Nine3Nine1[x].magnetism.rhoM[0].pmp(5)
    Nine3Nine1[x].magnetism.rhoM[1].pmp(5)
    Nine3Nine1[x].magnetism.thetaM[0].range(0,359)
    Nine3Nine1[x].magnetism.thetaM[1].range(0,359)

    x += 1

# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["n3n1-0t.reflA", None, "n3n1-0t.reflC", "n3n1-0t.reflD"])

experiment = Experiment(probe=probe, sample=Nine3Nine1, dz=0.3, dA=None)
problem = FitProblem(experiment)
