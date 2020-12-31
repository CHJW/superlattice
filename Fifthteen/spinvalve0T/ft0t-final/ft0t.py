'''
 Magnetic fitting for 15 superlattice measure on Platypus in 0T field
Program: Refl1D Program

Version 0.2
Author Jackson Wong

Structure values are taken from 0T fitting.
Canting of the magnetic layers are done in this program.
Canting is defined with reference to LNO layer.
ThetaM 270 is set for LNO and LSMO is canted above and below it. 
Based on original paper canting between LSMO layers can go as high as 110 degrees.
Magnetism twist needs to be added to LNO layer, LSMO is presumed uniform.
'''

from refl1d.names import *
from refl1d.probe import *


#LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
#LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
#STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)
LNO = Material(formula='LaNiO3', name = 'LaNiO3', density=7.08699, fitby='bulk_density')
LSMO = Material(formula='LaSrMnO3', name = 'LaSrMnO3', density=6.91822, fitby='bulk_density')
STO = Material(formula='SrTiO3', name = 'SrTiO3', density=5.11, fitby='bulk_density')

#Model
Fifthteen = (STO (0, 1.48406) 
                | LSMO (43.9436, 1.00192, magnetism=Magnetism(rhoM=0.90244, thetaM=336.83)) | LNO(10.5544,0.89458 , magnetism = MagnetismTwist(rhoM=[0.30131,0.30398], thetaM=[358.36,359])) 
                | LSMO (43.9123, 0.88818, magnetism=Magnetism(rhoM=0.93079, thetaM=168.937)) | LNO(13.7712, 1.01728, magnetism = MagnetismTwist(rhoM=[0.30846,0.29964], thetaM=[358.889,303.254])) 
                | LSMO (43.4734, 2.86707, magnetism=Magnetism(rhoM=1.0936, thetaM=335.96)) | LNO(10.8029, 1.4111, magnetism = MagnetismTwist(rhoM=[0.29589,0.29027], thetaM=[16.7441,118.111])) 
                | LSMO (40.9252, 1.27971, magnetism=Magnetism(rhoM=1.03473, thetaM=186.325)) | LNO(13.5988, 2.75903, magnetism = MagnetismTwist(rhoM=[0.29751,0.28417], thetaM=[227.003,42.5519])) 
                | LSMO (42.2507, 1.60266, magnetism=Magnetism(rhoM=1.05353, thetaM=354.421)) | LNO(12.1348, 0.65622, magnetism = MagnetismTwist(rhoM=[0.29036,0.31195], thetaM=[222.585,102.928])) 
                | LSMO (42.607, 0.5764, magnetism=Magnetism(rhoM=1.08973, thetaM=347.962)) | LNO(11.7814, 1.75723, magnetism = MagnetismTwist(rhoM=[0.28403,0.28406], thetaM=[245.976,326.061])) 
                | LSMO (41.5947, 0.82658, magnetism=Magnetism(rhoM=0.93429, thetaM=179.71)) | LNO(13.8,1.0997 , magnetism = MagnetismTwist(rhoM=[0.31194,0.315], thetaM=[324.319,358.763])) 
                | LSMO (39.7534, 5.12963, magnetism=Magnetism(rhoM=0.97207, thetaM=183.281)) | LNO(11.3156,2.84768 , magnetism = MagnetismTwist(rhoM=[0.3012,0.28591], thetaM=[21.557,266.272])) 
                | LSMO (40.2288,3.69616 , magnetism=Magnetism(rhoM=1.04391, thetaM=358.433)) | LNO(13.2715, 1.00074, magnetism = MagnetismTwist(rhoM=[0.2887,0.29488], thetaM=[245.23,349.806])) 
                | LSMO (43.1498, 7.85582, magnetism=Magnetism(rhoM=0.93087, thetaM=357.261)) | LNO(13.0963, 1.12694, magnetism = MagnetismTwist(rhoM=[0.30181,0.29581], thetaM=[172.583,346.67])) 
                | LSMO (28.3583, 5.30436, magnetism=Magnetism(rhoM=1.06148, thetaM=352.79)) | LNO(13.7033,7.65706 , magnetism = MagnetismTwist(rhoM=[0.30244,0.28668], thetaM=[158.513,200.561])) 
                | LSMO (28.0037,0.85924 , magnetism=Magnetism(rhoM=0.90948, thetaM=352.677)) | LNO(12.5021,1.69542 , magnetism = MagnetismTwist(rhoM=[0.3072,0.30189], thetaM=[309.735,303.114])) 
                | LSMO (30.0088, 1.23665, magnetism=Magnetism(rhoM=1.02917, thetaM=36.9048)) | LNO(11.6117, 0.51415, magnetism = MagnetismTwist(rhoM=[0.31387,0.31112], thetaM=[314.447,132.101])) 
                | LSMO (29.1262,5.58317 , magnetism=Magnetism(rhoM=0.90003, thetaM=340.082)) | LNO(11.0999, 1.64706, magnetism = MagnetismTwist(rhoM=[0.2871,0.30039], thetaM=[116.12,233.227])) 
                | LSMO (28.2659, 1.38284, magnetism=Magnetism(rhoM=0.95903, thetaM=357.5)) | LNO(11.0855, 0.6981, magnetism = MagnetismTwist(rhoM=[0.28401,0.29755], thetaM=[26.3857,119.964])) 
                | air)




# Define the fittable parameters as usual, including the magnetism attributes.

#Substrate fittings
Fifthteen[0].interface.range(0.5,10)

#LSMO Fittings
x = 1
while x < 31:
    Fifthteen[x].material.density.pmp(5)
    Fifthteen[x].thickness.pmp(20)
    Fifthteen[x].interface.range(0.5,10)
    Fifthteen[x].magnetism.rhoM.pmp(10)
    Fifthteen[x].magnetism.thetaM.range(0,359)
    x += 2

#LNO fittings
y = 2
while y < 31:
    Fifthteen[y].material.density.pmp(5)
    Fifthteen[y].thickness.pmp(20)
    Fifthteen[y].interface.range(0.5,10)
    Fifthteen[y].magnetism.rhoM[0].pmp(5)
    Fifthteen[y].magnetism.rhoM[1].pmp(5)
    Fifthteen[y].magnetism.thetaM[0].range(0,359)
    Fifthteen[y].magnetism.thetaM[1].range(0,359) 
    y += 2

'''
x = 1
while x < 31:
    #LSMO layer only
    Fifthteen[x].magnetism.rhoM.pmp(50)
    Fifthteen[x].magnetism.thetaM.range(150, 390)
    x += 2
'''
# Load the data

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["ft0t.reflA", None, "ft0t.reflC", "ft0t.reflD"])


experiment = Experiment(probe=probe, sample=Fifthteen, dz=0.3, dA=None)
problem = FitProblem(experiment)
