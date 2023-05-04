import time

from Window import pygame
from Pages import MainPage, LevelOnePage
from Levels import LevelOne

# initialise all classes needed
mainPage = MainPage()
levelOne = LevelOne()
levelOnePage = LevelOnePage()


def startGame():
    """
    This is where the game start, it should be called from the outside world.
    """
    while True:
        if not levelOne.gameIsOn:
            getMainPageEvents()
            mainPage.showBackground()
            mainPage.showWelcomeTextLine()
        elif levelOne.gameIsOn:
            getLevelOnePageEvents(levelOne.plane)
            levelOnePage.showBackground()
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
            elif levelOnePage.needTOShowInstructionText:
                if levelOnePage.instruction_textStartTime == 0:
                    levelOnePage.instruction_textStartTime = time.time()
                levelOnePage.instruction_textEndTime = time.time()
                levelOnePage.instruction_textLastTime = levelOnePage.instruction_textEndTime - levelOnePage.instruction_textStartTime
                if levelOnePage.instruction_textLastTime <= 6:
                    levelOnePage.showInstructionText()
                else:
                    levelOnePage.needTOShowInstructionText = False
            levelOne.loadStuff(levelOnePage)

        pygame.display.update()


def getLevelOnePageEvents(plane):
    """
    This function will get all events for the level one page
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
                plane.shoot(plane.position_x + 35, plane.position_y)
        elif event.type == pygame.KEYUP:
            plane.speed_x = 0
            plane.speed_y = 0


def getMainPageEvents():
    """
    This function will get all events for the main page
    """
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mainPage.button.collidepoint(event.pos):
                levelOne.gameIsOn = True


if __name__ == '__main__':
    startGame()
