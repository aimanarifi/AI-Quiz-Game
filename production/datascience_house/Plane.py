import math


class Plane:
    def __init__(self):
        self.position_x = 0
        self.position_y = 675
        self.speed_x = 0  # level speed
        self.speed_y = 0  # vertical speed
        self.velocity1 = 3  # velocity size (one direction)
        self.velocity2 = -3  # velocity size (one direction)
        self.all_bullets = []

    # Upgrading spacecraft performance to increase speed.
    def move_speed_improve(self):
        self.velocity1 = 5.5
        self.velocity2 = -5.5

    # Upgrading spacecraft performance to enable bullets to automatically track enemies.
    @staticmethod
    def auto_track(bullet, enemies):
        distances = []
        for enemy in enemies:
            distance = math.sqrt(((bullet.position_x + 5) - (enemy.position_x + 15)) ** 2 + (
                    bullet.position_y - enemy.position_y) ** 2)
            distances.append(distance)
        distance_min = min(distances)  # The nearest enemy to the bullet (Euclidean distance).
        indices = [i for i, d in enumerate(distances) if d == distance_min]
        enemy = enemies[indices[0]]
        bullet_level_distance_enemy = bullet.position_x - enemy.position_x
        bullet_vertical_distance_enemy = bullet.position_y - enemy.position_y

        if 1150 < abs(bullet_level_distance_enemy) <= 1200:
            bullet.speed_x = 7.5
        elif 1100 < abs(bullet_level_distance_enemy) <= 1150:
            bullet.speed_x = 7.2
        elif 1050 < abs(bullet_level_distance_enemy) <= 1100:
            bullet.speed_x = 6.9
        elif 1000 < abs(bullet_level_distance_enemy) <= 1050:
            bullet.speed_x = 6.6
        elif 950 < abs(bullet_level_distance_enemy) <= 1000:
            bullet.speed_x = 6.3
        elif 900 < abs(bullet_level_distance_enemy) <= 950:
            bullet.speed_x = 6
        elif 850 < abs(bullet_level_distance_enemy) <= 900:
            bullet.speed_x = 5.7
        elif 800 < abs(bullet_level_distance_enemy) <= 850:
            bullet.speed_x = 5.4
        elif 750 < abs(bullet_level_distance_enemy) <= 800:
            bullet.speed_x = 5.1
        elif 700 < abs(bullet_level_distance_enemy) <= 750:
            bullet.speed_x = 4.8
        elif 650 < abs(bullet_level_distance_enemy) <= 700:
            bullet.speed_x = 4.5
        elif 600 < abs(bullet_level_distance_enemy) <= 650:
            bullet.speed_x = 4.2
        elif 550 < abs(bullet_level_distance_enemy) <= 600:
            bullet.speed_x = 3.9
        elif 500 < abs(bullet_level_distance_enemy) <= 550:
            bullet.speed_x = 3.6
        elif 450 < abs(bullet_level_distance_enemy) <= 500:
            bullet.speed_x = 3.3
        elif 400 < abs(bullet_level_distance_enemy) <= 450:
            bullet.speed_x = 3
        elif 350 < abs(bullet_level_distance_enemy) <= 400:
            bullet.speed_x = 2.7
        elif 300 < abs(bullet_level_distance_enemy) <= 350:
            bullet.speed_x = 2.4
        elif 250 < abs(bullet_level_distance_enemy) <= 300:
            bullet.speed_x = 2.1
        elif 200 < abs(bullet_level_distance_enemy) <= 250:
            bullet.speed_x = 1.8
        elif 150 < abs(bullet_level_distance_enemy) <= 200:
            bullet.speed_x = 1.5
        elif 100 < abs(bullet_level_distance_enemy) <= 150:
            bullet.speed_x = 1.2
        elif 50 < abs(bullet_level_distance_enemy) <= 100:
            bullet.speed_x = 0.9
        elif abs(bullet_level_distance_enemy) <= 50:
            bullet.speed_x = 0.6

        if 750 < abs(bullet_vertical_distance_enemy) <= 800:
            bullet.speed_y = 6.8
        elif 700 < abs(bullet_vertical_distance_enemy) <= 750:
            bullet.speed_y = 6.4
        elif 650 < abs(bullet_vertical_distance_enemy) <= 700:
            bullet.speed_y = 6
        elif 600 < abs(bullet_vertical_distance_enemy) <= 650:
            bullet.speed_y = 5.6
        elif 550 < abs(bullet_vertical_distance_enemy) <= 600:
            bullet.speed_y = 5.2
        elif 500 < abs(bullet_vertical_distance_enemy) <= 550:
            bullet.speed_y = 4.8
        elif 450 < abs(bullet_vertical_distance_enemy) <= 500:
            bullet.speed_y = 4.4
        elif 400 < abs(bullet_vertical_distance_enemy) <= 450:
            bullet.speed_y = 4
        elif 350 < abs(bullet_vertical_distance_enemy) <= 400:
            bullet.speed_y = 3.6
        elif 300 < abs(bullet_vertical_distance_enemy) <= 350:
            bullet.speed_y = 3.2
        elif 250 < abs(bullet_vertical_distance_enemy) <= 300:
            bullet.speed_y = 2.8
        elif 200 < abs(bullet_vertical_distance_enemy) <= 250:
            bullet.speed_y = 2.4
        elif 150 < abs(bullet_vertical_distance_enemy) <= 200:
            bullet.speed_y = 2
        elif 100 < abs(bullet_vertical_distance_enemy) <= 150:
            bullet.speed_y = 1.6
        elif 50 < abs(bullet_vertical_distance_enemy) <= 100:
            bullet.speed_y = 1.2
        elif abs(bullet_vertical_distance_enemy) <= 50:
            bullet.speed_y = 0.8

        # If the bullet is on the left or right of the enemy.
        if bullet_level_distance_enemy < 0:
            bullet.position_x += bullet.speed_x
        elif bullet_level_distance_enemy > 0:
            bullet.position_x -= bullet.speed_x

        # If the bullet is above or below the enemy.
        if bullet_vertical_distance_enemy < 0:
            bullet.position_y += bullet.speed_y
        elif bullet_vertical_distance_enemy > 0:
            bullet.position_y -= bullet.speed_y

    def shoot(self, x, y):
        new_bullet = Bullet(x, y)
        self.all_bullets.append(new_bullet)


class Bullet:
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.speed_x = 0
        self.speed_y = 0
        self.speed_default = 10
