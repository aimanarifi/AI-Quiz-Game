import time
from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.LevelTwoPageText import LevelTwoPageText


class LevelTwoPage:
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/LevelTwoBackground.jpg')
        self.levelTwoPageText = LevelTwoPageText()

        # 欢迎文字(玩家没有答题)的显示属性
        self.needToShowIntroduction1Text = True

        # 按钮选项的显示属性
        self.needToShowButtons = True

        # 提醒文字(玩家选择答题后)的显示属性
        self.needToShowReminder1Text = True
        self.reminder1_textStartTime = 0
        self.reminder1_textEndTime = 0
        self.reminder1_textLastTime = 0

        # 提醒文字(玩家答题失败)的显示属性
        self.reminder2_textStartTime = 0
        self.reminder2_textEndTime = 0
        self.reminder2_textLastTime = 0

        self.showText_beforeGame = True

        # 提醒文字(玩家答题成功)的显示属性
        self.needToShowReminder3Text = True
        self.reminder3_textStartTime = 0
        self.reminder3_textEndTime = 0
        self.reminder3_textLastTime = 0

        # 欢迎文字(玩家已答题)的显示属性
        self.needToShowIntroduction2Text = False
        self.introduction2_textStartTime = 0
        self.introduction2_textEndTime = 0
        self.introduction2_textLastTime = 0

        # 提醒文字(飞机性能)的显示属性
        self.needToShowReminder4Text = False
        self.reminder4_textStartTime = 0
        self.reminder4_textEndTime = 0
        self.reminder4_textLastTime = 0

        # 提醒文字(游戏结束)的显示属性
        self.needTOShowEndText = True
        self.end_textStartTime = 0
        self.end_textEndTime = 0
        self.end_textLastTime = 0

        # 提醒文字(退出关卡)的显示属性
        self.needToShowExitText = False

        # 玩家选择答题的按钮
        self.button_acceptChallenge = pygame.Rect(375, 500, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_acceptChallenge)
        self.text_acceptChallenge = font.render("Click here to start!", True, (255, 255, 255))
        self.text_rect_acceptChallenge = self.text_acceptChallenge.get_rect(center=self.button_acceptChallenge.center)

        # 玩家拒绝答题的按钮
        self.button_refuseChallenge = pygame.Rect(685, 500, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_refuseChallenge)
        self.text_refuseChallenge = font.render("Click here to go back!", True, (255, 255, 255))
        self.text_rect_refuseChallenge = self.text_refuseChallenge.get_rect(center=self.button_refuseChallenge.center)

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showTextBeforeQuestions(self, levelTwo):
        if not levelTwo.acceptChallenge:
            self.showIntroduction1Text()
            self.showButtons()

    def showIntroduction1Text(self):
        if self.needToShowIntroduction1Text:
            window.blit(self.levelTwoPageText.introduction1_textLine1, (280, 170))
            window.blit(self.levelTwoPageText.introduction1_textLine2, (280, 220))
            window.blit(self.levelTwoPageText.introduction1_textLine3, (280, 270))
            window.blit(self.levelTwoPageText.introduction1_textLine4, (280, 320))
            window.blit(self.levelTwoPageText.introduction1_textLine5, (280, 370))
            window.blit(self.levelTwoPageText.introduction1_textLine6, (280, 420))

    def showButtons(self):
        if self.needToShowButtons:
            window.blit(self.text_acceptChallenge, self.text_rect_acceptChallenge)
            window.blit(self.text_refuseChallenge, self.text_rect_refuseChallenge)

    def showReminder1Text(self):
        if self.needToShowReminder1Text:
            if self.reminder1_textStartTime == 0:
                self.reminder1_textStartTime = time.time()
            self.reminder1_textEndTime = time.time()
            self.reminder1_textLastTime = self.reminder1_textEndTime - self.reminder1_textStartTime
            if self.reminder1_textLastTime < 5:
                window.blit(self.levelTwoPageText.reminder1_textLine1, (280, 170))
                window.blit(self.levelTwoPageText.reminder1_textLine2, (280, 220))
                window.blit(self.levelTwoPageText.reminder1_textLine3, (280, 270))
            else:
                self.needToShowReminder1Text = False

    def showReminder2Text(self, levelTwo):
        if self.reminder2_textStartTime == 0:
            self.reminder2_textStartTime = time.time()
        self.reminder2_textEndTime = time.time()
        self.reminder2_textLastTime = self.reminder2_textEndTime - self.reminder2_textStartTime
        if self.reminder2_textLastTime < 5:
            window.blit(self.levelTwoPageText.reminder2_textLine1, (280, 170))
            window.blit(self.levelTwoPageText.reminder2_textLine2, (280, 220))
            window.blit(self.levelTwoPageText.reminder2_textLine3, (280, 270))
            window.blit(self.levelTwoPageText.reminder2_textLine4, (280, 320))
        else:
            self.reminder2_textStartTime = 0
            self.reminder2_textEndTime = 0
            self.reminder2_textLastTime = 0
            self.needToShowIntroduction1Text = True
            self.needToShowButtons = True
            levelTwo.acceptChallenge = False
            levelTwo.needToDoQuestions = True

    def showTextBeforeGame(self):
        self.showReminder3Text()
        self.showIntroduction2Text()
        self.showReminder4Text()

    def showReminder3Text(self):
        if self.needToShowReminder3Text:
            if self.reminder3_textStartTime == 0:
                self.reminder3_textStartTime = time.time()
            self.reminder3_textEndTime = time.time()
            self.reminder3_textLastTime = self.reminder3_textEndTime - self.reminder3_textStartTime
            if self.reminder3_textLastTime < 2:
                window.blit(self.levelTwoPageText.reminder3_textLine1, (290, 220))
                window.blit(self.levelTwoPageText.reminder3_textLine2, (290, 270))
                window.blit(self.levelTwoPageText.reminder3_textLine3, (290, 320))
            else:
                self.needToShowReminder3Text = False
                self.needToShowIntroduction2Text = True

    def showIntroduction2Text(self):
        if self.needToShowIntroduction2Text:
            if self.introduction2_textStartTime == 0:
                self.introduction2_textStartTime = time.time()
            self.introduction2_textEndTime = time.time()
            self.introduction2_textLastTime = self.introduction2_textEndTime - self.introduction2_textStartTime
            if self.introduction2_textLastTime < 2:
                window.blit(self.levelTwoPageText.introduction2_textLine1, (280, 170))
                window.blit(self.levelTwoPageText.introduction2_textLine2, (280, 220))
                window.blit(self.levelTwoPageText.introduction2_textLine3, (280, 270))
                window.blit(self.levelTwoPageText.introduction2_textLine4, (280, 320))
                window.blit(self.levelTwoPageText.introduction2_textLine5, (280, 370))
            else:
                self.needToShowIntroduction2Text = False
                self.needToShowReminder4Text = True

    def showReminder4Text(self):
        if self.needToShowReminder4Text:
            if self.reminder4_textStartTime == 0:
                self.reminder4_textStartTime = time.time()
            self.reminder4_textEndTime = time.time()
            self.reminder4_textLastTime = self.reminder4_textEndTime - self.reminder4_textStartTime
            if self.reminder4_textLastTime < 2:
                window.blit(self.levelTwoPageText.reminder4_textLine, (290, 490))
            else:
                self.needToShowReminder4Text = False
                self.showText_beforeGame = False

    def showEndText(self):
        window.blit(self.levelTwoPageText.end_textLine1, (280, 170))
        window.blit(self.levelTwoPageText.end_textLine2, (280, 220))
        window.blit(self.levelTwoPageText.end_textLine3, (280, 270))
        window.blit(self.levelTwoPageText.end_textLine4, (280, 320))
        window.blit(self.levelTwoPageText.end_textLine5, (280, 370))

    def showExitText(self):
        window.blit(self.levelTwoPageText.exit_textLine1, (314, 315))
        window.blit(self.levelTwoPageText.exit_textLine2, (314, 365))
