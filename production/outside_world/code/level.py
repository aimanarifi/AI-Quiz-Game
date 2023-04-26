import pygame
import os
from settings import *
from player import Player
from sprites import Generic, Portal, Blacksmith, Wave, Fish, Tree
from pytmx.util_pygame import load_pygame


def get_images_portal(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        image_surface_resized = pygame.transform.scale(image_surface, (75, 75))
        surfaces.append(image_surface_resized)

    return surfaces


def get_images(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        surfaces.append(image_surface)

    return surfaces


class Level:
    def __init__(self):
        # get the display surface
        self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        # importing tmx file (tiled map)
        tmx_data = load_pygame('../data/tmx/outside_world.tmx')
        print("alex bakers mum is in notty house")

        # importing static tiles
        # water
        for x, y, surf in tmx_data.get_layer_by_name('Water Layer').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # ground
        for x, y, surf in tmx_data.get_layer_by_name('Ground Layer').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # paths
        for x, y, surf in tmx_data.get_layer_by_name('Path Layer').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        #cliffs
        for x, y, surf in tmx_data.get_layer_by_name('Cliffs').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # layers that can be traversed over (grass, grass overlay, shrubs, flowers)
        for layer in ['Grass', 'Grass Overlay', 'Shrubs', 'Flowers', 'Water Rocks', 'Water Flora']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # layers that should not be traversed over / should force collision (bush, rocks)
        for layer in ['Bush', 'Rocks']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # ladder
        for x, y, surf in tmx_data.get_layer_by_name('Ladder').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # more layers that can be traversed over (stairs)
        for x, y, surf in tmx_data.get_layer_by_name('Stairs').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # more layers that can not be traversed over (environment, ground tree trucks)
        for layer in ['Environment', 'Ground Tree Trunks']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # house entrance
        for x, y, surf in tmx_data.get_layer_by_name('House Entrance').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # trees
        for obj in tmx_data.get_layer_by_name('Tree Objects'):
            Tree((obj.x, obj.y), obj.image, self.all_sprites, obj.name, LAYERS['tree'])

        # importing animated object tiles
        # blacksmith / stat man
        blacksmith_frames = get_images('../../assets/graphics/outside_world_graphics/Blacksmith')
        for obj in tmx_data.get_layer_by_name('Blacksmith'):
            Blacksmith((obj.x, obj.y), blacksmith_frames, [self.all_sprites, self.collision_sprites])

        # waves
        for obj in tmx_data.get_layer_by_name('Waves'):
            Wave((obj.x, obj.y), obj.name, self.all_sprites)

        # fish
        for obj in tmx_data.get_layer_by_name('Fish'):
            Fish((obj.x, obj.y), obj.name, self.all_sprites)

        # TODO Make animation smooth or replace portals
        # portals
        portal_frames = get_images_portal('../../assets/graphics/outside_world_graphics/Portal/animated')
        for obj in tmx_data.get_layer_by_name('Portal'):
            # obj_image = pygame.transform.scale(obj.image, (obj.width, obj.width))
            Portal((obj.x, obj.y), portal_frames, [self.all_sprites, self.collision_sprites])

        # player
        self.player = Player((100, 100), self.all_sprites, self.collision_sprites)

        # image of tiled map for testing
        Generic(
            pos=(0, 0),
            surf=pygame.image.load("../data/tmx/outside_world.png").convert_alpha(),
            groups=self.all_sprites,
            z=LAYERS["ground"],
        )

    def run(self, dt):
        self.display_surface.fill('black')
        #self.display_surface.blit(Generic.hitbox)
        self.all_sprites.layered_draw(self.player)
        self.all_sprites.update(dt)
        # pygame.transform.scale(self.display_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # zoom
        self.zoom_scale = 2.5
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
            if (layer != 8) and (layer != 9):
                for sprite in self.sprites():
                    if sprite.z == layer:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.internal_surf.blit(sprite.image, offset_rect)
            else:
                for sprite in sorted(self.sprites(), key = lambda sprite: (sprite.rect.centery + sprite.rect.h/1.5)):
                    #print(sprite.rect.centery)
                    if sprite.z == layer:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.internal_surf.blit(sprite.image, offset_rect)

        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=(self.half_w, self.half_h))

        self.display_surface.blit(scaled_surf, scaled_rect)
