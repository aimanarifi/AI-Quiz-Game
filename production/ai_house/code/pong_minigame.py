import pygame
from pygame.locals import *
import sys, os
from pygame import mixer
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from production.general.quiz import Quiz 
import production.general.db.DatabaseService as DB
# from production.ai_house.code.intro import intro_level
# from production.ai_house.code.main2 import Game 
# from production.ai_house.code.level2 import Level
# from production.ai_house_main import *





pygame.init()
    
screen_width = 1280
screen_height = 720


    # global screen,screen_width,screen_height, fpsClock, bg_img,margin
    # global live_ball, fps, white, font

pygame.display.set_caption('AI House')
player_stats = DB.get_user()




screen = pygame.display.set_mode((screen_width, screen_height))
end = False

#define background image
bg_img = pygame.image.load('ai_house/images/game_bg.jpg')
bg_img = pygame.transform.scale(bg_img,(screen_width,screen_height))

exp = 0


quiz_status = None



#define game variables
margin = 50


fps = 70
live_ball = False
fpsClock = pygame.time.Clock()



#define colours
white = (255, 255, 255)

#define font
font = pygame.font.Font('graphics/font/Gameplaya.ttf', 20)

def miniquiz(player_score, cpu_score):
    global  quiz_status, exp, i
    i=0
    mixer.music.pause()
    quiz1 = Quiz("Question 1. Which of the following Narrow AI systems would you want to include when building the Broad AI system for a self-driving car?", ["Long-term weather patterns","Information from the Global Positioning System (GPS)","Entertainment trends","International news"],"Information from the Global Positioning System (GPS)")
    quiz2 = Quiz("Question 2. What one word best describes what AI can do?", ["Predict","Decide","Think","Calculate"], "Predict")
    quiz3 = Quiz("Question 3. Fill in the blank. Data scientists describe a library of text and data used to train machine learning systems as a ________. ", ["Corpus","Collation","Collection","Compilation"],"Corpus")
    quiz4 = Quiz("Question 4. What is the first step a machine must take in order to win a debate?", ["Ingest content from a corpus of publications, books, articles and web sites.","Build an argument using all the elements in the corpus of the opponent opening speech.","Understand human speech in order to listen and object to debate coach instructions.","Recite a corpus of text in a silly, rapid, or hostile way that could distract the opponent."],"Ingest content from a corpus of publications, books, articles and web sites.")
    
    quizzes = [quiz1,quiz2, quiz3, quiz4]
    
    
    for quiz in quizzes:
        quiz.run()
        if quiz.get_score() == 1:
            exp += 10
        
    
        quiz_status = False
    mixer.music.unpause()

    
    mixer.music.play()
    
        
    
        

    # loop = True
    # while loop:
    #     for event in pygame.event.get():
    #             if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    #                 loop = False
    #                 print("b")
    

    
    
def draw_board():
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin), 2)



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))




class paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(x, y, 20, 90)
        self.speed = 7
        self.ai_speed = 6

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)
            print("up")
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)
            print("down")

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

    def ai(self):
        #ai to move the paddle automatically
        #move down
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.ai_speed)
        #move up
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.ai_speed)



class ball():
    def __init__(self, x, y):
        self.reset(x, y)


    def move(self):

        #check collision with top margin
        if self.rect.top < margin:
            self.speed_y *= -1
        #check collision with bottom of the screen
        if self.rect.bottom > screen_height:
            self.speed_y *= -1
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1

        #check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.left > screen_width:
            self.winner = -1

        #update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner


    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)


    def reset(self, x, y):
        self.x = x
        self.y = y
        self.ball_rad = 8
        self.rect = Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -7
        self.speed_y = 5
        self.winner = 0# 1 is the player and -1 is the CPU



 #create paddles


def run(player_score, cpu_score):
    global quiz_status
    live_ball = False
    winner = 0
    speed_increase = 0
    
    #create game loop
    run = True
    
    while run:
        
        screen.blit(bg_img,(0,0))
        fpsClock.tick(fps) 
        draw_board()
        draw_text('CPU: ' + str(cpu_score), font, white, 20, 15)
        draw_text('P1: ' + str(player_score), font, white, screen_width - 100, 15)
        draw_text('BALL SPEED: ' + str(abs(pong.speed_x)), font, white, screen_width // 2 - 100 , 15)
        draw_text('EXP: ' + str(exp), font, white, screen_width // 2 + 200  , 15)
        
        #draw paddles
        player_paddle.draw()
        cpu_paddle.draw()
        

        

        if live_ball == True:
            speed_increase += 1.5
            winner = pong.move()
            if winner == 0:
                #draw ball
                pong.draw()
                #move paddles
                player_paddle.move()
                cpu_paddle.ai()
            else:
                live_ball = False
                if winner == 1:
                    player_score += 1
                    pong.speed_x += 1
                    

                elif winner == -1:
                    cpu_score += 1


        #print player instructions
        if player_score == 2:
            while quiz_status == True:
                print("Running quiz page")
                miniquiz(player_score, cpu_score)
                live_ball = True


        if live_ball == False:
            if winner == 0:
                draw_text('CLICK ANYWHERE TO START', font, white,425 , screen_height // 2 -100)
                draw_text('USE ARROW KEYS TO MOVE', font, white, (screen_width //2)-200 , screen_height // 2 -50)
                draw_text("YOU WILL BE QUIZZED IF YOU CAN SCORE TWICE AGAINST THE AI", font, white, (screen_width //2)-400 , screen_height // 2 -10)
                draw_text("You'll gain 10 EXP for each correct answer", font, white, (screen_width //2)-300 , screen_height // 2 + 20 )



                
                
            if winner == 1:
                quiz_status = True
                draw_text('YOU SCORED!', font, white, 520, screen_height // 2 -100)
                draw_text('CLICK ANYWHERE TO START', font, white,(screen_width //2)-200 , screen_height // 2 -50)
                
                    
                    
                
            if winner == -1:
                draw_text('CPU SCORED!', font, white, 520, screen_height // 2 -100)
                draw_text('CLICK ANYWHERE TO START', font, white, (screen_width //2)-200 , screen_height // 2 -50)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and live_ball == False:
                live_ball = True
                pong.reset(screen_width - 60, screen_height // 2 + 50)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                player_stats.exp_ai += exp
                if player_stats.highscore_ai < player_score:
                    player_stats.highscore_ai = player_score
                
                DB.update_user(player_stats)

                print("a")
                


        if speed_increase > 500:
            speed_increase = 0
            if pong.speed_x < 0:
                pong.speed_x -= 1
            if pong.speed_x > 0:
                pong.speed_x += 1
            if pong.speed_y < 0:
                pong.speed_y -= 1
            if pong.speed_y > 0:
                pong.speed_y += 1
            
           

            
        pygame.display.update()
    


player_paddle = paddle(screen_width - 40, screen_height // 2)
cpu_paddle = paddle(20, screen_height // 2)

#create pong ball
pong = ball(screen_width - 60, screen_height // 2 + 50)


    
    
    
   
   