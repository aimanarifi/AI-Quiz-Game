"""
AI Group Project Team 7 Spring22/23

Desc: This module control and display the minigame of the cloud house.
It imports level_builder so it can display the the minigame level 

Created by: Muhammad Kamaludin
Modified by:
Last modified: 27/4/2023
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

import pygame
import level_builder
import production.general.quiz as quiz

def run_level(level: level_builder.Level):
    """
    Execute the level as well as the quiz
    """

    global screen, bg, clock
    on_click = False
    quiz_state = False
    is_complete = False
    locked_tile = None

    #It will stays in the loop until it is complete or if it changes to quiz state, as it will enter new loop to render quiz
    while not (is_complete or quiz_state):

        on_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                on_click = True

        
        pygame.draw.rect(screen,(25,36,40),bg)
        level.display_on_screen(screen)
        
        #Effect on tiles
        for tile in [tile for row in level.layout for tile in row]: #flatten the list
            
            if tile.type in ['blank','input','output']: continue
            
            #hover effect
            if tile.rect.collidepoint(pygame.mouse.get_pos()):
                temp_surf = pygame.transform.scale_by(tile.surf,1.2)
                temp_rect = temp_surf.get_rect(center=tile.rect.center)
                screen.blit(temp_surf,temp_rect)

            #rotate tile on click
            if (level.is_answered or not tile.locked) and on_click and tile.rect.collidepoint(pygame.mouse.get_pos()):
                tile.rotate()
                is_complete = level.is_complete() and level.is_answered
            
            elif tile.locked and on_click and tile.rect.collidepoint(pygame.mouse.get_pos()):
                quiz_state = True
                locked_tile = tile
        
        pygame.display.update()
        clock.tick(60)

    
    if not level.is_answered:
        level.is_answered = level.quiz.run()
        locked_tile.unlock()
        locked_tile = None
        run_level(level)


def setup(**setting):

    global screen, bg, clock
    global levels
    
    
    screen = pygame.display.get_surface()
    bg = pygame.Rect((0,0),screen.get_size())

    clock = pygame.time.Clock()
    difficulty = setting["difficulty"]
    levels = level_builder.get_levels( 3*(difficulty-1)+1,3*(difficulty-1)+3)
    quizzes = [quiz.Quiz(f"Question {i}", ["A","B","C","D"],"B") for i in range(len(levels))]

    #set quizzes to the sublevels
    for i, level in enumerate(levels):
        level.quiz = quizzes[i]


    return True

def run(diff: int = 0):
    """
    This is the entry point of the minigame
    """
    setup(difficulty = diff)

    global levels
    print(len(levels))
    for level in levels:
        run_level(level)

    #display score page
    

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('Cloud house: Currently running directly from minigame.py')
    run()