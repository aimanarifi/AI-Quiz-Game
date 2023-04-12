"""
AI Group Project Team 7 Spring22/23

Desc: This module responsible for the statistics page
Created by: Muhammad Kamaludin
Modified by:
Last modified: 9/4/2023
"""
import pygame
from typing import Optional

pygame.init()

HOUSES = ["A.I.","Blockchain","Cloud Computing","Cybersecurity","Data Science", "Internet of Things"]
player_name = "Statistics"
money = 0
exp = 0
exps = [0,0,0,0,0,0]
personal_bests = [0,0,0,0,0,0]
clock = pygame.time.Clock()
render = True
stats_blocks = [ None for i in range(14)]

class StatsBlock(pygame.sprite.Sprite):

    """
    This text block is a wrapper consists of three types text surfaces(header,subheader and data).
    This is used for example to handle the display of data like 
    
    'AI House              <-- Header
    
     exp:            20    <-- subheader:    data
     personal best:  40'   <-- subheader:    data *number of subheaders is dynamic

    """

    large_font = pygame.font.Font(pygame.font.get_default_font(), 32)
    small_font = pygame.font.Font(pygame.font.get_default_font(), 24)

    #https://www.schemecolor.com/brown-tan-monochromatic.php
    PRIMARY_COLOUR = (253, 217, 181)
    SECONDARY_COLOUR = (237, 142, 48)
    TERTIARY_COLOUR = (146, 68, 0)

    DIMENSION = (323,200)

    def __init__(self, header: str, subheaders: list[str], data: list[float|str]):
        self.image = pygame.Surface(self.DIMENSION)
        self.image.fill(self.SECONDARY_COLOUR)
        self.rect = self.image.get_rect()
        self.set_header(header)
        min_len = min(len(subheaders),len(data))
        self.set_subheaders(subheaders[:min_len])
        self.set_data(data[:min_len])

    def set_size(self, width: int, height:int):
        self.image = pygame.Surface((width,height))
        self.image.fill(self.SECONDARY_COLOUR)
        self.rect = self.image.get_rect()

    def set_header(self, header: str):
        self.header = header
        self.header_surf = self.large_font.render(header, False, "Black")
        self.header_rect = self.header_surf.get_rect()

    def set_subheaders(self, subheaders: list[str]):
        self.subheaders_surf, self.subheaders_rect = [ None for i in range(len(subheaders)) ],[ None for i in range(len(subheaders))]
        self.subheaders = subheaders
        for i in range(len(subheaders)):
            self.subheaders_surf[i] = self.small_font.render(self.subheaders[i], False, "Black")
            self.subheaders_rect[i] = self.subheaders_surf[i].get_rect()

    def set_data(self, data: list[str|float]):
        self.data, self.data_surf, self.data_rect = ["" for i in range(len(data))],[ None for i in range(len(data)) ],[ None for i in range(len(data))]

        for i in range(len(data)):
            self.data[i] = f"{data[i]:,.2f}" if isinstance(data[i], float) else str(data[i])
            self.data_surf[i] = self.small_font.render(self.data[i], False, "Black")
            self.data_rect[i] = self.data_surf[i].get_rect()

    def format(self, left: Optional[int] = None, top: Optional[int] = None, right: Optional[int] = None, bottom: Optional[int] = None):
        """
        Format the size of the wrapper or to position the text surfaces nicely
        Assuming the wrapper using image, size is fixed
        """
  
        self.rect.left = left if left is not None else self.rect.left
        self.rect.top = top if top is not None else self.rect.top
        self.rect.right = right if right is not None else self.rect.right
        self.rect.bottom = bottom if bottom is not None else self.rect.bottom
        
        #pos the header and data in a stack
        SPACING = (8,16,24,32)
        self.header_rect.topleft = (self.rect.left + SPACING[1], self.rect.top + SPACING[1])
        
        for i in range(len(self.subheaders)):
            if i:
                self.subheaders_rect[i].topleft = (self.header_rect.left, self.subheaders_rect[i-1].bottom + SPACING[1]) 
            else:
                self.subheaders_rect[i].topleft = (self.header_rect.left, self.header_rect.bottom + SPACING[2]) 
            self.data_rect[i].topright = (self.rect.right - SPACING[1], self.subheaders_rect[i].top)
    
    def display(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
        screen.blit(self.header_surf, self.header_rect)

        for i in range(len(self.subheaders)):
            screen.blit(self.subheaders_surf[i], self.subheaders_rect[i])
            screen.blit(self.data_surf[i], self.data_rect[i])

def setup(player):
    """
    TODO: fetch all data from player instance variable
    """
    global stats_blocks
    
    for i, header in enumerate([player_name] + HOUSES):
        if i:
            stats_blocks[i] = StatsBlock(header, ['Experience','Personal Best'], [exps[i-1],personal_bests[i-1]])
        else:
            stats_blocks[i] = StatsBlock(header, ['Overall experience'], [exp])
            stats_blocks[i].set_size(screen.get_width()-32*2,100)

    stats_blocks = [block for block in stats_blocks if block is not None]

    #Position the stats block in a big header and 2x3 grid below it
    REF_POINT = (screen.get_width()/2 , screen.get_height()/2 + 60) # the center between four option blocks (x,y)
    for index, block in enumerate(stats_blocks):

        if  not index:
            block.format(left = 32, top= 32)
            continue

        binary_index = format(index, '03b')
        #set the row
        if sum([ int(n) for n in binary_index]) == 2:
            block.format(top=REF_POINT[1] + 12)
        else:
            block.format(bottom=REF_POINT[1] - 12)

        #set the column
        if binary_index[0] == binary_index[1]:
            block.format(right=REF_POINT[0]-block.rect.width/2-24)
        elif binary_index[0] == binary_index[2]:
            block.format(left=REF_POINT[0]+block.rect.width/2+24)
        elif binary_index[1] == binary_index[2]:
            block.format(left=REF_POINT[0]-block.rect.width/2)


def run(screen: pygame.Surface, player):
    
    setup(player)

    while render:
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        for block in stats_blocks:
            block.display(screen)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":

    screen = pygame.display.set_mode((1080,608))
    screen.fill(StatsBlock.PRIMARY_COLOUR)
    run(screen, "Yolo")

