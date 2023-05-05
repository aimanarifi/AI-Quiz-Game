import pygame
from typing import Optional
from production.general.db import DatabaseService as DB

pygame.init()

# HOUSES = ["A.I.","Blockchain","Cloud Computing","Cybersecurity","Data Science", "Internet of Things"]

# money = 0
# exp = 0
# exps = [0,0,0,0,0,0]
# personal_bests = [0,0,0,0,0,0]

# stats_blocks = [ None for i in exps]


page_title = "Achievements"
clock = pygame.time.Clock()
#graphis object
FONT_PATH = 'graphics/font/PeaberryBase.ttf'
large_font = pygame.font.Font(FONT_PATH, 48)
medium_font = pygame.font.Font(FONT_PATH, 24)
small_font = pygame.font.Font(FONT_PATH, 16)
screen = None
bg_surf, bg_rect = None, None
statsblocks_wrapper_surf, statsblocks_wrapper_rect = None, None
title_surf, title_rect = None, None
title_bg_surf, title_bg_rect = None, None
button_surf, button_rect = None, None
exp_bg_surf, exp_bg_rect = None, None
exp_surfs, exp_rects = [None,None], [None, None]
trophy = pygame.image.load('assets/graphics/player_house_graphics/trophy.png') 
biggest_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4.3)

class Achievement(pygame.sprite.Sprite):

    """
    This text block is a wrapper consists of three types text surfaces(header,subheader and data).
    This is used for example to handle the display of data like 
    
    'Achievemnt name              <-- Header
    
     Achievement explanation               Trophy picture

    """

    def __init__(self, name: str, explanation: str, trophy_pic, pos: tuple):
        temp_path =  'graphics/art/UI/beige_rectangle_5x2.png'
        self.image = pygame.transform.scale_by(pygame.image.load(temp_path),(12,4.3))
        self.rect = self.image.get_rect()
        self.explan = explanation
        self.trophy_pic = trophy_pic
        self.name_text_surf = medium_font.render(name, False, 'Black')
        self.explan_text_surf = small_font.render(explanation, False, 'Black')
        self.pos = pos
        

        

    def set_size(self, width: int, height:int):
        self.image = pygame.Surface((width,height))
        self.image.fill(self.SECONDARY_COLOUR)
        self.rect = self.image.get_rect()

    
    
    def display(self):
        screen.blit(self.image, self.pos)
        screen.blit(self.name_text_surf, (self.image.get_width()-850, self.pos[1]+ 10))
        screen.blit(self.explan_text_surf, (self.image.get_width()-850, self.pos[1]+ 40))
        screen.blit(self.trophy_pic,(self.image.get_width() - 80, self.pos[1] + 15) )

        
       
        

def setup():
    """
    Initialise necessary things
    """
    global screen, bg_surf,bg_rect, stats_blocks, statsblocks_wrapper_surf, statsblocks_wrapper_rect
    global title_surf, title_rect, title_bg_surf, title_bg_rect, button_surf, button_rect
    global exp, exp_bg_surf, exp_bg_rect, exp_surfs, exp_rects

    screen = pygame.display.get_surface()
    bg_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"),2)
    bg_rect = bg_surf.get_rect()
    title_surf = large_font.render(page_title, False, 'White')
    title_rect = title_surf.get_rect(topleft=(64,64))
    title_bg_surf = pygame.image.load('graphics/art/UI/black_bar1_6x1.png')
    title_bg_surf = pygame.transform.scale(title_bg_surf, (title_rect.width+16, title_rect.height/2))
    title_bg_rect = title_bg_surf.get_rect(bottomleft=(title_rect.left-8, title_rect.bottom))

    player_stats = DB.get_user()

    
  
   


    #Position the stats block in a wrapper and 2x3 grid below it
    statsblocks_wrapper_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/brown_rectangle_14x6.png'),5.2)
    statsblocks_wrapper_rect = statsblocks_wrapper_surf.get_rect()
    statsblocks_wrapper_rect.midbottom = (screen.get_width()/2, screen.get_height() - 64)
    
    # REF_POINT = statsblocks_wrapper_rect.center # the center between sixoption blocks
    # temp_spacing = ((statsblocks_wrapper_rect.height - 2*stats_blocks[0].rect.height - 64)/3,
    #                 (statsblocks_wrapper_rect.width - 3*stats_blocks[0].rect.width - 64)/4 ) #(row,col)
    # for index, block in enumerate(stats_blocks):
    #     binary_index = format(index+1, '03b')
    #     #set the row
    #     if sum([ int(n) for n in binary_index]) == 2:
    #         block.format(top=REF_POINT[1] + temp_spacing[0]/2)
    #     else:
    #         block.format(bottom=REF_POINT[1] - temp_spacing[0]/2)

    #     #set the column
    #     if binary_index[0] == binary_index[1]:
    #         block.format(right=REF_POINT[0] - block.rect.width/2 - temp_spacing[1])
    #     elif binary_index[0] == binary_index[2]:
    #         block.format(left=REF_POINT[0] + block.rect.width/2 + temp_spacing[1])
    #     elif binary_index[1] == binary_index[2]:
    #         block.format(left=REF_POINT[0] - block.rect.width/2)

    button_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/back_button.png'),4.0)
    button_rect = button_surf.get_rect(bottomright=(screen.get_width()-64, title_rect.bottom ))
    pygame.mixer.init()

def run():

    setup()
    global button_surf
    inc, counter = 1,0
    mouse_hold, on_click = False, False
    loop = True
    
    while loop:
        counter += 1
        on_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                on_click = True
        #Button microinteraction
        if button_rect.collidepoint(pygame.mouse.get_pos()):

            if pygame.mouse.get_pressed()[0]:
                button_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/back_button_clicked.png'),4.0)
                if not mouse_hold:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/button_click.wav'))
                mouse_hold = True
            else:
                mouse_hold = False
                button_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/back_button.png'),4.0)
            
            loop = False if on_click else True

        #animate bg
        inc = -1 if bg_rect.left == 0 else inc
        inc = 1 if bg_rect.right == screen.get_width() else inc
        if not counter % 2:
            bg_rect.left += inc

        #Blit everything
        #pygame.draw.rect(screen,"#262b44",screen.get_rect())
        screen.blit(bg_surf, bg_rect)
        screen.blit(title_bg_surf, title_bg_rect)
        screen.blit(title_surf, title_rect)
        
       
        screen.blit(button_surf, button_rect)
        
        achi = Achievement("Welcome to IBM Village", "This is a welcome achievement. We hope you continue to earn more trophies", trophy, (50,150))
        achi.display()
       
        
        pygame.display.update()
        clock.tick(60)



