import mbuild as mb
import numpy as np
import pytest

class CF3(mb.Compound):
    def __init__(self):
        super(CF3, self).__init__()
        
        mb.load('CF3.pdb', compound=self)
        
        port1 = mb.Port(anchor=self[0], orientation=[1,0,0],separation=0.07)
        self.add(port1,label='port1')
