'''
 Non-Magnetic fitting for Triple 5 superlattice measure on Platypus in 1T field
Program: Refl1D Program

Version 0.1
Author Jackson Wong


'''

from refl1d.names import *
from refl1d.probe import *
from refl1d.anstodata import ANSTOData, load, load_magnetic, Platypus
import re
import sys
import os.path
from bumps.fitproblem import load_problem
from bumps.cli import load_model

# We still need the nuclear structure, so define the materials.
PARS_PATTERN = re.compile(r"^(?P<label>.*) (?P<value>[^ ]*)\n$")
def load_best(problem, path):
    """
    Load parameter values from a file.
    """
    # Reload the individual parameters from a saved par file. Use the value
    # from the model as the default value.  Keep track of which parameters are
    # defined in the file so we can see if any are missing.
    problem_labels = make_unique(problem.labels()) #Create problem labels that are unique
    
    targets = dict(zip(problem_labels, problem.getp())) #make dict from unique labels
    defined = set()
    labs = []
    if not os.path.isfile(path):
        path = os.path.join(path, problem.name+".par")
    with open(path, 'rt') as fid:
        for line in fid:
            m = PARS_PATTERN.match(line)
            label, value = m.group('label'), float(m.group('value'))
            label, labs = check_unique(label, labs)
            if label in targets:
                targets[label] = value
                defined.add(label)

    values = [targets[label] for label in labs]
    problem.setp(np.asarray(values))
    
    # Identify the missing parameters if any.  These are stuffed into the
    # the problem definition as an optional "undefined" attribute, with
    # one bit for each parameter.  If all parameters are defined, then none
    # are undefined.  This ugly hack is to support a previous ugly hack in
    # which undefined parameters are initialized with LHS but defined
    # parameters are initialized with eps, cov or random.
    # TODO: find a better way to "free" parameters on --resume/--pars.
    if len(values) != len(defined):
        undefined = [label not in defined for label in problem.labels()]
        problem.undefined = np.asarray(undefined)
    return problem

def check_unique( label, labels ):   
    '''
    Checks if the addition of <label> to the list <labels> is unique. 
    If unique, add <label> to <labels>. 
    If not unique, makes a unique version of <label> and inserts into <labels>.
    '''
    if label in labels:
        dups = [duplicate for duplicate in labels if label in duplicate]
        num_dups = len(dups)
        label = label + "_" + str(num_dups)
        labels.append(label)
    elif label not in labels:
        labels.append(label)
    return label, labels

def make_unique(arr):
    '''
    Returns unique list of strings with numbered suffixes depending on degeneracy. 
    '''
    uniques = []
    i = 0
    for entry in arr:
        if entry not in uniques:
            uniques.append(entry)
        else:
            lyrs = [ param for param in uniques if entry in param ]
            layer_number = len(lyrs)
            temp_entry = entry + "_" + str(layer_number)
            uniques.append(temp_entry)
    return uniques

#model = r"superlattice\Triple5data\T5unpol\T5fit.py"
store = r"C:\Users\oliver\OneDrive - UNSW\code\jackson_superlattice\superlattice\Triple5data\T5unpol\OP_diff-ev1"
cwd = os.getcwd()

# load model, then from this model load best fit
model = load_model(os.path.join(store, "T5fit.py"))
p_fit = load_best(model, store)

p = p_fit.getp()
STO = SLD (name = 'SrTiO3', rho = 3.54)
LSMO = SLD(name="LSMO", rho=p[1])
LNO = SLD(name="LNO", rho=p[4])
thetaM = 90

LSMO_mag = FreeMagnetism( z = np.linspace(0,1,9), rhoM = np.full(9,5), thetaM = np.full(9,90) )
LNO_mag = FreeMagnetism( z = np.linspace(0,1,3), rhoM = np.full(3,0.2), thetaM = np.full(3,90) )

#LSMO_lyrs_mag = [ LSMO_mag for i in range(1,16) ]
LNO_lyrs_mag = [ LNO_mag for i in range(1,16) ]

LSMO_lyrs_mag = [ Magnetism( rhoM=1, thetaM=90, interface_above=0, interface_below=0, name="LSMO_mag_" + str(i) ) for i in range(1,16)]
LNO_lyrs_mag1 = [ Magnetism( rhoM=0, thetaM=90, name="LNO_3uc_bottom_mag_" + str(i) ) for i in range(1,6) ]
LNO_lyrs_mag2 = [ Magnetism( rhoM=0, thetaM=90, name="LNO_1uc_mag_" + str(i) ) for i in range(1,6) ]
LNO_lyrs_mag3 = [ Magnetism( rhoM=0, thetaM=90, name="LNO_3uc_top_mag_" + str(i) ) for i in range(1,6) ]




# define experiment based off best fit
experiment = p_fit.fitness
sample = experiment.sample

# Load the data
pth = os.getcwd()
PLP = Platypus()
data_dir = r'C:\Users\oliver\OneDrive - UNSW\code\jackson_superlattice\superlattice\Triple5data\1 Tesla'
probe = PLP.load_magnetic(pp=os.path.join(data_dir, 'c_PLP0045024PolCorr.dat'), 
                        pm=os.path.join(data_dir, 'c_PLP0045021PolCorr.dat'), 
                        mp=None,
                        mm=os.path.join(data_dir, 'PLP0045020PolCorr.dat') )

for magl in LSMO_lyrs_mag:
    magl.rhoM.range(0,4)
    magl.interface_above.range(0,10)
    magl.interface_below.range(0,10)

LSMO_lyrs_mag[0].interface_below.range(0,0.1)

for magl in LNO_lyrs_mag1:
    magl.rhoM.range(0,0.5)



for magl in LNO_lyrs_mag2:
    magl.rhoM.range(0,0.5)
    

for magl in LNO_lyrs_mag3:
    magl.rhoM.range(0,0.5)



experiment = Experiment(probe=probe, sample=sample, dz=0.3, dA=None)
problem = FitProblem(experiment)

problem.save('model.pickle')
