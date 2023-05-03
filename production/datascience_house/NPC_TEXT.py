import pygame


class TextLevelOne:
    def __init__(self):
        self.text_box_position_x = 290
        self.text_box_position_y = 270
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 35)
        self.textLine1 = self.font.render("Well done! The Gate of Xuan Kong has been opened.", True, self.text_color)
        self.textLine2 = self.font.render("Please proceed to the next interstellar destination.", True, self.text_color)


class TextLevelTwo:
    def __init__(self):
        self.text_box_position_x = 290
        self.text_box_position_y = 270
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 35)
        self.textLine1 = self.font.render("Hello there! You've worked hard all the way!", True, self.text_color)
        self.textLine2 = self.font.render("I am a Scorpio constellation interstellar navigator", True, self.text_color)
        self.textLine3 = self.font.render("and in charge of navigating through this constellation.", True, self.text_color)
        s = "You need my permission to enter the Scorpio constellation. According to regulations, you need to answer a few questions. Do you have the courage to accept the challenge? There are 10 questions in total, and if you answer 7 correctly, you win! Good luck!"


class TextLevelThree:
    def __init__(self):
        pass
