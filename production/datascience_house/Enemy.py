"""
Last modified: 03/05/2023
Written by Zhongjie Huang
"""
import random


class Enemy:
    def __init__(self, position_x, position_y, speed_x, speed_y):
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.all_bullets = []
        self.fire_StartTime = 0
        self.fire_EndTime = 0
        self.fire_LastTime = 0

    def shoot(self):
        new_bullet = Bullet(self.position_x, self.position_y, random.randint(-1, 1))
        self.all_bullets.append(new_bullet)


class Bullet:
    def __init__(self, position_x, position_y, speed_x):
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = 4
