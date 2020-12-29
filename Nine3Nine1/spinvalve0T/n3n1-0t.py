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
LNO = Material(formula='LaNiO3', name = 'LaNiO3', density=7.41988, fitby='bulk_density')
LSMO = Material(formula='LaSrMnO3', name = 'LaSrMnO3', density=6.91916, fitby='bulk_density')
STO = Material(formula='SrTiO3', name = 'SrTiO3', density=5.11, fitby='bulk_density')

#Need to add magnetic twist to LNO layers


Nine3Nine1 = (STO (0,7.98539) 
                | LSMO (38.5473, 1.02092,magnetism=Magnetism(rhoM=1.09986, thetaM=342.041)) | LNO(11.8772, 1.51548, magnetism=MagnetismTwist(rhoM=[0.29537,0.30365], thetaM=[287.051,357.313])) 
                | LSMO (33.2081, 4.56194,magnetism=Magnetism(rhoM=0.95070, thetaM=145.136)) | LNO(4.68803, 6.47384, magnetism=MagnetismTwist(rhoM=[0.31500,0.28414], thetaM=[288.993,195.728])) 
                | LSMO (39.6920, 5.87110,magnetism=Magnetism(rhoM=1.08504, thetaM=336.515)) | LNO(13.1840, 7.72752, magnetism=MagnetismTwist(rhoM=[0.28439,0.28920], thetaM=[323.529,358.912])) 
                | LSMO (39.5114, 7.21133,magnetism=Magnetism(rhoM=1.09643, thetaM=174.083)) | LNO(5.07038, 6.35704, magnetism=MagnetismTwist(rhoM=[0.30885,0.28532], thetaM=[354.052,357.338])) 
                | LSMO (35.1926, 0.50010,magnetism=Magnetism(rhoM=0.99506, thetaM=307.894)) | LNO(12.0119, 0.51679, magnetism=MagnetismTwist(rhoM=[0.30577,0.28629], thetaM=[136.78,206.86])) 
                | LSMO (38.8763, 7.94969,magnetism=Magnetism(rhoM=1.07344, thetaM=186.882)) | LNO(4.98015, 3.98380, magnetism=MagnetismTwist(rhoM=[0.30116,0.29635], thetaM=[31.3608,183.495])) 
                | LSMO (30.4542, 6.63135,magnetism=Magnetism(rhoM=1.00055, thetaM=324.510)) | LNO(12.0372, 4.94668, magnetism=MagnetismTwist(rhoM=[0.28406,0.28400], thetaM=[242.034,156.715])) 
                | LSMO (36.8098, 7.78109,magnetism=Magnetism(rhoM=0.95023, thetaM=358.993)) | LNO(4.45858, 6.17408, magnetism=MagnetismTwist(rhoM=[0.29456,0.28629], thetaM=[193.622,18.0416])) 
                | LSMO (36.9003, 5.39519,magnetism=Magnetism(rhoM=1.08178, thetaM=358.960)) | LNO(10.9377, 1.62792, magnetism=MagnetismTwist(rhoM=[0.28867,0.28582], thetaM=[355.71,343.31])) 
                | LSMO (33.9545, 1.07144,magnetism=Magnetism(rhoM=0.91294, thetaM=358.977)) | LNO(4.78720, 1.37923, magnetism=MagnetismTwist(rhoM=[0.30839,0.29682], thetaM=[324.68,350.52])) 
                | LSMO (39.9855, 2.03961,magnetism=Magnetism(rhoM=1.09738, thetaM=358.352)) | LNO(14.5909, 0.87991, magnetism=MagnetismTwist(rhoM=[0.30945,0.31105], thetaM=[357.823,32.5683])) 
                | LSMO (30.0406, 0.85465,magnetism=Magnetism(rhoM=0.90495, thetaM=355.151)) | LNO(4.64230, 1.15256, magnetism=MagnetismTwist(rhoM=[0.28401,0.29875], thetaM=[358.948,213.299])) 
                | LSMO (34.3899, 0.53196,magnetism=Magnetism(rhoM=1.09991, thetaM=184.830)) | LNO(14.5228, 1.36541, magnetism=MagnetismTwist(rhoM=[0.29307,0.29604], thetaM=[28.0634,38.8337])) 
                | LSMO (29.0149, 9.48518,magnetism=Magnetism(rhoM=1.05359, thetaM=358.711)) | LNO(4.46244, 0.50602, magnetism=MagnetismTwist(rhoM=[0.30422,0.29634], thetaM=[0.03144,71.9855])) 
                | LSMO (32.0732, 9.94405,magnetism=Magnetism(rhoM=1.09998, thetaM=354.403)) | LNO(10.8609, 6.97576, magnetism=MagnetismTwist(rhoM=[0.30017,0.30720], thetaM=[353.046,28.132])) 
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
