"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import time
from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.LevelTwoPageText import LevelTwoPageText


class LevelTwoPage:
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/LevelTwoBackground.jpg')
        self.levelTwoPageText = LevelTwoPageText()

        # The display attributes for the introduction text when the player doesn't answer the questions
        self.needToShowIntroduction1Text = True

        # The display attributes for the button options
        self.needToShowButtons = True

        # The display attributes for the reminder text after the player selects an answer
        self.needToShowReminder1Text = True
        self.reminder1_textStartTime = 0
        self.reminder1_textEndTime = 0
        self.reminder1_textLastTime = 0

        # The display attributes for the reminder text when the player fails to answer a question
        self.reminder2_textStartTime = 0
        self.reminder2_textEndTime = 0
        self.reminder2_textLastTime = 0

        self.showText_beforeGame = True

        # The display attributes for the reminder text when the player successfully answers a question
        self.needToShowReminder3Text = True
        self.reminder3_textStartTime = 0
        self.reminder3_textEndTime = 0
        self.reminder3_textLastTime = 0

        # The display attributes for the introduction text when the player has already answered a question
        self.needToShowIntroduction2Text = False
        self.introduction2_textStartTime = 0
        self.introduction2_textEndTime = 0
        self.introduction2_textLastTime = 0

        # The display attributes for the reminder text regarding the aircraft's performance
        self.needToShowReminder4Text = False
        self.reminder4_textStartTime = 0
        self.reminder4_textEndTime = 0
        self.reminder4_textLastTime = 0

        # The display attributes for the reminder text when the game is over
        self.needTOShowEndText = True
        self.end_textStartTime = 0
        self.end_textEndTime = 0
        self.end_textLastTime = 0

        # The display attributes for the reminder text when exiting the level
        self.needToShowExitText = False

        self.needToShowDefeatedText = True
        self.defeated_text_startTime = 0
        self.defeated_text_endTime = 0
        self.defeated_text_lastTime = 0

        # The button for the player to choose to answer the questions
        self.button_acceptChallenge = pygame.Rect(385, 500, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_acceptChallenge)
        self.text_acceptChallenge = font.render("Click here to start!", True, (255, 255, 255))
        self.text_rect_acceptChallenge = self.text_acceptChallenge.get_rect(center=self.button_acceptChallenge.center)

        # The button for the player to refuse answering the questions
        self.button_refuseChallenge = pygame.Rect(695, 500, 210, 40)
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
            window.blit(self.levelTwoPageText.introduction1_textLine1, (290, 170))
            window.blit(self.levelTwoPageText.introduction1_textLine2, (290, 220))
            window.blit(self.levelTwoPageText.introduction1_textLine3, (290, 270))
            window.blit(self.levelTwoPageText.introduction1_textLine4, (290, 320))
            window.blit(self.levelTwoPageText.introduction1_textLine5, (290, 370))
            window.blit(self.levelTwoPageText.introduction1_textLine6, (290, 420))

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
            countdown_text_time_left = 7 - self.reminder1_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (7 - self.reminder1_textLastTime) >= 0:
                window.blit(self.levelTwoPageText.reminder1_textLine1, (420, 270))
                window.blit(self.levelTwoPageText.reminder1_textLine2, (420, 320))
                window.blit(self.levelTwoPageText.reminder1_textLine3, (420, 370))
                window.blit(self.levelTwoPageText.reminder1_textLine4, (575, 420))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminder1Text = False
                self.reminder1_textStartTime = 0
                self.reminder1_textEndTime = 0
                self.reminder1_textLastTime = 0

    def showReminder2Text(self, levelTwo):
        if self.reminder2_textStartTime == 0:
            self.reminder2_textStartTime = time.time()
        self.reminder2_textEndTime = time.time()
        self.reminder2_textLastTime = self.reminder2_textEndTime - self.reminder2_textStartTime
        countdown_text_time_left = 7 - self.reminder2_textLastTime
        countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
        if (7 - self.reminder2_textLastTime) >= 0:
            window.blit(self.levelTwoPageText.reminder2_textLine1, (325, 260))
            window.blit(self.levelTwoPageText.reminder2_textLine2, (325, 310))
            window.blit(self.levelTwoPageText.reminder2_textLine3, (325, 360))
            window.blit(self.levelTwoPageText.reminder2_textLine4, (325, 410))
            window.blit(countdown_text, (10, 690))
        else:
            self.needToShowIntroduction1Text = True
            self.needToShowButtons = True
            levelTwo.acceptChallenge = False
            levelTwo.needToDoQuestions = True
            self.reminder2_textStartTime = 0
            self.reminder2_textEndTime = 0
            self.reminder2_textLastTime = 0

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
            countdown_text_time_left = 7 - self.reminder3_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (7 - self.reminder3_textLastTime) >= 0:
                window.blit(self.levelTwoPageText.reminder3_textLine1, (315, 283))
                window.blit(self.levelTwoPageText.reminder3_textLine2, (315, 333))
                window.blit(self.levelTwoPageText.reminder3_textLine3, (315, 383))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminder3Text = False
                self.needToShowIntroduction2Text = True
                self.reminder3_textStartTime = 0
                self.reminder3_textEndTime = 0
                self.reminder3_textLastTime = 0

    def showIntroduction2Text(self):
        if self.needToShowIntroduction2Text:
            if self.introduction2_textStartTime == 0:
                self.introduction2_textStartTime = time.time()
            self.introduction2_textEndTime = time.time()
            self.introduction2_textLastTime = self.introduction2_textEndTime - self.introduction2_textStartTime
            countdown_text_time_left = 12 - self.introduction2_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (12 - self.introduction2_textLastTime) >= 0:
                window.blit(self.levelTwoPageText.introduction2_textLine1, (315, 170))
                window.blit(self.levelTwoPageText.introduction2_textLine2, (315, 220))
                window.blit(self.levelTwoPageText.introduction2_textLine3, (315, 270))
                window.blit(self.levelTwoPageText.introduction2_textLine4, (315, 320))
                window.blit(self.levelTwoPageText.introduction2_textLine5, (315, 370))
                window.blit(self.levelTwoPageText.introduction2_textLine6, (315, 420))
                window.blit(self.levelTwoPageText.introduction2_textLine7, (587, 470))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowIntroduction2Text = False
                self.needToShowReminder4Text = True
                self.introduction2_textStartTime = 0
                self.introduction2_textEndTime = 0
                self.introduction2_textLastTime = 0

    def showReminder4Text(self):
        if self.needToShowReminder4Text:
            if self.reminder4_textStartTime == 0:
                self.reminder4_textStartTime = time.time()
            self.reminder4_textEndTime = time.time()
            self.reminder4_textLastTime = self.reminder4_textEndTime - self.reminder4_textStartTime
            countdown_text_time_left = 7 - self.reminder4_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (7 - self.reminder4_textLastTime) >= 0:
                window.blit(self.levelTwoPageText.reminder4_textLine, (290, 513))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminder4Text = False
                self.showText_beforeGame = False
                self.reminder4_textStartTime = 0
                self.reminder4_textEndTime = 0
                self.reminder4_textLastTime = 0

    def showEndText(self):
        window.blit(self.levelTwoPageText.end_textLine1, (317, 170))
        window.blit(self.levelTwoPageText.end_textLine2, (317, 220))
        window.blit(self.levelTwoPageText.end_textLine3, (317, 270))
        window.blit(self.levelTwoPageText.end_textLine4, (317, 320))
        window.blit(self.levelTwoPageText.end_textLine5, (317, 370))
        window.blit(self.levelTwoPageText.end_textLine6, (317, 420))

    def showExitText(self):
        window.blit(self.levelTwoPageText.exit_textLine1, (314, 315))
        window.blit(self.levelTwoPageText.exit_textLine2, (337, 365))
