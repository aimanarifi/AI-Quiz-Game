import time
from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.LevelOnePageText import LevelOnePageText


class LevelOnePage:
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
            countdown_text_time_left = 11 - self.introduction_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (11 - self.introduction_textLastTime) >= 0:
                window.blit(self.levelOnePageText.introduction_textLine1, (280, 170))
                window.blit(self.levelOnePageText.introduction_textLine2, (280, 220))
                window.blit(self.levelOnePageText.introduction_textLine3, (280, 270))
                window.blit(self.levelOnePageText.introduction_textLine4, (280, 320))
                window.blit(self.levelOnePageText.introduction_textLine5, (565, 370))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowIntroductionText = False
                self.needToShowReminder1Text = True

    def showReminderText(self):
        if self.needToShowReminder1Text:
            if self.reminder_textStartTime == 0:
                self.reminder_textStartTime = time.time()
            self.reminder_textEndTime = time.time()
            self.reminder_textLastTime = self.reminder_textEndTime - self.reminder_textStartTime
            countdown_text_time_left = 6 - self.reminder_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (6 - self.reminder_textLastTime) >= 0:
                window.blit(self.levelOnePageText.reminder_textLine1, (355, 500))
                window.blit(self.levelOnePageText.reminder_textLine2, (550, 550))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminder1Text = False
                self.showText_beforeGame = False

    def showEndText(self):
        window.blit(self.levelOnePageText.end_textLine1, (245, 170))
        window.blit(self.levelOnePageText.end_textLine2, (245, 220))
        window.blit(self.levelOnePageText.end_textLine3, (245, 270))
        window.blit(self.levelOnePageText.end_textLine4, (245, 320))
        window.blit(self.levelOnePageText.end_textLine5, (480, 370))

    def showExitText(self):
        window.blit(self.levelOnePageText.exit_textLine1, (314, 315))
        window.blit(self.levelOnePageText.exit_textLine2, (337, 365))
