'''
 Non-Magnetic fitting for 9-3/9-1 superlattice measure on Platypus in 1T field
Program: Refl1D Program

Version 0.1
Author Jackson Wong

Notes: This program doesn't account for any magnetic fitting.
Theoretically the 1T field will suppress any magnetic effects therefore only observing structure.
RhoM is fitted here but the canting is not.
'''

from refl1d.names import *
from refl1d.probe import *


LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)


Nine3Nine1 = (STO (0, 1.5) 
                | Slab (material = SLD(rho=6.593), thickness = 35.9, interface = 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=90)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=90)) 
                | air)


# Define the fittable parameters as usual, including the magnetism attributes.

x = 1
while x < 31:
    #Nine3Nine1[x].material.rho.pmp(5)
    Nine3Nine1[x].thickness.pmp(12)
    Nine3Nine1[x].interface.range(0.5,1.5)
    #Nine3Nine1[x].magnetism.rhoM.pmp(20)
    #Nine3Nine1[x].magnetism.thetaM.range(0, 359)
    
    x += 1

# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["n3n1-1t.reflA", None, "n3n1-1t.reflC", "n3n1-1t.reflD"])

experiment = Experiment(probe=probe, sample=Nine3Nine1, dz=0.3, dA=None)
problem = FitProblem(experiment)
