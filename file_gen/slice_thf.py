tmport mbuild as mb
from foyer import Forcefield
from foyer.tests.utils import get_fn
import foyer as foyer

#load all mol2 files and name them
thf= mb.load('mol2/THF.mol2')
thf.name = 'thf'
tf2n = mb.load('mol2/tf2n.mol2')
tf2n.name ='tf2n'
bmim = mb.load('mol2/bmim.mol2')
bmim.name = 'bmim'

#fill box with IL's and solvent 
system = mb.fill_box(compound=[bmim, tf2n, thf],
        n_compounds=[200, 200, 1163], box = [7, 7, 7])

#forloop to add IL's or solvents to respective compounds
il = mb.Compound()
solvent = mb.Compound()
for child in system.children:
    if child.name in ['bmim','tf2n']:
        il.add(mb.clone(child))
    elif child.name == 'thf':
        solvent.add(mb.clone(child))
        #print("add")

#Set variable to forcefields
opls = Forcefield(name='oplsaa')
lopes = Forcefield('lopes.xml')
#print(foyer.__file__)

solventPM = opls.apply(solvent,residues='thf') # apply forcefields to solvent
ilPM = lopes.apply(il, residues=['bmim','tf2n'])  #apply forcefield to IL's

# Scale charges by 0.8
scale = 0.8
if scale != 1.0:
    print("Scaling charges... ")
    for atom in ilPM.atoms:
        atom.charge *= scale
systemPM = ilPM + solventPM #Use parmed files to combine forcefields

#Save system to .gro and .top files
systemPM.save('IL-thf.gro', overwrite=True)
systemPM.save('IL-thf.top', overwrite=True)

