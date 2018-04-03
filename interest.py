from constants import *
import numpy as np


class Interest:

    def __init__(self):
        self.vector = np.random.rand(VECTOR_SIZE)

    def distance(self, interest):
        return np.linalg.norm(self.vector - interest.vector)
