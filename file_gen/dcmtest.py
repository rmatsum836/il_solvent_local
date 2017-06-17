import mbuild as mb
from foyer import Forcefield
from foyer.tests.utils import get_fn
import foyer as foyer

dcm = mb.load('pdb/DCM.pdb')
dcm.name = 'dcm'

#fill box with IL's and solvent 
system = mb.fill_box(compound= dcm,
        n_compounds= 10, box = [7, 7, 7])

#forloop to add IL's or solvents to respective compounds
il = mb.Compound()
solvent = mb.Compound()
for child in system.children:
    if child.name in ['bmim','tf2n']:
        il.add(mb.clone(child))
    elif child.name == 'dcm':
        solvent.add(mb.clone(child))
        #print("add")

#Set variable to forcefields
opls = Forcefield(name='oplsaa')
#print(foyer.__file__)

solventPM = opls.apply(solvent, residues='dcm') # apply forcefields to solvent

systemPM = solventPM #Use parmed files to combine forcefields

#Save system to .gro and .top files
systemPM.save('testdcm.gro', overwrite=True)
systemPM.save('testdcm.top', overwrite=True)

