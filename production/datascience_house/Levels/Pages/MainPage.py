from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.MainPageText import MainPageText


class MainPage:
    """
    This class is used to design the main page, including a background image, text and a button.
    It provides two methods which will be called by its object to show all the things.
    """
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/mainBackground.jpg')
        self.mainPageText = MainPageText()

        # 进入第一关的按钮
        self.button_levelOne = pygame.Rect(545, 460, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelOne)
        self.text_levelOne = font.render("Click here to start level one!", True, (255, 255, 255))
        self.text_rect_levelOne = self.text_levelOne.get_rect(center=self.button_levelOne.center)

        # 进入第二关的按钮
        self.button_levelTwo = pygame.Rect(545, 510, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelTwo)
        self.text_levelTwo = font.render("Click here to start level two!", True, (255, 255, 255))
        self.text_rect_levelTwo = self.text_levelTwo.get_rect(center=self.button_levelTwo.center)

        # 进入第三关的按钮
        self.button_levelThree = pygame.Rect(545, 560, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelThree)
        self.text_levelThree = font.render("Click here to start level three!", True, (255, 255, 255))
        self.text_rect_levelThree = self.text_levelThree.get_rect(center=self.button_levelThree.center)

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showIntroductionTextLine(self):
        window.blit(self.mainPageText.introduction_textLine1, (240, 170))
        window.blit(self.mainPageText.introduction_textLine2, (240, 220))
        window.blit(self.mainPageText.introduction_textLine3, (240, 270))
        window.blit(self.mainPageText.introduction_textLine4, (240, 320))
        window.blit(self.mainPageText.introduction_textLine5, (240, 370))

    def showButtons(self, levelTwo, levelThree):
        # 玩家需要先完成前面的关卡才能进入后面的关卡
        window.blit(self.text_levelOne, self.text_rect_levelOne)
        # if levelTwo.passed:
        window.blit(self.text_levelTwo, self.text_rect_levelTwo)
        # if levelThree.passed:
        window.blit(self.text_levelThree, self.text_rect_levelThree)
