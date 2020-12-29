'''
 Non-Magnetic fitting for Triple 5 superlattice measure on Platypus in 1T field
Program: Refl1D Program

Version 0.1
Author Jackson Wong


'''

from refl1d.names import *
from refl1d.probe import *

# Material definition. rho is calculated. May need some fitting.
#LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
#LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
#STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)
LNO = Material(formula='LaNiO3', name = 'LaNiO3', density=7.06537, fitby='bulk_density')
LSMO = Material(formula='LaSrMnO3', name = 'LaSrMnO3', density=6.79908, fitby='bulk_density')
STO = Material(formula='SrTiO3', name = 'SrTiO3', density=5.11, fitby='bulk_density')


Ftriple5Model = (STO (0,9.89169 ) 
                | LSMO (33.5658,0.76642 , magnetism=Magnetism(rhoM=1.04563 , thetaM=266.196)) | LNO(15.90761,9.99339, magnetism=MagnetismTwist(rhoM=[0.2843,0.31311], thetaM=[280.301,257.403])) 
                | LSMO (33.1737,9.66111 , magnetism=Magnetism(rhoM=1.09789 , thetaM=270.22)) | LNO(16.0722,3.94918, magnetism=MagnetismTwist(rhoM=[0.30958,0.30338], thetaM=[283.735,246.792])) 
                | LSMO (40.8688, 1.57905, magnetism=Magnetism(rhoM=1.02069 , thetaM=271.499)) | LNO(11.5397,3.65818, magnetism=MagnetismTwist(rhoM=[0.29264,0.29449], thetaM=[49.9542,326.203])) 
                | LSMO (40.9909, 1.25485, magnetism=Magnetism(rhoM= 0.93458, thetaM=261.054)) | LNO(14.6253,8.53794, magnetism=MagnetismTwist(rhoM=[0.28423,0.2843], thetaM=[355.558,333.18]))
                | LSMO (30.633, 2.06129, magnetism=Magnetism(rhoM=0.96066 , thetaM=263.062)) | LNO(12.6483,0.77522, magnetism=MagnetismTwist(rhoM=[0.28409,0.31121], thetaM=[20.0183,75.9676])) 
                | LSMO (36.5615, 2.48523, magnetism=Magnetism(rhoM= 0.90795, thetaM=254.356)) | LNO(1.94748,0.89886, magnetism=MagnetismTwist(rhoM=[0.30225,0.28436], thetaM=[133.139,159.982])) 
                | LSMO (32.8075, 1.13959, magnetism=Magnetism(rhoM=0.93707 , thetaM=293.208)) | LNO(2.47781,9.99983, magnetism=MagnetismTwist(rhoM=[0.31498,0.28676], thetaM=[286.401,327.905])) 
                | LSMO (27.295, 3.62445, magnetism=Magnetism(rhoM= 0.90667, thetaM=156.505)) | LNO(4.18721,2.51733, magnetism=MagnetismTwist(rhoM=[0.28536,0.28557], thetaM=[282.162,348.902])) 
                | LSMO (37.3961,8.28983 , magnetism=Magnetism(rhoM= 1.02681, thetaM=279.373)) | LNO(5.77523,1.65156, magnetism=MagnetismTwist(rhoM=[0.29843,0.30366], thetaM=[163.738,115.722]))
                | LSMO (38.6841, 0.62459, magnetism=Magnetism(rhoM=0.91255 , thetaM=283.065)) | LNO(3.63994,9.99853, magnetism=MagnetismTwist(rhoM=[0.31489,0.31497], thetaM=[19.5409,10.1358])) 
                | LSMO (30.7093, 9.99659, magnetism=Magnetism(rhoM=0.9072 , thetaM=160.301)) | LNO(12.0461,6.20966, magnetism=MagnetismTwist(rhoM=[0.30114,0.28706], thetaM=[356.684,358.851])) 
                | LSMO (36.4751, 2.13678, magnetism=Magnetism(rhoM=0.90192 , thetaM=307.648)) | LNO(12.324,9.10359, magnetism=MagnetismTwist(rhoM=[0.31445,0.31049], thetaM=[146.864,188.864])) 
                | LSMO (36.024, 9.99699, magnetism=Magnetism(rhoM= 0.90344, thetaM=313.308)) | LNO(17.0774,9.25329, magnetism=MagnetismTwist(rhoM=[0.31412,0.31468], thetaM=[257.142,2.81631]))
                | LSMO (35.6866,1.88988 , magnetism=Magnetism(rhoM=0.90002 , thetaM=187.125)) | LNO(17.8631,8.8208, magnetism=MagnetismTwist(rhoM=[0.28409,0.28454], thetaM=[350.36,358.825])) 
                | LSMO (34.3625, 9.99809, magnetism=Magnetism(rhoM= 1.07019, thetaM=265.85)) | LNO(16.2209,1.05208, magnetism=MagnetismTwist(rhoM=[0.30143,0.31498], thetaM=[262.274,293.401])) 
                | air)



# Define the fittable parameters as usual, including the magnetism attributes.

#Substrate fittings
Ftriple5Model[0].interface.range(0.5,10)

#LSMO Fittings
x = 1
while x < 31:
    Ftriple5Model[x].material.density.pmp(5)
    Ftriple5Model[x].thickness.pmp(20)
    Ftriple5Model[x].interface.range(0.5,10)
    Ftriple5Model[x].magnetism.rhoM.pmp(10)
    Ftriple5Model[x].magnetism.thetaM.range(0,359)
    x += 2

#LNO fittings
y = 2
while y < 31:
    Ftriple5Model[y].material.density.pmp(5)
    Ftriple5Model[y].thickness.pmp(50)
    Ftriple5Model[y].interface.range(0.5,10)
    Ftriple5Model[y].magnetism.rhoM[0].pmp(5)
    Ftriple5Model[y].magnetism.rhoM[1].pmp(5)
    Ftriple5Model[y].magnetism.thetaM[0].range(0,359)
    Ftriple5Model[y].magnetism.thetaM[1].range(0,359) 
    y += 2

# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["t5-1t.reflA", None, "t5-1t.reflC", "t5-1t.reflD"])


experiment = Experiment(probe=probe, sample=Ftriple5Model, dz=0.3, dA=None)
problem = FitProblem(experiment)
