"""
Last modified: 15/05/2023
Written by Zhongjie Huang
"""
import time
import random
from production.datascience_house.Window import pygame, window
from production.datascience_house.Plane import Plane
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Levels.CommonFunctions import showQuestions, image_bullet, image_bullet_auto_track, showPlane_setPlaneMoveRange, showScoreObtained, showEnemy, image_enemy_weapon, hitByEnemy_judge, hit_judge, end
from production.datascience_house.Levels.Pages.LevelThreePage import LevelThreePage


class LevelThree:
    def __init__(self):
        self.name = 'level three'
        self.gameIsOn = False  # Control of whether the player has entered the current level
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.levelThreePage = LevelThreePage()
        self.enemies = []  # All enemies
        self.allEnemies = 90  # Total number of enemies
        self.enemiesPresent = 0  # Enemies that have appeared
        self.score = 0  # Score
        self.acceptChallenge = False  # Control of whether the player accepts answering questions
        self.refuseChallenge = False  # Control of whether the player refuses answering questions
        self.questionScore = 0  # The player's score in answering questions
        self.questionAnswered = False  # Control of whether the player has answered questions
        self.needToDoQuestions = True

    # Call this method after the start of the current level/game.
    def loadStuff(self):
        self.levelThreePage.showBackground()

        if not self.questionAnswered:
            self.levelThreePage.showTextBeforeQuestions(self)
            if self.acceptChallenge:
                self.levelThreePage.showReminder1Text()
                if not self.levelThreePage.needToShowReminder1Text:
                    if self.needToDoQuestions:
                        pygame.mixer.music.pause()
                        showQuestions(self, 3)
                        if self.questionScore / 9 >= 0.7:
                            pygame.mixer.music.unpause()
                            self.questionAnswered = True
                            self.questionScore = 0
                        else:
                            pygame.mixer.music.unpause()
                            self.needToDoQuestions = False
                            self.questionScore = 0
                if not self.needToDoQuestions:
                    self.levelThreePage.showReminder2Text(self)
            elif self.refuseChallenge:
                self.gameIsOn = False
                self.refuseChallenge = False
                self.levelThreePage.needToShowReminder1Text = True
        else:
            self.levelThreePage.showTextBeforeGame()

            if not self.levelThreePage.showText_beforeGame:
                showPlane_setPlaneMoveRange(self.plane)
                self.plane.showHealth()
                showScoreObtained(self)

                self.showPlaneBullet()

                # Up to fifteen enemies can exist simultaneously,
                # and the total number of enemies and their movement speed are increased compared to the second level.
                if self.enemiesPresent < self.allEnemies:
                    while len(self.enemies) < 15:
                        self.enemies.append(Enemy(random.randint(0, 1250), -28, random.randint(-4, 4), 0.25))
                        self.enemiesPresent += 1
                elif not self.enemies:
                    end(self.levelThreePage, self, 11)

                showEnemy(self)
                self.showEnemyBullet()

                hitByEnemy_judge(self)
                hit_judge(self)  # To check whether a bullet has hit an enemy

    def showPlaneBullet(self):
        for bullet in self.plane.all_bullets:
            if bullet.position == 'right':
                window.blit(image_bullet, (bullet.position_x, bullet.position_y))
                bullet.position_y -= bullet.speed_default
                bullet.position_x -= bullet.speed_x
            elif bullet.position == 'middle':
                window.blit(image_bullet, (bullet.position_x, bullet.position_y))
                bullet.position_y -= bullet.speed_default
            elif bullet.position == 'left':
                window.blit(image_bullet, (bullet.position_x, bullet.position_y))
                bullet.position_y -= bullet.speed_default
                bullet.position_x += bullet.speed_x
            elif bullet.position == 'auto_track':
                window.blit(image_bullet_auto_track, (bullet.position_x, bullet.position_y))
                self.plane.auto_track(bullet, self.enemies)
            i = 0
            while i < len(self.plane.all_bullets):
                if self.plane.all_bullets[i].position_y < -100:
                    del self.plane.all_bullets[i]
                else:
                    i += 1

    def showEnemyBullet(self):
        for enemy in self.enemies:
            # In level three, the enemy fires a bullet every three seconds.
            if enemy.fire_StartTime == 0:
                enemy.fire_StartTime = time.time()
            enemy.fire_EndTime = time.time()
            enemy.fire_LastTime = enemy.fire_EndTime - enemy.fire_StartTime
            if enemy.fire_LastTime >= 3:
                enemy.shoot()
                enemy.fire_StartTime = 0
                enemy.fire_EndTime = 0
        for enemy in self.enemies:
            for bullet in enemy.all_bullets:
                window.blit(image_enemy_weapon, (bullet.position_x, bullet.position_y))
                bullet.position_x += bullet.speed_x
                bullet.position_y += bullet.speed_y
                if bullet.position_y > 750:
                    enemy.all_bullets.remove(bullet)
        i = 0
        while i < len(self.enemies):
            if self.enemies[i].position_y > 750:
                del self.enemies[i]
            else:
                i += 1

    # To reset all the states of the level when the player exits,
    # you can call this method to ensure that the player can restart the level without encountering any errors.
    def finish(self, levelThreePage):
        if 1190 > self.plane.position_x > 1010 and 28 < self.plane.position_y < 172:
            self.gameIsOn = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
            self.enemiesPresent = 0
            self.acceptChallenge = False
            self.questionScore = 0
            self.questionAnswered = False
            levelThreePage.needToShowIntroduction1Text = True
            levelThreePage.needToShowButtons = True
            levelThreePage.needToShowReminder1Text = True
            levelThreePage.reminder1_textStartTime = 0
            levelThreePage.reminder1_textEndTime = 0
            levelThreePage.reminder1_textLastTime = 0
            levelThreePage.showText_beforeGame = True
            levelThreePage.needToShowReminder3Text = True
            levelThreePage.reminder3_textStartTime = 0
            levelThreePage.reminder3_textEndTime = 0
            levelThreePage.reminder3_textLastTime = 0
            levelThreePage.needToShowIntroduction2Text = False
            levelThreePage.introduction2_textStartTime = 0
            levelThreePage.introduction2_textEndTime = 0
            levelThreePage.introduction2_textLastTime = 0
            levelThreePage.needToShowReminder4Text = False
            levelThreePage.reminder4_textStartTime = 0
            levelThreePage.reminder4_textEndTime = 0
            levelThreePage.reminder4_textLastTime = 0
            levelThreePage.needTOShowEndText = True
            levelThreePage.end_textStartTime = 0
            levelThreePage.end_textEndTime = 0
            levelThreePage.end_textLastTime = 0
            levelThreePage.needToShowExitText = False
