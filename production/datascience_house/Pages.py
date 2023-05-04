"""
Last modified: 03/05/2023
Written by Zhongjie Huang

"""
import pygame
from production.datascience_house.Window import window
from production.datascience_house.NPC_TEXT import TextMainPage, TextLevelOnePage, text_box_position_x, text_box_position_y, font


class MainPage:
    """
    This class is used to design the main page, including a background image, text and a button.
    It provides two methods which will be called by its object to show all the things.
    """
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/mainBackground.jpg')
        self.textMainPage = TextMainPage()
        self.button = pygame.Rect(545, 500, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button)
        self.text = font.render("Click here to start!", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=self.button.center)

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showWelcomeTextLine(self):
        window.blit(self.textMainPage.welcome_textLine1, (text_box_position_x - 50, text_box_position_y - 100))
        window.blit(self.textMainPage.welcome_textLine2, (text_box_position_x - 50, text_box_position_y - 50))
        window.blit(self.textMainPage.welcome_textLine3, (text_box_position_x - 50, text_box_position_y))
        window.blit(self.textMainPage.welcome_textLine4, (text_box_position_x - 50, text_box_position_y + 50))
        window.blit(self.textMainPage.welcome_textLine5, (text_box_position_x - 50, text_box_position_y + 100))
        window.blit(self.text, self.text_rect)


class LevelOnePage:
    """
    This class is used to design the level one page, including a background image and text.
    Some text only needs to be displayed temporarily and then disappear automatically. I created variables for start, end, and duration to
    track the time changes and achieve this functionality.
    It provides several methods to show all the things.
    """
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/LevelOneBackground.jpg')
        self.textLevelOnePage = TextLevelOnePage()
        self.needTOShowWelcomeText = True
        self.welcome_textStartTime = 0
        self.welcome_textEndTime = 0
        self.welcome_textLastTime = 0
        self.needTOShowInstructionText = False
        self.instruction_textStartTime = 0
        self.instruction_textEndTime = 0
        self.instruction_textLastTime = 0
        self.needTOShowEndText = True
        self.end_textStartTime = 0
        self.end_textEndTime = 0
        self.end_textLastTime = 0
        self.needToShowExitText = False

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showWelcomeText(self):
        window.blit(self.textLevelOnePage.welcome_textLine1, (text_box_position_x - 50, text_box_position_y - 100))
        window.blit(self.textLevelOnePage.welcome_textLine2, (text_box_position_x - 50, text_box_position_y - 50))
        window.blit(self.textLevelOnePage.welcome_textLine3, (text_box_position_x - 50, text_box_position_y))
        window.blit(self.textLevelOnePage.welcome_textLine4, (text_box_position_x - 50, text_box_position_y + 50))

    def showInstructionText(self):
        window.blit(self.textLevelOnePage.instruction_textLine1, (text_box_position_x + 90, text_box_position_y + 150))
        window.blit(self.textLevelOnePage.instruction_textLine2, (text_box_position_x + 285, text_box_position_y + 200))

    def showEndText(self):
        window.blit(self.textLevelOnePage.end_textLine1, (text_box_position_x - 60, text_box_position_y - 100))
        window.blit(self.textLevelOnePage.end_textLine2, (text_box_position_x - 60, text_box_position_y - 50))
        window.blit(self.textLevelOnePage.end_textLine3, (text_box_position_x - 60, text_box_position_y))
        window.blit(self.textLevelOnePage.end_textLine4, (text_box_position_x - 60, text_box_position_y + 50))

    def showExitText(self):
        window.blit(self.textLevelOnePage.exit_textLine1, (text_box_position_x + 24, text_box_position_y + 45))
        window.blit(self.textLevelOnePage.exit_textLine2, (text_box_position_x + 24, text_box_position_y + 95))
