import mbuild as mb
import numpy as np

class CH3(mb.Compound):
    def __init__(self):
        super(CH3, self).__init__()

        mb.load('ch3.pdb', compound=self)
        mb.Compound.translate(self, -self[0].pos)  # Move carbon to origin.

        port = mb.Port(anchor=self[0])
        self.add(port, label='port1')
        # Place the port at approximately half a C-C bond length.
        mb.Compound.translate(self['port1'], [0, -0.07, 0]) 

