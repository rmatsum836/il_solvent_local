import mbuild as mb
import numpy as np
import pytest

class singleN(mb.Compound):
    def __init__(self):
        super(singleN, self).__init__()
        
        mb.load('SingleN.pdb', compound=self)
        singleN.translate(self, -self[0].pos) #move Nitrogen to origin
        port1 = mb.Port(anchor = self[0], orientation = [0, 1, 0], separation = 0.07) 
        self.add(port1, label = 'port1')
        
        for i, portname in enumerate(['port2', 'port3', 'port4']):
            port = mb.Port(anchor=self[0], orientation =[0,1,0], separation=0.07)
            port.rotate(109*np.pi/180, [1,0,0])
            port.rotate(i*120*np.pi/180,[0,1,0])
            self.add(port, label=portname)
