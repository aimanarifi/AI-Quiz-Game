"""
Last modified: 15/05/2023
Written by Zhongjie Huang
"""
import random
from production.datascience_house.Plane import Plane
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Window import window
from production.datascience_house.Levels.CommonFunctions import image_bullet, showPlane_setPlaneMoveRange, showScoreObtained, showEnemy, hitByEnemy_judge, hit_judge, end
from production.datascience_house.Levels.Pages.LevelOnePage import LevelOnePage


class LevelOne:
    def __init__(self):
        self.name = 'level one'
        self.gameIsOn = False  # Control of whether the player has entered the current level
        self.plane = Plane()
        self.levelOnePage = LevelOnePage()
        self.enemies = []  # All enemies
        self.allEnemies = 30  # Total number of enemies
        self.enemiesPresent = 0  # Enemies that have appeared
        self.score = 0  # Score

    # Call this method after the start of the current level/game.
    def loadStuff(self):
        self.levelOnePage.showBackground()
        self.levelOnePage.showTextBeforeGame()

        if not self.levelOnePage.showText_beforeGame:
            showPlane_setPlaneMoveRange(self.plane)
            self.plane.showHealth()
            showScoreObtained(self)

            self.showBullet()

            # Up to five enemies can exist simultaneously.
            if self.enemiesPresent < self.allEnemies:
                while len(self.enemies) < 5:
                    self.enemies.append(Enemy(random.randint(0, 1250), -28, random.randint(-2, -2), 0.1))
                    self.enemiesPresent += 1
            # If no enemies, end the game
            if not self.enemies:
                end(self.levelOnePage, self, 11)

            showEnemy(self)

            hitByEnemy_judge(self)
            hit_judge(self)  # To check whether a bullet has hit an enemy

    def showBullet(self):
        for bullet in self.plane.all_bullets:
            window.blit(image_bullet, (bullet.position_x, bullet.position_y))
            bullet.position_y -= bullet.speed_default
        i = 0
        while i < len(self.plane.all_bullets):
            if self.plane.all_bullets[i].position_y < -100:
                del self.plane.all_bullets[i]
            else:
                i += 1

    # To reset all the states of the level when the player exits,
    # call this method to ensure that the player can restart the level without encountering errors.
    def finish(self, levelOnePage):
        if 1190 > self.plane.position_x > 1010 and 28 < self.plane.position_y < 172:
            self.gameIsOn = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
            self.enemiesPresent = 0
            levelOnePage.needToShowIntroductionText = True
            levelOnePage.welcome_textStartTime = 0
            levelOnePage.welcome_textEndTime = 0
            levelOnePage.welcome_textLastTime = 0
            levelOnePage.reminder_textStartTime = 0
            levelOnePage.reminder_textEndTime = 0
            levelOnePage.reminder_textLastTime = 0
            levelOnePage.needToShowEndText = True
            levelOnePage.end_textStartTime = 0
            levelOnePage.end_textEndTime = 0
            levelOnePage.end_textLastTime = 0
            levelOnePage.needToShowExitText = False
