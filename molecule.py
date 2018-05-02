from particle import Particle
import numpy as np

class Molecule:

    def __init__(self, pos1, pos2, m1, m2, k, L0):
        self.p1 = Particle(pos1, m1)
        self.p2 = Particle(pos2, m2)
        self.k = k
        self.L0 = L0

    def get_displ(self):
        return self.p2.pos - self.p1.pos

    def get_force(self):
        displ = self.get_displ()
        print(displ)
        return -1*self.k*displ
