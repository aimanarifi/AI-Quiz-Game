"""
Last modified: 03/05/2023
Written by Zhongjie Huang

这个类定义了游戏的四个页面(主页, 第一关, 第二关和第三关)中的背景, 音乐,和按钮, 以及展示这些和文字的方法
"""
import pygame
from production.datascience_house.Window import window
from production.datascience_house.PageText import TextMainPage, TextLevelOnePage, TextLevelTwoPage, TextLevelThreePage, text_box_position_x, text_box_position_y, font


class MainPage:
    """
    This class is used to design the main page, including a background image, text and a button.
    It provides two methods which will be called by its object to show all the things.
    """
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/mainBackground.jpg')
        self.textMainPage = TextMainPage()

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

    def showWelcomeTextLine(self):
        window.blit(self.textMainPage.welcome_textLine1, (text_box_position_x - 50, text_box_position_y - 100))
        window.blit(self.textMainPage.welcome_textLine2, (text_box_position_x - 50, text_box_position_y - 50))
        window.blit(self.textMainPage.welcome_textLine3, (text_box_position_x - 50, text_box_position_y))
        window.blit(self.textMainPage.welcome_textLine4, (text_box_position_x - 50, text_box_position_y + 50))
        window.blit(self.textMainPage.welcome_textLine5, (text_box_position_x - 50, text_box_position_y + 100))

    def showButtons(self, levelTwo, levelThree):
        # 玩家需要先完成前面的关卡才能进入后面的关卡
        window.blit(self.text_levelOne, self.text_rect_levelOne)
        if levelTwo.passed:
            window.blit(self.text_levelTwo, self.text_rect_levelTwo)
        if levelThree.passed:
            window.blit(self.text_levelThree, self.text_rect_levelThree)


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

        # 欢迎文字的显示属性
        self.needTOShowWelcomeText = True
        self.welcome_textStartTime = 0
        self.welcome_textEndTime = 0
        self.welcome_textLastTime = 0

        # 提醒文字(飞机操控)的显示属性
        self.needTOShowInstructionText = False
        self.instruction_textStartTime = 0
        self.instruction_textEndTime = 0
        self.instruction_textLastTime = 0

        # 提醒文字(游戏结束)的显示属性
        self.needTOShowEndText = True
        self.end_textStartTime = 0
        self.end_textEndTime = 0
        self.end_textLastTime = 0

        # 提醒文字(退出关卡的显示属性
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


class LevelTwoPage:
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/LevelTwoBackground.jpg')
        self.textLevelTwoPage = TextLevelTwoPage()

        # 欢迎文字(玩家没有答题)的显示属性
        self.needToShowWelcome1Text = True

        # 按钮选项的显示属性
        self.needToShowButtons = True

        # 提醒文字(玩家选择答题后)的显示属性
        self.needToShowIntroduction1Text = True
        self.introduction1_textStartTime = 0
        self.introduction1_textEndTime = 0
        self.introduction1_textLastTime = 0

        # 提醒文字(玩家答题失败)的显示属性
        self.needToShowIntroduction2Text = True
        self.introduction2_textStartTime = 0
        self.introduction2_textEndTime = 0
        self.introduction2_textLastTime = 0

        # 玩家是否进入答题状态的控制
        self.timeToDoQuestions = False

        # 提醒文字(玩家答题成功)的显示属性
        self.needToShowWelcome2Text = True
        self.welcome2_textStartTime = 0
        self.welcome2_textEndTime = 0
        self.welcome2_textLastTime = 0

        # 欢迎文字(玩家已答题)的显示属性
        self.needToShowWelcome3Text = False
        self.welcome3_textStartTime = 0
        self.welcome3_textEndTime = 0
        self.welcome3_textLastTime = 0

        # 提醒文字(飞机性能)的显示属性
        self.needToShowInstructionText = False
        self.instruction_textStartTime = 0
        self.instruction_textEndTime = 0
        self.instruction_textLastTime = 0

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

    def showWelcome1Text(self):
        window.blit(self.textLevelTwoPage.welcome1_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelTwoPage.welcome1_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelTwoPage.welcome1_textLine3, (text_box_position_x - 10, text_box_position_y))
        window.blit(self.textLevelTwoPage.welcome1_textLine4, (text_box_position_x - 10, text_box_position_y + 50))
        window.blit(self.textLevelTwoPage.welcome1_textLine5, (text_box_position_x - 10, text_box_position_y + 100))
        window.blit(self.textLevelTwoPage.welcome1_textLine6, (text_box_position_x - 10, text_box_position_y + 150))

    def showButtons(self):
        window.blit(self.text_acceptChallenge, self.text_rect_acceptChallenge)
        window.blit(self.text_refuseChallenge, self.text_rect_refuseChallenge)

    def showIntroduction1Text(self):
        window.blit(self.textLevelTwoPage.introduction1_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelTwoPage.introduction1_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelTwoPage.introduction1_textLine3, (text_box_position_x - 10, text_box_position_y))

    def showIntroduction2Text(self):
        window.blit(self.textLevelTwoPage.introduction2_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelTwoPage.introduction2_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelTwoPage.introduction2_textLine3, (text_box_position_x - 10, text_box_position_y))
        window.blit(self.textLevelTwoPage.introduction2_textLine4, (text_box_position_x - 10, text_box_position_y + 50))

    def showWelcome2Text(self):
        window.blit(self.textLevelTwoPage.welcome2_textLine1, (text_box_position_x, text_box_position_y - 50))
        window.blit(self.textLevelTwoPage.welcome2_textLine2, (text_box_position_x, text_box_position_y))
        window.blit(self.textLevelTwoPage.welcome2_textLine3, (text_box_position_x, text_box_position_y + 50))

    def showWelcome3Text(self):
        window.blit(self.textLevelTwoPage.welcome3_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelTwoPage.welcome3_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelTwoPage.welcome3_textLine3, (text_box_position_x - 10, text_box_position_y))
        window.blit(self.textLevelTwoPage.welcome3_textLine4, (text_box_position_x - 10, text_box_position_y + 50))
        window.blit(self.textLevelTwoPage.welcome3_textLine5, (text_box_position_x - 10, text_box_position_y + 100))

    def showInstructionText(self):
        window.blit(self.textLevelTwoPage.instruction_textLine, (text_box_position_x, text_box_position_y + 220))

    def showEndText(self):
        window.blit(self.textLevelTwoPage.end_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelTwoPage.end_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelTwoPage.end_textLine3, (text_box_position_x - 10, text_box_position_y))
        window.blit(self.textLevelTwoPage.end_textLine4, (text_box_position_x - 10, text_box_position_y + 50))
        window.blit(self.textLevelTwoPage.end_textLine5, (text_box_position_x - 10, text_box_position_y + 100))

    def showExitText(self):
        window.blit(self.textLevelTwoPage.exit_textLine1, (text_box_position_x + 24, text_box_position_y + 45))
        window.blit(self.textLevelTwoPage.exit_textLine2, (text_box_position_x + 24, text_box_position_y + 95))


class LevelThreePage:
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/LevelThreeBackground.png')
        self.textLevelThreePage = TextLevelThreePage()

        # 欢迎文字(玩家没有答题)的显示属性
        self.needToShowWelcome1Text = True

        # 按钮选项的显示属性
        self.needToShowButtons = True

        # 提醒文字(玩家选择答题后)的显示属性
        self.needToShowIntroduction1Text = True
        self.introduction1_textStartTime = 0
        self.introduction1_textEndTime = 0
        self.introduction1_textLastTime = 0

        # 提醒文字(玩家答题失败)的显示属性
        self.needToShowIntroduction2Text = True
        self.introduction2_textStartTime = 0
        self.introduction2_textEndTime = 0
        self.introduction2_textLastTime = 0

        # 玩家是否进入答题状态的控制
        self.timeToDoQuestions = False

        # 提醒文字(玩家答题成功)的显示属性
        self.needToShowWelcome2Text = True
        self.welcome2_textStartTime = 0
        self.welcome2_textEndTime = 0
        self.welcome2_textLastTime = 0

        # 欢迎文字(玩家已答题)的显示属性
        self.needToShowWelcome3Text = False
        self.welcome3_textStartTime = 0
        self.welcome3_textEndTime = 0
        self.welcome3_textLastTime = 0

        # 提醒文字(飞机性能)的显示属性
        self.needToShowInstructionText = False
        self.instruction_textStartTime = 0
        self.instruction_textEndTime = 0
        self.instruction_textLastTime = 0

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

    def showWelcome1Text(self):
        window.blit(self.textLevelThreePage.welcome1_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelThreePage.welcome1_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelThreePage.welcome1_textLine3, (text_box_position_x - 10, text_box_position_y))
        window.blit(self.textLevelThreePage.welcome1_textLine4, (text_box_position_x - 10, text_box_position_y + 50))
        window.blit(self.textLevelThreePage.welcome1_textLine5, (text_box_position_x - 10, text_box_position_y + 100))

    def showButtons(self):
        window.blit(self.text_acceptChallenge, self.text_rect_acceptChallenge)
        window.blit(self.text_refuseChallenge, self.text_rect_refuseChallenge)

    def showIntroduction1Text(self):
        window.blit(self.textLevelThreePage.introduction1_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelThreePage.introduction1_textLine2, (text_box_position_x - 10, text_box_position_y - 50))

    def showIntroduction2Text(self):
        window.blit(self.textLevelThreePage.introduction2_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelThreePage.introduction2_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelThreePage.introduction2_textLine3, (text_box_position_x - 10, text_box_position_y))

    def showWelcome_afterQuestionAnsweredText(self):
        window.blit(self.textLevelThreePage.welcome_afterQuestionAnswered_textLine1, (text_box_position_x - 10, text_box_position_y - 80))
        window.blit(self.textLevelThreePage.welcome_afterQuestionAnswered_textLine2, (text_box_position_x - 10, text_box_position_y - 30))
        window.blit(self.textLevelThreePage.welcome_afterQuestionAnswered_textLine3, (text_box_position_x - 10, text_box_position_y + 20))
        window.blit(self.textLevelThreePage.welcome_afterQuestionAnswered_textLine4, (text_box_position_x - 10, text_box_position_y + 70))
        window.blit(self.textLevelThreePage.welcome_afterQuestionAnswered_textLine5, (text_box_position_x - 10, text_box_position_y + 120))

    def showWelcome3Text(self):
        window.blit(self.textLevelThreePage.welcome3_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelThreePage.welcome3_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelThreePage.welcome3_textLine3, (text_box_position_x - 10, text_box_position_y))
        window.blit(self.textLevelThreePage.welcome3_textLine4, (text_box_position_x - 10, text_box_position_y + 50))
        window.blit(self.textLevelThreePage.welcome3_textLine5, (text_box_position_x - 10, text_box_position_y + 100))

    def showInstructionText(self):
        window.blit(self.textLevelThreePage.instruction_textLine1, (text_box_position_x + 30, text_box_position_y + 150))
        window.blit(self.textLevelThreePage.instruction_textLine2, (text_box_position_x + 50, text_box_position_y + 200))

    def showEndText(self):
        window.blit(self.textLevelThreePage.end_textLine1, (text_box_position_x - 10, text_box_position_y - 100))
        window.blit(self.textLevelThreePage.end_textLine2, (text_box_position_x - 10, text_box_position_y - 50))
        window.blit(self.textLevelThreePage.end_textLine3, (text_box_position_x - 10, text_box_position_y))

    def showExitText(self):
        window.blit(self.textLevelThreePage.exit_textLine1, (text_box_position_x + 24, text_box_position_y + 45))
        window.blit(self.textLevelThreePage.exit_textLine2, (text_box_position_x + 24, text_box_position_y + 95))


def playMusic():
    pygame.mixer.music.load('datascience_house/music/game.mp3')
    pygame.mixer.music.play()
