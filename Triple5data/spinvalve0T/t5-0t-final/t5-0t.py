'''
 Magnetic fitting for Triple 5 superlattice measure on Platypus in 0T field
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
LNO = Material(formula='LaNiO3', name = 'LaNiO3', density=7.06209, fitby='bulk_density')
LSMO = Material(formula='LaSrMnO3', name = 'LaSrMnO3', density=6.58148, fitby='bulk_density')
STO = Material(formula='SrTiO3', name = 'SrTiO3', density=5.11, fitby='bulk_density')

Ftriple5Model = (STO (0, 2.98048) 
                | LSMO (38.8999, 0.51014, magnetism=Magnetism(rhoM=0.95166, thetaM=244.176)) | LNO(12.7032,5.01484 , magnetism=MagnetismTwist(rhoM=[0.35342,0.35853 ], thetaM=[32.1931,358.989 ])) 
                | LSMO (32.4846,3.65181 , magnetism=Magnetism(rhoM=0.9891, thetaM=55.8437)) | LNO(12.5858, 1.75276, magnetism=MagnetismTwist(rhoM=[0.36502, 0.34943], thetaM=[355.533, 286.535])) 
                | LSMO (29.0032,1.41811 , magnetism=Magnetism(rhoM=1.07741, thetaM=210.472)) | LNO(16.0714,5.16351, magnetism=MagnetismTwist(rhoM=[0.23353, 0.23], thetaM=[358.882, 358.105])) 
                | LSMO (33.5454, 0.52474, magnetism=Magnetism(rhoM=0.94574, thetaM=358.99)) | LNO(10.5814, 1.55881, magnetism=MagnetismTwist(rhoM=[0.23874,0.25287 ], thetaM=[357.282,36.99 ])) 
                | LSMO (35.045, 5.14023, magnetism=Magnetism(rhoM=1.0093, thetaM=207.341)) | LNO(9.62165,1.22099 , magnetism=MagnetismTwist(rhoM=[0.24301,0.23189 ], thetaM=[334.368,262.982 ])) 
                | LSMO (40.1497,1.87147 , magnetism=Magnetism(rhoM=1.01155, thetaM=343.126)) | LNO(2.7654,0.7523 , magnetism=MagnetismTwist(rhoM=[0.24945, 0.23551], thetaM=[33.936,30.6496 ])) 
                | LSMO (36.0393,1.55895 , magnetism=Magnetism(rhoM=1.07976, thetaM=193.429)) | LNO(2.79262, 1.22581, magnetism=MagnetismTwist(rhoM=[0.23567,0.24553 ], thetaM=[167.577, 269.155])) 
                | LSMO (33.0478,1.67011 , magnetism=Magnetism(rhoM=0.99505, thetaM=210.583)) | LNO(4.7999, 5.09213, magnetism=MagnetismTwist(rhoM=[0.24683,0.22911 ], thetaM=[126.566,130.467 ])) 
                | LSMO (31.5457, 2.58718, magnetism=Magnetism(rhoM=0.92912, thetaM=227.288)) | LNO(3.59994,2.07557, magnetism=MagnetismTwist(rhoM=[0.23079, 0.2354], thetaM=[232.44, 14.352])) 
                | LSMO (40.0318, 3.07494, magnetism=Magnetism(rhoM=1.03509, thetaM=321.261)) | LNO(2.09991, 0.71931, magnetism=MagnetismTwist(rhoM=[0.22802,0.23101 ], thetaM=[177.185, 357.399])) 
                | LSMO (37.9853, 2.95439, magnetism=Magnetism(rhoM=0.95372, thetaM=335.938)) | LNO(11.8145, 0.56594, magnetism=MagnetismTwist(rhoM=[0.23916,0.23121 ], thetaM=[358.937, 358.743])) 
                | LSMO (32.0912, 0.59175, magnetism=Magnetism(rhoM=0.90094, thetaM=358.928)) | LNO(16.3844, 9.44459, magnetism=MagnetismTwist(rhoM=[0.25252,0.2369 ], thetaM=[345.342,358.967 ])) 
                | LSMO (38.4145,6.48231, magnetism=Magnetism(rhoM=0.98285, thetaM=354.615)) | LNO(18.9857,7.68797 , magnetism=MagnetismTwist(rhoM=[0.23033,0.23905 ], thetaM=[342.7, 354.786])) 
                | LSMO (40.1354,1.87124 , magnetism=Magnetism(rhoM=0.97955, thetaM=324.662)) | LNO(12.9764, 2.41025, magnetism=MagnetismTwist(rhoM=[0.23598,0.24581 ], thetaM=[126.023,164.297 ])) 
                | LSMO (33.0862, 8.32957, magnetism=Magnetism(rhoM=0.93131, thetaM=358.914)) | LNO(6.96165, 1.71513, magnetism=MagnetismTwist(rhoM=[0.23122,0.22925 ], thetaM=[60.072, 358.976])) 
                | air)

'''
Ftriple5Model = (STO (0, 1.5) 
                | LSMO (35.8999763551114, 0.991517161690633, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.0976456838363, 0.999999082416319, magnetism = MagnetismTwist(rhoM=[0.359887279200240, 0.359887279200240], thetaM=[225, 370])) 
                | LSMO (35.8999607635805, 0.999175920489308, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(10.9169002913730, 0.999797836931400, magnetism = MagnetismTwist(rhoM=[0.359995735700992, 0.359995735700992], thetaM=[370, 250])) 
                | LSMO (35.8999102407187, 0.998563478223095, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(10.9034319621133, 0.999656470600024, magnetism = MagnetismTwist(rhoM=[0.240164589877360, 0.240164589877360], thetaM=[250, 370])) 
                | LSMO (35.8999962256821, 0.999868959773099, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(10.9000804415887, 0.999839264340448, magnetism = MagnetismTwist(rhoM=[0.240104189851583, 0.240104189851583], thetaM=[370, 300])) 
                | LSMO (35.8996855141303, 0.999919864658957, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(10.9009823787915, 0.983972211557809, magnetism = MagnetismTwist(rhoM=[0.240000502704399, 0.240000502704399], thetaM=[300, 300])) 
                | LSMO (35.8991583571373, 0.999906373186372, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.65011617632097, 0.094555122591131, magnetism = MagnetismTwist(rhoM=[0.240006446619767, 0.240006446619767], thetaM=[300, 200])) 
                | LSMO (35.8990924710759, 0.999910204777874, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.65151140811020, 0.999649877824892, magnetism = MagnetismTwist(rhoM=[0.240359082467019, 0.240359082467019], thetaM=[200, 210])) 
                | LSMO (35.8980801338978, 0.999505157651077, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.65027014866513, 0.997330674718383, magnetism = MagnetismTwist(rhoM=[0.240387492054324, 0.240387492054324], thetaM=[210, 200])) 
                | LSMO (35.8995336479275, 0.990857273516943, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.65002581675318, 0.976162607220891, magnetism = MagnetismTwist(rhoM=[0.240629521588475, 0.240629521588475], thetaM=[200, 200])) 
                | LSMO (35.8998166208382, 0.167715882298592, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(3.65186218808489, 0.995629872663096, magnetism = MagnetismTwist(rhoM=[0.240007333171385, 0.240007333171385], thetaM=[200, 350])) 
                | LSMO (35.8997151614967, 0.999967444794469, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.0954114128222, 0.999140742454424, magnetism = MagnetismTwist(rhoM=[0.240007682731784, 0.240007682731784], thetaM=[350, 200])) 
                | LSMO (35.8994921298259, 0.996701647340918, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.0999329014014, 0.999524722222122, magnetism = MagnetismTwist(rhoM=[0.240459978602768, 0.240459978602768], thetaM=[200, 350])) 
                | LSMO (35.8935215395010, 0.999602204637915, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.0999195693942, 0.980382300305929, magnetism = MagnetismTwist(rhoM=[0.240051473205527, 0.240051473205527], thetaM=[350, 200])) 
                | LSMO (35.8968441132639, 0.992620056061417, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.0999770976278, 0.991720118175803, magnetism = MagnetismTwist(rhoM=[0.240130673183340, 0.240130673183340], thetaM=[200, 200])) 
                | LSMO (35.8991979583523, 0.997051441367232, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(12.0999770976278, 0.991720118175803, magnetism = MagnetismTwist(rhoM=[0.240130673183340, 0.240130673183340], thetaM=[200, 200])) 
                | air)


MagnetismTwist(rhoM=(0.359887279200240, 0.359887279200240), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.359995735700992, 0.359995735700992), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240164589877360, 0.240164589877360), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240104189851583, 0.240104189851583), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240000502704399, 0.240000502704399), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240006446619767, 0.240006446619767), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240359082467019, 0.240359082467019), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240387492054324, 0.240387492054324), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240629521588475, 0.240629521588475), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240007333171385, 0.240007333171385), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240007682731784, 0.240007682731784), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240459978602768, 0.240459978602768), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240051473205527, 0.240051473205527), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240130673183340, 0.240130673183340), thetaM=(250, 280))
MagnetismTwist(rhoM=(0.240130673183340, 0.240130673183340), thetaM=(250, 280))


'''
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

'''
x = 2
while x < 31:
    
    #Ftriple5Model[x].thickness.pmp(5)
    #Ftriple5Model[x].interface.range(0,1)
    #Ftriple5Model[x].magnetism.rhoM[0].pmp(20)
    #Ftriple5Model[x].magnetism.rhoM[1].pmp(20)
    Ftriple5Model[x].magnetism.thetaM[0].pmp(100)
    Ftriple5Model[x].magnetism.thetaM[1].pmp(100)
    x += 2
'''
# Load the data
 
instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["t5-0t.reflA",  None, "t5-0t.reflC", "t5-0t.reflD"])

experiment = Experiment(probe=probe, sample=Ftriple5Model, dz=0.3, dA=None)
problem = FitProblem(experiment)
