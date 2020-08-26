'''
 Non-Magnetic fitting for Triple 5 superlattice measure on Platypus in 1T field
Program: Refl1D Program

Version 0.1
Author Jackson Wong


'''

from refl1d.names import *
from refl1d.probe import *

# We still need the nuclear structure, so define the materials.

LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)


Ftriple5Model = (STO (0, 1.5) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.85, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (34.1, 2, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 2, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | air)



# Define the fittable parameters as usual, including the magnetism attributes.

x = 1

while x < 31:
    Ftriple5Model[x].thickness.pmp(5)
    Ftriple5Model[x].interface.range(0,5)
    #Ftriple5Model[x].magnetism.rhoM.pmp(10)
    #Ftriple5Model[x].magnetism.thetaM.range(0,359)
    x += 1

# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["t5-1t.reflA", None, "t5-1t.reflC", "t5-1t.reflD"])


experiment = Experiment(probe=probe, sample=Ftriple5Model, dz=0.3, dA=None)
problem = FitProblem(experiment)
