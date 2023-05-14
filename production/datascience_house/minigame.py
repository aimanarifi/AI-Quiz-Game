"""
Last modified: 03/05/2023
Written by Zhongjie Huang
"""
import time

from production.datascience_house.Window import pygame
from production.datascience_house.Pages import MainPage, LevelOnePage, LevelTwoPage, LevelThreePage, playMusic
from production.datascience_house.Levels import LevelOne, LevelTwo, LevelThree, showQuestions

# initialise all classes needed and play music

mainPage = MainPage()
levelOne = LevelOne()
levelTwo = LevelTwo()
levelThree = LevelThree()
levelOnePage = LevelOnePage()
levelTwoPage = LevelTwoPage()
levelThreePage = LevelThreePage()
# playMusic()    this function needs to be called in start game


def startGame():
    clock = pygame.time.Clock()  # 控制游戏的帧率
    playMusic()
    """
    This is where the game start, it should be called from the outside world.
    """
    while True:
        clock.tick(60)
        # 如果玩家没有进入任何关卡, 显示主页面, 按钮选择并播放音乐
        if not levelOne.gameIsOn and not levelTwo.gameIsOn and not levelThree.gameIsOn:
            mainPage.showBackground()
            mainPage.showWelcomeTextLine()
            mainPage.showButtons(levelTwo, levelThree)
            getMainPageEvents()
        # 如果玩家选择进入第一关
        elif levelOne.gameIsOn:
            levelOnePage.showBackground()
            # 显示10秒欢迎文字
            if levelOnePage.needTOShowWelcomeText:
                if levelOnePage.welcome_textStartTime == 0:
                    levelOnePage.welcome_textStartTime = time.time()
                levelOnePage.welcome_textEndTime = time.time()
                levelOnePage.welcome_textLastTime = levelOnePage.welcome_textEndTime - levelOnePage.welcome_textStartTime
                if levelOnePage.welcome_textLastTime <= 10:
                    levelOnePage.showWelcomeText()
                else:
                    levelOnePage.needTOShowWelcomeText = False
                    levelOnePage.needTOShowInstructionText = True
            # 10秒欢迎文字显示完后, 显示6秒提醒文字
            if levelOnePage.needTOShowInstructionText:
                if levelOnePage.instruction_textStartTime == 0:
                    levelOnePage.instruction_textStartTime = time.time()
                levelOnePage.instruction_textEndTime = time.time()
                levelOnePage.instruction_textLastTime = levelOnePage.instruction_textEndTime - levelOnePage.instruction_textStartTime
                if levelOnePage.instruction_textLastTime <= 6:
                    levelOnePage.showInstructionText()
                else:
                    levelOnePage.needTOShowInstructionText = False
            # 6秒提醒文字显示完后, 开始游戏
            levelOne.loadStuff(levelOnePage)
            getEvents(levelOne.plane)
        # 如果玩家选择进入第二关
        elif levelTwo.gameIsOn:
            levelTwoPage.showBackground()
            # 如果玩家没有答题, 显示欢迎文字和按钮选项
            if not levelTwo.questionAnswered:
                if levelTwoPage.needToShowWelcome1Text and levelTwoPage.needToShowButtons:
                    levelTwoPage.showWelcome1Text()
                    levelTwoPage.showButtons()
                # 如果玩家选择回答问题
                elif levelTwo.acceptChallenge:
                    # 显示5秒提醒文字
                    if levelTwoPage.needToShowIntroduction1Text:
                        if levelTwoPage.introduction1_textStartTime == 0:
                            levelTwoPage.introduction1_textStartTime = time.time()
                        levelTwoPage.introduction1_textEndTime = time.time()
                        levelTwoPage.introduction1_textLastTime = levelTwoPage.introduction1_textEndTime - levelTwoPage.introduction1_textStartTime
                        if levelTwoPage.introduction1_textLastTime <= 5:
                            levelTwoPage.showIntroduction1Text()
                        else:
                            levelTwoPage.needToShowIntroduction1Text = False
                            levelTwoPage.timeToDoQuestions = True
                    # 玩家开始答题
                    if levelTwoPage.timeToDoQuestions:
                        pygame.mixer.music.pause()
                        showQuestions(levelTwo)
                        # 如果玩家答题正确
                        if levelTwo.questionScore/len(levelTwo.allQuestions) >= 0.7:
                            levelTwo.questionAnswered = True
                            levelTwo.acceptChallenge = False
                        # 如果玩家答题错误, 显示3秒提醒文字, 随后返回欢迎文字和按钮选项
                        else:
                            pygame.mixer.music.unpause()
                            if levelTwoPage.needToShowIntroduction2Text:
                                if levelTwoPage.introduction2_textStartTime == 0:
                                    levelTwoPage.introduction2_textStartTime = time.time()
                                levelTwoPage.introduction2_textEndTime = time.time()
                                levelTwoPage.introduction2_textLastTime = levelTwoPage.introduction2_textEndTime - levelTwoPage.introduction2_textStartTime
                                if levelTwoPage.introduction2_textLastTime <= 3:
                                    levelTwoPage.showIntroduction2Text()
                                else:
                                    levelTwoPage.needToShowIntroduction2Text = False
                                    levelTwo.acceptChallenge = False
                # 如果玩家不选择答题, 则退出第二关
                elif levelTwo.refuseChallenge:
                    levelTwo.gameIsOn = False
                    levelTwo.acceptChallenge = False
                    levelTwo.refuseChallenge = False
            # 如果玩家已经答题
            else:
                pygame.mixer.music.unpause()
                # 显示5秒提醒文字
                if levelTwoPage.needToShowWelcome2Text:
                    if levelTwoPage.welcome2_textStartTime == 0:
                        levelTwoPage.welcome2_textStartTime = time.time()
                    levelTwoPage.welcome2_textEndTime = time.time()
                    levelTwoPage.welcome2_textLastTime = levelTwoPage.welcome2_textEndTime - levelTwoPage.welcome2_textStartTime
                    if levelTwoPage.welcome2_textLastTime <= 5:
                        levelTwoPage.showWelcome2Text()
                    else:
                        levelTwoPage.needToShowWelcome2Text = False
                        levelTwoPage.needToShowWelcome3Text = True
                # 5秒提醒文字显示完后显示10秒欢迎文字
                if levelTwoPage.needToShowWelcome3Text:
                    if levelTwoPage.welcome3_textStartTime == 0:
                        levelTwoPage.welcome3_textStartTime = time.time()
                    levelTwoPage.welcome3_textEndTime = time.time()
                    levelTwoPage.welcome3_textLastTime = levelTwoPage.welcome3_textEndTime - levelTwoPage.welcome3_textStartTime
                    if levelTwoPage.welcome3_textLastTime <= 10:
                        levelTwoPage.showWelcome3Text()
                    else:
                        levelTwoPage.needToShowWelcome3Text = False
                        levelTwoPage.needToShowInstructionText = True
                # 10秒欢迎文字显示完后, 显示5秒提醒文字
                if levelTwoPage.needToShowInstructionText:
                    if levelTwoPage.instruction_textStartTime == 0:
                        levelTwoPage.instruction_textStartTime = time.time()
                    levelTwoPage.instruction_textEndTime = time.time()
                    levelTwoPage.instruction_textLastTime = levelTwoPage.instruction_textEndTime - levelTwoPage.instruction_textStartTime
                    if levelTwoPage.instruction_textLastTime <= 5:
                        levelTwoPage.showInstructionText()
                    else:
                        levelTwoPage.needToShowInstructionText = False
                # 5秒提醒文字显示完后, 开始游戏
                levelTwo.loadStuff(levelTwoPage)
            getEvents(levelTwo.plane)
        # 如果玩家选择进入第三关
        elif levelThree.gameIsOn:
            levelThreePage.showBackground()
            # 如果玩家没有答题, 显示欢迎文字和按钮选项
            if not levelThree.questionAnswered:
                if levelThreePage.needToShowWelcome1Text and levelThreePage.needToShowButtons:
                    levelThreePage.showWelcome1Text()
                    levelThreePage.showButtons()
                # 如果玩家选择答题
                elif levelThree.acceptChallenge:
                    # 显示5秒提醒文字
                    if levelThreePage.needToShowIntroduction1Text:
                        if levelThreePage.introduction1_textStartTime == 0:
                            levelThreePage.introduction1_textStartTime = time.time()
                        levelThreePage.introduction1_textEndTime = time.time()
                        levelThreePage.introduction1_textLastTime = levelThreePage.introduction1_textEndTime - levelThreePage.introduction1_textStartTime
                        if levelThreePage.introduction1_textLastTime <= 5:
                            levelThreePage.showIntroduction1Text()
                        else:
                            levelThreePage.needToShowIntroduction1Text = False
                            levelThreePage.timeToDoQuestions = True
                    # 玩家开始答题
                    if levelThreePage.timeToDoQuestions:
                        pygame.mixer.music.pause()
                        showQuestions(levelThree)
                        # 如果玩家答题正确
                        if levelThree.questionScore / len(levelThree.allQuestions) >= 0.7:
                            levelThree.questionAnswered = True
                            levelThree.acceptChallenge = False
                        # 如果玩家答题错误, 返回欢迎文字和按钮选项
                        else:
                            pygame.mixer.music.unpause()
                            if levelThreePage.needToShowIntroduction2Text:
                                if levelThreePage.introduction2_textStartTime == 0:
                                    levelThreePage.introduction2_textStartTime = time.time()
                                levelThreePage.introduction2_textEndTime = time.time()
                                levelThreePage.introduction2_textLastTime = levelThreePage.introduction2_textEndTime - levelThreePage.introduction2_textStartTime
                                if levelThreePage.introduction2_textLastTime <= 3:
                                    levelThreePage.showIntroduction2Text()
                                else:
                                    levelThreePage.needToShowIntroduction2Text = False
                                    levelThree.acceptChallenge = False
                # 如果玩家不选择答题, 则退出第三关
                elif levelThree.refuseChallenge:
                    levelThree.gameIsOn = False
                    levelThree.acceptChallenge = False
                    levelThree.refuseChallenge = False
            # 如果玩家已经答题
            else:
                pygame.mixer.music.unpause()
                # 显示5秒提醒文字
                if levelThreePage.needToShowWelcome2Text:
                    if levelThreePage.welcome2_textStartTime == 0:
                        levelThreePage.welcome2_textStartTime = time.time()
                    levelThreePage.welcome2_textEndTime = time.time()
                    levelThreePage.welcome2_textLastTime = levelThreePage.welcome2_textEndTime - levelThreePage.welcome2_textStartTime
                    if levelThreePage.welcome2_textLastTime <= 50:
                        levelThreePage.showWelcome_afterQuestionAnsweredText()
                    else:
                        levelThreePage.needToShowWelcome2Text = False
                        levelThreePage.needToShowWelcome3Text = True
                # 5秒提醒文字显示完后, 显示10秒欢迎文字
                if levelThreePage.needToShowWelcome3Text:
                    if levelThreePage.welcome3_textStartTime == 0:
                        levelThreePage.welcome3_textStartTime = time.time()
                    levelThreePage.welcome3_textEndTime = time.time()
                    levelThreePage.welcome3_textLastTime = levelThreePage.welcome3_textEndTime - levelThreePage.welcome3_textStartTime
                    if levelThreePage.welcome3_textLastTime <= 10:
                        levelThreePage.showWelcome3Text()
                    else:
                        levelThreePage.needToShowWelcome3Text = False
                        levelThreePage.needToShowInstructionText = True
                # 10秒欢迎文字显示完后, 显示5秒提醒文字
                if levelThreePage.needToShowInstructionText:
                    if levelThreePage.instruction_textStartTime == 0:
                        levelThreePage.instruction_textStartTime = time.time()
                    levelThreePage.instruction_textEndTime = time.time()
                    levelThreePage.instruction_textLastTime = levelThreePage.instruction_textEndTime - levelThreePage.instruction_textStartTime
                    if levelThreePage.instruction_textLastTime <= 5:
                        levelThreePage.showInstructionText()
                    else:
                        levelThreePage.needToShowInstructionText = False
                # 5秒提醒文字显示完后, 开始游戏
                levelThree.loadStuff(levelThreePage)
            getEvents(levelThree.plane)

        pygame.display.update()


def getMainPageEvents():
    """
    This function will get all events from the main page
    """
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mainPage.button_levelOne.collidepoint(event.pos):
                levelOne.gameIsOn = True
            elif mainPage.button_levelTwo.collidepoint(event.pos):
                levelTwo.gameIsOn = True
            elif mainPage.button_levelThree.collidepoint(event.pos):
                levelThree.gameIsOn = True


def getEvents(plane):
    """
    This function will get all events from the level one page
    """
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # move left
                plane.speed_x = plane.velocity2
            elif event.key == pygame.K_RIGHT:  # move right
                plane.speed_x = plane.velocity1
            elif event.key == pygame.K_UP:  # move up
                plane.speed_y = plane.velocity2
            elif event.key == pygame.K_DOWN:  # move down
                plane.speed_y = plane.velocity1
            elif event.key == pygame.K_w:  # shoot bullet
                if levelOne.gameIsOn:
                    plane.shoot(plane.position_x + 35, plane.position_y)
                elif levelTwo.gameIsOn:
                    plane.shoot_threeBullets(plane.position_x + 35, plane.position_y, 2, 10)
                elif levelThree.gameIsOn:
                    plane.shoot_threeBullets(plane.position_x + 35, plane.position_y, 2, 10)
            elif event.key == pygame.K_r and levelThree.gameIsOn:
                plane.shoot_auto_track(plane.position_x + 35, plane.position_y)
        elif event.type == pygame.KEYUP:
            plane.speed_x = 0
            plane.speed_y = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if levelTwo.gameIsOn:
                if levelTwoPage.button_acceptChallenge.collidepoint(event.pos):
                    levelTwo.acceptChallenge = True
                    levelTwoPage.needToShowWelcome1Text = False
                    levelTwoPage.needToShowButtons = False
                elif levelTwoPage.button_refuseChallenge.collidepoint(event.pos):
                    levelTwo.refuseChallenge = True
            if levelThree.gameIsOn:
                if levelThreePage.button_acceptChallenge.collidepoint(event.pos):
                    levelThree.acceptChallenge = True
                    levelThreePage.needToShowWelcome1Text = False
                    levelThreePage.needToShowButtons = False
                elif levelThreePage.button_refuseChallenge.collidepoint(event.pos):
                    levelThreePage.refuseChallenge = True


if __name__ == '__main__':
    startGame()
