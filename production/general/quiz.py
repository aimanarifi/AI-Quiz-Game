"""
AI Group Project Team 7 Spring22/23

Desc: This module contains Quiz and Quiz.Option classes that is used for the general quiz template
Created by: Muhammad Kamaludin
Modified by:
Last modified: 8/4/2023
"""

import pygame

pygame.init()

class Quiz:

    #Essential graphics object
    background = None
    question_surf, question_rect = None, None
    button_txt, button_txt_rect = None, None 
    submit_button , submit_button_rect = None, None

    question_font = pygame.font.Font(pygame.font.get_default_font(), 32)
    button_font = pygame.font.Font(pygame.font.get_default_font(), 24)

    #Non graphics object
    clock = pygame.time.Clock()
    is_submitted = False
    on_click = False
    class Option(pygame.sprite.Sprite):

        option_font = pygame.font.Font(pygame.font.get_default_font(), 20)
        BLOCK_WIDTH = 300
        BLOCK_HEIGHT = 80

        def __init__(self, txt: str, is_answer: bool):
            super().__init__()

            #the block 
            self.image = pygame.Surface((self.BLOCK_WIDTH, self.BLOCK_HEIGHT))
            self.rect = self.image.get_rect()
            self.txt = Quiz.Option.option_font.render(txt, False, 'Black')
            self.txt_rect = self.txt.get_rect(center=self.rect.center)
            self.is_answer = is_answer



        def set_position(self, sides: list[int]):

            self.rect.left = int(sides[0]) if sides[0] else self.rect.left
            self.rect.top = int(sides[1]) if sides[1] else self.rect.top
            self.rect.right = int(sides[2]) if sides[2] else self.rect.right
            self.rect.bottom = int(sides[3]) if sides[3] else self.rect.bottom
            self.txt_rect.center = self.rect.center

        def update(self, quiz):
            #Create hover and click effect
            if self == quiz.selected_option:
                self.image.fill('Yellow')
            elif self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image.fill((254, 250, 224))
            else:
                self.image.fill('White')

            if quiz.is_submitted:
                if self.is_answer:
                    self.image.fill('Green')
                if self == quiz.selected_option and not self.is_answer:
                    self.image.fill('Red')

            screen.blit(self.txt,self.txt_rect)

    def __init__(self, question: str, choice: list[str], answer: str):

        self.question = question

        self.options = [self.Option(opt, opt == answer) for opt in choice]
        self.options_group = pygame.sprite.Group()
        for opt in self.options:
            self.options_group.add(opt)

        self.selected_option = None
        self.score = 0
        self.clock = pygame.time.Clock()
        self.start_time = 0
        self.end_time = 0

    def display(self, screen: pygame.Surface):

        screen.blit(self.background, (0,0))
        screen.blit(self.question_surf, self.question_rect)
        screen.blit(self.submit_button, self.submit_button_rect)
        screen.blit(self.button_txt, self.button_txt_rect)
        self.options_group.draw(screen)
        self.options_group.update(self)
    
    def setup(self, screen: pygame.Surface):
        """
        Initialize essential graphics objects
        """
        #set the background
        self.background = pygame.Surface(screen.get_size())
        self.background.fill('Black')
        #Set the question
        self.question_surf = self.question_font.render(self.question,False , "White")
        self.question_rect = self.question_surf.get_rect(center=( screen.get_width()/2 , 200))
        #set the answer options
        REF_POINT = (screen.get_width()/2 , screen.get_height()*3/4-100) # the center between four option blocks (x,y)
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
        self.button_txt = self.button_font.render("submit", False, 'Black')
        self.button_txt_rect = self.button_txt.get_rect()
        self.submit_button = pygame.Surface((self.button_txt_rect.width+16,self.button_txt_rect.height+16))
        self.submit_button.fill("White")
        self.submit_button_rect = self.submit_button.get_rect(midbottom=(REF_POINT[0], screen.get_height() - 32))
        self.button_txt_rect.center = self.submit_button_rect.center

    def run(self, screen: pygame.Surface):

        self.setup(screen)

        #Actual quiz logic
        is_finished = False
        while not is_finished:
            
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
                    self.selected_option = opt if opt.rect.collidepoint(pygame.mouse.get_pos()) else self.selected_option

            #Handle interaction(s) with the submit button 
            if self.on_click and self.submit_button_rect.collidepoint(pygame.mouse.get_pos()) and self.selected_option is not None:
                is_finished = self.is_submitted if self.is_submitted else is_finished
                self.is_submitted = True
                self.button_txt = self.button_font.render("Continue", False, 'Black')
                self.button_txt_rect = self.button_txt.get_rect(center=self.submit_button_rect.center)

            self.display(screen)

            pygame.display.update()
            self.clock.tick(60)

        return True

    def get_quizzes():
        """TO DO
        static method to fetch quiz from db
        """
        return False

if __name__ == "__main__":

    screen = pygame.display.set_mode((720,720))
    pygame.display.set_caption("Quiz page")

    q1 = Quiz("This is the prompt", ["AAAA","BBBB","CCCC","DDDD"], "CCCC")
    q1.run(screen)

