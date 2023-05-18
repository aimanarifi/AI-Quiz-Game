from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.MainPageText import MainPageText


class MainPage:
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/mainBackground.jpg')
        self.mainPageText = MainPageText()

        # The button to enter the first level
        self.button_levelOne = pygame.Rect(545, 460, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelOne)
        self.text_levelOne = font.render("Click here to start level one!", True, (255, 255, 255))
        self.text_rect_levelOne = self.text_levelOne.get_rect(center=self.button_levelOne.center)

        # The button to enter the second level
        self.button_levelTwo = pygame.Rect(545, 510, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelTwo)
        self.text_levelTwo = font.render("Click here to start level two!", True, (255, 255, 255))
        self.text_rect_levelTwo = self.text_levelTwo.get_rect(center=self.button_levelTwo.center)

        # The button to enter the third level
        self.button_levelThree = pygame.Rect(545, 560, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelThree)
        self.text_levelThree = font.render("Click here to start level three!", True, (255, 255, 255))
        self.text_rect_levelThree = self.text_levelThree.get_rect(center=self.button_levelThree.center)

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showIntroductionTextLine(self):
        window.blit(self.mainPageText.introduction_textLine1, (230, 170))
        window.blit(self.mainPageText.introduction_textLine2, (230, 220))
        window.blit(self.mainPageText.introduction_textLine3, (230, 270))
        window.blit(self.mainPageText.introduction_textLine4, (230, 320))
        window.blit(self.mainPageText.introduction_textLine5, (450, 370))

    def showButtons(self):
        # Players need to complete the previous levels before they can proceed to the next levels
        window.blit(self.text_levelOne, self.text_rect_levelOne)
        window.blit(self.text_levelTwo, self.text_rect_levelTwo)
        window.blit(self.text_levelThree, self.text_rect_levelThree)
