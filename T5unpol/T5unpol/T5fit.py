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

LNO = SLD(name = 'LaNiO3', rho = 6.359)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7)
STO = SLD (name = 'SrTiO3', rho = 3.54)

# Defining Structure

# Repeat structure

threelayer = LSMO(34.1, 2) | LNO (11.5, 2)
onelayer = LSMO(34.1, 2) | LNO (3.85, 2)
Rtriple5Model = STO(0,5) | threelayer*5 | onelayer*5 | threelayer*5 | air

Ftriple5Model = STO (0, 1.5) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(3.85, 2) | LSMO (34.1, 2) | LNO(3.85, 2) | LSMO (34.1, 2) | LNO(3.85, 2) | LSMO (34.1, 2) | LNO(3.85, 2) | LSMO (34.1, 2) | LNO(3.85, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | LSMO (34.1, 2) | LNO(11.5, 2) | air

# Loading data

pth = os.getcwd()
PLP = Platypus ()

probe = PLP.load(os.path.join(pth, r'C:\Users\Jackson\Desktop\a\superlattice\program\Jackson\Triple5data\T5unpol\T5unpol.dat'))


# Fitting parameters

threelayer[0].thickness.pmp(1)
threelayer[1].thickness.pmp(5)
onelayer[0].thickness.pmp(1)
onelayer[1].thickness.pmp(5)
threelayer[0].interface.range(0,1)
threelayer[1].interface.range(0,1)
onelayer[0].interface.range(0,1)
onelayer[1].interface.range(0,1)
Rtriple5Model[0].interface.range(0,1)
Rtriple5Model[1].interface.range(0,1)
Rtriple5Model[2].interface.range(0,1)
Rtriple5Model[3].interface.range(0,1)

x = 1
while x < 31:
    Ftriple5Model[x].thickness.pmp(5)
    Ftriple5Model[x].interface.range(0,1)
    Ftriple5Model[x].material.rho.pmp(10)
   
    x += 1


# Fitting code

MR = Experiment(probe=probe, sample=Rtriple5Model)
MF = Experiment(probe=probe, sample=Ftriple5Model)

problem = FitProblem([MR, MF])
