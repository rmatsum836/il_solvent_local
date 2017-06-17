import mbuild as mb
from foyer import Forcefield
from foyer.tests.utils import get_fn
import foyer as foyer

#load all mol2 files and name them
bmim = mb.load('mol2/bmim.mol2')
bmim.name = 'bmim'
tf2n = mb.load('mol2/tf2n.mol2')
tf2n.name ='tf2n'
dmf = mb.load('DMF.mol2')
dmf.name = 'dmf'

#fill box with IL's and solvent 
system = mb.fill_box(compound=[bmim, tf2n, dmf],
        n_compounds=[20, 20, 114], box = [7, 7, 7]) #8

#forloop to add IL's or solvents to respective compounds
il = mb.Compound()
solvent = mb.Compound()
for child in system.children:
    if child.name in ['bmim','tf2n']:
        il.add(mb.clone(child))
    elif child.name == 'dmf':
        solvent.add(mb.clone(child))
        #print("add")

#Set variable to forcefields
opls = Forcefield(name='oplsaa')
lopes = Forcefield('lopes.xml')
#print(foyer.__file__)

solventPM = opls.apply(solvent, residues = 'dmf') # apply forcefields to solvent
ilPM = lopes.apply(il, residues=['bmim','tf2n'])  #apply forcefield to IL's

# Scale charges by 0.8
"""scale = 0.8
if scale != 1.0:
    print("Scaling charges... ")
    for atom in ilPM.atoms:
        atom.charge *= scale"""

systemPM = ilPM + solventPM #Use parmed files to combine forcefields

#Save system to .gro and .top files
systemPM.save('IL-dmf.gro', overwrite=True)
systemPM.save('IL-dmf.top', overwrite=True)

