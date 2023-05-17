"""
Last modified: 15/05/2023
Written by Zhongjie Huang
"""
import random


class Enemy:
    def __init__(self, position_x, position_y, speed_x, speed_y):
        # 敌人的位置
        self.position_x = position_x
        self.position_y = position_y

        # 敌人的移速
        self.speed_x = speed_x
        self.speed_y = speed_y

        # 敌人发射的所有子弹
        self.all_bullets = []

        # 敌人发射子弹的频率控制
        self.fire_StartTime = 0
        self.fire_EndTime = 0
        self.fire_LastTime = 0

        # 敌人是否被子弹(飞机)击中
        self.hitByBullet = False

        # 敌人是否与飞机相撞
        self.hitByPlane = False

    def shoot(self):
        new_bullet = Bullet(self.position_x, self.position_y, random.randint(-2, 2))
        self.all_bullets.append(new_bullet)


class Bullet:
    def __init__(self, position_x, position_y, speed_x):
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = 4
