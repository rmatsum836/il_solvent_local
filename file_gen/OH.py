import mbuild as mb
import numpy as np

class OH(mb.Compound):
    def __init__(self):
        super(OH,self).__init__()
        
        mb.load('OH.pdb', compound=self)
        OH.translate(self, -self[0].pos)
        port1 = mb.Port(anchor = self[0], orientation = [1,0,0], separation = 0.07) 
        self.add(port1, label = 'port1')
        
        #Rotate port
        port1.rotate(109*np.pi/180,[0,1,0])

if __name__ == '__main__':
    m = OH()
    m.visualize(show_ports=True)
