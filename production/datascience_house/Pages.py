from Window import window, pygame
from NPC_TEXT import TextMainPage, TextLevelOnePage, text_box_position_x, text_box_position_y, font


class MainPage:
    def __init__(self):
        self.image_background = pygame.image.load('images/mainBackground.jpg')
        self.textMainPage = TextMainPage()
        self.button = pygame.Rect(580, 500, 210, 50)
        pygame.draw.rect(window, (0, 255, 0), self.button)
        self.text = font.render("Click here to start!", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=self.button.center)

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showWelcomeTextLine(self):
        window.blit(self.textMainPage.welcome_textLine1, (text_box_position_x - 50, text_box_position_y - 100))
        window.blit(self.textMainPage.welcome_textLine2, (text_box_position_x - 50, text_box_position_y - 50))
        window.blit(self.textMainPage.welcome_textLine3, (text_box_position_x - 50, text_box_position_y))
        window.blit(self.textMainPage.welcome_textLine4, (text_box_position_x - 50, text_box_position_y + 50))
        window.blit(self.textMainPage.welcome_textLine5, (text_box_position_x - 50, text_box_position_y + 100))
        window.blit(self.text, self.text_rect)


class LevelOnePage:
    def __init__(self):
        self.image_background = pygame.image.load('images/LevelOneBackground.jpg')
        self.textLevelOnePage = TextLevelOnePage()
        self.needTOShowWelcomeText = True
        self.welcomeTextStartTime = 0
        self.welcomeTextEndTime = 0
        self.welcomeTextLastTime = 0
        self.needTOShowInstructionText = False
        self.instructionTextStartTime = 0
        self.instructionTextEndTime = 0
        self.instructionTextLastTime = 0
        self.needTOShowEndText = True
        self.endTextStartTime = 0
        self.endTextEndTime = 0
        self.endTextLastTime = 0
        self.needToShowExitText = False
        self.exitTextStartTime = 0
        self.exitTextEndTime = 0
        self.exitTextLastTime = 0

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showWelcomeText(self):
        window.blit(self.textLevelOnePage.welcome_textLine1, (text_box_position_x - 50, text_box_position_y - 100))
        window.blit(self.textLevelOnePage.welcome_textLine2, (text_box_position_x - 50, text_box_position_y - 50))
        window.blit(self.textLevelOnePage.welcome_textLine3, (text_box_position_x - 50, text_box_position_y))
        window.blit(self.textLevelOnePage.welcome_textLine4, (text_box_position_x - 50, text_box_position_y + 50))

    def showInstructionText(self):
        window.blit(self.textLevelOnePage.instruction_textLine1, (text_box_position_x + 90, text_box_position_y + 150))
        window.blit(self.textLevelOnePage.instruction_textLine2, (text_box_position_x + 285, text_box_position_y + 200))

    def showEndText(self):
        window.blit(self.textLevelOnePage.end_textLine1, (text_box_position_x - 60, text_box_position_y - 100))
        window.blit(self.textLevelOnePage.end_textLine2, (text_box_position_x - 60, text_box_position_y - 50))
        window.blit(self.textLevelOnePage.end_textLine3, (text_box_position_x - 60, text_box_position_y))
        window.blit(self.textLevelOnePage.end_textLine4, (text_box_position_x - 60, text_box_position_y + 50))

    def showExitText(self):
        window.blit(self.textLevelOnePage.exit_textLine1, (text_box_position_x + 18, text_box_position_y))
        window.blit(self.textLevelOnePage.exit_textLine2, (text_box_position_x + 18, text_box_position_y + 50))
