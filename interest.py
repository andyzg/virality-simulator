from constants import *
import numpy as np


class Interest:

    def __init__(self, content=False):
        if content:
            self.vector = np.array([0.5, 0.5, 0.5])
        else:
            self.vector = np.random.rand(VECTOR_SIZE)

    def distance(self, interest):
        distance = np.linalg.norm(self.vector - interest.vector)
        return 1 - (distance / (0.25 * 3) ** 0.5)
