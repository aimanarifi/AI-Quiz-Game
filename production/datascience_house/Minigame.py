"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
from production.datascience_house.Window import pygame

from production.datascience_house.Levels.Pages.MainPage import MainPage

from production.datascience_house.Levels.LevelOne import LevelOne
from production.datascience_house.Levels.LevelTwo import LevelTwo
from production.datascience_house.Levels.LevelThree import LevelThree

from production.datascience_house.Events import getMainPageEvents, getLevelPageEvents


def startGame():
    """
    This is where the game start, it should be called from the outside world.
    """
    clock = pygame.time.Clock()  # Control the frame rate of the game

    mainPage = MainPage()
    levelOne = LevelOne()
    levelTwo = LevelTwo()
    levelThree = LevelThree()

    pygame.mixer.music.load('datascience_house/music/game.mp3')
    pygame.mixer.music.play(-1)

    while not mainPage.goBack:
        clock.tick(60)
        # If the player hasn't entered any level, display the main page with button selection
        if not levelOne.gameIsOn and not levelTwo.gameIsOn and not levelThree.gameIsOn:
            mainPage.showBackground()
            mainPage.showIntroductionTextLine()
            mainPage.showButtons()
            getMainPageEvents(mainPage, levelOne, levelTwo, levelThree)
        # If the player selects to enter the first level
        elif levelOne.gameIsOn:
            levelOne.loadStuff()
            getLevelPageEvents(levelOne.plane, levelOne, levelOne.levelOnePage)
        # If the player selects to enter the second level
        elif levelTwo.gameIsOn:
            levelTwo.loadStuff()
            getLevelPageEvents(levelTwo.plane, levelTwo, levelTwo.levelTwoPage)
        # If the player selects to enter the third level
        elif levelThree.gameIsOn:
            levelThree.loadStuff()
            getLevelPageEvents(levelThree.plane, levelThree, levelThree.levelThreePage)

        pygame.display.update()

    del clock
    del mainPage
    del levelOne
    del levelTwo
    del levelThree


if __name__ == '__main__':
    startGame()
