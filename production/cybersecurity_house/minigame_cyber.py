import pygame
from random import randint

class TicTacToe():
    def __init__(self, game):
        self.game = game
        self.first_turn = randint(0,1)

        if self.first_turn == 0:
            self.player_turn = False
        else:
            self.player_turn = True

        self.winner = None

        self.board_array = ["-", "-", "-",
                            "-", "-", "-",
                            "-", "-", "-"]

    def check_input(self):
        key = pygame.key.get_pressed()

        if (not self.winner) and self.player_turn:
            if key[pygame.K_1] and self.board_array[0] == "-":
                self.board_array[0] = "x"
                self.player_turn = False
            elif self.board_array[0] == "o":
                print("piece dere")

        if (not self.winner) and self.player_turn:
            if key[pygame.K_2] and self.board_array[1] == "-":
                self.board_array[1] = "x"
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_3] and self.board_array[2] == "-":
                self.board_array[2] = "x"
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_4] and self.board_array[3] == "-":
                self.board_array[3] = "x"
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_5] and self.board_array[4] == "-":
                self.board_array[4] = "x"
                self.player_turn = False
            elif self.board_array[4] == "o":
                print("piece dere")

        if (not self.winner) and self.player_turn:
            if key[pygame.K_6] and self.board_array[5] == "-":
                self.board_array[5] = "x"
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_7] and self.board_array[6] == "-":
                self.board_array[6] = "x"
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_8] and self.board_array[7] == "-":
                self.board_array[7] = "x"
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_9] and self.board_array[8] == "-":
                self.board_array[8] = "x"
                self.player_turn = False
            elif self.board_array[8] == "o":
                print("piece dere")

    # check for win or tie
    def checkHorizontal(self):
        if self.board_array[0] == self.board_array[1] == self.board_array[2] and self.board_array[0] != "-":
            self.winner = self.board_array[0]
            return True
        elif self.board_array[3] == self.board_array[4] == self.board_array[5] and self.board_array[3] != "-":
            self.winner = self.board_array[3]
            return True
        elif self.board_array[6] == self.board_array[7] == self.board_array[8] and self.board_array[6] != "-":
            self.winner = self.board_array[6]
            return True

    def checkRow(self):
        if self.board_array[0] == self.board_array[3] == self.board_array[6] and self.board_array[0] != "-":
            self.winner = self.board_array[0]
            return True
        elif self.board_array[1] == self.board_array[4] == self.board_array[7] and self.board_array[1] != "-":
            self.winner = self.board_array[1]
            return True
        elif self.board_array[2] == self.board_array[5] == self.board_array[8] and self.board_array[2] != "-":
            self.winner = self.board_array[3]
            return True

    def checkDiag(self):
        if self.board_array[0] == self.board_array[4] == self.board_array[8] and self.board_array[0] != "-":
            self.winner = self.board_array[0]
            return True
        elif self.board_array[2] == self.board_array[4] == self.board_array[6] and self.board_array[4] != "-":
            self.winner = self.board_array[2]
            return True

    def checkIfWin(self):
        if self.checkHorizontal() or self.checkRow() or self.checkDiag():
            print(f"The winner is {self.winner}!")

    def checkIfTie(self):
        if "-" not in self.board_array:
            print("It is a tie!")

    def computer_move(self):
        while not self.player_turn:
            position = randint(0, 8)
            if self.board_array[position] == "-":
                self.board_array[position] = "o"
                self.player_turn = True

    def draw_board(self):
        pass

    def run(self):
        if not self.player_turn:
            self.computer_move()
        else:
            self.check_input()

        self.checkIfWin()
        self.checkIfTie()


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    INSTRUCTION_OFFSET = 10
    PIECE_OFFSET = 20

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        self.tic_tac_toe = TicTacToe(self)

        self.large_font = pygame.font.Font('assets/Khonjin.ttf', 72)
        self.medium_font = pygame.font.Font("assets/Khonjin.ttf", 32)
        self.small_font = pygame.font.Font("assets/Khonjin.ttf", 28)

        self.bg_surf = pygame.transform.scale(pygame.image.load('assets/imgs/bg.png'),
                                              (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.grid_surf = pygame.transform.scale(pygame.image.load('assets/imgs/img18.png'),
                                                (self.SCREEN_WIDTH / 5, self.SCREEN_WIDTH / 5))

        self.x_surf = self.large_font.render("x", False, (101, 64, 83))
        self.o_surf = self.large_font.render("o", False, (101, 64, 83))

        self.title_surf = self.large_font.render("Tic-Tac-Toe", False, (168, 96, 93))
        self.instruction_surf = self.medium_font.render("Instructions", False, (101, 64, 83))
        self.instruction_surf_l1 = self.small_font.render("   - Let AI take it's turn (if o' turn)", False, (101, 64, 83))
        self.instruction_surf_l2 = self.small_font.render("   - Take your turn (if x' turn)", False, (101, 64, 83))
        self.instruction_surf_l3 = self.small_font.render("   - Answer question correctly", False, (101, 64, 83))
        self.instruction_surf_l4 = self.small_font.render("   - Or your move will be randomised !!", False, (101, 64, 83))
        self.instruction_surf_l5 = self.small_font.render("   - Win to increase score !!", False, (101, 64, 83))
        # self.tic_tac_toe = TicTacToe(self)

        self.center_piece_offset_width = self.grid_surf.get_width()/6 - self.x_surf.get_width()/2
        self.center_piece_offset_height = + self.grid_surf.get_height()/6 - self.x_surf.get_height()/2

        self.draw_x_o_dict = {
            "1": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.center_piece_offset_height),

            "2": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width()/3
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.center_piece_offset_height),

            "3": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 2*(self.grid_surf.get_width()/3)
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.center_piece_offset_height),

            "4": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height()/3
                  + self.center_piece_offset_height),

            "5": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width()/3
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height()/3
                  + self.center_piece_offset_height),

            "6": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 2*(self.grid_surf.get_width()/3)
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height()/3
                  + self.center_piece_offset_height),

            "7": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 2*(self.grid_surf.get_height()/3)
                  + self.center_piece_offset_height),

            "8": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width()/3
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 2*(self.grid_surf.get_height()/3)
                  + self.center_piece_offset_height),

            "9": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 2*(self.grid_surf.get_width()/3)
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 2*(self.grid_surf.get_height()/3)
                  + self.center_piece_offset_height)
        }

    def new_game(self):
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.new_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

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

    def draw_board(self):
        for index, value in enumerate(self.tic_tac_toe.board_array):
            index_str = str(index+1)
            if value != "-":
                if value == "x":
                    self.screen.blit(self.x_surf, self.draw_x_o_dict[index_str])
                elif value == "o":
                    self.screen.blit(self.o_surf, self.draw_x_o_dict[index_str])


    def run(self):
        while True:
            self.setup()
            self.tic_tac_toe.run()
            self.draw_board()
            self.check_events()
            pygame.display.update()
            self.clock.tick(60)

            '''print(1)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height()/6)

            print(2)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 3*self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height()/6)

            print(3)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 5*self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height()/6)

            print(4)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 3*self.grid_surf.get_height()/6)

            print(5)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 3*self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 3*self.grid_surf.get_height()/6)

            print(6)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 5*self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 3*self.grid_surf.get_height()/6)

            print(7)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 5*self.grid_surf.get_height()/6)

            print(8)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 3*self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 5*self.grid_surf.get_height()/6)

            print(9)
            print(self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 5*self.grid_surf.get_width()/6)
            print(self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 5*self.grid_surf.get_height()/6)'''

if __name__ == '__main__':
    game = Game()
    game.run()
