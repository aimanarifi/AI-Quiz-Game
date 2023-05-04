import time

from Window import pygame
from Pages import MainPage, LevelOnePage
from Levels import LevelOne

mainPage = MainPage()
levelOnePage = LevelOnePage()
levelOne = LevelOne()


def startGame():
    while True:
        if not levelOne.gameIsOn:
            getMainPageEvents()
            mainPage.showBackground()
            mainPage.showWelcomeTextLine()

        elif levelOne.gameIsOn:
            getLevelOnePageEvents(levelOne.plane)
            levelOnePage.showBackground()

            if levelOnePage.needTOShowWelcomeText:
                if levelOnePage.welcomeTextStartTime == 0:
                    levelOnePage.welcomeTextStartTime = time.time()
                levelOnePage.welcomeTextEndTime = time.time()
                levelOnePage.welcomeTextLastTime = levelOnePage.welcomeTextEndTime - levelOnePage.welcomeTextStartTime
                if levelOnePage.welcomeTextLastTime <= 10:
                    levelOnePage.showWelcomeText()
                else:
                    levelOnePage.needTOShowWelcomeText = False
                    levelOnePage.needTOShowInstructionText = True
            elif levelOnePage.needTOShowInstructionText:
                if levelOnePage.instructionTextStartTime == 0:
                    levelOnePage.instructionTextStartTime = time.time()
                levelOnePage.instructionTextEndTime = time.time()
                levelOnePage.instructionTextLastTime = levelOnePage.instructionTextEndTime - levelOnePage.instructionTextStartTime
                if levelOnePage.instructionTextLastTime <= 6:
                    levelOnePage.showInstructionText()
                else:
                    levelOnePage.needTOShowInstructionText = False

            levelOne.loadStuff(levelOnePage)

        pygame.display.update()


def getLevelOnePageEvents(plane):
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
                plane.shoot(plane.position_x + 35, plane.position_y)
        elif event.type == pygame.KEYUP:
            plane.speed_x = 0
            plane.speed_y = 0


def getMainPageEvents():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mainPage.button.collidepoint(event.pos):
                levelOne.gameIsOn = True


if __name__ == '__main__':
    startGame()
