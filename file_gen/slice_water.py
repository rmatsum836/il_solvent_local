import mbuild as mb
from foyer import Forcefield
from foyer.tests.utils import get_fn
import foyer as foyer

#load all mol2 files and name them
bmim = mb.load('mol2/bmim.mol2')
bmim.name = 'bmim'
tf2n = mb.load('mol2/tf2n.mol2')
tf2n.name ='tf2n'
h2o = mb.load('mol2/tip3p.mol2')
h2o.name = 'h2o'

#fill box with IL's and solvent 
system = mb.fill_box(compound=[bmim, tf2n, h2o],
        n_compounds=[20, 20, 13], box = [5, 5, 5])

#forloop to add IL's or solvents to respective compounds
il = mb.Compound()
solvent = mb.Compound()
for child in system.children:
    if child.name in ['bmim','tf2n']:
        il.add(mb.clone(child))
    elif child.name == 'h2o':
        solvent.add(mb.clone(child))
        #print("add")

#Set variable to forcefields
tip3p = Forcefield('tip3p.xml')
lopes = Forcefield('lopes.xml')
#print(foyer.__file__)

solventPM = tip3p.apply(solvent, residues = 'h2o') # apply forcefields to solvent
solventPM.save('h2otest.top', overwrite=True)
ilPM = lopes.apply(il, residues=['bmim','tf2n'])  #apply forcefield to IL's
ilPM.save('iltest.top', overwrite=True)

# Scale charges by 0.8
scale = 0.8
if scale != 1.0:
    print("Scaling charges... ")
    for atom in ilPM.atoms:
        atom.charge *= scale

systemPM = ilPM + solventPM #Use parmed files to combine forcefields

#Save system to .gro and .top files
systemPM.save('IL-h2o-2.gro', overwrite=True)
systemPM.save('IL-h2o-2.top', overwrite=True)

