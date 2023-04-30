import pygame
import minigame
import production.general.db.DatabaseService as DB
from sys import exit

def setup():
    """
    Declare essential variables and objects
    """

    global screen, clock, bg, bg_rect, house_surf, house_rect
    global player_surf, player_rect, player_stats
    global levels_access_rect
    global text_bubble_surf, text_bubble_rect
    global key_hold, key_hold_counter

    screen = pygame.display.get_surface()
    screen.fill((25,36,40))
    clock = pygame.time.Clock()

    bg = pygame.transform.scale_by(pygame.image.load("cloud_house/assets/cloud_base.png"),2.5)
    bg_rect = bg.get_rect(center=screen.get_rect().center)
    house_surf = pygame.Surface((500,500)) # <--This is temp- Load house image
    house_rect = house_surf.get_rect(center=screen.get_rect().center)
    
    player_surf = pygame.Surface((20,20))
    player_rect = player_surf.get_rect(midbottom=house_rect.midbottom)
    player_stats = DB.get_user()
    
    print(player_stats)
    levels_access_rect = [pygame.Rect(0,0, 100, 100) for i in range(3)]
    levels_access_rect[0].midleft = (house_rect.left, 440)
    levels_access_rect[1].midright = (house_rect.right, 250)
    levels_access_rect[2].midright = (house_rect.right, 460)

    text_bubble_surf, text_bubble_rect = None, None
    key_hold, key_hold_counter = False, 0
    
def display():
    """
    Blit everything
    """

    screen.blit(bg,bg_rect)
    #screen.blit(house_surf, house_rect)

    for level_access_rect in levels_access_rect:
        pygame.draw.rect(screen, (139,94,52), level_access_rect)

    screen.blit(player_surf, player_rect)
    
    if text_bubble_surf:
        screen.blit(text_bubble_surf, text_bubble_rect)


def check_player_movement():
    """
    player can navigate using wasd or arrow keys
    """
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player_rect.top > house_rect.top:
        player_rect.y -= 2

    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_rect.bottom < house_rect.bottom:
        player_rect.y += 2

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_rect.left > house_rect.left:
        player_rect.x -= 2

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_rect.right < house_rect.right:
        player_rect.x += 2

def check_player_level_access():
    """
    This function controls the interaction of player with the minigame access point

    There is an internal function that is used to check player holding a key for certain period of time
    """
    
    def hold_f_to_enter(difficulty: int = 0):
        """
        This detects player holding f for until counter hits 100.
        The counter resets if the key is released or after it reaches 100
        """
        global key_hold, key_hold_counter

        if not pygame.key.get_pressed()[pygame.K_f]: return
        
        if key_hold:
            key_hold_counter += 1

            if key_hold_counter == 100:
                print("successfully hold")
                key_hold_counter = 0
                minigame.run(difficulty, player_stats)

        else:
            key_hold = True
            key_hold_counter = 0

    global text_bubble_surf, text_bubble_rect
    any_collision = False

    #Upon collision, it shows instruction to access the game and handle all necessary input
    for i, access_rect in enumerate(levels_access_rect):

        if player_stats.exp_cloud >= i and player_rect.colliderect(access_rect):
            any_collision = True
            hold_f_to_enter( i + 1)
            if not text_bubble_surf:
                text_bubble_surf = pygame.Surface((100,20))
                text_bubble_surf.fill("Green")
                text_bubble_rect = text_bubble_surf.get_rect(midbottom = access_rect.midtop)

    if not any_collision:
        text_bubble_rect, text_bubble_surf = None, None

def run():
    """
    The cloud house entry point and it controls all stuff
    """

    global key_hold
    loop = True
    setup()

    while loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                key_hold = False

            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                loop = False


        check_player_movement()
        check_player_level_access()
        display()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('Cloud house: Currently running directly from cloud_house.py')
    run()