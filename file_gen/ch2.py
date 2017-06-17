import mbuild as mb
import numpy as np
import pytest

class CH2(mb.Compound):
    def __init__(self):
        super(CH2,self).__init__()
        carbon = mb.Particle(name='C')
        self.add(carbon, label= 'C[$]')

        self.add(mb.Particle(name='H', pos=[-0.11, 0, 0]), label='HC[$]')
        self.add(mb.Particle(name='H', pos=[0.11, 0, 0]), label ='HC[$]')

        self.add_bond((self[0], self['HC'][0]))
        self.add_bond((self[0], self['HC'][1]))
        
        port1 = mb.Port(anchor=carbon)
        self.add(port1, label = 'port1')
        mb.Compound.translate(self['port1'], [0, 0.07,0])
        mb.rotate_around_x(self['port1'], 0.57)
        
        port2 = mb.Port(anchor=carbon)
        self.add(port2, label= 'port2')
        mb.Compound.translate(self['port2'], [0, -0.07, 0])
        mb.rotate_around_y(self['port2'], 3.14)
        mb.rotate_around_x(self['port2'], -0.57)
        self.visualize(show_ports=True)
