"""
Last modified: 03/05/2023
Written by Zhongjie Huang

这个类定义了三个关卡的游戏过程和题目展示:
飞机(玩家), 敌人和子弹的显示;
提供了让玩家进行答题的方法, 对玩家是否通过答题判断;
游戏开始后的过程和结束时的控制(重置关卡数据);
"""
import random
import time
import math
import pygame
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Plane import Plane
from production.datascience_house.Window import window
from production.general.quiz import Quiz
from production.datascience_house.PageText import font

image_plane = pygame.image.load('datascience_house/images/Plane.jpg')  # 飞机
image_bullet = pygame.image.load('datascience_house/images/weapon.jpg')  # 子弹
image_bullet_auto_track = pygame.image.load('datascience_house/images/weapon_auto_track.jpg')  # 子弹(自动跟踪)
image_enemy = pygame.image.load('datascience_house/images/enemy.jpg')  # 敌人
image_enemy_weapon = pygame.image.load('datascience_house/images/Enemy_weapon.jpg')  # 敌人子弹
image_exit = pygame.image.load('datascience_house/images/exit.png')  # 关卡出口
sound_hit = pygame.mixer.Sound('datascience_house/music/hit.mp3')  # 击中敌人音效


class LevelOne:
    def __init__(self):
        self.gameIsOn = False  # 玩家是否进入本关卡的状态控制
        self.plane = Plane()
        self.enemies = []  # 所有敌人
        self.allEnemies = 30  # 敌人总数
        self.enemiesPresent = 0  # 已出现的敌人
        self.score = 0  # 得分

    # 本关游戏开始后, 调用此方法
    def loadStuff(self, levelOnePage):
        showPlane_setPlaneMoveRange(self.plane)
        self.plane.showHealth()
        showScoreObtained(self)

        self.showBullet()

        # 最多同时存在5个敌人
        if self.enemiesPresent < self.allEnemies:
            while len(self.enemies) < 5:
                self.enemies.append(Enemy(random.randint(0, 1250), -28, 2, 0.1))
                self.enemiesPresent += 1
        elif not self.enemies:
            end(levelOnePage, self, 12)

        showEnemy(self.enemies)

        hitByEnemy_judge(self)

        hit_judge(self)  # 检测子弹是否命中敌人

    def showBullet(self):
        for bullet in self.plane.all_bullets:
            window.blit(image_bullet, (bullet.position_x, bullet.position_y))
            bullet.position_y -= bullet.speed_default
            if bullet.position_y < -100:
                self.plane.all_bullets.remove(bullet)

    # 玩家退出本关时, 调用此方法, 将关卡的所有状态重置, 以便玩家可以重新开始本关卡而不出现错误
    def finish(self, levelOnePage):
        if 1190 > self.plane.position_x > 1010 and 28 < self.plane.position_y < 172:
            self.gameIsOn = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
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
        self.gameIsOn = False  # 玩家是否进入本关卡的状态控制
        self.passed = True  # 玩家是否已通过本关卡的状态控制
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.enemies = []  # 所有敌人
        self.allEnemies = 60  # 敌人总数
        self.enemiesPresent = 0  # 已出现的敌人
        self.score = 0  # 得分
        self.allQuestions = [
            [
                "Which of the following is one of the most fundamental characteristics of a data scientist?",
                ("Being proficient in R or Python", "Having a sense of curiosity about all things",
                 "Using open-source software libraries and packages",
                 "Having a strong background in high power computing (HPC)"),
                "Having a sense of curiosity about all things"
            ],
            [
                "The field of data science is the process of _____________. Select all that apply. "
                "A: preparing data for analysis and processing; B: working exclusively with spreadsheets and table; "
                "C: performing advanced data analysis; D: visualizing the results to reveal patterns.",
                ("AC", "ACD", "BD", "BCD"),
                "ACD"
            ],
            [
                "When thinking about the 5 main Vs of data, what does Veracity refer to?",
                ("Refers to the vast amounts of data generated every second",
                 "Refers to the different types of data we can now use.",
                 "Refers to the speed at which new data is generated and the speed at which data moves around",
                 "Refers to the trustworthiness of the data"),
                "Refers to the trustworthiness of the data"
            ],
            [
                "Data in all of its forms, both structured and unstructured, would be the focus of which of the following 5 V’s of data?",
                ("Volume", "Velocity", "Variety", "Veracity"),
                "Variety"
            ],
            [
                "Which of the following are examples of unstructured data? Select all that apply. A: CSV files; B: Facebook images; "
                "C: Records in IBM DB2 database D: Twitter feeds",
                ("AB", "AC", "BC", "BD"),
                "BD"
            ],
            [
                "A data analyst is reviewing an Excel spreadsheet from an insurance company. The customer data that she is analyzing "
                "is sorted by name, home address, policy number, etc. What type of data is she most likely working with? ",
                ("Structured data", "Unstructured data", "Bilaterally structured data", "Unilaterally structured data"),
                "Structured data"
            ]
        ]
        self.acceptChallenge = False  # 玩家是否接受答题的状态控制
        self.refuseChallenge = False  # 玩家是否拒绝答题的状态控制
        self.questionScore = 0  # 玩家的答题得分
        self.questionAnswered = False  # 玩家是否已答题的状态控制

    # 本关游戏开始后, 调用此方法
    def loadStuff(self, levelTwoPage):
        showPlane_setPlaneMoveRange(self.plane)

        self.showBullet()

        # 最多同时存在10个敌人, 敌人总数和移速较第一关提升
        if self.enemiesPresent < self.allEnemies:
            while len(self.enemies) < 10:
                self.enemies.append(Enemy(random.randint(0, 1250), -28, 2, 0.2))
                self.enemiesPresent += 1
        elif not self.enemies:
            end(levelTwoPage, self, 12)

        showEnemy(self.enemies)

        hit_judge(self)  # 检测子弹是否命中敌人

    def showBullet(self):
        for bullets in self.plane.everyThreeBullets:
            window.blit(image_bullet, (bullets[0].position_x, bullets[0].position_y))
            window.blit(image_bullet, (bullets[1].position_x, bullets[1].position_y))
            window.blit(image_bullet, (bullets[2].position_x, bullets[2].position_y))
            bullets[0].position_y -= bullets[0].speed_default
            bullets[1].position_y -= bullets[1].speed_y
            bullets[1].position_x -= bullets[1].speed_x
            bullets[2].position_y -= bullets[2].speed_y
            bullets[2].position_x += bullets[2].speed_x
            if bullets[0].position_y < -100:
                self.plane.everyThreeBullets.remove(bullets)

    # 玩家退出本关时, 调用此方法, 将关卡的所有状态重置, 以便玩家可以重新开始本关卡而不出现错误
    def finish(self, levelTwoPage):
        if 1190 > self.plane.position_x > 1010 and 28 < self.plane.position_y < 172:
            self.gameIsOn = False
            self.passed = True
            self.enemiesPresent = 0
            self.acceptChallenge = False
            self.refuseChallenge = False
            self.questionScore = 0
            self.questionAnswered = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
            levelTwoPage.needToShowWelcome1Text = True
            levelTwoPage.needToShowButtons = True
            levelTwoPage.needToShowIntroduction1Text = True
            levelTwoPage.introduction1_textStartTime = 0
            levelTwoPage.introduction1_textEndTime = 0
            levelTwoPage.introduction1_textLastTime = 0
            levelTwoPage.needToShowIntroduction2Text = True
            levelTwoPage.introduction2_textStartTime = 0
            levelTwoPage.introduction2_textEndTime = 0
            levelTwoPage.introduction2_textLastTime = 0
            levelTwoPage.timeToDoQuestions = False
            levelTwoPage.needToShowWelcome2Text = True
            levelTwoPage.welcome2_textStartTime = 0
            levelTwoPage.welcome2_textEndTime = 0
            levelTwoPage.welcome2_textLastTime = 0
            levelTwoPage.needToShowWelcome3Text = False
            levelTwoPage.welcome3_textStartTime = 0
            levelTwoPage.welcome3_textEndTime = 0
            levelTwoPage.welcome3_textLastTime = 0
            levelTwoPage.needToShowInstructionText = False
            levelTwoPage.instruction_textStartTime = 0
            levelTwoPage.instruction_textEndTime = 0
            levelTwoPage.instruction_textLastTime = 0
            levelTwoPage.needTOShowEndText = True
            levelTwoPage.end_textStartTime = 0
            levelTwoPage.end_textEndTime = 0
            levelTwoPage.end_textLastTime = 0
            levelTwoPage.needToShowExitText = False


class LevelThree:
    def __init__(self):
        self.gameIsOn = False  # 玩家是否进入本关卡的状态控制
        self.passed = True  # 玩家是否已通过本关卡的状态控制
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.enemies = []  # 所有敌人
        self.allEnemies = 90  # 敌人总数
        self.enemiesPresent = 0  # 已出现的敌人
        self.score = 0  # 得分
        self.allQuestions = [
            [
                "Which of the following tasks is a typical role of a Data Engineer?",
                ("Collect and clean data", "Statistical computing", "Visualizing the data", "All the above"),
                "Statistical computing"
            ],
            [
                "Which of the following tasks is a typical role of a Data Analyst?",
                ("Collect and clean data", "Statistical computing", "Visualizing the data", "All the above"),
                "Collect and clean data"
            ],
            [
                "Which of the following tasks is a typical role of a Data Scientist?",
                ("Collect and clean data", "Statistical computing", "Visualizing the data", "All the above"),
                "Visualizing the data"
            ],
            [
                "Data cleansing often consumes 80% of a data engineers’ or data scientists’ time. "
                "Which of the following tasks is specific to data cleansing? Select all that apply. A: Merging multiple datasets; "
                "B: Imputing for missing values; C: Visualizing the data set; D: Feature engineering.",
                ("AB", "AC", "BC", "BD"),
                "AB"
            ],
            [
                "Data Exploration can be best summarized as the process of ___________.",
                ("Cleaning and organizing data into a usable format",
                 "Examining and visualizing data to find undiscovered patterns and relationships",
                 "Importing data into a machine learning model ", "All the above "),
                "Examining and visualizing data to find undiscovered patterns and relationships"
            ],
            [
                "Data Modeling can best be summarized as the process of ______________.",
                ("Creating a visualization to communicate connections between data points and structures.",
                 "Cleaning and munging data into a usable format", "Examining data for hidden patterns",
                 "All the above"),
                "Creating a visualization to communicate connections between data points and structures."
            ],
            [
                "Which of the following is a Data Model?",
                ("Entity-Relationship model", "Relational data model", "Object-oriented data model", "All the above"),
                "All the above"
            ],
            [
                "_____________ is the stage whereby a data model is analyzed for its quality and efficiency in solving a problem.",
                ("Data Cleansing", "Data Modeling", "Model Implementation", "Model Deployment"),
                "Model Implementation"
            ],
            [
                "_____________ is the stage whereby a data model is tested for its quality and put into production.",
                ("Data Cleansing", "Data Modeling", "Model Implementation", "Model Deployment"),
                "Model Deployment"
            ],
        ]
        self.acceptChallenge = False  # 玩家是否接受答题的状态控制
        self.refuseChallenge = False  # 玩家是否拒绝答题的状态控制
        self.questionScore = 0  # 玩家的答题得分
        self.questionAnswered = False  # 玩家是否已答题的状态控制

    # 本关游戏开始后, 调用此方法
    def loadStuff(self, levelThreePage):
        showPlane_setPlaneMoveRange(self.plane)

        self.showPlaneBullet()

        # 最多同时存在15个敌人, 敌人总数和移速较第二关提升
        if self.enemiesPresent < self.allEnemies:
            while len(self.enemies) < 15:
                self.enemies.append(Enemy(random.randint(0, 1250), -28, 2, 0.25))
                self.enemiesPresent += 1
        elif not self.enemies:
            end(levelThreePage, self, 12)

        showEnemy(self.enemies)

        self.showEnemyBullet()

        hit_judge(self)  # 检测子弹是否命中敌人

    def showPlaneBullet(self):
        for bullets in self.plane.everyThreeBullets:
            window.blit(image_bullet, (bullets[0].position_x, bullets[0].position_y))
            window.blit(image_bullet, (bullets[1].position_x, bullets[1].position_y))
            window.blit(image_bullet, (bullets[2].position_x, bullets[2].position_y))
            bullets[0].position_y -= bullets[0].speed_default
            bullets[1].position_y -= bullets[1].speed_y
            bullets[1].position_x -= bullets[1].speed_x
            bullets[2].position_y -= bullets[2].speed_y
            bullets[2].position_x += bullets[2].speed_x
            if bullets[0].position_y < -100:
                self.plane.everyThreeBullets.remove(bullets)
        for bullet in self.plane.all_auto_track_bullets:
            window.blit(image_bullet_auto_track, (bullet.position_x, bullet.position_y))
            Plane.auto_track(bullet, self.enemies)

    def showEnemyBullet(self):
        for enemy in self.enemies:
            # 在第三关中, 敌人每隔三秒发射一次子弹
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

    # 玩家退出本关时, 调用此方法, 将关卡的所有状态重置, 以便玩家可以重新开始本关卡而不出现错误
    def finish(self, levelThreePage):
        if 1190 > self.plane.position_x > 1010 and 28 < self.plane.position_y < 172:
            self.gameIsOn = False
            self.passed = True
            self.enemiesPresent = 0
            self.acceptChallenge = False
            self.refuseChallenge = False
            self.questionScore = 0
            self.questionAnswered = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
            levelThreePage.needToShowWelcome1Text = True
            levelThreePage.needToShowButtons = True
            levelThreePage.needToShowIntroduction1Text = True
            levelThreePage.introduction1_textStartTime = 0
            levelThreePage.introduction1_textEndTime = 0
            levelThreePage.introduction1_textLastTime = 0
            levelThreePage.needToShowIntroduction2Text = True
            levelThreePage.introduction2_textStartTime = 0
            levelThreePage.introduction2_textEndTime = 0
            levelThreePage.introduction2_textLastTime = 0
            levelThreePage.timeToDoQuestions = False
            levelThreePage.needToShowWelcome2Text = True
            levelThreePage.welcome2_textStartTime = 0
            levelThreePage.welcome2_textEndTime = 0
            levelThreePage.welcome2_textLastTime = 0
            levelThreePage.needToShowWelcome3Text = False
            levelThreePage.welcome3_textStartTime = 0
            levelThreePage.welcome3_textEndTime = 0
            levelThreePage.welcome3_textLastTime = 0
            levelThreePage.needToShowInstructionText = False
            levelThreePage.instruction_textStartTime = 0
            levelThreePage.instruction_textEndTime = 0
            levelThreePage.instruction_textLastTime = 0
            levelThreePage.needTOShowEndText = True
            levelThreePage.end_textStartTime = 0
            levelThreePage.end_textEndTime = 0
            levelThreePage.end_textLastTime = 0
            levelThreePage.needToShowExitText = False


def showQuestions(level):
    for question in level.allQuestions:
        q = question[0]
        options = [question[1][0], question[1][1], question[1][2], question[1][3]]
        correct_option = question[2]
        quiz = Quiz(q, options, correct_option)
        quiz.run()
        level.questionScore += quiz.get_score()


# 飞机不可以移动出界(超出屏幕范围)
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
    score_bar = font.render("score: " + str(level.score), True, (255, 255, 255))
    window.blit(score_bar, (10, 10))


# 敌人在触碰到屏幕边缘时会折返
def showEnemy(enemies):
    for enemy in enemies:
        window.blit(image_enemy, (enemy.position_x, enemy.position_y))
        if enemy.position_x > 1250 or enemy.position_x < 0:
            enemy.speed_x *= -1
        if enemy.position_y > 692 or enemy.position_y < -28:
            enemy.speed_y *= -1
        enemy.position_x += enemy.speed_x
        enemy.position_y += enemy.speed_y


def hitByEnemy_judge(level):
    for enemy in level.enemies:
        distance_plane_enemy = math.sqrt(((enemy.position_x + 15) - (level.plane.position_x + 37)) ** 2 + ((enemy.position_y + 14) - (level.plane.position_y + 27)) ** 2)
        if distance_plane_enemy < 40:
            level.plane.HP_current -= 10
            level.plane.healthBar_width = (level.plane.HP_current/level.plane.HP_max) * level.plane.healthBar_width
            if level.score > 0:
                level.score -= 1
            level.enemies.remove(enemy)


# To determine whether bullets have hit enemies.
def hit_judge(level):
    for bullet in level.plane.all_bullets:
        for enemy in level.enemies:
            distance_bullet_enemy = math.sqrt(((bullet.position_x + 5) - (enemy.position_x + 16.5)) ** 2 + (
                    bullet.position_y - enemy.position_y) ** 2)
            # If hit, both the enemy and the bullet disappear simultaneously.
            if distance_bullet_enemy < 17:
                level.score += 1
                sound_hit.play()  # hit sound effect
                level.enemies.remove(enemy)
                level.plane.all_bullets.remove(bullet)
                hit = True
                if hit:
                    break


# 敌人全部被消灭(已出现的敌人数量等于最大敌人数量)时, 调用此方法
def end(levelPage, level, seconds):
    if levelPage.needTOShowEndText:
        if levelPage.end_textStartTime == 0:
            levelPage.end_textStartTime = time.time()
        levelPage.end_textEndTime = time.time()
        levelPage.end_textLastTime = levelPage.end_textEndTime - levelPage.end_textStartTime
        if levelPage.end_textLastTime <= seconds:
            levelPage.showEndText()
        else:
            levelPage.needTOShowEndText = False
            levelPage.needToShowExitText = True
    elif levelPage.needToShowExitText:
        levelPage.showExitText()
        window.blit(image_exit, (1100, 100))
        level.finish(levelPage)
