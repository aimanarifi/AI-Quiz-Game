import pygame
from os import walk
import os
from settings import *


def get_images(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        surfaces.append(image_surface)

    return surfaces


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # animation setup
        self.animation_status = "forward_idle"
        self.frame_index = 0

        self.animations = {'forward_idle': get_images('assets/graphics/player-animations/forward/idle'),
                           'forward': get_images('assets/graphics/player-animations/forward/movement'),
                           'right_idle': get_images('assets/graphics/player-animations/right/idle'),
                           'right': get_images('assets/graphics/player-animations/right/movement'),
                           'left_idle': get_images('assets/graphics/player-animations/left/idle'),
                           'left': get_images('assets/graphics/player-animations/left/movement'),
                           'backward_idle': get_images(
                               'assets/graphics/player-animations/backward/idle'),
                           'backward': get_images(
                               'assets/graphics/player-animations/backward/movement')}

        # image setup
        self.image = self.animations[self.animation_status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS["Decor"]

        # movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 150

    def animate(self, dt):
        self.frame_index += 6 * dt

        if self.frame_index >= len(self.animations[self.animation_status]):
            self.frame_index = 0

        self.image = self.animations[self.animation_status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.animation_status = "backward"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.animation_status = "forward"
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.animation_status = "right"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.animation_status = "left"
        else:
            self.direction.x = 0

    def check_status(self):
        # idle
        if self.direction.magnitude() == 0:
            self.animation_status = self.animation_status.split('_')[0] + '_idle'

    def move(self, dt):
        # normalisation
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # hor movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # ver movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.check_status()

        self.move(dt)
        self.animate(dt)
    

    def checkCollision(self, sprite1, sprite2):
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            
    