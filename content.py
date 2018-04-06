from interest import Interest
from uuid import uuid1
from constants import *


class Content:

    def __init__(self):
        self.interest = Interest(True)
        self.uuid = uuid1()

        self.virality = 0  # Shares / Impressions
        self.score = START_SCORE  # Score decays after each timestep
        self.is_dead = False
        self._timestep = 0
        self.shared_by = {}

    def timestep(self):
        if not self.is_dead:
            self.decay()
            self._timestep += 1

    def decay(self):
        self.score /= START_SCORE ** (1.0 / TIMESTEPS_TILL_DEAD)
        if self.score <= 1:
            self.is_dead = True

    def is_shared(self, nid):
        self.shared_by[nid] = self.timestep
        self.score += 1
