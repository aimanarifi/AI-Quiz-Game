import time
from production.datascience_house.Window import pygame, window
from production.datascience_house.Levels.Pages.PageText.LevelOnePageText import LevelOnePageText


class LevelOnePage:
    """
    This class is used to design the level one page, including a background image and text.
    Some text only needs to be displayed temporarily and then disappear automatically. I created variables for start, end, and duration to
    track the time changes and achieve this functionality.
    It provides several methods to show all the things.
    """
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/LevelOneBackground.jpg')
        self.levelOnePageText = LevelOnePageText()

        self.showText_beforeGame = True

        # 欢迎文字的显示属性
        self.needToShowIntroductionText = True
        self.introduction_textStartTime = 0
        self.introduction_textEndTime = 0
        self.introduction_textLastTime = 0

        # 提醒文字(飞机操控)的显示属性
        self.needToShowReminder1Text = False
        self.reminder_textStartTime = 0
        self.reminder_textEndTime = 0
        self.reminder_textLastTime = 0

        # 提醒文字(游戏结束)的显示属性
        self.needTOShowEndText = True
        self.end_textStartTime = 0
        self.end_textEndTime = 0
        self.end_textLastTime = 0

        # 提醒文字(退出关卡的显示属性
        self.needToShowExitText = False

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showTextBeforeGame(self):
        if self.showText_beforeGame:
            self.showIntroductionText()
            self.showReminderText()

    def showIntroductionText(self):
        if self.needToShowIntroductionText:
            if self.introduction_textStartTime == 0:
                self.introduction_textStartTime = time.time()
            self.introduction_textEndTime = time.time()
            self.introduction_textLastTime = self.introduction_textEndTime - self.introduction_textStartTime
            if self.introduction_textLastTime < 10:
                window.blit(self.levelOnePageText.introduction_textLine1, (240, 170))
                window.blit(self.levelOnePageText.introduction_textLine2, (240, 220))
                window.blit(self.levelOnePageText.introduction_textLine3, (240, 270))
                window.blit(self.levelOnePageText.introduction_textLine4, (240, 320))
            else:
                self.needToShowIntroductionText = False
                self.needToShowReminder1Text = True

    def showReminderText(self):
        if self.needToShowReminder1Text:
            if self.reminder_textStartTime == 0:
                self.reminder_textStartTime = time.time()
            self.reminder_textEndTime = time.time()
            self.reminder_textLastTime = self.reminder_textEndTime - self.reminder_textStartTime
            if self.reminder_textLastTime < 6:
                window.blit(self.levelOnePageText.reminder_textLine1, (380, 420))
                window.blit(self.levelOnePageText.reminder_textLine2, (575, 470))
            else:
                self.needToShowReminder1Text = False
                self.showText_beforeGame = False

    def showEndText(self):
        window.blit(self.levelOnePageText.end_textLine1, (230, 170))
        window.blit(self.levelOnePageText.end_textLine2, (230, 220))
        window.blit(self.levelOnePageText.end_textLine3, (230, 270))
        window.blit(self.levelOnePageText.end_textLine4, (230, 320))

    def showExitText(self):
        window.blit(self.levelOnePageText.exit_textLine1, (314, 315))
        window.blit(self.levelOnePageText.exit_textLine2, (314, 365))
