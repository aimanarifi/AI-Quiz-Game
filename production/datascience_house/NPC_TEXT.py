"""
Last modified: 03/05/2023
Written by Zhongjie Huang
"""
from Window import pygame

text_box_position_x = 290
text_box_position_y = 270
text_color = (0, 0, 0)
font = pygame.font.Font(None, 35)


class TextMainPage:
    def __init__(self):
        self.welcome_textLine1 = font.render("Welcome to the Data Science House. Begin your fantastic journey now!", True, text_color)
        self.welcome_textLine2 = font.render("Here, you will play the role of an interstellar traveler piloting a fighter jet,", True, text_color)
        self.welcome_textLine3 = font.render("exploring different galaxies and helping the intergalactic steward eliminate", True, text_color)
        self.welcome_textLine4 = font.render("space destroyers.", True, text_color)
        self.welcome_textLine5 = font.render("Begin your fantastic journey now!", True, text_color)


class TextLevelOnePage:
    def __init__(self):
        self.welcome_textLine1 = font.render("Welcome to Scorpio Interstellar. I am the messenger here. We have been", True, text_color)
        self.welcome_textLine2 = font.render("attacked by some interstellar disruptors who spread viruses to disrupt", True, text_color)
        self.welcome_textLine3 = font.render("the ecology of this interstellar system. If you can help us eliminate them,", True, text_color)
        self.welcome_textLine4 = font.render(" I would be very grateful. Good luck!", True, text_color)
        self.instruction_textLine1 = font.render("Press up, down, left or right to move your plane.", True, text_color)
        self.instruction_textLine2 = font.render("Press w to fire.", True, text_color)
        self.end_textLine1 = font.render("Wow, it's incredible that you were able to eliminate those monsters.", True, text_color)
        self.end_textLine2 = font.render("To thank you for your help, let me give you some crystals from our interstellar", True, text_color)
        self.end_textLine3 = font.render("system. They can make your spacecraft faster and also enhance your weapons.", True, text_color)
        self.end_textLine4 = font.render("I wish you a pleasant journey.", True, text_color)
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, text_color)
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, text_color)


class TextLevelTwoPage:
    def __init__(self):
        self.welcome_textLine1 = font.render("Hello there! You've worked hard all the way!", True, text_color)
        self.welcome_textLine2 = font.render("I am a Scorpio constellation interstellar navigator", True, text_color)
        self.welcome_textLine3 = font.render("and in charge of navigating through this constellation.", True, text_color)
        self.welcome_textLine4 = font.render("You need my permission to enter the Scorpio constellation.", True, text_color)
        self.welcome_textLine5 = font.render("According to regulations, you need to answer a few questions.", True, text_color)
        self.welcome_textLine6 = font.render("Do you have the courage to accept the challenge?", True, text_color)
        self.introduction_textLine1 = font.render("There are 10 questions in total.", True, text_color)
        self.introduction_textLine2 = font.render("If you answer 7 correctly, you win! Good luck!", True, text_color)


class TextLevelThreePage:
    def __init__(self):
        pass
