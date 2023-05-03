import pygame
from project.production.datascience_house.Levels import LevelOne
# from project.production.datascience_house.minigame import startGame


def startGame():

    levelOne = LevelOne()
    levelOne.gameIsOn = True

    while True:
        if levelOne.gameIsOn:
            getEvents(levelOne.plane)
            levelOne.show()

        pygame.display.update()


def getEvents(plane):
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


if __name__ == '__main__':
    startGame()
