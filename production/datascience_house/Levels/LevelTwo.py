"""
Last modified: 15/05/2023
Written by Zhongjie Huang
"""
import random
from production.datascience_house.Window import window
from production.datascience_house.Plane import Plane
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Levels.CommonFunctions import showQuestions, image_bullet, showPlane_setPlaneMoveRange, showScoreObtained, showEnemy, hitByEnemy_judge, hit_judge, end
from production.datascience_house.Levels.Pages.LevelTwoPage import LevelTwoPage


class LevelTwo:
    def __init__(self):
        self.name = 'level two'
        self.gameIsOn = False  # Control of whether the player has entered the current level
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.levelTwoPage = LevelTwoPage()
        self.enemies = []  # All enemies
        self.allEnemies = 60  # Total number of enemies
        self.enemiesPresent = 0  # Enemies that have appeared
        self.score = 0  # Score
        self.acceptChallenge = False  # Control of whether the player accepts answering questions
        self.refuseChallenge = False  # Control of whether the player refuses answering questions
        self.questionScore = 0  # The player's score in answering questions
        self.questionAnswered = False  # Control of whether the player has answered questions
        self.needToDoQuestions = True

    # Call this method after the start of the current level/game.
    def loadStuff(self):
        self.levelTwoPage.showBackground()

        if not self.questionAnswered:
            self.levelTwoPage.showTextBeforeQuestions(self)
            if self.acceptChallenge:
                self.levelTwoPage.showReminder1Text()
                if self.needToDoQuestions:
                    showQuestions(self, 2)
                    if self.questionScore / 6 >= 0.7:
                        self.questionAnswered = True
                    else:
                        self.needToDoQuestions = False
                if not self.needToDoQuestions:
                    self.levelTwoPage.showReminder2Text(self)
            elif self.refuseChallenge:
                self.gameIsOn = False
                self.refuseChallenge = False
                self.levelTwoPage.needToShowReminder1Text = True
        else:
            self.levelTwoPage.showTextBeforeGame()

            if not self.levelTwoPage.showText_beforeGame:
                showPlane_setPlaneMoveRange(self.plane)
                self.plane.showHealth()
                showScoreObtained(self)

                self.showBullet()

                # Up to ten enemies can exist simultaneously,
                # and the total number of enemies and their movement speed are increased compared to the first level.
                if self.enemiesPresent < self.allEnemies:
                    while len(self.enemies) < 10:
                        self.enemies.append(Enemy(random.randint(0, 1250), -28, random.randint(-3, 3), 0.2))
                        self.enemiesPresent += 1
                if not self.enemies:
                    end(self.levelTwoPage, self, 12)

                showEnemy(self)

                hitByEnemy_judge(self)
                hit_judge(self)  # To check whether a bullet has hit an enemy

    def showBullet(self):
        for bullet in self.plane.all_bullets:
            window.blit(image_bullet, (bullet.position_x, bullet.position_y))
            if bullet.position == 'right':
                bullet.position_y -= bullet.speed_default
                bullet.position_x -= bullet.speed_x
            elif bullet.position == 'middle':
                bullet.position_y -= bullet.speed_default
            elif bullet.position == 'left':
                bullet.position_y -= bullet.speed_default
                bullet.position_x += bullet.speed_x
        i = 0
        while i < len(self.plane.all_bullets):
            if self.plane.all_bullets[i].position_y < -100:
                del self.plane.all_bullets[i]
            else:
                i += 1

    # To reset all the states of the level when the player exits,
    # you can call this method to ensure that the player can restart the level without encountering any errors.
    def finish(self, levelTwoPage):
        if 1190 > self.plane.position_x > 1010 and 28 < self.plane.position_y < 172:
            self.gameIsOn = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
            self.enemiesPresent = 0
            self.acceptChallenge = False
            self.questionScore = 0
            self.questionAnswered = False
            levelTwoPage.needToShowIntroduction1Text = True
            levelTwoPage.needToShowButtons = True
            levelTwoPage.needToShowReminder1Text = True
            levelTwoPage.reminder1_textStartTime = 0
            levelTwoPage.reminder1_textEndTime = 0
            levelTwoPage.reminder1_textLastTime = 0
            levelTwoPage.showText_beforeGame = True
            levelTwoPage.needToShowReminder3Text = True
            levelTwoPage.reminder3_textStartTime = 0
            levelTwoPage.reminder3_textEndTime = 0
            levelTwoPage.reminder3_textLastTime = 0
            levelTwoPage.introduction2_textStartTime = 0
            levelTwoPage.introduction2_textEndTime = 0
            levelTwoPage.introduction2_textLastTime = 0
            levelTwoPage.reminder4_textStartTime = 0
            levelTwoPage.reminder4_textEndTime = 0
            levelTwoPage.reminder4_textLastTime = 0
            levelTwoPage.needTOShowEndText = True
            levelTwoPage.end_textStartTime = 0
            levelTwoPage.end_textEndTime = 0
            levelTwoPage.end_textLastTime = 0
            levelTwoPage.needToShowExitText = False
