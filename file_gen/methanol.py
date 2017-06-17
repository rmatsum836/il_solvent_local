import mbuild as mb
import numpy as np
from ch3 import CH3
from OH import OH

class methanol(mb.Compound):
    def __init__(self):
        super(methanol, self).__init__()
        
        self.add(CH3(),label='carbon')
        self.add(OH(),label='hydroxide')
        
        #attach the ch3 and hydroxide group
        mb.force_overlap(move_this=self['carbon'],
                from_positions=self['carbon']['port1'],
                to_positions=self['hydroxide']['port1'])
if __name__ == '__main__':
    m = methanol()
    m.visualize(show_ports=True)
