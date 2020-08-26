'''
 Magnetic fitting for Triple 5 superlattice measure on Platypus in 0T field
Program: Refl1D Program

Version 0.1
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

# We still need the nuclear structure, so define the materials.

LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)



Ftriple5Model = (STO (0, 1.5) 
                | LSMO (35.8999763551114, 0.991517161690633, magnetism=MagnetismTwist(rhoM=[0.199999354485650,0.199999354485650], thetaM=[225,225])) | LNO(12.0976456838363, 0.999999082416319, magnetism = MagnetismTwist(rhoM=[0.359887279200240, 0.359887279200240], thetaM=[225, 370])) 
                | LSMO (35.8999607635805, 0.999175920489308, magnetism=MagnetismTwist(rhoM=[0.199284476207290,0.199284476207290], thetaM=[370,370])) | LNO(10.9169002913730, 0.999797836931400, magnetism = MagnetismTwist(rhoM=[0.359995735700992, 0.359995735700992], thetaM=[370, 250])) 
                | LSMO (35.8999102407187, 0.998563478223095, magnetism=MagnetismTwist(rhoM=[0.800047645372031,0.800047645372031], thetaM=[250,250])) | LNO(10.9034319621133, 0.999656470600024, magnetism = MagnetismTwist(rhoM=[0.240164589877360, 0.240164589877360], thetaM=[250, 370])) 
                | LSMO (35.8999962256821, 0.999868959773099, magnetism=MagnetismTwist(rhoM=[0.800438263427779,0.800438263427779], thetaM=[370,370])) | LNO(10.9000804415887, 0.999839264340448, magnetism = MagnetismTwist(rhoM=[0.240104189851583, 0.240104189851583], thetaM=[370, 300])) 
                | LSMO (35.8996855141303, 0.999919864658957, magnetism=MagnetismTwist(rhoM=[0.800261975838851,0.800261975838851], thetaM=[300,300])) | LNO(10.9009823787915, 0.983972211557809, magnetism = MagnetismTwist(rhoM=[0.240000502704399, 0.240000502704399], thetaM=[300, 300])) 
                | LSMO (35.8991583571373, 0.999906373186372, magnetism=MagnetismTwist(rhoM=[0.800000001495303,0.800000001495303], thetaM=[300,300])) | LNO(3.65011617632097, 0.094555122591131, magnetism = MagnetismTwist(rhoM=[0.240006446619767, 0.240006446619767], thetaM=[300, 200])) 
                | LSMO (35.8990924710759, 0.999910204777874, magnetism=MagnetismTwist(rhoM=[0.800237079690324,0.800237079690324], thetaM=[200,200])) | LNO(3.65151140811020, 0.999649877824892, magnetism = MagnetismTwist(rhoM=[0.240359082467019, 0.240359082467019], thetaM=[200, 210])) 
                | LSMO (35.8980801338978, 0.999505157651077, magnetism=MagnetismTwist(rhoM=[0.800027783748864,0.800027783748864], thetaM=[210,210])) | LNO(3.65027014866513, 0.997330674718383, magnetism = MagnetismTwist(rhoM=[0.240387492054324, 0.240387492054324], thetaM=[210, 200])) 
                | LSMO (35.8995336479275, 0.990857273516943, magnetism=MagnetismTwist(rhoM=[0.800207063285033,0.800207063285033], thetaM=[200,200])) | LNO(3.65002581675318, 0.976162607220891, magnetism = MagnetismTwist(rhoM=[0.240629521588475, 0.240629521588475], thetaM=[200, 200])) 
                | LSMO (35.8998166208382, 0.167715882298592, magnetism=MagnetismTwist(rhoM=[0.800045205257954,0.800045205257954], thetaM=[200,200])) | LNO(3.65186218808489, 0.995629872663096, magnetism = MagnetismTwist(rhoM=[0.240007333171385, 0.240007333171385], thetaM=[200, 350])) 
                | LSMO (35.8997151614967, 0.999967444794469, magnetism=MagnetismTwist(rhoM=[0.800040558631474,0.800040558631474], thetaM=[350,350])) | LNO(12.0954114128222, 0.999140742454424, magnetism = MagnetismTwist(rhoM=[0.240007682731784, 0.240007682731784], thetaM=[350, 200])) 
                | LSMO (35.8994921298259, 0.996701647340918, magnetism=MagnetismTwist(rhoM=[0.800163252980095,0.800163252980095], thetaM=[200,200])) | LNO(12.0999329014014, 0.999524722222122, magnetism = MagnetismTwist(rhoM=[0.240459978602768, 0.240459978602768], thetaM=[200, 350])) 
                | LSMO (35.8935215395010, 0.999602204637915, magnetism=MagnetismTwist(rhoM=[0.800144206991338,0.800144206991338], thetaM=[350,350])) | LNO(12.0999195693942, 0.980382300305929, magnetism = MagnetismTwist(rhoM=[0.240051473205527, 0.240051473205527], thetaM=[350, 200])) 
                | LSMO (35.8968441132639, 0.992620056061417, magnetism=MagnetismTwist(rhoM=[0.800027329735383,0.800027329735383], thetaM=[200,200])) | LNO(12.0999770976278, 0.991720118175803, magnetism = MagnetismTwist(rhoM=[0.240130673183340, 0.240130673183340], thetaM=[200, 200])) 
                | LSMO (35.8991979583523, 0.997051441367232, magnetism=MagnetismTwist(rhoM=[0.800011562986436,0.800011562986436], thetaM=[200,200])) | LNO(12.0999770976278, 0.991720118175803, magnetism = MagnetismTwist(rhoM=[0.240130673183340, 0.240130673183340], thetaM=[200, 200])) 
                | air)

'''
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


x = 1
while x < 31:
    
    #Ftriple5Model[x].thickness.pmp(5)
    #Ftriple5Model[x].interface.range(0,1)
    Ftriple5Model[x].magnetism.rhoM[0].pmp(5)
    Ftriple5Model[x].magnetism.rhoM[1].pmp(5)
    Ftriple5Model[x].magnetism.thetaM[0].range(0,359)
    Ftriple5Model[x].magnetism.thetaM[1].range(0,359)
    x += 1
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
#probe = instrument.load_magnetic(["n101Gc1.reflA", None, None, None])
probe = instrument.load_magnetic(["n101Gc1.reflA", "n101Gc1f.reflB", "n101Gc1.reflC", "n101Gc1.reflD"])
#probe = instrument.load_magnetic([None, None, n101Gc1.reflC, None])

experiment = Experiment(probe=probe, sample=Ftriple5Model, dz=0.2, dA=None)
problem = FitProblem(experiment)
