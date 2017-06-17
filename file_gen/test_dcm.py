import mbuild as mb
from foyer import Forcefield
from foyer.tests.utils import get_fn
import foyer as foyer

dcm = mb.load('DCM.mol2')
dcm_box = mb.fill_box(compound=dcm(),n_compounds=200,box=[4,4,4])
dcm_box.save('test_dcm.gro')
dcm_box.save('test_dcm.top', forcefield_name='oplsaa')
