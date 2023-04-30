import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))

import pygame
from production.player_house.code.settings5 import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=LAYERS['Floor']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
