"""
Last modified: 03/05/2023
Written by Zhongjie Huang
"""
import random
import time

from Window import pygame, window
from Plane import Plane, math
from Enemy import Enemy

image_plane = pygame.image.load('images/Plane.jpg')
image_bullet = pygame.image.load('images/weapon.jpg')
image_enemy = pygame.image.load('images/enemy.jpg')
image_exit = pygame.image.load('images/exit.png')

sound_hit = pygame.mixer.Sound('music/hit.mp3')


class LevelOne:
    """
    This class is used to design the level one for this game, including the game status, plane and enemy.
    It will call some functions to show the plane, enemy, bullet as well as their attributes.
    """
    def __init__(self):
        self.image_level_one_background = pygame.image.load('images/LevelOneBackground.jpg')
        pygame.mixer.music.load('music/LevelOneFight.mp3')
        pygame.mixer.music.play(-1)
        self.enemies = []
        self.allEnemies = 30
        self.enemiesPresent = 0
        self.plane = Plane()
        self.gameIsOn = False

    def loadStuff(self, levelOnePage):
        showPlane_setPlaneMoveRange(self.plane)

        showBulletLevelOne(self.plane.all_bullets)

        # 规定敌人的当前数量和最大数量
        if self.enemiesPresent < self.allEnemies:
            while len(self.enemies) < 5:
                self.enemies.append(Enemy(random.randint(0, 1250), -28, 2, 0.1))
                self.enemiesPresent += 1
        else:
            if not self.enemies:
                if levelOnePage.needTOShowEndText:
                    if levelOnePage.end_textStartTime == 0:
                        levelOnePage.end_textStartTime = time.time()
                    levelOnePage.end_textEndTime = time.time()
                    levelOnePage.end_textLastTime = levelOnePage.end_textEndTime - levelOnePage.end_textStartTime
                    if levelOnePage.end_textLastTime <= 12:
                        levelOnePage.showEndText()
                    else:
                        levelOnePage.needTOShowEndText = False
                        levelOnePage.needToShowExitText = True
                elif levelOnePage.needToShowExitText:
                    levelOnePage.showExitText()
                    window.blit(image_exit, (1100, 100))
                    self.finish(levelOnePage)

        showEnemyLevelOne(self.enemies)

        hit_judge(self.plane, self.enemies)

    def finish(self, levelOnePage):
        """
        This function will end the level one.
        It will reset all the variables related to level one page, to make sure the player can restart it.
        """
        if self.plane.position_x >= 1010 and 28 <= self.plane.position_y <= 172:
            self.gameIsOn = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
            self.allEnemies = 30
            self.enemiesPresent = 0
            levelOnePage.needTOShowWelcomeText = True
            levelOnePage.welcome_textStartTime = 0
            levelOnePage.welcome_textEndTime = 0
            levelOnePage.welcome_textLastTime = 0
            levelOnePage.needTOShowInstructionText = False
            levelOnePage.instruction_textStartTime = 0
            levelOnePage.instruction_textEndTime = 0
            levelOnePage.instruction_textLastTime = 0
            levelOnePage.needTOShowEndText = True
            levelOnePage.end_textStartTime = 0
            levelOnePage.end_textEndTime = 0
            levelOnePage.end_textLastTime = 0
            levelOnePage.needToShowExitText = False


class LevelTwo:
    def __init__(self):
        self.image_level_two_background = pygame.image.load('images/LevelTwoBackground.jpg')
        pygame.mixer.music.load('music/LevelTwoFight.mp3')
        pygame.mixer.music.play(-1)
        self.enemies = []
        self.allEnemies = 60
        self.enemiesPresent = 0
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.gameIsOn = False

    def show(self):
        window.blit(self.image_level_two_background, (0, 0))

        showPlane_setPlaneMoveRange(self.plane)

        # showBullet(self.plane.all_bullets)

        # showEnemy(self.enemies)

        hit_judge(self.plane, self.enemies)


class LevelThree:
    def __init__(self):
        self.image_level_three_background = pygame.image.load('images/LevelThreeBackground.jpg')
        pygame.mixer.music.load('music/LevelThreeFight.mp3')
        pygame.mixer.music.play(-1)
        self.enemies = []
        self.allEnemies = 90
        self.enemiesPresent = 0
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.gameIsOn = False

    def show(self):
        window.blit(self.image_level_three_background, (0, 0))

        showPlane_setPlaneMoveRange(self.plane)

        # showBullet(self.plane.all_bullets)

        # showEnemy(self.enemies)

        hit_judge(self.plane, self.enemies)


def showPlane_setPlaneMoveRange(plane):
    window.blit(image_plane, (plane.position_x, plane.position_y))
    plane.position_x += plane.speed_x
    plane.position_y += plane.speed_y
    # Setting the range of movement for the spacecraft.
    if plane.position_x > 1205:
        plane.position_x = 1205
    elif plane.position_x < 0:
        plane.position_x = 0
    if plane.position_y > 666:
        plane.position_y = 666
    elif plane.position_y < 0:
        plane.position_y = 0


def hit_judge(plane, enemies):
    # To determine whether a bullet has hit an enemy.
    for bullet in plane.all_bullets:
        for enemy in enemies:
            distance_bullet_enemy = math.sqrt(((bullet.position_x + 5) - (enemy.position_x + 16.5)) ** 2 + (
                    bullet.position_y - enemy.position_y) ** 2)
            # If hit, both the enemy and the bullet disappear simultaneously.
            if distance_bullet_enemy < 17:
                sound_hit.play()
                enemies.remove(enemy)
                plane.all_bullets.remove(bullet)
                hit = True
                if hit:
                    break


def showBulletLevelOne(allBullets):
    for bullet in allBullets:
        window.blit(image_bullet, (bullet.position_x, bullet.position_y))
        bullet.position_y -= bullet.speed_default
        if bullet.position_y < -100:
            allBullets.remove(bullet)


def showEnemyLevelOne(enemies):
    for enemy in enemies:
        window.blit(image_enemy, (enemy.position_x, enemy.position_y))
        if enemy.position_x > 1250 or enemy.position_x < 0:
            enemy.speed_x *= -1
        if enemy.position_y > 692 or enemy.position_y < -28:
            enemy.speed_y *= -1
        enemy.position_x += enemy.speed_x
        enemy.position_y += enemy.speed_y
