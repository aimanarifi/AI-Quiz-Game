import pygame
from settings import *
from player import Player
from sprites import Generic


class Level:
    def __init__(self):
        # get the display surface
        self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self):
        self.player = Player((100, 100), self.all_sprites)
        Generic(
            pos=(0, 0),
            surf=pygame.image.load("player_house/data/tmx/player_house.png").convert_alpha(),
            groups=self.all_sprites,
            z=LAYERS["Floor"],
        )

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.layered_draw(self.player)
        self.all_sprites.update(dt)
        pygame.transform.scale(self.display_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))


   
            


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # zoom
        self.zoom_scale = 3.5
        self.internal_surf_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center=(self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

    def layered_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        self.internal_surf.fill('black')

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.internal_surf.blit(sprite.image, offset_rect)

        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=(self.half_w, self.half_h))

        self.display_surface.blit(scaled_surf, scaled_rect)
