import pygame
from os import walk
import os
from settings import *


def get_images(folder_dir):
    surface_list = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surface)

    return surface_list


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.status = "forward_idle"
        self.frame_index = 0

        self.animations = {'forward_idle': get_images('../../assets/graphics/player-animations/forward/idle'),
                           'forward': get_images('../../assets/graphics/player-animations/forward/movement'),
                           'right_idle': get_images('../../assets/graphics/player-animations/right/idle'),
                           'right': get_images('../../assets/graphics/player-animations/right/movement'),
                           'left_idle': get_images('../../assets/graphics/player-animations/left/idle'),
                           'left': get_images('../../assets/graphics/player-animations/left/movement'),
                           'backward_idle': get_images(
                               '../../assets/graphics/player-animations/backward/idle'),
                           'backward': get_images(
                               '../../assets/graphics/player-animations/backward/movement')}

        # general setup
        # self.image = pygame.Surface((32, 64))
        # self.image.fill('green')

        #print(len(get_images('./graphics/player-animations/forward/idle')))
        #print(len(get_images2('C://Users//alex7//OneDrive//Pictures//Camera Roll')))
        #print(len(get_images2('../assets/graphics/player-animations/forward/idle')))
        #print(len(get_images2('../../assets/graphics/player-animations/forward/idle')))

        #print(self.frame_index)
        #print(self.animations[self.status])
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def animate(self, dt):
        self.frame_index += 6 * dt

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "backward"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "forward"
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

    def get_status(self):

        # idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

    def move(self, dt):

        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.get_status()

        self.move(dt)
        self.animate(dt)
