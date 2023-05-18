from production.datascience_house.Window import pygame


def getMainPageEvents(mainPage, levelOne, levelTwo, levelThree):
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
            if mainPage.button_levelTwo.collidepoint(event.pos):
                levelTwo.gameIsOn = True
            if mainPage.button_levelThree.collidepoint(event.pos):
                levelThree.gameIsOn = True


def getLevelPageEvents(plane, level, levelPage):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # move left
                plane.speed_x = plane.velocity2
            if event.key == pygame.K_RIGHT:  # move right
                plane.speed_x = plane.velocity1
            if event.key == pygame.K_UP:  # move up
                plane.speed_y = plane.velocity2
            if event.key == pygame.K_DOWN:  # move down
                plane.speed_y = plane.velocity1
            # shoot bullet
            if event.key == pygame.K_w:
                if level.name == 'level one':
                    plane.shoot(plane.position_x + 35, plane.position_y)
                if level.name == 'level two' or level.name == 'level three':
                    plane.shoot_threeBullets(plane.position_x + 35, plane.position_y)
            # shoot auto-track bullet (level 3)
            if event.key == pygame.K_r and level.name == 'level three':
                plane.shoot_auto_track(plane.position_x + 35, plane.position_y)
        if event.type == pygame.KEYUP:
            plane.speed_x = 0
            plane.speed_y = 0
        if level.name != 'level one':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if levelPage.button_acceptChallenge.collidepoint(event.pos):
                    level.acceptChallenge = True
                    levelPage.needToShowIntroduction1Text = False
                    levelPage.needToShowButtons = False
                if levelPage.button_refuseChallenge.collidepoint(event.pos):
                    level.refuseChallenge = True
