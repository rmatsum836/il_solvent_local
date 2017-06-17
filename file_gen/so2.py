import mbuild as mb
import numpy as np
import pytest

class SO2(mb.Compound):
    def __init__(self):
        super(SO2, self).__init__()
        
        mb.load('SO2.pdb',compound=self)
        SO2.translate(self, -self[0].pos) #move SO2 to origin
        
        port1 = mb.Port(anchor=self[0], orientation=[1,0,0],separation=0.07) 
        self.add(port1,label='port1')
        port1.rotate(59*np.pi/180,[0,1,0])
        
        port2 = mb.Port(anchor=self[0], orientation=[1,0,0],separation=0.07)
        self.add(port2,label='port2')
        port2.rotate(301*np.pi/180,[0,1,0])
