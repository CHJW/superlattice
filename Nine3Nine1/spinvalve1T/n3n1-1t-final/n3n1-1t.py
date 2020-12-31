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


#LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
#LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
#STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)
LNO = Material(formula='LaNiO3', name = 'LaNiO3', density=7.40213, fitby='bulk_density')
LSMO = Material(formula='LaSrMnO3', name = 'LaSrMnO3', density=6.91949, fitby='bulk_density')
STO = Material(formula='SrTiO3', name = 'SrTiO3', density=5.11, fitby='bulk_density')

Nine3Nine1 = (STO (0,5.7609) 
                | LSMO (37.6695, 1.14386, magnetism=Magnetism(rhoM=1.02705, thetaM=339.247)) | LNO(11.9787, 1.25632, magnetism=MagnetismTwist(rhoM=[0.2899, 0.30373], thetaM=[306.136, 355.25])) 
                | LSMO (33.786, 4.36655, magnetism=Magnetism(rhoM=0.97207, thetaM=152.527)) | LNO(4.77773, 4.41015, magnetism=MagnetismTwist(rhoM=[0.315, 0.28748], thetaM=[313.387, 171.227])) 
                | LSMO (39.4537, 6.44815, magnetism=Magnetism(rhoM=1.06696, thetaM=337.938)) | LNO(13.0152, 5.61937, magnetism=MagnetismTwist(rhoM=[0.29064, 0.29088], thetaM=[298.959, 358.93])) 
                | LSMO (39.6302, 8.40231, magnetism=Magnetism(rhoM=1.03469, thetaM=173.456)) | LNO(4.52885, 6.89322, magnetism=MagnetismTwist(rhoM=[0.29768, 0.28542], thetaM=[331.383, 358.417])) 
                | LSMO (35.6275, 2.88602, magnetism=Magnetism(rhoM=0.98744, thetaM=306.273)) | LNO(12.4855, 1.03026, magnetism=MagnetismTwist(rhoM=[0.30868,0.28598], thetaM=[94.9326,237.261])) 
                | LSMO (38.3148, 6.7784, magnetism=Magnetism(rhoM=1.06852, thetaM=186.304)) | LNO(4.98862,3.93053, magnetism=MagnetismTwist(rhoM=[0.29923,0.29856], thetaM=[19.0571,297.738])) 
                | LSMO (30.2153, 7.24113, magnetism=Magnetism(rhoM=0.99067, thetaM=325.1)) | LNO(12.1451,5.84927, magnetism=MagnetismTwist(rhoM=[0.28521,0.28856], thetaM=[232.631,156.357])) 
                | LSMO (36.7346, 5.5068, magnetism=Magnetism(rhoM=0.93378, thetaM=356.707)) | LNO(4.34831,5.81364, magnetism=MagnetismTwist(rhoM=[0.29296,0.28584], thetaM=[288.362,31.8871])) 
                | LSMO (37.0891, 4.08716, magnetism=Magnetism(rhoM=1.07317, thetaM=358.96)) | LNO(10.8841,1.75752, magnetism=MagnetismTwist(rhoM=[0.28808,0.28576], thetaM=[355.553,345.909])) 
                | LSMO (34.7837, 1.05867, magnetism=Magnetism(rhoM=0.91221, thetaM=358.99)) | LNO(4.63916,1.27298, magnetism=MagnetismTwist(rhoM=[0.31021,0.29491], thetaM=[334.414,308.201])) 
                | LSMO (39.9663,4.32897 , magnetism=Magnetism(rhoM=1.09345, thetaM=358.107)) | LNO(14.1405,1.2381, magnetism=MagnetismTwist(rhoM=[0.30877,0.2977], thetaM=[358.185,26.4077])) 
                | LSMO (31.533, 1.2992, magnetism=Magnetism(rhoM=0.90511, thetaM=349.362)) | LNO(4.35297,1.03656, magnetism=MagnetismTwist(rhoM=[0.2894,0.2948], thetaM=[358.936,272.169])) 
                | LSMO (33.7723, 3.49333, magnetism=Magnetism(rhoM=1.09992, thetaM=181.259)) | LNO(14.509,1.6951, magnetism=MagnetismTwist(rhoM=[0.30336,0.29995], thetaM=[39.2734,34.4845])) 
                | LSMO (29.2796, 9.43459, magnetism=Magnetism(rhoM=1.04151, thetaM=358.859)) | LNO(4.42365,0.98498, magnetism=MagnetismTwist(rhoM=[0.30437,0.29542], thetaM=[27.6001,84.021])) 
                | LSMO (31.4322,9.28468 , magnetism=Magnetism(rhoM=0.98009, thetaM=356.14)) | LNO(11.3016,5.97574, magnetism=MagnetismTwist(rhoM=[0.29517,0.31071], thetaM=[355.394,20.1668])) 
                | air)

'''
Nine3Nine1 = (STO (0, 1.5) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270))
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270))  
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.86, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1, magnetism=Magnetism(rhoM=0.3, thetaM=270)) 
                | air)

'''

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
probe = instrument.load_magnetic(["n3n1-1t.reflA", None, "n3n1-1t.reflC", "n3n1-1t.reflD"])

experiment = Experiment(probe=probe, sample=Nine3Nine1, dz=0.3, dA=None)
problem = FitProblem(experiment)
