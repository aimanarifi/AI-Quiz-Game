import pygame as pg
import pygame.image


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    INSTRUCTION_OFFSET = 10

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.clock = pg.time.Clock()

        self.large_font = pygame.font.Font('assets/Khonjin.ttf', 72)
        self.medium_font = pygame.font.Font("assets/Khonjin.ttf", 32)
        self.small_font = pygame.font.Font("assets/Khonjin.ttf", 28)

        self.bg_surf = pygame.transform.scale(pygame.image.load('assets/imgs/bg.png'),
                                              (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.grid_surf = pygame.transform.scale(pygame.image.load('assets/imgs/img18.png'),
                                                (self.SCREEN_WIDTH / 5, self.SCREEN_WIDTH / 5))

        self.title_surf = self.large_font.render("Tic-Tac-Toe", False, (168, 96, 93))
        self.instruction_surf = self.medium_font.render("Instructions", False, (101, 64, 83))
        self.instruction_surf_l1 = self.small_font.render("   - Let AI take it's turn (if o' turn)", False, (101, 64, 83))
        self.instruction_surf_l2 = self.small_font.render("   - Take your turn (if x' turn)", False, (101, 64, 83))
        self.instruction_surf_l3 = self.small_font.render("   - Answer question correctly", False, (101, 64, 83))
        self.instruction_surf_l4 = self.small_font.render("   - Or your move will be randomised !!", False, (101, 64, 83))
        self.instruction_surf_l5 = self.small_font.render("   - Win to increase score !!", False, (101, 64, 83))
        # self.tic_tac_toe = TicTacToe(self)

    def new_game(self):
        pass
        # self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                # sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()

    def setup(self):
        # background
        self.screen.blit(self.bg_surf, (0, 0))

        # game grid
        self.screen.blit(self.grid_surf, (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2,
                                          self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2))

        # title
        self.screen.blit(self.title_surf, (self.SCREEN_WIDTH / 2 - self.title_surf.get_width() / 2,
                                           80 - self.title_surf.get_height() / 2))

        # instructions
        self.screen.blit(self.instruction_surf, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                 + self.grid_surf.get_width() + game.INSTRUCTION_OFFSET,
                                                 self.grid_surf.get_height() - self.instruction_surf.get_height() / 2))

        self.screen.blit(self.instruction_surf_l1, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + game.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf.get_height()))

        self.screen.blit(self.instruction_surf_l2, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + game.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height()*2))

        self.screen.blit(self.instruction_surf_l3, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + game.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height()*3))

        self.screen.blit(self.instruction_surf_l4, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + game.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height()*4))
        self.screen.blit(self.instruction_surf_l5, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + game.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height()*5))

    def run(self):
        while True:
            self.setup()
            # self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
