"""
AI Group Project Team 7 Spring22/23

Desc: This module contains Quiz and Quiz.Option classes that is used for the general quiz template
Created by: Muhammad Kamaludin
Modified by:
Last modified: 14/4/2023
"""

import pygame
from typing import Optional
pygame.init()

class Quiz:

    #Essential graphics object
    screen = None
    background,background_rect = None, None
    question_bg_surf, question_bg_rect = None, None
    question_surf, question_rect = None, None
    button_txt, button_txt_rect = None, None 
    submit_button , submit_button_rect = None, None

    FONT_PATH = "graphics/font/PeaberryBase.ttf"
    question_font = pygame.font.Font(FONT_PATH, 32)
    button_font = pygame.font.Font(FONT_PATH, 24)

    CLOUD_CROSS = pygame.transform.scale_by(pygame.image.load("graphics/art/cloud_cross.png"),4)
    CLOUD_CIRCLE = pygame.transform.scale_by(pygame.image.load("graphics/art/cloud_circle.png"),4)
    CLOUD_TICK = pygame.transform.scale_by(pygame.image.load("graphics/art/cloud_tick.png"),4)

    #Non graphics object
    clock = pygame.time.Clock()
    is_submitted = False
    on_click = False

    class Option(pygame.sprite.Sprite):
        option_font = None
        def __init__(self, txt: str, is_answer: bool, quiz: Optional[any] = None):
            super().__init__()
            self.quiz = quiz
            self.option_font = pygame.font.Font(self.quiz.FONT_PATH, 20) if self.quiz  else pygame.font.Font(pygame.font.get_default_font(), 20)
            self.image = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/beige_rectangle_2x7.png"),4.5)
            self.rect = self.image.get_rect()
            self.txt = self.option_font.render(txt, False, 'Black')
            self.txt_rect = self.txt.get_rect(center=self.rect.center)
            self.is_answer = is_answer

        def set_position(self, sides: list[int]):

            self.rect.left = int(sides[0]) if sides[0] else self.rect.left
            self.rect.top = int(sides[1]) if sides[1] else self.rect.top
            self.rect.right = int(sides[2]) if sides[2] else self.rect.right
            self.rect.bottom = int(sides[3]) if sides[3] else self.rect.bottom
            self.txt_rect.center = self.rect.center

        def update(self, quiz):
            #click effect
            if self == quiz.selected_option:
                self.quiz.screen.blit(Quiz.CLOUD_CIRCLE, (self.rect.right - 64 -16,self.rect.top + 32))

            if quiz.is_submitted:
                if self.is_answer:
                    self.quiz.screen.blit(Quiz.CLOUD_TICK, (self.rect.right - 64 -16,self.rect.top + 32))
                if self == quiz.selected_option and not self.is_answer:
                    self.quiz.screen.blit(Quiz.CLOUD_CROSS, (self.rect.right - 64 -16,self.rect.top + 32))

            self.quiz.screen.blit(self.txt,self.txt_rect)

    def __init__(self, question: str, choice: list[str], answer: str):

        self.question = question

        self.options = [self.Option(opt, opt == answer,self) for opt in choice]
        self.options_group = pygame.sprite.Group()
        for opt in self.options:
            self.options_group.add(opt)
        self.selected_option = None

    def display(self):

        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.question_bg_surf,self.question_bg_rect)
        self.screen.blit(self.question_surf, self.question_rect)
        self.screen.blit(self.submit_button, self.submit_button_rect)
        self.screen.blit(self.button_txt, self.button_txt_rect)
        self.options_group.draw(self.screen)
        self.options_group.update(self)
    
    def setup(self):
        """
        Initialize essential graphics objects
        """
        #set the background
        self.screen = pygame.display.get_surface()
        self.background = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"),2)
        self.background_rect = self.background.get_rect()
        #self.background.fill('#262b44')
        #Set the question
        self.question_bg_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/brown_rectangle_3x14.png"),4.5)
        self.question_bg_rect = self.question_bg_surf.get_rect(midtop=(self.screen.get_width()/2,64))
        self.question_surf = self.question_font.render(self.question,False , "White")
        self.question_rect = self.question_surf.get_rect(center=(self.question_bg_rect.center))
        #set the answer options
        REF_POINT = (self.screen.get_width()/2 , self.screen.get_height()*3/4-50) # the center between four option blocks (x,y)
        for index, opt in enumerate(self.options):
            binary_index = format(index, '02b')
            sides = [0,0,0,0] #value of [left, top, right, bottom]
            if int(binary_index[0]):
                sides[1] = REF_POINT[1] + 4
            else:
                sides[3] = REF_POINT[1] - 4

            if int(binary_index[1]):
                sides[0] = REF_POINT[0] + 4
            else:
                sides[2] = REF_POINT[0] - 4
            
            opt.set_position(sides)
            self.options_group.add(opt)
        
        #set submit button
        self.button_txt = self.button_font.render("submit", False, 'White')
        self.button_txt_rect = self.button_txt.get_rect()
        self.submit_button = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png"),4.5)
        self.submit_button_rect = self.submit_button.get_rect(midbottom=(REF_POINT[0], self.screen.get_height() - 16))
        self.button_txt_rect.center = self.submit_button_rect.center

        #play BGM
        pygame.mixer.init()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('graphics/audio/quiz_bgm.wav'),-1)

    def run(self):

        self.setup()

        #some variable for animation
        counter,inc = 0, 1
        temp_rect = self.button_txt_rect.bottom
        mouse_hold = False

        #Actual quiz logic
        is_finished = False
        while not is_finished:
            counter += 1
            self.on_click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    self.on_click = True

            
            #Handle interaction(s) with the answer options
            if not self.is_submitted and self.on_click:
                for opt in self.options:
                    #self.selected_option = opt if opt.rect.collidepoint(pygame.mouse.get_pos()) else self.selected_option
                    if opt.rect.collidepoint(pygame.mouse.get_pos()):
                        self.selected_option = opt
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/quiz_select_answer.wav'))

            #Handle interaction(s) with the submit button 
            if self.submit_button_rect.collidepoint(pygame.mouse.get_pos()):
                
                #button click micro interaction
                if pygame.mouse.get_pressed()[0]:
                    self.submit_button = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1_clicked.png").convert_alpha(),4.5)
                    self.button_txt_rect.bottom = temp_rect + 4
                    if not mouse_hold:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/button_click.wav'))
                    mouse_hold = True   
                else:
                    mouse_hold = False
                    self.submit_button = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png").convert_alpha(),4.5)
                    self.button_txt_rect.bottom = temp_rect

                #Update quiz state
                if self.on_click and self.selected_option:
                    is_finished = self.is_submitted if self.is_submitted else is_finished
                    self.is_submitted = True
                    self.button_txt = self.button_font.render("Continue", False, 'White')
                    self.button_txt_rect = self.button_txt.get_rect(center=self.submit_button_rect.center)
    
                    if self.selected_option.is_answer:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('graphics/audio/quiz_correct.wav'))
                    else:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('graphics/audio/quiz_wrong.wav'))

            #animate background
            inc = -1 if self.background_rect.left == 0 else inc
            inc = 1 if self.background_rect.right == self.screen.get_width() else inc
            if not counter % 2:
                self.background_rect.left += inc    
            
            self.display()

            pygame.display.update()
            self.clock.tick(60)

        return True

    def get_score(self):

        if self.selected_option:
            return int(self.selected_option.is_answer)
        else:
            return 0
    
if __name__ == "__main__":

    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Quiz page")

    #create quiz object
    q1 = Quiz("This is the prompt", ["AAAA","BBBB","CCCC","DDDD"], "CCCC")

    #run the page
    q1.run()

    #get score
    print(q1.get_score())

