'''
 Non- Magnetic fitting for Triple 5 superlattice measure on Platypus
Program: Refl1D Program

Version 0.1
Author Jackson Wong

Notes: This program doesn't account for any magnetic fitting.
'''

# Import data package

import os
import refl1d
from refl1d.names import *
from refl1d.material import Material, Vacuum, SLD
from refl1d.model import Repeat, Slab, Stack, Layer
from refl1d.anstodata import ANSTOData, load, Platypus
from refl1d.probe import PolarizedNeutronProbe, PolarizedQProbe, PolarizedNeutronQProbe
from refl1d.reflectivity import reflectivity, magnetic_reflectivity

# Defining Materia
sld = []
sld[0] = 3.54
sld[1] = 3.7
sld[2] = 6.359

LNO = SLD(name = 'LaNiO3', rho = 6.359)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7)
STO = SLD (name = 'SrTiO3', rho = 3.54)



# Defining Structure

model = STO(0, 1.5) | LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | \
    LSMO(34.1, 2) | LNO(3.85, 2) | LSMO(34.1, 2) | LNO(3.85, 2) | LSMO(34.1, 2) | LNO(3.85, 2) | LSMO(34.1, 2) | LNO(3.85, 2) | LSMO(34.1, 2) | LNO(3.85, 2) | \
    LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | LSMO(34.1, 2) | LNO(11.5, 2) | air

# Loading data

pth =os.path.abspath( os.path.dirname(__file__))
PLP = Platypus()

probe = PLP.load(os.path.join(pth, 'T5unpol.dat'))


# Fitting parameters

#
#for layer in Ftriple5Model:
#    layer.thickness.pmp(20)
#    layer.interface.range(0,5)
#    layer.material.rho.pmp

x = 1
for x in range(1, len(model)):
    model[x].thickness.pmp(20)
    model[x].interface.range(0,5)
    model[x].material.rho.pmp(20)
    x += 1


# Fitting code

#MR = Experiment(probe=probe, sample=Rtriple5Model)
MF = Experiment(probe=probe, sample=Ftriple5Model)

problem = FitProblem(MF)



#refl1d.stajconvert.save_mlayer(problem, 'unpol_555_diff_evo.staj')
