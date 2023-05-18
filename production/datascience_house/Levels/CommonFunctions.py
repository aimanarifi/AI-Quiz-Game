"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import math
import time
from production.datascience_house.Window import pygame, window, font
from production.general.db.DatabaseService import get_questions

image_plane = pygame.image.load('datascience_house/images/Plane.jpg')  # plane
image_bullet = pygame.image.load('datascience_house/images/weapon.jpg')  # bullet
image_bullet_auto_track = pygame.image.load('datascience_house/images/weapon_auto_track.jpg')  # bullet(auto-track)
image_enemy = pygame.image.load('datascience_house/images/enemy.jpg')  # enemy
image_enemy_weapon = pygame.image.load('datascience_house/images/Enemy_weapon.jpg')  # enemy bullet
image_exit = pygame.image.load('datascience_house/images/exit.png')  # level exit
sound_hit = pygame.mixer.Sound('datascience_house/music/hit.mp3')  # hit sound effect


def showQuestions(level, questionsIndex):
    questions = get_questions(questionsIndex, 'datascience')
    for question in questions:
        question.run()
        level.questionScore += question.get_score()


# The airplane cannot move out of bounds (beyond the screen range).
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


def showScoreObtained(level):
    if level.name == 'level one' or level.name == 'level two':
        score_bar = font.render("score: " + str(level.score), True, (255, 255, 255))
        window.blit(score_bar, (10, 10))
    if level.name == 'level three':
        score_bar = font.render("score: " + str(level.score), True, (125, 125, 125))
        window.blit(score_bar, (10, 10))


# The enemy will bounce back when it touches the edge of the screen.
def showEnemy(level):
    for enemy in level.enemies:
        window.blit(image_enemy, (enemy.position_x, enemy.position_y))
        if enemy.position_x > 1250 or enemy.position_x < 0:
            enemy.speed_x *= -1
        if enemy.position_y > 692 or enemy.position_y < -28:
            enemy.speed_y *= -1
        enemy.position_x += enemy.speed_x
        enemy.position_y += enemy.speed_y


def showRemainingEnemies(level):
    if level.name == 'level one' or level.name == 'level two':
        remainingEnemies_bar = font.render("remaining enemies: " + str(level.allEnemies - level.enemyDestroyed), True, (255, 255, 255))
        window.blit(remainingEnemies_bar, (1000, 10))
    if level.name == 'level three':
        remainingEnemies_bar = font.render("remaining enemies: " + str(level.allEnemies - level.enemyDestroyed), True,
                                           (125, 125, 125))
        window.blit(remainingEnemies_bar, (1000, 10))


def hitByEnemy_judge(level):
    for enemy in level.enemies:
        distance_plane_enemy = math.sqrt(((enemy.position_x + 15) - (level.plane.position_x + 37)) ** 2 + (
                    (enemy.position_y + 14) - (level.plane.position_y + 27)) ** 2)
        if distance_plane_enemy < 40:
            level.plane.HP_current -= 10
            level.plane.healthBar_width = (level.plane.HP_current / level.plane.HP_max) * level.plane.healthBar_width
            if level.score > 0:
                level.score -= 1
            enemy.hitByPlane = True
            level.enemyDestroyed += 1
    i = 0
    while i < len(level.enemies):
        if level.enemies[i].hitByPlane:
            del level.enemies[i]
        else:
            i += 1


def hit_judge(level):
    for bullet in level.plane.all_bullets:
        for enemy in level.enemies:
            distance_bullet_enemy = math.sqrt(((bullet.position_x + 5) - (enemy.position_x + 16.5)) ** 2 + (
                    bullet.position_y - enemy.position_y) ** 2)
            if distance_bullet_enemy < 17:
                level.score += 1
                sound_hit.play()  # hit sound effect
                enemy.hitByBullet = True
                bullet.hitEnemy = True
                level.enemyDestroyed += 1
    i1 = 0
    while i1 < len(level.plane.all_bullets):
        if level.plane.all_bullets[i1].hitEnemy:
            del level.plane.all_bullets[i1]
        else:
            i1 += 1
    i2 = 0
    while i2 < len(level.enemies):
        if level.enemies[i2].hitByBullet:
            del level.enemies[i2]
        else:
            i2 += 1


# Call this method when all enemies have been eliminated (the number of existing enemies is equal to the maximum number of enemies).
def end(levelPage, level, seconds):
    if levelPage.needTOShowEndText:
        if levelPage.end_textStartTime == 0:
            levelPage.end_textStartTime = time.time()
        levelPage.end_textEndTime = time.time()
        levelPage.end_textLastTime = levelPage.end_textEndTime - levelPage.end_textStartTime
        countdown_text_time_left = seconds - levelPage.end_textLastTime
        countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
        if (seconds - levelPage.end_textLastTime) >= 0:
            levelPage.showEndText()
            window.blit(countdown_text, (10, 690))
        else:
            levelPage.needTOShowEndText = False
            levelPage.needToShowExitText = True
            levelPage.end_textStartTime = 0
            levelPage.end_textEndTime = 0
            levelPage.end_textLastTime = 0
    if levelPage.needToShowExitText:
        levelPage.showExitText()
        window.blit(image_exit, (1100, 100))
        level.finish(levelPage)
