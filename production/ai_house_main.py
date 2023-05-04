
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

import pygame 

from production.ai_house.code.main2 import Game 


pygame.init()
# pygame.display.set_caption('Cloud house: Currently running directly from cloudhouse main')


game = Game()
game.run()