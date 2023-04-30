"""
    @Author : Kyungtae Han, Student 
    @Date: 2023.March.23rd
    @Institution : University of Sheffield
    @Email: khan3@sheffield.ac.uk 
    @Last modified by: Kyungtae Han 
    @Last Modified time: 2023-April-15th
    @Description : Specially made for AI Group Project with IBM, Dr.Emma Norling, Dr.Matthew Ellis and Dr. Roger Moore. 
    @NPC : Dr.Emma Norling, Dr. Matthew Ellis and Dr.Roger Moore.
       Copyright : Kyungtae Han. Strongly disagree with plagiarism, distribution of codes unless stated. 
"""
#!/usr/bin/env python3
import pygame
from pygame.locals import *
import pygame.freetype
from pygame import mixer 

import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import sqlite3 
import math
import os
import sys




os.chdir("production/blockchain_house/ibm_blockchain")


print("Your Current Directory in BlockChain House Main file is = ",os.getcwd())
#production/blockchain_house/ibm_blockchain/
  
# # appending the parent directory path
# sys.path.append('project/production/blockchain_house/ibm_blockchain')

# from sceneStack import SceneStack

#from pydub import AudioSegment
#from pydub.playback import play







pygame.init()

WIDTH = 1024
HEIGHT = 800
FPS = 60

GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0, 0, 128)
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK_BROWN = (139,69,19)
SKYBLUE = (0,181,226)
DARK_GRAY = (222,222,222)
LAWN_GREEN = (124,252,0)
ORANGE = (255,165,0)
ROSE = (243, 58, 106)
PURPLE = (138,43,226)


SCORE = 0 
SCORE_INCREMENT = 10

FONT_DIRECTORY = "assets/font/PressStart2P.ttf"
GAME_FONT = pygame.font.Font(FONT_DIRECTORY, 24)

DIALOG_COUNT = 0
TOWN_NPC_DIALOG_INDEX = 0 
EASYMODE_NPC_INDEX = 0
MEDIUMMODE_NPC_INDEX = 0
HARDMODE_NPC_INDEX = 0


IS_SPACEBAR_PRESSED_0 = False
QUIZ_INDEX = 0
QUIZ_NPC_DIALOG_INDEX = 0 
IS_QUIZ_STARTED = False



def resetSurface(screen):
    return screen.fill(BLACK)

########################################### Object Start #####################################################
class ObjectStack:
    def __init__(self):
        self.next = self
    
    def processInput(self, events, pressed_keys):
        print("Object Stack made by Kyungtae Han")

    def update(self):
        print("Object Stack made by Kyungtae Han")

    def render(self, screen):
        print("Object Stack made by Kyungtae Han")

    def push(self, next_obj):
        self.next = next_obj
    
    def pop(self):
        self.push(None)

class IBMWatson: 
    def __init__(self):
        print("hello world ")
       # authenticator = IAMAuthenticator('FbVBCmrflY290CiorB8QH9mUT-nuybxutzFzZLNjTspT')
        # text_to_speech = TextToSpeechV1(
        #     authenticator=authenticator
       # )

        # text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/2340778d-f272-4d32-bf19-1d83f9ad9a0d')

        # with open('hello_world.wav', 'wb') as audio_file:
        #     audio_file.write(
        #         text_to_speech.synthesize(
        #             watsonText,
        #             voice='en-US_KevinV3Voice',
        #             accept='audio/wav'        
        #         ).get_result().content) 

    # @staticmethod
    # def autoplay():
    #     song = AudioSegment.from_wav('hello_world copy.wav')
    #     play(song)
        
class Sqlite: 
    def __init__(self):
        self.commonConn = sqlite3.connect('../../general/db/AIGame.db')
        self.localConn = sqlite3.connect('LocalBlockChain.db')
    
    def selectFromAchievementbyID(self,id):
        cur = self.localConn.cursor()
        # print(type(str(id)),"    " ,difficulty)
        # print("SELECT * FROM Achievement WHERE id = "+str(id)")
        cur.execute("SELECT * FROM Achievement WHERE id = "+str(id)+";")
       
        rows = cur.fetchall()
        return rows # tuples in list
    
    
    def updateHighScore(self,idnum,highScorenum):
        id = str(idnum)
        highScore = str(highScorenum)
   
        if self.getHighestScore(idnum) < highScorenum:
            print("Inn")
            self.commonConn.execute("UPDATE USER SET HIGHSCORE_BLOCKCHAIN = "+ highScore +" WHERE ID = " + id)
            self.commonConn.commit()
        # self.commonConn.close()
        
        self.localConn.execute("UPDATE Leaderboard SET score = "+ highScore +" WHERE id = " + id)
        self.localConn.commit()
        # self.localConn.close()
        # print ("records created succesffuly")
        # conn.close()
        # print("uh-oh, you didn't override this in the child class")
    
    def getHighestScore(self,id):
        cur = self.commonConn.cursor()
        cur.execute("SELECT * FROM USER")
        rows = cur.fetchall()
        for row in rows:
            if row[0] == id:
                return row[11]
        return 0
        
    
    def selectFromLocalBlockChain(self):
        cur = self.localConn.cursor()
        cur.execute("SELECT * FROM LeaderBoard")

        rows = cur.fetchall()
        return rows # tuples in list 
        # print(type(rows[0]))
        
        # for row in rows:
        #     print(row[1])
    
    def selectFromAIGame(self):
        cur = self.commonConn.cursor()
        cur.execute("SELECT * FROM USER")

        rows = cur.fetchall()
        return rows #tuples in list 
        # print(type(rows[0]))
        
        # for row in rows:
        #     print(row[1])
            
    def close(self):
        self.localConn.close()
        self.commonConn.close()
        print("Closed Databases Successfully")
        
    
                 
class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.Font(FONT_DIRECTORY, 32)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
 
    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    # def show(self,screen):
    #     screen.blit(button1.surface, (self.x, self.y))
    
    # def show2(self,screen):
    #     screen.blit(button2.surface, (self.x, self.y))
        
    # def show3(self,screen):
    #     screen.blit(button3.surface, (self.x, self.y))        
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")

class MiniSprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        # print("background = ",self.rect,image)

        self.rect.topleft = [startx, starty]
        
       

    def update(self):
        pass
        
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
isLeft = False
isRight = False 
walkCount = 0
VELOCITY = 12

MINI_PLAYER_X = 0
MINI_PLAYER_Y = 630
                    
class MiniPlayer(MiniSprite):
    def __init__(self, path, startx, starty):
        super().__init__(path, startx, starty)
        self.speed = 4 
        self.standardImage = pygame.image.load("assets/character/down/down1.png")
        # self.walkCycle = [pygame.image.load("ibm_blockchain/assets/char1.png"),
        #                   pygame.image.load("ibm_blockchain/assets/char2.png"),
        #                   pygame.image.load("ibm_blockchain/assets/char3.png")]
        self.walk_cycle = [pygame.image.load("assets/character/right/right1.png"),
                           pygame.image.load("assets/character/right/right2.png"),
                           pygame.image.load("assets/character/right/right3.png")]
        self.facing_left = False 
        self.facing_right = False 
        self.animationIndex = 0 
        
        self.x = startx 
        self.y = starty
    
    def getMiniPlayerRect(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        return self.rect 
    
    def gravityCheck(self,groupObj):
        return pygame.sprite.spritecollideany(self , groupObj, False)   
        
    def draw(self,screen):
        global walkCount
        # print ("walkCount = ",walkCount//4, " ", self.facing_left, self.facing_right)
        # print("self.x = ", self.x , " self.y = ", self.y)
        # print(self.rect)
        
        
        if walkCount + 1 >= 27:
            walkCount = 0

        if self.facing_left:
            
            walkImage = self.walk_cycle[walkCount%3]
            walkImage = pygame.transform.scale(walkImage,(50,50))
            walkImage = pygame.transform.flip(walkImage,True,False)
            screen.blit(walkImage, (self.x,self.y))
            walkCount +=1
            # print("Innnnn")
        
        elif self.facing_right:
            walkImage = self.walk_cycle[walkCount%3]
            walkImage = pygame.transform.scale(walkImage,(50,50))
            screen.blit(walkImage, (self.x,self.y))
            walkCount +=1
            # print("Innnnn")
               
        else:
            self.image = pygame.transform.scale(self.standardImage,(50,50))
            screen.blit(self.image, self.rect)
           
        
    # def animationRender(self):
        # self.image = self.walk_cycle[self.animationIndex]
        
        # if self.facing_left:
        #     self.image = pygame.transform.flip(self.image,True,False)
        #     print("walk ani in")
        
        # if self.animationIndex < len(self.walk_cycle)-1:
        #     self.animationIndex +=1 
        #     print("add more index in ", self.animationIndex)
            
        # else:
        #     self.animationIndex = 0 
        #  global walkCount
       

        #  if walkCount + 1 >= 27:
        #         walkCount = 0

        #  if self.facing_left:
        #     win.blit(self.walk_cycle[walkCount//3], (x,y))
        #     walkCount += 1
        
        #  elif not self.facing_left:
        #     win.blit(self.walk_cycle[walkCount//3], (x,y))
        #     walkCount +=1
        #  else:
        #     win.blit(char, (x,y))
            
        
    def update(self,key):
        global walkCount
        global VELOCITY
        global MINI_PLAYER_X 
        global MINI_PLAYER_Y 
        # print("self facing left =", self.facing_left )
        # print("self facing right = ", self.facing_right)
        # key = pygame.key.get_pressed()  
        
         #    if keyPress[K_LEFT]:
         #         EASY_PLAYER_X -= VELOCITY
         #    if keyPress[K_RIGHT]:
         #         EASY_PLAYER_X += VELOCITY
         #    if keyPress[K_UP]:
         #         EASY_PLAYER_Y -= VELOCITY
         #    if keyPress[K_DOWN]:
         #         EASY_PLAYER_Y += VELOCITY 
          
        if key[pygame.K_LEFT]:
            self.facing_left = True
            self.facing_right = False
            # self.standardImage = pygame.image.load("ibm_blockchain/assets/char3.png")
            # self.walk_animation()
            MINI_PLAYER_X -= VELOCITY
            
            # self.move(-self.speed,0)
        elif key[pygame.K_RIGHT] :
            self.facing_left = False
            self.facing_right = True 
            # self.standardImage = pygame.image.load("ibm_blockchain/assets/char4.png")
            # self.walk_animation()
            # self.move(self.speed,0)
            MINI_PLAYER_X += VELOCITY
            
        else : 
            self.facing_left = False 
            self.facing_right = False 
            walkCount = 0
        # elif key[pygame.K_UP]:
        #     # self.standardImage = pygame.image.load("ibm_blockchain/assets/char2.png")
        #     self.move(0,-self.speed)
        # elif key[pygame.K_DOWN]:
        #     # self.standardImage = pygame.image.load("ibm_blockchain/assets/char1.png")
        #     self.move(0,self.speed)
        # else:
        #     self.image = self.standardImage
        
     
             
    
   
        
    def move(self, x, y):
        self.rect.move_ip([x,y])
        # if walkCount + 1 >= 27:
        #         walkCount = 0

        # if self.facing_left:
        #     win.blit(self.walk_cycle[walkCount//3], (x,y))
        #     walkCount += 1
        
        # elif not self.facing_left:
        #     win.blit(self.walk_cycle[walkCount//3], (x,y))
        #     walkCount +=1
        # else:
        #     win.blit(char, (x,y))
        
        

class MiniPlatform(MiniSprite):
    def __init__(self, path, startx, starty):
        super().__init__(path, startx, starty)
        self.x = startx 
        self.y = starty
        #print("self.rect.topleft = miniplatform", self.rect.topleft)
        # self.rect = pygame.Rect(startx, starty, 50, 50)
        # self.image = pygame.transform.scale(self.image,(50,50))
        # print("platform size = ",self.rect,"  ",self.image)
        
    
    def getPlatformRect(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        return self.rect
    
    def changeScale(self):
        self.image = pygame.transform.scale(self.image,(50,20))
        
    def draw(self,screen):
        global RED
        self.image = pygame.transform.scale(self.image,(50,50))
        # pygame.draw.rect(screen, RED, self.rect)
        screen.blit(self.image, self.rect)
                            
                    
                    
class Ball:
    def __init__(self, x, y, radius, screen, dx,dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.dx = dx 
        self.dy = dy
        #  def render(self):
        # pygame.draw.circle(self.screen, GREEN, [self.x, self.y], self.radius)
        # print("Hello world")
        
    def update(self):
        pass
        # self.x += 10
        # self.y += 10
        # print("pos = ",self.x," ",self.y)
        
    def render(self): 
        pygame.draw.circle(self.screen, GREEN, [self.x, self.y], self.radius)

class Platform: 
    def __init__(self, x, y, radius, screen, dx,dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.dx = dx 
        self.dy = dy
        #  def render(self):
        # pygame.draw.circle(self.screen, GREEN, [self.x, self.y], self.radius)
        # print("Hello world")
        
    def update(self):
        # self.x += 10
        # self.y += 10
        pass
        #print("pos = ",self.x," ",self.y)
        
    def render(self): 
        pygame.draw.circle(self.screen, GREEN, [self.x, self.y], self.radius)
       
class Meso: 
    def __init__(self, x, y, radius, screen, dx,dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.dx = dx 
        self.dy = dy
    
    def drawMeso(self):
        print("Hello Meso.")
                
class Player:   
    def __init__(self, name, x, y, scaleX, scaleY,path):
        
        
        self.x = x
        self.y = y 
       
        self.scaleX = scaleX 
        self.scaleY = scaleY
        self.character = pygame.image.load(path)
        self.character = pygame.transform.scale( self.character, (scaleX,scaleY) )
        self.characterRect = self.character.get_rect()
        self.name = name
    
    def getPlayerRect(self):
        return self.characterRect
    
    # Character Render Function
    def drawCharacter(self,screen):
        # print("Hello World")
        screen.blit(self.character,(self.x,self.y))   
        self.characterRect.topleft = self.x,self.y
        #pygame.draw.rect(screen, RED, self.characterRect,4)        
       
     
class Npc: 
    def __init__(self, screen, name, x, y, scaleX, scaleY,path):
        self.screen = screen
        self.x = x
        self.y = y 
        self.scaleX = scaleX 
        self.scaleY = scaleY
        self.npc = pygame.image.load(path)
        self.npc = pygame.transform.scale( self.npc, (scaleX,scaleY) )
        self.name = name
        self.npcRect = self.npc.get_rect()
        
        #  def render(self):
        # pygame.draw.circle(self.screen, GREEN, [self.x, self.y], self.radius)
        # print("Hello world")
    
    def getNpcRect(self):
        self.npcRect = pygame.Rect(self.x, self.y, self.scaleX, self.scaleY)
        return self.npcRect
        
    def update(self):
        # self.x += 10
        # self.y += 10
        # print("pos = ",self.x," ",self.y)
        pass 
    def render(self): 
        self.screen.blit(self.npc,(self.x,self.y))  
        
        #Name Tag
        # global WHITE
        # global BLACK
        # NAME_PADDING_X = 10
        # NAME_PADDING_Y = 5
        # NAME_X = self.x + NAME_PADDING_X
        # NAME_Y = self.y + self.scaleY + NAME_PADDING_Y
        # GAME_FONT = pygame.font.Font(FONT_DIRECTORY, 18)
        # pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y+self.scaleY, 100, 30))
        # self.screen.blit(GAME_FONT.render(self.name, True, BLACK), (NAME_X, NAME_Y))   
        
        
        self.npcRect.topleft = self.x,self.y
        #pygame.draw.rect(self.screen, RED, self.npcRect,4)        
        # print("npc rect = ", self.npcRect)
       

class ScoreBoard: 
    def __init__(self, screen, score, x, y):
        self.text = GAME_FONT.render(f'Score: {score}', True, GREEN, BLUE)
        self.screen = screen 
        self.textRect = self.text.get_rect()
        self.x = x 
        self.y = y 
        
        #SCORE += SCORE_INCREMENT
        
    def render(self):
        self.textRect.center = (self.x,self.y)
        self.screen.blit(self.text, (self.x,self.y))

class ProgressBar:
    def __init__(self, screen, name, x, y, scaleX, scaleY,path):
        
        self.screen = screen
        self.x = x
        self.y = y 
        self.scaleX = scaleX 
        self.scaleY = scaleY
        self.npc = pygame.image.load(path)
        self.npc = pygame.transform.scale( self.npc, (scaleX,scaleY) )
        self.name = name
    
class ExpBar: 
    def __init__(self, screen, name, x, y, scaleX, scaleY,path):
        self.screen = screen
        self.x = x
        self.y = y 
        self.scaleX = scaleX 
        self.scaleY = scaleY
        self.npc = pygame.image.load(path)
        self.npc = pygame.transform.scale( self.npc, (scaleX,scaleY) )
        self.name = name


IS_DATABASE_OPEN_1 = False
IS_ACHIEVEMENT_OPEN = False 
achievementLib = []
class Achievement: 
    def __init__(self, screen):
        self.screen = screen
    
    def render(self,id):
        pygame.draw.rect(self.screen, BLUE, pygame.Rect(60, 60, 900, 600), border_radius = 15)
        
        global FONT_DIRECTORY
        
        ibmLogo = pygame.image.load("assets/ibmlogo.jpeg")
        ibmLogo = pygame.transform.scale(ibmLogo,(150,100))
        self.screen.blit(ibmLogo,(80,80))
        
        uniLogo = pygame.image.load("assets/uniLogo.png")
        uniLogo = pygame.transform.scale(uniLogo,(150,100))
        self.screen.blit(uniLogo,(760,80))
        
        GAME_FONT = pygame.font.Font(FONT_DIRECTORY, 18)
        title = GAME_FONT.render('IBM BlockChain Achievement', True, WHITE)
        self.screen.blit(title,  (260, 110))
        
        GAME_FONT2 = pygame.font.Font(FONT_DIRECTORY, 15)
        rank = GAME_FONT2.render('ID', True, RED)
        self.screen.blit(rank,  (150, 200))
        
        # id = GAME_FONT2.render('ID', True, WHITE)
        # self.screen.blit(id,  (230, 200))
        
        username = GAME_FONT2.render('Difficulty', True, RED)
        self.screen.blit(username,  (320, 200)) 
        
        highest_score = GAME_FONT2.render('Badge', True, RED)
        self.screen.blit(highest_score,  (700, 200)) 
        
        global IS_DATABASE_OPEN_1, achievementLib
        
        if not IS_DATABASE_OPEN_1:
            IS_DATABASE_OPEN_1 = True 
            sqlRunner = Sqlite() 
            achievementInfos = sqlRunner.selectFromAchievementbyID(id)
            achievementLib= achievementInfos
            print(achievementLib)
            sqlRunner.close()
             
        else:
            pass
        
        i = 0
        for row in achievementLib : 
            #print(row)
            GAME_FONT2 = pygame.font.Font(FONT_DIRECTORY, 15) 
            
            id = GAME_FONT2.render(str(row[0]),True,RED)
            self.screen.blit(id,  (150, 250 + 30*i)) 
            
            difficulty = GAME_FONT2.render(str(row[1]),True,RED)
            self.screen.blit(difficulty,  (320, 250 + 30*i))
            
            
            GAME_FONT3 = pygame.font.Font(FONT_DIRECTORY, 12) 
            badgeName = "Blockchain "+str(row[1])+" mode "+str(row[2])+" times slayer"
            badge = GAME_FONT3.render(badgeName,True,RED)
            self.screen.blit(badge,  (500, 250 + 30*i))
             
            
            i+=1
        
        
        # new_score = GAME_FONT2.render('Your Progress', True, RED)
        # self.screen.blit(new_score,  (610, 200)) 
        

IS_DATABASE_OPEN_2 = False 
IS_STATS_OPEN = False
class Stats: # Level, Exp
    def __init__(self, screen): 
        self.screen = screen
        
    def render(self,id):
        global IS_DATABASE_OPEN_2     
        global usersRows, leaderBoardRows 
        
        # Saving Data in Global List 
        if not IS_DATABASE_OPEN_2:
            IS_DATABASE_OPEN_2 = True 
            sqlRunner = Sqlite()
            
            usersSamples = sqlRunner.selectFromAIGame()  # AIGame.db, Tuples in List 
            for usersSample in usersSamples: 
                usersRows.append(usersSample)
            
            
            leaderBoardSamples = sqlRunner.selectFromLocalBlockChain() # LocalBlockChain.db, Tuples in List 
            for leaderBoardSample in leaderBoardSamples: 
                leaderBoardRows.append(leaderBoardSample)
            
            sqlRunner.close()
            
        else:
            pass
        
        blockChainStatsInfo = []
        j=0
        for i in range(0,len(leaderBoardRows)):
            if usersRows and j<len(usersRows):
                #print(usersRows[j])
                usersRow = usersRows[j]
                leaderBoardRow = leaderBoardRows[j]
                
                # Only when ID is equal
                if usersRow[0] is leaderBoardRow[0] : 
                    eachInfo = tuple((usersRow[0],usersRow[1],usersRow[2],usersRow[3],usersRow[5]))
                    # blockChainRankInfo.append(usersRow[0]) # id 
                    # blockChainRankInfo.append(usersRow[1]) # Username 
                    # blockChainRankInfo.append(usersRow[11]) # Highest Score
                    # blockChainRankInfo.append(leaderBoardRow[3]) # New Score
                    blockChainStatsInfo.append(eachInfo)
                    
                j+=1
            else:
                break
        #print(blockChainStatsInfo)
        
        userInfo = None 
        
       
        
        for info in blockChainStatsInfo:
                if info[0] == id:
                    userInfo = info 
        #print(userInfo)
            
        pygame.draw.rect(self.screen, BLUE, pygame.Rect(60, 60, 900, 600), border_radius = 15)
            
        ibmLogo = pygame.image.load("assets/ibmlogo.jpeg")
        ibmLogo = pygame.transform.scale(ibmLogo,(150,100))
        self.screen.blit(ibmLogo,(80,80))
            
        uniLogo = pygame.image.load("assets/uniLogo.png")
        uniLogo = pygame.transform.scale(uniLogo,(150,100))
        self.screen.blit(uniLogo,(760,80))
            
        GAME_FONT = pygame.font.Font(FONT_DIRECTORY, 24)
        title = GAME_FONT.render('IBM BlockChain Stats', True, WHITE)
        self.screen.blit(title,  (260, 110))
            
        GAME_FONT2 = pygame.font.Font(FONT_DIRECTORY, 15)
        rank = GAME_FONT2.render('ID', True, RED)
        self.screen.blit(rank,  (150, 200))
            
            # id = GAME_FONT2.render('ID', True, WHITE)
            # self.screen.blit(id,  (230, 200))
            
        username = GAME_FONT2.render('Username', True, RED)
        self.screen.blit(username,  (280, 200)) 
            
        highest_score = GAME_FONT2.render('Money', True, RED)
        self.screen.blit(highest_score,  (470, 200)) 
            
        new_score = GAME_FONT2.render('Your Progress', True, RED)
        self.screen.blit(new_score,  (610, 200)) 
            
            
        if userInfo is not None:    
            # Personal Info 
            id = GAME_FONT2.render(str(userInfo[0]),True,RED)
            self.screen.blit(id,  (150, 250)) 
                
            username = GAME_FONT2.render(userInfo[1],True,RED)
            self.screen.blit(username,  (280, 250)) 
                
            money = GAME_FONT2.render(str(userInfo[2]),True,RED)
            self.screen.blit(money,  (470, 250)) 
                
            totalExp = GAME_FONT2.render(str(userInfo[3]),True,RED)
            self.screen.blit(totalExp,  (750, 250)) 
            
            blockChainExp = GAME_FONT2.render(str(userInfo[4])+" / ",True,RED)
            self.screen.blit(blockChainExp,  (650, 250)) 
                
            
            
           
    
        
IS_DATABASE_OPEN_3 = False             
IS_LEADERBOARD_OPEN = False 
#IS_DATABASE_OPEN = False 
usersRows = []
leaderBoardRows = []        
class LeaderBoard: 
    def __init__(self, screen): 
        self.screen = screen
    
    def render(self):
        # usersRows = None 
        # leaderBoardRows = None 
        global IS_DATABASE_OPEN_3 
        global usersRows, leaderBoardRows 
        
        # Saving Data in Global List 
        if not IS_DATABASE_OPEN_3:
            IS_DATABASE_OPEN_3 = True 
            sqlRunner = Sqlite()
            usersSamples = sqlRunner.selectFromAIGame()  # AIGame.db, Tuples in List 
            print(usersSamples)
            for usersSample in usersSamples: 
                usersRows.append(usersSample)
            
            leaderBoardSamples = sqlRunner.selectFromLocalBlockChain() # LocalBlockChain.db, Tuples in List 
            
            for leaderBoardSample in leaderBoardSamples: 
                leaderBoardRows.append(leaderBoardSample)
            
            sqlRunner.close()
        else:
            pass
            
        #print(usersRows)    
        # leaderBoardRows.sort(key=lambda x: x[3], reverse = True )
        # usersRows.sort(key=lambda x:x[11], reverse = True )
        # print(usersRows)
        # print(leaderBoardRows)
        
        blockChainRankInfo = []
        
        j=0
        for i in range(0,len(leaderBoardRows)):
            if usersRows and j<len(usersRows):
                usersRow = usersRows[j]
                leaderBoardRow = leaderBoardRows[j]
                
                # Only when ID is equal
                if usersRow[0] is leaderBoardRow[0] : 
                    eachInfo = tuple((usersRow[0],usersRow[1],usersRow[11],leaderBoardRow[3]))
                    # blockChainRankInfo.append(usersRow[0]) # id 
                    # blockChainRankInfo.append(usersRow[1]) # Username 
                    # blockChainRankInfo.append(usersRow[11]) # Highest Score
                    # blockChainRankInfo.append(leaderBoardRow[3]) # New Score
                    blockChainRankInfo.append(eachInfo)
                    
                j+=1
            else:
                break
        
        
        
        blockChainRankInfo = sorted(blockChainRankInfo,key=lambda x:x[-1],reverse = True)
        # print(blockChainRankInfo)
        
        global BLUE 
        global WHITE 
        global PURPLE
        global RED
        
        pygame.draw.rect(self.screen, BLUE, pygame.Rect(60, 60, 900, 600), border_radius = 15)
        
        # gameBackground = pygame.image.load("ibm_blockchain/assets/npc/ibmBackground.jpeg")
        # gameBackground = pygame.transform.scale(gameBackground,(900,600))
        # self.screen.blit(gameBackground,(60,60))
        ibmLogo = pygame.image.load("assets/ibmlogo.jpeg")
        ibmLogo = pygame.transform.scale(ibmLogo,(150,100))
        self.screen.blit(ibmLogo,(80,80))
        
        uniLogo = pygame.image.load("assets/uniLogo.png")
        uniLogo = pygame.transform.scale(uniLogo,(150,100))
        self.screen.blit(uniLogo,(760,80))
        
        
        
        GAME_FONT = pygame.font.Font(FONT_DIRECTORY, 18)
        title = GAME_FONT.render('IBM BlockChain LeaderBoard', True, WHITE)
        self.screen.blit(title,  (260, 110))
        
        GAME_FONT2 = pygame.font.Font(FONT_DIRECTORY, 15)
        rank = GAME_FONT2.render('Rank', True, RED)
        self.screen.blit(rank,  (150, 200))
        
        # id = GAME_FONT2.render('ID', True, WHITE)
        # self.screen.blit(id,  (230, 200))
        
        username = GAME_FONT2.render('Username', True, RED)
        self.screen.blit(username,  (280, 200)) 
        
        highest_score = GAME_FONT2.render('Highest Score', True, RED)
        self.screen.blit(highest_score,  (470, 200)) 
        
        new_score = GAME_FONT2.render('New Score', True, RED)
        self.screen.blit(new_score,  (710, 200)) 
        
        height = 30 
        k=0
        for eachPerson in blockChainRankInfo:
            rank = GAME_FONT2.render(str(k+1),True,RED)
            self.screen.blit(rank,  (150, 250+height*k)) 
            
            username = GAME_FONT2.render(eachPerson[1],True,RED)
            self.screen.blit(username,  (280, 250+height*k)) 
            
            highest_score = GAME_FONT2.render(str(eachPerson[2]),True,RED)
            self.screen.blit(highest_score,  (470, 250+height*k)) 
            
            new_score = GAME_FONT2.render(str(eachPerson[3]),True,RED)
            self.screen.blit(new_score,  (710, 250+height*k)) 
            
            k+=1
            
                
class Quiz: 
    def __init__(self, screen, x , y , quiz_content, answer):
        self.screen = screen
        self.x = x 
        self.y = y 
        self.quiz_content = quiz_content
        self.answer = answer 
        
        
    
    def writeText(self):
        print("Hello World")
        # FONT_DIRECTORY = "ibm_blockchain/assets/PressStart2P.ttf"
        # QUIZ_FONT = pygame.font.Font(FONT_DIRECTORY, 24)
        
        
        
        # ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 24)
    
    def checkAnswer(self,userAnswer):
        return self.answer is userAnswer
        
    def render(self):
        radius = 10
        global RED
        
        BIG_RECT_WIDTH = 900 
        BIG_RECT_HEIGHT = 600 
        pygame.draw.rect(self.screen, WHITE, (self.x,self.y,BIG_RECT_WIDTH,BIG_RECT_HEIGHT), border_top_left_radius=radius, border_top_right_radius=radius, border_bottom_left_radius=radius, border_bottom_right_radius=radius)
        
        gameBackground = pygame.image.load("assets/npc/ibmBackground.jpeg")
        gameBackground = pygame.transform.scale(gameBackground,(BIG_RECT_WIDTH,BIG_RECT_HEIGHT))
        self.screen.blit(gameBackground,(self.x,self.y))
        
        # Quiz Shown Here 
        QUIZ_MARGIN_X = 10 
        QUIZ_MARGIN_Y = 50
        QUIZ_WIDTH = BIG_RECT_WIDTH - (2*QUIZ_MARGIN_X)
        QUIZ_HEIGHT = 100
        
        global GREEN
        QUIZ_X = self.x+QUIZ_MARGIN_X # Quiz Tab X Coordinate   
        QUIZ_Y = self.y+QUIZ_MARGIN_Y # Quiz Tab Y Coordinate 
        pygame.draw.rect(self.screen, RED, (QUIZ_X, QUIZ_Y, QUIZ_WIDTH, QUIZ_HEIGHT))
        
        # Top Left Answer Tab
        QA_HEIGHT_GAP = 30 # Gap between Quiz and Answer tabs 
       
        radius = 15 
        LEFT_ANSWER_X = self.x+QUIZ_MARGIN_X
        TOP_ANSWER_Y = self.y+QUIZ_MARGIN_Y+QUIZ_HEIGHT+QA_HEIGHT_GAP # Top Y coordinate 
        ANSWER_WIDTH = QUIZ_WIDTH/2
        ANSWER_HEIGHT = 330
        #ANSWER_TAB_HEIGHT = (BIG_RECT_HEIGHT - (2*QUIZ_MARGIN_Y + ANSWER_HEIGHT_GAP+ QA_HEIGHT_GAP) )/2
        pygame.draw.rect(self.screen, GREEN, (LEFT_ANSWER_X, TOP_ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT),border_radius = radius)
        
        
        # # Bottom Left Answer Tab 
        ANSWER_HEIGHT_GAP = 20 
        # BOTTOM_ANSWER_Y = TOP_ANSWER_Y+ANSWER_HEIGHT_GAP+180 # Bottom Y coordinate
        
        # pygame.draw.rect(self.screen, RED, (LEFT_ANSWER_X, BOTTOM_ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT))
        
        
        # Top Right Answer Tab 
        ANSWER_WIDTH_GAP = 5 
        RIGHT_ANSWER_X = LEFT_ANSWER_X + ANSWER_WIDTH + ANSWER_WIDTH_GAP
        pygame.draw.rect(self.screen, GREEN, (RIGHT_ANSWER_X, TOP_ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT),border_radius = radius)
        
        # # Bottom Right Answer Tab 
        # ANSWER_WIDTH_GAP = 5 
        # RIGHT_ANSWER_X = LEFT_ANSWER_X + ANSWER_WIDTH + ANSWER_WIDTH_GAP
        # pygame.draw.rect(self.screen, RED, (RIGHT_ANSWER_X, BOTTOM_ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT))
        
        ######### Displaying Questions and Answers #########################
        QUIZ_PADDING_X  = 30 
        QUIZ_PADDING_Y = 30
        QUIZ_TEXT_X = QUIZ_X + QUIZ_PADDING_X
        QUIZ_TEXT_Y = QUIZ_Y + QUIZ_PADDING_Y 
        
        global FONT_DIRECTORY
        FONT_SIZE = 16
        QUIZ_FONT = pygame.font.Font(FONT_DIRECTORY, FONT_SIZE)
        quiz1_content = self.quiz_content
        
        for index in range(0,len(quiz1_content)):
            eachChar = quiz1_content[index]
            quiz1 =  QUIZ_FONT.render(eachChar, True, GREEN)
            if index >46: 
                newIndex = index % 45
                self.screen.blit(quiz1,(QUIZ_TEXT_X + FONT_SIZE*newIndex, QUIZ_TEXT_Y+FONT_SIZE))
            else:
                self.screen.blit(quiz1,(QUIZ_TEXT_X + FONT_SIZE*index, QUIZ_TEXT_Y))
        
        
       
        # self.screen.blit(quiz1,(QUIZ_TEXT_X, QUIZ_TEXT_Y))
        
        
        ###### Answer 
        ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 120)
        ANSWER_PADDING_X = 70
        ANSWER_PADDING_Y = 70
        
        # Top-Left 
       
        LEFT_TEXT_X = LEFT_ANSWER_X + ANSWER_PADDING_X 
        TOP_TEXT_Y = TOP_ANSWER_Y + ANSWER_PADDING_Y 
        answer1_content = "O"
        answer1 =  ANSWER_FONT.render(answer1_content, True, BLUE)
        self.screen.blit(answer1,(LEFT_TEXT_X, TOP_TEXT_Y))
        
        # # Bottom-Left 
        # BOTTOM_TEXT_Y = TOP_TEXT_Y + ANSWER_HEIGHT_GAP + ANSWER_HEIGHT
        # answer2_content = "IBM"
        # answer2 = ANSWER_FONT.render(answer2_content, True, GREEN)
        # self.screen.blit(answer2,(LEFT_TEXT_X, BOTTOM_TEXT_Y))
        
        # Top-Right 
        
        RIGHT_TEXT_X = LEFT_ANSWER_X + ANSWER_WIDTH_GAP + ANSWER_WIDTH + ANSWER_PADDING_X
        answer3_content = "X"
        answer3 = ANSWER_FONT.render(answer3_content, True, RED)
        self.screen.blit(answer3,(RIGHT_TEXT_X, TOP_TEXT_Y))
        
        # # Bottom-Right 
        # answer4_content = "IBM"
        # answer4 = ANSWER_FONT.render(answer4_content, True, GREEN)
        # self.screen.blit(answer4,(RIGHT_TEXT_X, BOTTOM_TEXT_Y))
                     
class Inventory: 
     def __init__(self, screen, name, x, y, scaleX, scaleY,path):
        
        self.screen = screen
        self.x = x
        self.y = y 
        self.scaleX = scaleX 
        self.scaleY = scaleY
        self.npc = pygame.image.load(path)
        self.npc = pygame.transform.scale( self.npc, (scaleX,scaleY) )
        self.name = name
                                          
class Dialog: 
    def __init__(self, screen, npcFilePath, npcName, dialogue_content, endChatButton, prevButton, nextButton, yesButton, noButton):
        self.screen = screen
        self.npcFilePath = npcFilePath 
        self.npcName = npcName 
        self.dialogue_content = dialogue_content 
        self.endChatButton = endChatButton
        self.prevButton = prevButton
        self.nextButton = nextButton
        self.yesButton = yesButton 
        self.noButton = noButton
        
    
    
    # @staticmethod 
    # def hearClick(self,event):
    #     print("Heard from Dialog Class")
    #     print(event)
    #     global LAWN_GREEN
    #     if self.nextButton:
    #         endChatRect = pygame.draw.rect(screen, LAWN_GREEN, pygame.Rect(50, 130, x, y))    
    #         return endChatRect
        
    #     return None
    
    def drawDialogText(self):
        global FONT_DIRECTORY 
        global BLACK
        global RED
        FONT_SIZE = 12
        endChatFont = pygame.font.Font(FONT_DIRECTORY, FONT_SIZE)
        
        # splitByChar = []
        # splitByChar.extend(self.dialogue_content)
        # print(splitByChar)
        n = 43
        splitByString = [self.dialogue_content[i:i+n] for i in range(0, len(self.dialogue_content), n)]
        # print(splitByString)
        
        
        
        
        # j=0
        # #+ FONT_SIZE*newIndex
        # for index in range(0,len(self.dialogue_content)):
        #     eachChar = self.dialogue_content[index]
        #     text =  endChatFont.render(eachChar, True, BLACK)
        #     if index > 44: 
        #         j+=1
        #         resetIndex = index % 45
        #         self.screen.blit(text,(390+ FONT_SIZE*resetIndex , 280+ (FONT_SIZE+10)*j))
        #     else:
        #         self.screen.blit(text,(390 + FONT_SIZE*index, 280))
        
        
        
        
       
       
        
        for index in range (0,len(splitByString)):
            text = endChatFont.render(splitByString[index],2,BLACK)
            text_rect = text.get_rect(topleft=(390,280+FONT_SIZE*index+10))
            # pygame.draw.rect(self.screen, RED, text_rect, 2)
            self.screen.blit(text,text_rect)
      
    
    def drawNPCFigure(self):
        
        npc = pygame.image.load(self.npcFilePath)
        npc = pygame.transform.scale( npc, (100,100) )
        self.screen.blit(npc,(160,300))
        
        DARK_GRAY = (105,105,105)
        radius = 10
        pygame.draw.rect(self.screen, DARK_GRAY, pygame.Rect(110, 390, 200,28),border_radius = radius)    
        
        
        endChatFont = pygame.font.Font(FONT_DIRECTORY, 12)
        text = endChatFont.render(self.npcName,4,WHITE)
        text_rect = text.get_rect(center=(140+70,405))
        self.screen.blit(text,text_rect)
        
        
        
    def drawEndChatButton(self):
        global LAWN_GREEN
        global FONT_DIRECTORY
        global WHITE
        isAllowed = self.endChatButton
        if isAllowed:
            radius = 10
            x = 60 
            y = 235+280+13
            width = 180 
            height = 28
            chatRect = pygame.draw.rect(self.screen, LAWN_GREEN, pygame.Rect(x, y, width,height),border_radius = radius)  
            
            endChatFont = pygame.font.Font(FONT_DIRECTORY, 12)
            text = endChatFont.render("END CHAT",4,WHITE)
            text_rect = text.get_rect(center=(150,y+15))
            self.screen.blit(text,text_rect)
            return chatRect
        
        return None
        
    def drawPrevButton(self):
        global LAWN_GREEN
        global FONT_DIRECTORY
        global WHITE
        isAllowed = self.prevButton
        if isAllowed:
            radius = 10
            chatRect = pygame.draw.rect(self.screen, LAWN_GREEN, pygame.Rect(730, 470, 90,28),border_radius = radius)    
              
            prevChatFont = pygame.font.Font(FONT_DIRECTORY, 12)
            text = prevChatFont.render("← PREV",4,WHITE)
            text_rect = text.get_rect(center=(730+45,470+15))
            self.screen.blit(text,text_rect)
            
            return chatRect
        
        return None
    
    def drawNextButton(self):
        global LAWN_GREEN
        isAllowed = self.nextButton
        if isAllowed:
            radius = 10
            chatRect = pygame.draw.rect(self.screen, LAWN_GREEN, pygame.Rect(830, 470, 90,28),border_radius = radius)    
            prevChatFont = pygame.font.Font(FONT_DIRECTORY, 12)
            text = prevChatFont.render("NEXT →",4,WHITE)
            text_rect = text.get_rect(center=(830+45,470+15))
            self.screen.blit(text,text_rect)
            
            return chatRect
        
        return None
    
    def drawYesButton(self):
        global ORANGE
        isAllowed = self.yesButton
        if isAllowed:
            radius = 10
            chatRect = pygame.draw.rect(self.screen, ORANGE, pygame.Rect(730, 235+280+13, 90,28),border_radius = radius)    
            prevChatFont = pygame.font.Font(FONT_DIRECTORY, 12)
            text = prevChatFont.render("YES",4,WHITE)
            text_rect = text.get_rect(center=(730+45,235+280+13+15))
            self.screen.blit(text,text_rect)
            
            return chatRect
        
        return None
         
    def drawNoButton(self):
        global ROSE
        isAllowed = self.noButton
        if isAllowed:
            radius = 10
            chatRect = pygame.draw.rect(self.screen, ROSE, pygame.Rect(830, 235+280+13, 90,28),border_radius = radius)    
            prevChatFont = pygame.font.Font(FONT_DIRECTORY, 12)
            text = prevChatFont.render("NO",4,WHITE)
            text_rect = text.get_rect(center=(830+45,235+280+13+15))
            self.screen.blit(text,text_rect)
            return chatRect
        
        return None   
        
    def render(self):
        global SKYBLUE
        global DARK_GRAY
        global WHITE
        
        radius = 10
        BIG_X = 50
        BIG_Y = 200
        BIG_WIDTH = 900 
        BIG_HEIGHT = 360
        pygame.draw.rect(self.screen, SKYBLUE, pygame.Rect(BIG_X, BIG_Y, BIG_WIDTH, BIG_HEIGHT), border_radius = radius)
        
        LITTLE_PADDING_X = 10 
        LITTLE_PADDING_Y = 35
        LITTLE_X = BIG_X+LITTLE_PADDING_X
        LITTLE_Y = BIG_Y+LITTLE_PADDING_Y
        LITTLE_WIDTH = BIG_WIDTH - 2 * LITTLE_PADDING_X 
        LITTLE_HEIGHT = BIG_HEIGHT - 2 * LITTLE_PADDING_Y
        
        
        pygame.draw.rect(self.screen, DARK_GRAY, pygame.Rect(LITTLE_X, LITTLE_Y, LITTLE_WIDTH, LITTLE_HEIGHT), border_radius = radius)
        
        
        
        DIALOG_PADDING_X = 300 
        DIALOG_PADDING_Y = 10
        DIALOG_X = BIG_X+DIALOG_PADDING_X
        DIALOG_Y =  BIG_Y+LITTLE_PADDING_Y + 10
        DIALOG_WIDTH = 580
        DIALOG_HEIGHT = LITTLE_HEIGHT - 2*DIALOG_PADDING_Y
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(DIALOG_X, DIALOG_Y , DIALOG_WIDTH, DIALOG_HEIGHT), border_radius = radius)
        
        koreaFlagPath = "assets/koreaFlag.png"
        
        uniLogoPath = "assets/uniLogo.png"
        uniLogo = pygame.image.load(koreaFlagPath)
        uniLogo = pygame.transform.scale( uniLogo, (100,50) )
        self.screen.blit(uniLogo,(100,430)) 
        
        ibmLogoPath = "assets/ibmlogo.jpeg"
        ibmLogo = pygame.image.load(ibmLogoPath)
        ibmLogo = pygame.transform.scale( ibmLogo, (100,50) )
        self.screen.blit(ibmLogo,(215,430)) 
        
        FONT_DIRECTORY = "assets/font/Satisfy-Regular.ttf"
        endChatFont = pygame.font.Font(FONT_DIRECTORY, 15)
        authorLogo = endChatFont.render("designed by Kyungtae Han",6,WHITE)
        authorLogo_rect = authorLogo.get_rect(center = (845,220)) # 235+280+13+15
        self.screen.blit(authorLogo,authorLogo_rect)
        #print(DIALOG_X,"    " ,DIALOG_HEIGHT)
        
        # endChatButton = self.drawEndChatButton(screen, 120,50, True)
        # print(endChatButton)
        
        
        ### Dialog box
        # pygame.display.get_surface().blit(self.surf, self.rect)
        # pygame.draw.rect(self.surf, "white", pygame.Rect(0, 0, 1000, 250), 4)
        ###

        ### Text
        # y = 25
        # lines = self.text.split("\n")
        # for line in lines:
        #     for i in range(len(line)):
        #         pygame.time.delay(35)
        #         font_surf = self.font.render(line[0:i+1], False, "white")
        #         font_rect = font_surf.get_rect(topleft = (25, y))
        #         self.surf.blit(font_surf, font_rect)
        #         pygame.display.update()
        #     y += 50


    
########################################################## Object End ############################################################

#####
# def exitButton(screen):
#     # Exit
#     exitButton = pygame.image.load("ibm_blockchain/assets/exitPygameIcon.png")
#     exitButton = pygame.transform.scale(exitButton,(50,50))
#     exitButtonRect = exitButton.get_rect(topleft=(30, 30))
#     pygame.draw.rect(screen, RED, exitButtonRect,4) 
#     screen.blit(exitButton, exitButtonRect)

def gravityCheck(singleObj,multiObj):
    return pygame.sprite.spritecollide(singleObj,multiObj,False)


IS_QUIZNPC_PLAYED = [True,True,True,True,True] 
quizNPCDialogVoice = [pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quizNPCDialog1.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quizNPCDialog2.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quizNPCDialog3.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quizNPCDialog4.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quizNPCDialog5.wav")]


def unknownQuizNPC(screen, events, keyPress, npcFilePath,npcRect,playerRect):
        global QUIZ_NPC_DIALOG_INDEX
        global IS_QUIZ_STARTED
        global MINI_PLAYER_X, MINI_PLAYER_Y
        global IS_SPACEBAR_PRESSED_0
        global QUIZ_INDEX 
        
        global IS_QUIZNPC_PLAYED, quizNPCDialogVoice 
        # global MINI_PLAYER_X
        # print("BEFORE COMING IN ", TOWN_NPC_DIALOG_INDEX)
        
        if npcRect.colliderect(playerRect) and keyPress[K_SPACE]:
           
            IS_SPACEBAR_PRESSED_0 = True
            print(IS_SPACEBAR_PRESSED_0)
            
        
        if npcRect.colliderect(playerRect) and  IS_SPACEBAR_PRESSED_0 is True and QUIZ_NPC_DIALOG_INDEX>=0 :
         
            if IS_QUIZNPC_PLAYED[QUIZ_NPC_DIALOG_INDEX] : 
                IS_QUIZNPC_PLAYED[QUIZ_NPC_DIALOG_INDEX] = False 
                quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].set_volume(1.4)
                quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].play() 
            # portal_sound.play()
            # PLAYER_X -= 1 
            # PLAYER_Y -= 1
            filePath = npcFilePath
            
            dialog1 = "I am Quiz NPC of IBM BlockChain World. Who are you there? "
            dialog2 = """... ... ... (Guards keeping Silence) ...... ..... .... .. .. ...... . . . . . hmmmm. OK. Seems like you don't have any intentions to reply my questions."""
            dialog3 = "We are the Unknown Spy from IBM. Our duty is to ask you IBM BlockChain Quizzes. Are you ready to solve the questions? "
            dialog4 = "We are currently working with University of Sheffield on IBM Watson Text-To-Speech, especially cooperating with AI Group Project. "
            dialog5 = "If you are ready, click Yes to start IBM BlockChain Quizzes. I will serve my duty until I die!!! (IBM the Unknown Spy speaking with Grandiosity. )"
            exitDialog = "It is said that you are not interested in our research with IBM. Talk to you later. (Emma is keeping push you behind.)"
            
            dialogStack = [Dialog(screen, filePath, "Quiz NPC", dialog1, True, True, True, False, False),
                           Dialog(screen, filePath, "Quiz NPC", dialog2, True, True, True, False, False),
                           Dialog(screen, filePath, "Quiz NPC", dialog3, True, True, True, False, False),
                           Dialog(screen, filePath, "Quiz NPC", dialog4, True, True, True, False, False),
                           Dialog(screen, filePath, "Quiz NPC", dialog5, True, True, False, True, True)
                           
                        ]
            
            
            dialogStack[QUIZ_NPC_DIALOG_INDEX].render()
            endChatRect =  dialogStack[QUIZ_NPC_DIALOG_INDEX].drawEndChatButton()
            nextChatRect = dialogStack[QUIZ_NPC_DIALOG_INDEX].drawNextButton()
            prevChatRect = dialogStack[QUIZ_NPC_DIALOG_INDEX].drawPrevButton()
            yesChatRect = dialogStack[QUIZ_NPC_DIALOG_INDEX].drawYesButton()
            noChatRect = dialogStack[QUIZ_NPC_DIALOG_INDEX].drawNoButton()
            dialogStack[QUIZ_NPC_DIALOG_INDEX].drawNPCFigure()
            dialogStack[QUIZ_NPC_DIALOG_INDEX].drawDialogText()
        
           
        
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                            
                                if endChatRect is not None and endChatRect.collidepoint(pygame.mouse.get_pos()):
                                    quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].stop() 
                                    QUIZ_NPC_DIALOG_INDEX = 0
                                    IS_SPACEBAR_PRESSED_0 = False 
                                     
                                    
                                if nextChatRect is not None and nextChatRect.collidepoint(pygame.mouse.get_pos()):
                                    quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].stop()
                                    
                                    QUIZ_NPC_DIALOG_INDEX +=1 
                                    IS_QUIZNPC_PLAYED[QUIZ_NPC_DIALOG_INDEX] = True 
                                  
                                     
                                if prevChatRect is not None and prevChatRect.collidepoint(pygame.mouse.get_pos()):
                                    quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].stop()
                                     
                                    QUIZ_NPC_DIALOG_INDEX -=1
                                    IS_QUIZNPC_PLAYED[QUIZ_NPC_DIALOG_INDEX] = True 
                                     
                                     
                                    
                                if yesChatRect is not None and yesChatRect.collidepoint(pygame.mouse.get_pos()):
                                    #  MINI_PLAYER_X, MINI_PLAYER_Y = 0 ,630
                                    quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].stop()
                                    
                                    IS_QUIZ_STARTED = True
                                    IS_SPACEBAR_PRESSED_0 = False 
                                    QUIZ_INDEX = 0
                                    #print(IS_QUIZ_STARTED)
                                     
                                    
                                if  noChatRect is not None and noChatRect.collidepoint(pygame.mouse.get_pos()):  
                                     quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].stop()
                                    #  MINI_PLAYER_X -=10
                                     QUIZ_NPC_DIALOG_INDEX = 0  
                                     IS_SPACEBAR_PRESSED_0 = False 
        else:    
            IS_QUIZNPC_PLAYED[QUIZ_NPC_DIALOG_INDEX] = True 
            quizNPCDialogVoice[QUIZ_NPC_DIALOG_INDEX].stop()
            QUIZ_NPC_DIALOG_INDEX = 0  
            IS_SPACEBAR_PRESSED_0 = False               
                    
                
class SceneStack:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("Scene Stack designed by Kyungtae Han. For Documentation, please see code documentation.")

    def Update(self):
        print("Scene Stack designed by Kyungtae Han. For Documentation, please see code documentation.")

    def Render(self, screen):
        print("Scene Stack designed by Kyungtae Han. For Documentation, please see code documentation.")

    def push(self, next_scene):
        self.next = next_scene
    
    def pop(self):
        self.push(None)



USER_ID = 1

PLAYER_X = 512
PLAYER_Y = 700        

IS_EMMAVOICE_PLAYED = [True,True,True,True,True] 
emmaNPCDialogVoice = [pygame.mixer.Sound("assets/npc/npcVoice/emma/emmaIntroVoice.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/emma/emmaDialog2Voice.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/emma/emmaDialog3Voice.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/emma/emmaDialog4Voice.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/emma/emmaDialog5Voice.wav")]
IS_SPACEBAR_PRESSED_1 = False    
WELCOME_VOICE = pygame.mixer.Sound("assets/miniplatform/welcome.wav")
OPEN_STATS_VOICE = pygame.mixer.Sound("assets/button/voice/openStats.wav")
OPEN_LEADERBOARD_VOICE = pygame.mixer.Sound("assets/button/voice/openLeaderBoard.wav") 
CLOSE_STATS_VOICE = pygame.mixer.Sound("assets/button/voice/closeStats.wav")
CLOSE_LEADERBOARD_VOICE = pygame.mixer.Sound("assets/button/voice/closeLeaderBoard.wav")
OPEN_ACHIEVEMENT_VOICE = pygame.mixer.Sound("assets/button/voice/openAchievement.wav")
CLOSE_ACHIEVEMENT_VOICE = pygame.mixer.Sound("assets/button/voice/closeAchievement.wav")
automaticRespawn_bgm = pygame.mixer.Sound("assets/miniplatform/winterTile/sound/magicalPowerSound.wav") 



class HomeNode(SceneStack):
    def __init__(self):
        SceneStack.__init__(self)
        # self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
        # self.character = pygame.transform.scale( self.character, (40,40) )
        #path = "ibm_blockchain/assets/ship.png"
        # global PLAYER_X 
        # global PLAYER_Y
        # print(PLAYER_X, PLAYER_Y,"in HomeNode")
        # self.player = Player("Kevin", PLAYER_X, PLAYER_Y, 50, 50, path)
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/mapleSheffield.mp3") 
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1,0.0)
        
        global WELCOME_VOICE 
        WELCOME_VOICE.play()
        
        x,y = 200,400
        VELOCITY = 8
        
    def ProcessInput(self, events, keyPress):
        self.events = events
        self.keyPress = keyPress
        # print("Hello WOrld")
        global PLAYER_X 
        global PLAYER_Y 
        global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_ACHIEVEMENT_OPEN
        # self.player.processInput(PLAYER_X,PLAYER_Y,events,pressed_keys)
        global OPEN_STATS_VOICE, OPEN_LEADERBOARD_VOICE, CLOSE_STATS_VOICE, CLOSE_LEADERBOARD_VOICE, OPEN_ACHIEVEMENT_VOICE, CLOSE_ACHIEVEMENT_VOICE
        
        # self.character.processInput(events, pressed_keys)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.push(GameIntroNode())
            if event.type == pygame.KEYDOWN and event.key == K_1:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True   
                    OPEN_LEADERBOARD_VOICE.play()
                else: 
                    IS_LEADERBOARD_OPEN = False 
                    CLOSE_LEADERBOARD_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_2: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True   
                    OPEN_STATS_VOICE.play()
                else: 
                    IS_STATS_OPEN = False    
                    CLOSE_STATS_VOICE.play() 
            
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True   
                    OPEN_ACHIEVEMENT_VOICE.play()
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False 
                    CLOSE_ACHIEVEMENT_VOICE.play()   
                    #CLOSE_STATS_VOICE.play()     
                
        VELOCITY = 10
        # for event in events:
        #     if event.type == pygame.KEYDOWN :
        #         if event.key == pygame.K_LEFT:
        #            print(PLAYER_X,PLAYER_Y,"in HomeNode ProcessInput")
        #            PLAYER_X -= velocity
        #         if event.key == pygame.K_RIGHT:
        #             print(PLAYER_X,PLAYER_Y,"in HomeNode ProcessInput")
        #             PLAYER_X += velocity
        #         if event.key == pygame.K_UP:
        #             print(PLAYER_X,PLAYER_Y,"in HomeNode ProcessInput")
        #             PLAYER_Y -= velocity
        #         if event.key == pygame.K_DOWN:   
        #             print(PLAYER_X,PLAYER_Y,"in HomeNode ProcessInput")
        #             PLAYER_Y += velocity 
        
        
        
       # Changing the coordinates of the player
        if keyPress[K_LEFT]:
            PLAYER_X -= VELOCITY
        if keyPress[K_RIGHT]:
            PLAYER_X += VELOCITY
        if keyPress[K_UP]:
            PLAYER_Y -= VELOCITY
        if keyPress[K_DOWN]:
            PLAYER_Y += VELOCITY  
        
    
        # print(PLAYER_X, PLAYER_Y)
        
        
    def Update(self):
        pass
    
    def Render(self, screen):
        
        # global PLAYER_X 
        # global PLAYER_Y
        # leftTreesRect = pygame.Rect(5,100,395,395)
        # pygame.draw.rect(screen, RED, leftTreesRect, 4)
        
        # rightTreesRect = pygame.Rect(620,102,400,400)
        # pygame.draw.rect(screen, RED, rightTreesRect, 4)
        
        # leftRiverRect = pygame.Rect(0,600,450,200)
        # pygame.draw.rect(screen,RED,leftRiverRect,4)
        
        # rightRiverRect = pygame.Rect(600,600,450,200)
        # pygame.draw.rect(screen,RED,rightRiverRect,4)
        
        # leftStatueRect = pygame.Rect(340,508,110,90)
        # pygame.draw.rect(screen,RED,leftStatueRect,4)
        
        # rightStatueRect = pygame.Rect(600,508,110,90)
        # pygame.draw.rect(screen,RED,rightStatueRect,4)
    
    
        # if playerRect.colliderect(leftTreesRect) or playerRect.colliderect(rightTreesRect):
        #     PLAYER_X =  512 
        #     PLAYER_Y = 500
            
        # if playerRect.colliderect(leftRiverRect) or playerRect.colliderect(rightRiverRect):  
        #     PLAYER_X =  512 
        #     PLAYER_Y = 700  
            
        # if playerRect.colliderect(leftStatueRect) or  playerRect.colliderect(rightStatueRect) : 
        #     PLAYER_X = 512
        #     PLAYER_Y = 508  
       
        resetSurface(screen)
        # path = "ibm_blockchain/assets/character/down/down1.png"
        # player = Player("Kevin", PLAYER_X, PLAYER_Y, 50, 50, path)
        # player.drawCharacter(screen)
        
        # global PLAYER_X 
        # global PLAYER_Y
        # leftTreesRect = pygame.Rect(5,100,395,395)
        # pygame.draw.rect(screen, RED, leftTreesRect, 4)
        
        # rightTreesRect = pygame.Rect(620,102,400,400)
        # pygame.draw.rect(screen, RED, rightTreesRect, 4)
        
        # leftRiverRect = pygame.Rect(0,600,450,200)
        # pygame.draw.rect(screen,RED,leftRiverRect,4)
        
        # rightRiverRect = pygame.Rect(600,600,450,200)
        # pygame.draw.rect(screen,RED,rightRiverRect,4)
        
        # leftStatueRect = pygame.Rect(340,508,110,90)
        # pygame.draw.rect(screen,RED,leftStatueRect,4)
        
        # rightStatueRect = pygame.Rect(600,508,110,90)
        # pygame.draw.rect(screen,RED,rightStatueRect,4)
    
    
        # if playerRect.colliderect(leftTreesRect) or playerRect.colliderect(rightTreesRect):
        #     PLAYER_X =  512 
        #     PLAYER_Y = 500
            
        # if playerRect.colliderect(leftRiverRect) or playerRect.colliderect(rightRiverRect):  
        #     PLAYER_X =  512 
        #     PLAYER_Y = 700  
            
        # if playerRect.colliderect(leftStatueRect) or  playerRect.colliderect(rightStatueRect) : 
        #     PLAYER_X = 512
        #     PLAYER_Y = 508  
        
         
        # Field 
        field = pygame.image.load("assets/background/field.png")
        field = pygame.transform.scale( field, (WIDTH,HEIGHT) )
        screen.blit(field,(0,0))
        
        # Statue
        statue = pygame.image.load("assets/background/statue.png")
        statue = pygame.transform.scale( statue, (100,100) ) 
        screen.blit(statue,(350,500))
        screen.blit(statue,(600,500))
        
        # River
        river = pygame.image.load("assets/background/river.png")
        river = pygame.transform.scale(river,(100,100))
        
        i = 600
        STEP = 100
        while(i<=1100) : 
            screen.blit(river,(i,600))
            rect = river.get_rect()
            rect.center = i+50,600+50
            #pygame.draw.rect(screen, GREEN, rect,4)
            screen.blit(river,(i,700))
            i+=STEP
        
        j = 350
        while(j>=-50) :
            screen.blit(river,(j,600))
            screen.blit(river,(j,700))
            j-=STEP
          
        # Tree    
        tree = pygame.image.load("assets/background/tree.png")
        tree = pygame.transform.scale( tree, (100,100) )  
     
        STEP = 100
        i = 100 
        while (i<500):
            screen.blit(tree,(0,i))
            rect = tree.get_rect()
            rect.center = 0+50,i+50
            screen.blit(tree,(100,i))
            screen.blit(tree,(200,i))
            screen.blit(tree,(300,i))
            
            screen.blit(tree,(630,i))
            screen.blit(tree,(730,i))
            screen.blit(tree,(830,i))
            screen.blit(tree,(930,i))
            
            rect = tree.get_rect()
            rect.center = i+50,600+50 
            #pygame.draw.rect(screen, RED, rect,4)
            i+=STEP
        
        global LIGHT_GREEN, ANSWER_FONT 
        pygame.draw.rect(screen, (51,51,51), pygame.Rect(432, 247, 180, 43), border_radius = 10 )
        
        LIGHT_GREEN = (234,230,70)
        FONT_DIRECTORY = "assets/font/PressStart2P.ttf"
        ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 10)
        answer1_content = "Dr.Emma Norling"
        answer1 =  ANSWER_FONT.render(answer1_content, True, LIGHT_GREEN)
        screen.blit(answer1,(452, 262))
            
        #NPC    
        # npcDesk = pygame.image.load("ibm_blockchain/assets/npcDesk.png")
        # npcDesk = pygame.transform.scale(npcDesk,(235,100))
        # screen.blit(npcDesk,(400,200))
        FONT_DIRECTORY = "assets/font/Satisfy-Regular.ttf"
        GAME_FONT = pygame.font.Font(FONT_DIRECTORY, 20)
        authorSignature = GAME_FONT.render('Kyungtae Han', True, WHITE)
        screen.blit(authorSignature, (900, 0))
        
        
        path = "assets/npc/jay.png"
        easyNPC = Npc (screen,"Emma", 460, 160, 100, 100, path)
        easyNPC.render()
        
        # Character
        global PLAYER_X, PLAYER_Y
        # screen.blit(self.character,(200,400))
        path = "assets/character/down/down1.png"
        player = Player("Kevin", PLAYER_X, PLAYER_Y, 50, 50, path)
        player.drawCharacter(screen)
        
        easyNPCRect = easyNPC.getNpcRect()
        playerRect = player.getPlayerRect()
        
        boundaryColor = (147,184,30)
        
        leftTreesRect = pygame.Rect(5,100,395,400)
        pygame.draw.rect(screen, boundaryColor , leftTreesRect, 1)
        
        rightTreesRect = pygame.Rect(620,99,410,400)
        pygame.draw.rect(screen, boundaryColor , rightTreesRect, 1)
        
        leftRiverRect = pygame.Rect(0,600,450,200)
        pygame.draw.rect(screen,boundaryColor ,leftRiverRect,1)
        
        rightRiverRect = pygame.Rect(600,600,450,200)
        pygame.draw.rect(screen,boundaryColor ,rightRiverRect,1)
        
        leftStatueRect = pygame.Rect(340,508,110,90)
        pygame.draw.rect(screen,boundaryColor ,leftStatueRect,1)
        
        rightStatueRect = pygame.Rect(600,508,110,90)
        pygame.draw.rect(screen,boundaryColor ,rightStatueRect,1)
    
        global automaticRespawn_bgm  
    
        if playerRect.colliderect(leftTreesRect) or playerRect.colliderect(rightTreesRect):
            automaticRespawn_bgm.play()
            PLAYER_X =  512 
            PLAYER_Y = 500
            
            
        if playerRect.colliderect(leftRiverRect) or playerRect.colliderect(rightRiverRect):  
            automaticRespawn_bgm.play()
            PLAYER_X =  512 
            PLAYER_Y = 700  
            
        if playerRect.colliderect(leftStatueRect) or  playerRect.colliderect(rightStatueRect) : 
            automaticRespawn_bgm.play()
            PLAYER_X = 512
            PLAYER_Y = 508   
        
        
        pygame.mixer.init() 
        portal_sound = pygame.mixer.Sound("assets/background/music/effect/maplestory_portal.mp3") 
        
        hover_sound = pygame.mixer.Sound("assets/background/music/effect/CLICK_009.wav")
        # emmaNPCIntroVoice = pygame.mixer.Sound("ibm_blockchain/assets/npc/npcVoice/emma/emmaIntroVoice.wav")
        
        
        
        count = 0 
        
        global TOWN_NPC_DIALOG_INDEX
        global IS_SPACEBAR_PRESSED_1, IS_EMMAVOICE_PLAYED
        
        # if easyNPCRect.colliderect(playerRect) and self.keyPress[K_SPACE]:
        #     IS_SPACEBAR_PRESSED = True
        # if easyNPCRect.colliderect(playerRect):
        #     IS_EMMAVOICE_PLAYED = True 
            
        # else:
        #     IS_EMMAVOICE_PLAYED = False 
        global emmaNPCDialogVoice   
        if easyNPCRect.colliderect(playerRect) and self.keyPress[K_SPACE]:
            IS_SPACEBAR_PRESSED_1 = True    
        
        # print("BEFORE COMING IN ", TOWN_NPC_DIALOG_INDEX)
        if easyNPCRect.colliderect(playerRect) and IS_SPACEBAR_PRESSED_1 is True and TOWN_NPC_DIALOG_INDEX>=0:
            if IS_EMMAVOICE_PLAYED[TOWN_NPC_DIALOG_INDEX] : 
                IS_EMMAVOICE_PLAYED[TOWN_NPC_DIALOG_INDEX] = False 
                emmaNPCDialogVoice[TOWN_NPC_DIALOG_INDEX].play()
                
            # portal_sound.play()
            # PLAYER_X -= 1 
            # PLAYER_Y -= 1
            filePath = "assets/npc/jay.png"
            
            dialog1 = "Hey there, are you busy right now? I am Dr. Emma Norling from University of Sheffield. I have something to talk with you."
            dialog2 = """Again, I'm Emma Norling, Senior University teacher. I obtained BEng (Hons) from the University of Melbourne, worked as a tutor and lecturer in the Department of Computer Science at this institution, moving on to complete my PhD in Computer Science here. I undertook postdoctoral studies in the Centre for Policy Modelling (Manchester Metropolitan University), before moving into a lecturing position in the School of Mathematics, Computing and Digital Technology there."""
            dialog3 = "Please look at my Google Scholar Page to get to know me. Here is the link: https://scholar.google.com/citations?user=J3qy6zUAAAAJ&hl=en . My email is : e.j.norling@sheffield.ac.uk . My office is Department of Computer Science, Regent Court (DCS), 211 Portobello, Sheffield, S1 4DP, Sheffield, United Kingdom.   "
            dialog4 = "We are currently working with IBM on AI, especially cooperating with AI Group Project. The University of Sheffield is planning to reach top 1-tier list as Stanford, MIT, and Harvard. "
            dialog5 = "Do you wanna go our initial model IBM BlockChain Minigame? This reflects my research interests centred around agent-based systems, particularly agent-based modelling of human behaviour, from cognitive modelling to social simulation! Oh!, it might be incorporated into computational models, both in the context of improving models of human behaviour, and also in designing better computational and robotic interfaces. (Automatically send you to IBM BlockChain Arcade Zone!)"
            exitDialog = "It is said that you are not interested in our research with IBM. Talk to you later. (Emma is keeping push you behind.)"
            
            dialogStack = [Dialog(screen, filePath, "Dr.Emma Norling", dialog1, True, False, True, False, False),
                           Dialog(screen, filePath, "Dr.Emma Norling", dialog2, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr.Emma Norling", dialog3, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr.Emma Norling", dialog4, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr.Emma Norling", dialog5, True, True, False, True, True)
                           
                        ]
            
            
            dialogStack[TOWN_NPC_DIALOG_INDEX].render()
            endChatRect =  dialogStack[TOWN_NPC_DIALOG_INDEX].drawEndChatButton()
            nextChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawNextButton()
            prevChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawPrevButton()
            yesChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawYesButton()
            noChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawNoButton()
            dialogStack[TOWN_NPC_DIALOG_INDEX].drawNPCFigure()
            dialogStack[TOWN_NPC_DIALOG_INDEX].drawDialogText()

            for event in self.events:
                    if event.type == pygame.MOUSEBUTTONDOWN :
                            if endChatRect is not None and endChatRect.collidepoint(pygame.mouse.get_pos()):
                                emmaNPCDialogVoice[TOWN_NPC_DIALOG_INDEX].stop()
                                TOWN_NPC_DIALOG_INDEX= 0
                                IS_SPACEBAR_PRESSED_1 = False  
                                 
                                #print(TOWN_NPC_DIALOG_INDEX)
                                hover_sound.play()
                               
                            if nextChatRect is not None and nextChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("nextChatRect")
                                hover_sound.play()
                                emmaNPCDialogVoice[TOWN_NPC_DIALOG_INDEX].stop()
                                IS_EMMAVOICE_PLAYED[TOWN_NPC_DIALOG_INDEX+1] = True 
                                TOWN_NPC_DIALOG_INDEX +=1 
                                #print(TOWN_NPC_DIALOG_INDEX)
                            if prevChatRect is not None and prevChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("prevChatRect")
                                emmaNPCDialogVoice[TOWN_NPC_DIALOG_INDEX].stop()
                                IS_EMMAVOICE_PLAYED[TOWN_NPC_DIALOG_INDEX-1] = True 
                                hover_sound.play()
                                TOWN_NPC_DIALOG_INDEX -=1
                                #print(TOWN_NPC_DIALOG_INDEX)
                                
                            if yesChatRect is not None and yesChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("yesChatRect")
                                emmaNPCDialogVoice[TOWN_NPC_DIALOG_INDEX].stop()
                                hover_sound.play()
                                #print(TOWN_NPC_DIALOG_INDEX)
                                portal_sound.play()
                                IS_SPACEBAR_PRESSED_1 = False 
                                self.push(GameIntroNode())
                            if  noChatRect is not None and noChatRect.collidepoint(pygame.mouse.get_pos()):  
                                #print("nochatrect")
                               
                                emmaNPCDialogVoice[TOWN_NPC_DIALOG_INDEX].stop()
                                hover_sound.play()
                                #print(TOWN_NPC_DIALOG_INDEX)
                                
                                TOWN_NPC_DIALOG_INDEX= 0
                                IS_SPACEBAR_PRESSED_1 = False  
                        
                    
            
            
            # self.pop()
            # self.push(GameIntroNode())
        else:    
            count+=1
            
            TOWN_NPC_DIALOG_INDEX = 0
            IS_SPACEBAR_PRESSED_1 = False
            IS_EMMAVOICE_PLAYED[TOWN_NPC_DIALOG_INDEX] = True 
            emmaNPCDialogVoice[TOWN_NPC_DIALOG_INDEX].stop()
            # IS_SPACEBAR_PRESSED = False           
            
        global USER_ID     
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(USER_ID)
        else: 
            pass
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(USER_ID)
        else: 
            pass
        
        # boundaryColor = (147,184,30)
        
        # leftTreesRect = pygame.Rect(5,100,395,395)
        # pygame.draw.rect(screen, boundaryColor , leftTreesRect, 1)
        
        # rightTreesRect = pygame.Rect(620,102,400,400)
        # pygame.draw.rect(screen, boundaryColor , rightTreesRect, 1)
        
        # leftRiverRect = pygame.Rect(0,600,450,200)
        # pygame.draw.rect(screen,boundaryColor ,leftRiverRect,1)
        
        # rightRiverRect = pygame.Rect(600,600,450,200)
        # pygame.draw.rect(screen,boundaryColor ,rightRiverRect,1)
        
        # leftStatueRect = pygame.Rect(340,508,110,90)
        # pygame.draw.rect(screen,boundaryColor ,leftStatueRect,1)
        
        # rightStatueRect = pygame.Rect(600,508,110,90)
        # pygame.draw.rect(screen,boundaryColor ,rightStatueRect,1)
    
    
        # if playerRect.colliderect(leftTreesRect) or playerRect.colliderect(rightTreesRect):
        #     PLAYER_X =  512 
        #     PLAYER_Y = 500
            
        # if playerRect.colliderect(leftRiverRect) or playerRect.colliderect(rightRiverRect):  
        #     PLAYER_X =  512 
        #     PLAYER_Y = 700  
            
        # if playerRect.colliderect(leftStatueRect) or  playerRect.colliderect(rightStatueRect) : 
        #     PLAYER_X = 512
        #     PLAYER_Y = 508   
    
        # global LIGHT_GREEN, ANSWER_FONT 
        # pygame.draw.rect(screen, (51,51,51), pygame.Rect(432, 247, 180, 43), border_radius = 10 )
        
        # LIGHT_GREEN = (234,230,70)
        # FONT_DIRECTORY = "ibm_blockchain/assets/font/PressStart2P.ttf"
        # ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 10)
        # answer1_content = "Dr.Emma Norling"
        # answer1 =  ANSWER_FONT.render(answer1_content, True, LIGHT_GREEN)
        # screen.blit(answer1,(452, 262))
        
        #print(pygame.mouse.get_pos())
        
        # self.player.drawCharacter(screen)   
        
EASY_WELCOME_VOICE = pygame.mixer.Sound("assets/npc/npcVoice/matthew/easyWelcome.wav")
MEDIUM_WELCOME_VOICE = pygame.mixer.Sound("assets/npc/npcVoice/roger/mediumWelcome.wav")
HARD_WELCOME_VOICE =  pygame.mixer.Sound("assets/npc/npcVoice/theKing/hardWelcome.wav")
class GameIntroNode(SceneStack):
    def __init__(self):
        global WIDTH, HEIGHT
        SceneStack.__init__(self)
        #self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
        #self.character = pygame.transform.scale( self.character, (40,40) )
        
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/gameOverWin.mp3") 
        pygame.mixer.music.play(-1,0.0)
        
        self.button1_x, self.button1_y = WIDTH/2-100, HEIGHT/2-100
        self.button2_x, self.button2_y = WIDTH/2-100, HEIGHT/2-50
        self.button3_x, self.button3_y = WIDTH/2-100, HEIGHT/2
        self.button1 = Button (
                 "EASY (x 1)",
                  (WIDTH/2-100, HEIGHT/2-100),
                  font = 50,
                  bg="navy",
                  feedback="OK"
       ) 
        self.button2 = Button (
            "MEDIUM (x 2)",
            ( self.button2_x, self.button2_y),
            font = 50,
            bg="navy",
            feedback="OK"
        ) 

        self.button3 = Button (
            "HARD (x 3)",
            (self.button3_x, self.button3_y),
            font = 50,
            bg="navy",
            feedback="OK"
        ) 
        
    def ProcessInput(self, events, pressed_keys):
        self.events = events 
        global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_ACHIEVEMENT_OPEN
        global OPEN_STATS_VOICE, OPEN_LEADERBOARD_VOICE, CLOSE_STATS_VOICE, CLOSE_LEADERBOARD_VOICE, OPEN_ACHIEVEMENT_VOICE, CLOSE_ACHIEVEMENT_VOICE
        global EASY_WELCOME_VOICE, MEDIUM_WELCOME_VOICE, HARD_WELCOME_VOICE
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.push(EasyModeNode())
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (415 <= mouse_x <= 601) and (346 <= mouse_y <= 419) :
                    #print("Easy clicked")   
                    EASY_WELCOME_VOICE.play()
                    self.push(EasyModeNode()) 
                if (418 <= mouse_x <= 598) and (450 <= mouse_y <= 514) : 
                    #print ("Medium clicked")
                    MEDIUM_WELCOME_VOICE.play()
                    self.push(MediumModeNode())
                if (418 <= mouse_x <= 595) and (548 <= mouse_y <= 617) :
                    #print("hard Clicked") 
                    HARD_WELCOME_VOICE.play()
                    self.push(HardModeNode())
                
                # Home Exit 
                if (20<=mouse_x<=60) and (20 <= mouse_y <= 60) : 
                    self.push(HomeNode())    
            
            if event.type == pygame.KEYDOWN and event.key == K_1:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True   
                    OPEN_LEADERBOARD_VOICE.play()
                else: 
                    IS_LEADERBOARD_OPEN = False 
                    CLOSE_LEADERBOARD_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_2: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True  
                    OPEN_STATS_VOICE.play() 
                else: 
                    IS_STATS_OPEN = False 
                    CLOSE_STATS_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True  
                    OPEN_ACHIEVEMENT_VOICE.play()
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False 
                    CLOSE_ACHIEVEMENT_VOICE.play()   
                    #CLOSE_STATS_VOICE.play()     
                
                # # Return Home 
                # if (60<=mouse_x<=100) and (60 <= mouse_y <= 100):
                #     self.push(GameIntroNode())    
                #     print(" Home clicked")
                
                    
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.mixer.init() 
        #hover_sound = pygame.mixer.Sound("ibm_blockchain/assets/MaplestoryMouseHover.wav") 
        if (415 <= mouse_x <= 601) and (346 <= mouse_y <= 419) :
            print("Easy Hovered")    
            #hover_sound.play(0)
        if (418 <= mouse_x <= 598) and (450 <= mouse_y <= 514) : 
            print ("Medium Hovered")
            #hover_sound.play(0)
        if (418 <= mouse_x <= 595) and (548 <= mouse_y <= 617) :
            print("hard Hovered")    
            #hover_sound.play(0)
            
    
    def Update(self):
        k = 0
        global SCORE 
        if k == 10: 
            SCORE +=10
        
    def Render(self, screen):
        global DARK_BROWN
        screen.fill(DARK_BROWN)
        
        
        gameBackground = pygame.image.load("assets/background/minigameBackground.png")
        gameBackground = pygame.transform.scale(gameBackground,(1024,800))
        screen.blit(gameBackground,(0,0))
        
        
        

        # # Field 
        # field = pygame.image.load("ibm_blockchain/assets/field.png")
        # field = pygame.transform.scale( field, (1024,800) )
        # screen.blit(field,(0,0))
        # ScoreBoard 
        
        
        # global SCORE
        # text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
        # textRect = text.get_rect()
        # textRect.center = (150,20)
        
        #SCORE += SCORE_INCREMENT
        # screen.blit(text, textRect)
        
        GAME_FONT2 = pygame.font.Font(FONT_DIRECTORY, 42)
        text = GAME_FONT2.render('IBM BLOCKCHAIN MINIGAME', True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 4)

        GAME_FONT3 = pygame.font.Font(FONT_DIRECTORY, 24)
        text2 = GAME_FONT3.render('PLEASE SELECT THE MODE TO CONTINUE...', True, GREEN, BLUE)
        textRect2 = text2.get_rect()
        textRect2.center = (WIDTH // 2 - 20  , HEIGHT // 4 + 100)

        # text3 = GAME_FONT3.render('Press [Y] to continue', True, WHITE, BLACK)
        # textRect3 = text3.get_rect()
        # textRect3.center = (WIDTH // 2 -20  , HEIGHT // 4 + 200)
        
        screen.blit(text, textRect)   
        screen.blit(text2, textRect2)   
        # screen.blit(text3, textRect3) 
        
        # ball1 = Ball(512, 400, 20, screen)
        # ball1.render()
        
        
        midWidth, midHeight = WIDTH/2, HEIGHT/2 
        global BLACK,WHITE
        
        sign_directory = "assets/font/Satisfy-Regular.ttf"
        sign_font = pygame.font.Font(sign_directory, 20)
        authorSignature = sign_font.render('Kyungtae Han', True, BLACK)
        screen.blit(authorSignature, (900, 0))
        
        #Easy
        button1 = pygame.image.load("assets/button/gameModeButton.png")
        button1 = pygame.transform.scale(button1,(200,200))
        button1_rect = button1.get_rect(center=(midWidth, midHeight))
        screen.blit(button1,button1_rect)
        # pygame.draw.rect(screen, BLUE, button1_rect,4) 
        #EasyText
        button1_text = GAME_FONT3.render('EASY', True, BLACK, WHITE)
        button1_textRect = button1_text.get_rect(center=(midWidth, midHeight-25))
        screen.blit(button1_text, button1_textRect)
        
        #Medium
        button2= pygame.image.load("assets/button/gameModeButton.png")
        button2 = pygame.transform.scale(button2,(200,200))
        button2_rect = button2.get_rect(center=(midWidth, midHeight+100))
        screen.blit(button2,button2_rect)
        # pygame.draw.rect(screen, RED, button2_rect,4) 
        #Medium Text
        button2_text = GAME_FONT3.render('MEDIUM', True, BLACK, WHITE)
        button2_textRect = button2_text.get_rect(center=(midWidth, midHeight+100-25))
        screen.blit(button2_text, button2_textRect)
        
        #Hard
        button3 = pygame.image.load("assets/button/gameModeButton.png")
        button3 = pygame.transform.scale(button3,(200,200))
        button3_rect = button3.get_rect(center=(midWidth, midHeight+100*2))
        screen.blit(button3,button3_rect)
        #Hard Text
        button3_text = GAME_FONT3.render('HARD', True, BLACK, WHITE)
        button3_textRect = button1_text.get_rect(center=(midWidth, midHeight+100*2-25))
        screen.blit(button3_text, button3_textRect)



        # #Exit
        # exitButton = pygame.image.load("ibm_blockchain/assets/exitPygameIcon.png")
        # exitButton = pygame.transform.scale(exitButton,(40,40))
        # exitButtonRect = exitButton.get_rect(topleft=(20, 20))
        # pygame.draw.rect(screen, RED, exitButtonRect,4) 
        # screen.blit(exitButton, exitButtonRect)
        
        #Refresh 
        refreshButtonPath = "assets/button/homeIcon.png"
        refreshButton = pygame.image.load(refreshButtonPath)
        refreshButton = pygame.transform.scale(refreshButton,(40,40))
        refreshButtonRect = refreshButton.get_rect(topleft=(20, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(refreshButton, refreshButtonRect)
        
        # University Logo 
        uniLogoPath = "assets/uniLogo.png"
        uniLogo = pygame.image.load(uniLogoPath)
        uniLogo = pygame.transform.scale(uniLogo,(300,80))
        uniLogoRect= uniLogo.get_rect(topleft=(200, 650))
        # pygame.draw.rect(screen, RED, uniLogoRect,4) 
        screen.blit(uniLogo, uniLogoRect)
        
        # University Logo 
        ibmLogoPath = "assets/ibmlogo.jpeg"
        ibmLogo = pygame.image.load(ibmLogoPath)
        ibmLogo = pygame.transform.scale(ibmLogo,(300,80))
        ibmLogoRect= ibmLogo.get_rect(topleft=(550, 650))
        # pygame.draw.rect(screen, RED, ibmLogoRect,4) 
        screen.blit(ibmLogo, ibmLogoRect)
        
        global USER_ID 
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(USER_ID)
        else: 
            pass
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(USER_ID)
        else: 
            pass
        
        # print(pygame.mouse.get_pos())
        
        # Button
        # screen.blit(self.button1.surface, (midWidth, midHeight))
        # screen.blit(self.button2.surface, (midWidth, midHeight+40))
        # screen.blit(self.button3.surface, (midWidth, midHeight+40*2))
        
BALL_START_X= 512
BALL_START_Y= 400
VEL_DX = 15 
VEL_DY = 1      

EASY_PLAYER_X = 512
EASY_PLAYER_Y = 400 
VELOCITY = 8

SHRIGEN_X = 1024 
SHRIGEN_Y = 420
IS_HIGHSCORE_UPDATED = False 


IS_MATTHEWVOICE_PLAYED_STACK = [True,True,True,True,True] 
matthewNPCDialogVoice = [pygame.mixer.Sound("assets/npc/npcVoice/matthew/matthewDialog1.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/matthew/matthewDialog2.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/matthew/matthewDialog3.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/matthew/matthewDialog4.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/matthew/matthewDialog5.wav")]

IS_SPACEBAR_PRESSED_2 = False     

IS_QUIZVOICE_PLAYED = [True]*10 
IS_QUIZVOICE_PLAYED_2 = [True]*10 
IS_QUIZVOICE_PLAYED_3 = [True]*10 


quizVoice = [pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz1.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz2.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz3.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz4.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz5.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz6.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz7.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz8.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz9.wav"),
             pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/quiz10.wav"),
             ]

ANSWER_CORRECT_VOICE = pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/answerCorrect.wav")
ANSWER_WRONG_VOICE = pygame.mixer.Sound("assets/npc/npcVoice/quizNPC/quiz/answerWrong.wav")

RETURN_HOME_VOICE = pygame.mixer.Sound("assets/button/voice/goingBackHome.wav")
MINIGAME_HOME_VOICE = pygame.mixer.Sound("assets/button/voice/returnMinigameHome.wav")
class EasyModeNode(SceneStack):
    def __init__(self):
        SceneStack.__init__(self)
        #self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
        #self.character = pygame.transform.scale( self.character, (40,40) )
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/Leafre.mp3") 
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)
        x,y = 200,400
        self.gravity = 1 
        
       
       
        
    def ProcessInput(self, events, keyPress):
       self.keyPress = keyPress
       self.events = events 
       global MINI_PLAYER_Y
       global MINI_PLAYER_X
       global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_HIGHSCORE_UPDATED, IS_ACHIEVEMENT_OPEN
       global OPEN_STATS_VOICE, OPEN_LEADERBOARD_VOICE, CLOSE_STATS_VOICE, CLOSE_LEADERBOARD_VOICE
       for event in events: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                # Move to the next scene when the user pressed Enter
                print("yes")
                self.push(GameOverNode())
            
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                MINI_PLAYER_Y -= 5 
            
            if event.type == pygame.KEYDOWN and event.key == K_1:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True   
                    OPEN_LEADERBOARD_VOICE.play()
                else: 
                    IS_LEADERBOARD_OPEN = False 
                    CLOSE_LEADERBOARD_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_2: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True   
                    OPEN_STATS_VOICE.play()
                else: 
                    IS_STATS_OPEN = False 
                    CLOSE_STATS_VOICE.play()
                    
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True 
                    OPEN_ACHIEVEMENT_VOICE.play()  
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False    
                    CLOSE_ACHIEVEMENT_VOICE.play()
                    #CLOSE_STATS_VOICE.play()     
             
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x, mouse_y = pygame.mouse.get_pos()
                global RETURN_HOME_VOICE, MINIGAME_HOME_VOICE
                # Home Exit 
                if (964<=mouse_x<=1004) and (20 <= mouse_y <= 60) : 
                    #RETURN_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    IS_HIGHSCORE_UPDATED = False 
                    self.push(HomeNode())  
                
                if (924<=mouse_x<=964) and (20 <= mouse_y <= 60) : 
                    MINIGAME_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    IS_HIGHSCORE_UPDATED = False
                    self.push(GameIntroNode())   
                    
       if keyPress[K_SPACE] and keyPress[K_RIGHT] :
            MINI_PLAYER_Y -= math.sqrt(3*(MINI_PLAYER_X+15)+MINI_PLAYER_Y) 
            MINI_PLAYER_X += 15 
            
       if keyPress[K_SPACE] and keyPress[K_LEFT] :
            MINI_PLAYER_Y -= math.sqrt(3*(MINI_PLAYER_X+15)+MINI_PLAYER_Y) 
            MINI_PLAYER_X -= 15     
    #    if keyPress[K_l] and not IS_LEADERBOARD_OPEN:
    #        IS_LEADERBOARD_OPEN = True      
    #    if keyPress[K_l] and IS_LEADERBOARD_OPEN: 
    #        IS_LEADERBOARD_OPEN = False 
            
              
        
       
        
    #    global EASY_PLAYER_X 
    #    global EASY_PLAYER_Y
        
        
    #    if keyPress[K_LEFT]:
    #         EASY_PLAYER_X -= VELOCITY
    #    if keyPress[K_RIGHT]:
    #         EASY_PLAYER_X += VELOCITY
    #    if keyPress[K_UP]:
    #         EASY_PLAYER_Y -= VELOCITY
    #    if keyPress[K_DOWN]:
    #         EASY_PLAYER_Y += VELOCITY   
                    
                    
    def Update(self):
        #pass
        # Ball Coordinate Update
        global BALL_START_X
        global BALL_START_Y
        global VEL_DX
        global VEL_DY
        BALL_START_X  = (BALL_START_X+VEL_DX)%1024
        BALL_START_Y  = (BALL_START_Y+VEL_DY)%800
   
    
    def Render(self, screen):
         # Field 
        # field = pygame.image.load("ibm_blockchain/assets/field.png")
        # field = pygame.transform.scale( field, (1024,800) )
        # screen.blit(field,(0,0))
        # mixer.init()
        # mixer.music.load('ibm_blockchain/assets/FloralLife.mp3')
        # mixer.music.play()
        
        resetSurface(screen)
        
         # global WIDTH, HEIGHT
        gameBackground = pygame.image.load("assets/background/minigameBackground.png")
        gameBackground = pygame.transform.scale(gameBackground,(1024,800))
        screen.blit(gameBackground,(0,0))
        
        npcTree = pygame.image.load("assets/npc/npcTree.png")
        npcTree = pygame.transform.scale(npcTree,(350,350))
        screen.blit(npcTree,(700,270))
        
       
        
        # mini Platform 1 
        # bottomPlatform = pygame.image.load("ibm_blockchain/assets/bottomPlatform.png")
        # bottomPlatform = pygame.transform.scale(bottomPlatform,(1024,120))
        # screen.blit(bottomPlatform,(0,680))
        
        # bottomRect = bottomPlatform.get_rect()
        # bottomRect.center = 0,700  
        # pygame.draw.rect(screen, GREEN, bottomRect,4)
        
        
        # #Exit
        # exitButton = pygame.image.load("ibm_blockchain/assets/exitPygameIcon.png")
        # exitButton = pygame.transform.scale(exitButton,(40,40))
        # exitButtonRect = exitButton.get_rect(topright=(1024-20, 20))
        # pygame.draw.rect(screen, RED, exitButtonRect,4) 
        # screen.blit(exitButton, exitButtonRect)
        
        
        
        #Refresh 
        refreshButtonPath = "assets/button/homeIcon.png"
        refreshButton = pygame.image.load(refreshButtonPath)
        refreshButton = pygame.transform.scale(refreshButton,(40,40))
        refreshButtonRect = refreshButton.get_rect(topright=(1024-20, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(refreshButton, refreshButtonRect)
        
        #Refresh 
        returnButtonPath = "assets/button/goBackHomeScreen.png"
        returnButton = pygame.image.load(returnButtonPath)
        returnButton = pygame.transform.scale(returnButton,(40,40))
        returnButtonRect = returnButton.get_rect(topright=(1024-20-40, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(returnButton, returnButtonRect)
        
        # # LeaderBoard 
        # leaderBoardButtonPath = "ibm_blockchain/assets/Leaderboard.png"
        # leaderBoardButton = pygame.image.load(leaderBoardButtonPath)
        # leaderBoardButton = pygame.transform.scale(leaderBoardButton,(40,40))
        # leaderBoardButtonRect = leaderBoardButton.get_rect(topright=(1024-20-40-40, 20))
        # # pygame.draw.rect(screen, RED, leaderBoardButtonRect,4) 
        # screen.blit(leaderBoardButton, leaderBoardButtonRect) 
        
        
        
        
        global SCORE
        # text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
        # textRect = text.get_rect()
        # textRect.center = (100,20)
        scoreBoard = ScoreBoard(screen, SCORE, 10, 10)
        scoreBoard.render()
        #SCORE += SCORE_INCREMENT
        #screen.blit(text, textRect)
        
        global BALL_START_X
        global BALL_START_Y
        global VEL_DX
        global VEL_DY
        
        ball1 = Ball(BALL_START_X, BALL_START_Y, 20, screen, 1,1)
        ball1.render()
        ball1.update()
        
        bottomPlatform = pygame.sprite.Group()
        miniTile1Path = "assets/miniplatform/tile1.png"
        miniTile2Path = "assets/miniplatform/tile2.png"
        # miniPlatform = MiniPlatform(platformPath,0,680) 
        
        # Bottom Platform
        for eachTileX in range(0,1048,50):
            bottomPlatform.add(MiniPlatform(miniTile1Path,eachTileX,680))
            bottomPlatform.add (MiniPlatform(miniTile2Path,eachTileX,730))
            bottomPlatform.add (MiniPlatform(miniTile2Path,eachTileX,780))
            
            # bottomPlatform.add (MiniPlatform(platformPath,eachTileX,730) )
            # bottomPlatform.add (MiniPlatform(platformPath,eachTileX,780) )
        
        # MiniPlatform
        for eachTileX in range(250,350,50):
            bottomPlatform.add(MiniPlatform(miniTile1Path,eachTileX,620))
            # bottomPlatform.add(MiniPlatform(miniTile1Path,300,620))
            # bottomPlatform.add(MiniPlatform(miniTile1Path,350,620))
        
        ## NPC Upper platform
        for eachTileX in range(650,1024,50):
            bottomPlatform.add(MiniPlatform(miniTile1Path,eachTileX,580))
            bottomPlatform.add(MiniPlatform(miniTile2Path,eachTileX,630))
            
        
        bottomPlatform.add(MiniPlatform(miniTile1Path,300,570))
        bottomPlatform.add(MiniPlatform(miniTile1Path,350,520))
        
        # Left Zig-Zag up 
        bottomPlatform.add(MiniPlatform(miniTile1Path,350,420))
        #bottomPlatform.add(MiniPlatform(miniTile1Path,400,370))
        bottomPlatform.add(MiniPlatform(miniTile1Path,300,370))
        bottomPlatform.add(MiniPlatform(miniTile1Path,250,320))
        bottomPlatform.add(MiniPlatform(miniTile1Path,200,270))
        bottomPlatform.add(MiniPlatform(miniTile1Path,150,220))
        
        for eachTileX in range (0,150,50):
            bottomPlatform.add(MiniPlatform(miniTile1Path,eachTileX,220))
            
        
        for eachTileX in range(400,600,50):
            bottomPlatform.add(MiniPlatform(miniTile1Path,eachTileX,470))
            
            
        # bottomPlatform.add(MiniPlatform(miniTile1Path,600,420))
        # bottomPlatform.add(MiniPlatform(miniTile1Path,650,370))
        # bottomPlatform.add(MiniPlatform(miniTile1Path,700,320))
        # bottomPlatform.add(MiniPlatform(miniTile1Path,750,270))
        # bottomPlatform.add(MiniPlatform(miniTile1Path,800,220))
        # for eachTileX in range (850,1000,50):
        #     bottomPlatform.add(MiniPlatform(miniTile1Path,eachTileX,220))
        
        unknownNPCPath = "assets/npc/leftdangerousNPC.png"
        unknownNPC = Npc (screen, "Juliet", 50, 145, 85, 85, unknownNPCPath)
        unknownNPC.render()
       
        
        
        
        # Magic Block   
        magicBlockPath = "assets/miniplatform/tile1.png"
        magicBlock = pygame.image.load(magicBlockPath)
        magicBlockRect = magicBlock.get_rect(topright=(650, 580))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(magicBlock, magicBlockRect)
        magicBlockPath = "assets/miniplatform/tile2.png"
        magicBlock = pygame.image.load(magicBlockPath)
        magicBlockRect2 = magicBlock.get_rect(topright=(650, 630))
        screen.blit(magicBlock, magicBlockRect2)
           
        bottomPlatform.draw(screen)
        
        
        
        shrigenPath = "assets/miniplatform/shrigen.png"
        shrigen = pygame.image.load(shrigenPath)
        
        global SHRIGEN_X 
        global SHRIGEN_Y
        global VEL_DX
        global VEL_DY
        SHRIGEN_X  = (SHRIGEN_X+VEL_DX)%1024
        # SHRIGEN_Y  = (SHRIGEN_Y+VEL_DY)%800
        
        shrigenRect = shrigen.get_rect(topright=(SHRIGEN_X, 390))
        shrigenRect2 = shrigen.get_rect(topright=(SHRIGEN_X, 320))
        shrigenRect3 = shrigen.get_rect(topright=(SHRIGEN_X, 250))
        #pygame.draw.rect(screen, GREEN, shrigenRect,4)
        screen.blit(shrigen, shrigenRect)
        screen.blit(shrigen, shrigenRect2)
        screen.blit(shrigen, shrigenRect3)
        
        global MINI_PLAYER_X 
        global MINI_PLAYER_Y
        #MINI_PLAYER_Y -= 47
        
         
        
        self.playerPath = "assets/character/right/right1 copy.png"
        self.player = MiniPlayer(self.playerPath, MINI_PLAYER_X, MINI_PLAYER_Y)
        playerRect = self.player.getMiniPlayerRect()
        
        if playerRect.colliderect(magicBlockRect) or  playerRect.colliderect(magicBlockRect2) :
            MINI_PLAYER_X -= 10 
        
        if shrigenRect.colliderect(playerRect) or  shrigenRect2.colliderect(playerRect) or  shrigenRect3.colliderect(playerRect):
            # MINI_PLAYER_X -= 10
            MINI_PLAYER_X +=50
        
        
        
        # Gravity Section
        #playerSprite = pygame.sprite.Group()
        #playerSprite.add(self.player)
        
      
        collidedPlatform = gravityCheck(self.player,bottomPlatform)
        # print("gravity check = ",len(gravityCheck(self.player,bottomPlatform)))
        
        if len(collidedPlatform) > 0 : 
               #print("in!")
               MINI_PLAYER_Y = collidedPlatform[0].rect.topleft[1] - 47 
               #print("IN =  ", collidedPlatform[0].rect)
        else:
            
            MINI_PLAYER_Y += 9.8 + self.gravity 
            
        
        
        self.player.update(self.keyPress)
        self.player.draw(screen)
        
        sign_directory = "assets/font/Satisfy-Regular.ttf"
        sign_font = pygame.font.Font(sign_directory, 20)
        authorSignature = sign_font.render('Kyungtae Han', True, BLACK)
        screen.blit(authorSignature, (900, 750))
       
        
        
        
        
        #print("going in = ")
        # player.move(100,200)
       
        
        
      
        
        
       
        
       
        #print(pygame.mouse.get_pos())
        
        # easyNPC =  pygame.image.load("ibm_blockchain/assets/easynpc1.png")
        # easyNPC = pygame.transform.scale( easyNPC, (100,100) )
        # screen.blit(easyNPC,(850,600))  
        # path = "ibm_blockchain/assets/easynpc1.png"
        # easyNPC = Npc (screen, "Kelly",850, 600, 100, 100, path)
        # easyNPC.render()
        
        # # global WIDTH, HEIGHT
        # gameBackground = pygame.image.load("ibm_blockchain/assets/minigameBackground.png")
        # gameBackground = pygame.transform.scale(gameBackground,(1024,800))
        # screen.blit(gameBackground,(0,0))
        
        # # mini Platform 1 
        # bottomPlatform = pygame.image.load("ibm_blockchain/assets/bottomPlatform.png")
        # bottomPlatform = pygame.transform.scale(bottomPlatform,(1024,120))
        # screen.blit(bottomPlatform,(0,680))
        
        # bottomRect = bottomPlatform.get_rect()
        # bottomRect.center = 0,700  
        # pygame.draw.rect(screen, GREEN, bottomRect,4)
        
        
        # global WIDTH
        # i = 0 
        # while (i<WIDTH):
        #    screen.blit(bottomCaveTile,(i,680)) 
        #    screen.blit(bottomCaveTile,(i,700)) 
        #    i+=90
           
        matthewNPCPath = "assets/npc/matthewEllis.png"
        easyNPC = Npc (screen, "Dr. Matthew Ellis", 720, 485, 100, 100, matthewNPCPath)
        easyNPC.render()
        
        julietNPCPath = "assets/npc/juliet.png"
        julietNPC = Npc (screen, "Juliet", 880, 500, 85, 85, julietNPCPath)
        julietNPC.render()
        
        global IS_QUIZ_STARTED,IS_HIGHSCORE_UPDATED,IS_QUIZVOICE_PLAYED,quizVoice, ANSWER_CORRECT_VOICE, ANSWER_WRONG_VOICE
        
        if IS_QUIZ_STARTED:
            
            quiz1_content = "Q1. There are 4 types of BlockChain networks."
            quiz2_content = "Q2. Mutable records is the key element of BlockChain."
            quiz3_content = "Q3. Consortium networks is a key element of BlockChain."
            quiz4_content = "Q4. Permissioned Networks is a key element of BlockChain.  "
            quiz5_content = "Q5. Rubbish Thinking in blockchain is an example of use case."
            quiz6_content = "Q6. IBM Blockchain Platform Software is optimized to deploy on Blue Hat® OpenShift®."
            quiz7_content = "Q7. The IBM Blockchain Platform is NOT powered by Hyperledger technology."
            quiz8_content = "Q8. In Blockchain, each transaction is recorded as a block of data"
            quiz9_content = "Q9. In Blockchain, each block is disconnected to the ones before and after it"
            quiz10_content = "Q10. In Blockchain, transactions are blocked together in an reversible chain"
            quiz = Quiz(screen, 80, 80, quiz1_content,True)
            
            global QUIZ_INDEX
            
            quizStack = [Quiz(screen, 80, 80, quiz1_content,True),Quiz(screen, 80, 80, quiz2_content,False),
                         Quiz(screen, 80, 80, quiz3_content,True), Quiz(screen, 80, 80, quiz4_content,True),
                         Quiz(screen, 80, 80, quiz5_content,False),Quiz(screen, 80, 80, quiz6_content,False),
                         Quiz(screen, 80, 80, quiz7_content,False), Quiz(screen, 80, 80, quiz8_content,True),
                         Quiz(screen, 80, 80, quiz9_content,False) , Quiz(screen, 80, 80, quiz10_content,False) ]
        
            if QUIZ_INDEX is len(quizStack):
                if not IS_HIGHSCORE_UPDATED:
                    Sqlite().updateHighScore(3,SCORE)
                    IS_HIGHSCORE_UPDATED = True 
                IS_QUIZ_STARTED = False 
                SCORE = 0
                pass
                # print("Dialogue")
                
            else:
                quizStack[QUIZ_INDEX].render()
                if IS_QUIZVOICE_PLAYED[QUIZ_INDEX] :
                    IS_QUIZVOICE_PLAYED[QUIZ_INDEX] = False 
                    quizVoice[QUIZ_INDEX].play()
                     
                for event in self.events: 
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # Home Exit 
                        if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
                            # self.push(HomeNode()) 
                            print(quiz.checkAnswer(True))
                            if quizStack[QUIZ_INDEX].checkAnswer(True):
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_CORRECT_VOICE.play()
                                SCORE += SCORE_INCREMENT
                                QUIZ_INDEX +=1
                                # quizStack[QUIZ_INDEX].render()
                            else:
                                
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_WRONG_VOICE.play()
                                QUIZ_INDEX+=1
                        
                        elif (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
                            # self.push(GameIntroNode()) 
                            print(quiz.checkAnswer(False)) 
                            if quizStack[QUIZ_INDEX].checkAnswer(False):
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_CORRECT_VOICE.play()
                                SCORE += SCORE_INCREMENT 
                                QUIZ_INDEX +=1
                            else:
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_WRONG_VOICE.play()
                                QUIZ_INDEX+=1 
                            
        
        
        
        
        miniPlayerRect = self.player.getMiniPlayerRect()
        pygame.draw.rect(screen, RED, miniPlayerRect,4) 
        miniNPCRect = easyNPC.getNpcRect()
        
        
        pygame.mixer.init() 
        portal_sound = pygame.mixer.Sound("assets/background/music/effect/maplestory_portal.mp3") 
        
        hover_sound = pygame.mixer.Sound("assets/background/music/effect/CLICK_009.wav")
        
        
        
        global EASYMODE_NPC_INDEX, IS_SPACEBAR_PRESSED_2, IS_MATTHEWVOICE_PLAYED_STACK, matthewNPCDialogVoice  
        
        # for event in self.events:
        #     if miniNPCRect.colliderect(playerRect) and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #         IS_SPACEBAR_PRESSED = True
        if miniNPCRect.colliderect(playerRect) and self.keyPress[K_SPACE]:
            IS_SPACEBAR_PRESSED_2 = True         
        
        # global MINI_PLAYER_X
        # print("BEFORE COMING IN ", TOWN_NPC_DIALOG_INDEX)
        if miniNPCRect.colliderect(miniPlayerRect) and IS_SPACEBAR_PRESSED_2 is True  and EASYMODE_NPC_INDEX>=0 :
         
         
            if IS_MATTHEWVOICE_PLAYED_STACK[EASYMODE_NPC_INDEX] : 
                IS_MATTHEWVOICE_PLAYED_STACK[EASYMODE_NPC_INDEX] = False 
                matthewNPCDialogVoice[EASYMODE_NPC_INDEX].play() 
                matthewNPCDialogVoice[EASYMODE_NPC_INDEX].set_volume(1.0)
            # portal_sound.play()
            # PLAYER_X -= 1 
            # PLAYER_Y -= 1
            filePath = matthewNPCPath
            
            dialog1_txt = open('assets/npc/npcVoice/matthew/matthewDialog/matthewDialog1.txt','r')
            dialog1 = dialog1_txt.read()
            dialog1_txt.close()
            
            dialog2_txt = open('assets/npc/npcVoice/matthew/matthewDialog/matthewDialog2.txt','r')
            dialog2 = dialog2_txt.read()
            dialog2_txt.close()
            
            dialog3_txt = open('assets/npc/npcVoice/matthew/matthewDialog/matthewDialog3.txt','r')
            dialog3 = dialog3_txt.read()
            dialog3_txt.close()
            
            dialog4_txt = open('assets/npc/npcVoice/matthew/matthewDialog/matthewDialog4.txt','r')
            dialog4 = dialog4_txt.read()
            dialog4_txt.close()
            
            dialog5_txt = open('assets/npc/npcVoice/matthew/matthewDialog/matthewDialog5.txt','r')
            dialog5 = dialog5_txt.read()
            dialog5_txt.close()
            
            
            if len(dialog1) > 590: 
                raise Exception("theKingDialog1 exceeded 590 characters.", len(dialog1))
            if len(dialog2) > 590: 
                raise Exception("theKingDialog2 exceeded 590 characters.", len(dialog2))
            if len(dialog3) > 590: 
                raise Exception("theKingDialog3 exceeded 590 characters.", len(dialog3))
            if len(dialog4) > 590: 
                raise Exception("theKingDialog4 exceeded 590 characters.", len(dialog4))
            if len(dialog5) > 590: 
                raise Exception("theKingDialog5 exceeded 590 characters.", len(dialog5))
            
            
            
            
            # dialog1 = "Hey there, have you come here from Dr. Emma Norling? Congratulations! You finally have reached here and completed the game! "
            # dialog2 = """I'm Matthew Ellis, the lecturer in Machine Learning and  and member of the Machine Learning Group at the Department of Computer Science. I graduated with a MPhys in Theoretical Physics from the University of York in 2011, before staying at York to undertake a PhD in Physics under Prof. Roy Chantrell."""
            # dialog3 = "After completing my PhD in 2015, I joined the group of Prof. Stefano Sanvito at Trinity College Dublin as a post-doctoral research fellow. In 2019, I joined the University of Sheffield as a post-doctoral research associate in the Bio-Inpsired Machine Learning group under Prof. Eleni Vasilaki developing machine learning models for neuromorphic computing in collaboration with the Department of Materials Science.   "
            # dialog4 = "We are currently working with IBM on Watson Text-To-Speech, especially cooperating with AI Group Project. The University of Sheffield is planning to reach top 1-tier list as Stanford, MIT, and Harvard. "
            # dialog5 = "This is what I've got to talk with you today. Do you want to go back to Dr. Emma Norling? (Automatically takes you to Dr. Emma Norling! If not, you can still leave with above exit button!)"
            exitDialog = "It is said that you are not interested in our research with IBM. Talk to you later. (Emma is keeping push you behind.)"
            
            dialogStack = [Dialog(screen, filePath, "Dr.Matthew Ellis", dialog1, True, False, True, False, False),
                           Dialog(screen, filePath, "Dr.Matthew Ellis", dialog2, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr.Matthew Ellis", dialog3, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr.Matthew Ellis", dialog4, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr.Matthew Ellis", dialog5, True, True, False, True, True)
                           
                        ]
            
            
            dialogStack[EASYMODE_NPC_INDEX].render()
            endChatRect =  dialogStack[EASYMODE_NPC_INDEX].drawEndChatButton()
            nextChatRect = dialogStack[EASYMODE_NPC_INDEX].drawNextButton()
            prevChatRect = dialogStack[EASYMODE_NPC_INDEX].drawPrevButton()
            yesChatRect = dialogStack[EASYMODE_NPC_INDEX].drawYesButton()
            noChatRect = dialogStack[EASYMODE_NPC_INDEX].drawNoButton()
            dialogStack[EASYMODE_NPC_INDEX].drawNPCFigure()
            dialogStack[EASYMODE_NPC_INDEX].drawDialogText()
            
            for event in self.events:
                    if event.type == pygame.MOUSEBUTTONDOWN :
                           
                           
                            if endChatRect is not None and endChatRect.collidepoint(pygame.mouse.get_pos()):
                                matthewNPCDialogVoice[EASYMODE_NPC_INDEX].stop()
                                EASYMODE_NPC_INDEX= 0  
                                IS_SPACEBAR_PRESSED_2 = False  
                                #print(EASYMODE_NPC_INDEX)
                                hover_sound.play()
                                
                            if nextChatRect is not None and nextChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("nextChatRect")
                                hover_sound.play()
                                matthewNPCDialogVoice[EASYMODE_NPC_INDEX].stop()
                                EASYMODE_NPC_INDEX +=1 
                                IS_MATTHEWVOICE_PLAYED_STACK[EASYMODE_NPC_INDEX] = True 
                                #matthewNPCDialogVoice[EASYMODE_NPC_INDEX].stop()
                                #print(EASYMODE_NPC_INDEX)
                            if prevChatRect is not None and prevChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("prevChatRect")
                                hover_sound.play()
                                matthewNPCDialogVoice[EASYMODE_NPC_INDEX].stop()
                                EASYMODE_NPC_INDEX -=1
                                IS_MATTHEWVOICE_PLAYED_STACK[EASYMODE_NPC_INDEX] = True
                                #print(EASYMODE_NPC_INDEX)
                                
                            if yesChatRect is not None and yesChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("yesChatRect")
                                matthewNPCDialogVoice[EASYMODE_NPC_INDEX].stop()
                                hover_sound.play()
                                #print(EASYMODE_NPC_INDEX)
                                portal_sound.play()
                                MINI_PLAYER_X, MINI_PLAYER_Y = 0 ,630
                                self.push(HomeNode())
                                
                            if  noChatRect is not None and noChatRect.collidepoint(pygame.mouse.get_pos()):  
                                #print("nochatrect")
                                matthewNPCDialogVoice[EASYMODE_NPC_INDEX].stop()
                                hover_sound.play()
                                #print(EASYMODE_NPC_INDEX)
                               
                                EASYMODE_NPC_INDEX= 0 
                                IS_SPACEBAR_PRESSED_2 = False   
                        
                    
            
            
            # self.pop()
            # self.push(GameIntroNode())
        else:    
            IS_SPACEBAR_PRESSED_2 = False    
            IS_MATTHEWVOICE_PLAYED_STACK[EASYMODE_NPC_INDEX] = True 
            matthewNPCDialogVoice[EASYMODE_NPC_INDEX].stop()
            EASYMODE_NPC_INDEX = 0
            
            # IS_SPACEBAR_PRESSED = False         
        
        unknownNPCRect = unknownNPC.getNpcRect()
        unknownQuizNPC(screen, self.events, self.keyPress,unknownNPCPath ,unknownNPCRect,playerRect)
        
        # global IS_QUIZ_STARTED,IS_HIGHSCORE_UPDATED
        
        # if IS_QUIZ_STARTED:
            
        #     quiz1_content = "Q1. There are 4 types of BlockChain networks."
        #     quiz2_content = "Q2. Mutable records is a key element of BlockChain."
        #     quiz3_content = "Q3. Consortium networks is a key element of BlockChain."
        #     quiz = Quiz(screen, 80, 80, quiz1_content,True)
            
        #     global QUIZ_INDEX
            
        #     quizStack = [Quiz(screen, 80, 80, quiz1_content,True),Quiz(screen, 80, 80, quiz2_content,False),Quiz(screen, 80, 80, quiz3_content,True)]
        
        #     if QUIZ_INDEX is len(quizStack):
        #         if not IS_HIGHSCORE_UPDATED:
        #             Sqlite().updateHighScore(3,SCORE)
        #             IS_HIGHSCORE_UPDATED = True 
        #         IS_QUIZ_STARTED = False 
        #         SCORE = 0
        #         pass
        #         # print("Dialogue")
                
        #     else:
        #         quizStack[QUIZ_INDEX].render()
        #         for event in self.events: 
        #             if event.type == pygame.MOUSEBUTTONDOWN :
        #                 mouse_x, mouse_y = pygame.mouse.get_pos()
        #                 # Home Exit 
        #                 if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
        #                     # self.push(HomeNode()) 
        #                     print(quiz.checkAnswer(True))
        #                     if quizStack[QUIZ_INDEX].checkAnswer(True):
                            
        #                         SCORE += SCORE_INCREMENT
        #                         QUIZ_INDEX +=1
        #                         # quizStack[QUIZ_INDEX].render()
        #                     else:
        #                         QUIZ_INDEX+=1
                        
        #                 elif (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
        #                     # self.push(GameIntroNode()) 
        #                     print(quiz.checkAnswer(False)) 
        #                     if quizStack[QUIZ_INDEX].checkAnswer(False):
                            
        #                         SCORE += SCORE_INCREMENT 
        #                         QUIZ_INDEX +=1
        #                     else:
        #                         QUIZ_INDEX+=1 
                            
                
        
        # Name Tag
        pygame.draw.rect(screen, (51,51,51), pygame.Rect(660, 600, 230, 43), border_radius = 10 )
        
        LIGHT_GREEN = (234,230,70)
        ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 12)
        answer1_content = "Dr.Matthew Ellis"
        answer1 =  ANSWER_FONT.render(answer1_content, True, LIGHT_GREEN)
        screen.blit(answer1,(680, 620))
        
        global USER_ID 
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(USER_ID)
        else: 
            pass
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(USER_ID)
        else: 
            pass
        
        if len(collidedPlatform) == 0 :
            self.gravity +=0.01
        else:
            self.graivty = 1 
             
        # dx = 10
        # dy = 10 
        
        # ball1 = Ball(512, 400, 20, screen, dx,dy)
        # ball1.render()
        # ball1.update()
        #pygame.draw.rect(screen, RED, pygame.Rect(550, 470, 10, 10))


IS_ROGERVOICE_PLAYED = [True,True,True,True,True] 
rogerNPCDialogVoice = [pygame.mixer.Sound("assets/npc/npcVoice/roger/rogerDialog1.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/roger/rogerDialog2.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/roger/rogerDialog3.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/roger/rogerDialog4.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/roger/rogerDialog5.wav")]

IS_SPACEBAR_PRESSED_4 = False 
        
class MediumModeNode(SceneStack):
    def __init__(self):
        SceneStack.__init__(self)
        #self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
        #self.character = pygame.transform.scale( self.character, (40,40) )
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/SnowyVillage.mp3") 
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)
       #x,y = 200,400
        #VELOCITY = 8
        
    def ProcessInput(self, events, keyPress):
        self.keyPress = keyPress
        self.events = events
        global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_ACHIEVEMENT_OPEN
        
        global MINI_PLAYER_X, MINI_PLAYER_Y
        global OPEN_STATS_VOICE, OPEN_LEADERBOARD_VOICE, CLOSE_STATS_VOICE, CLOSE_LEADERBOARD_VOICE, OPEN_ACHIEVEMENT_VOICE, CLOSE_ACHIEVEMENT_VOICE
        
        for event in events: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                # Move to the next scene when the user pressed Enter
                print("yes")
                self.push(GameOverNode())
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                MINI_PLAYER_Y -= 30     
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x, mouse_y = pygame.mouse.get_pos()
                global RETURN_HOME_VOICE, MINIGAME_HOME_VOICE
                # Home Exit 
                if (964<=mouse_x<=1004) and (20 <= mouse_y <= 60) : 
                    #RETURN_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(HomeNode())  
                if (924<=mouse_x<=964) and (20 <= mouse_y <= 60) : 
                    MINIGAME_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(GameIntroNode())  
            
            if event.type == pygame.KEYDOWN and event.key == K_1:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True  
                    OPEN_LEADERBOARD_VOICE.play() 
                else: 
                    IS_LEADERBOARD_OPEN = False 
                    CLOSE_LEADERBOARD_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_2: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True   
                    OPEN_STATS_VOICE.play()
                else: 
                    IS_STATS_OPEN = False 
                    CLOSE_STATS_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True   
                    OPEN_ACHIEVEMENT_VOICE.play()
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False 
                    CLOSE_ACHIEVEMENT_VOICE.play()   
                    #CLOSE_STATS_VOICE.play()     
                    
        if keyPress[K_SPACE] and keyPress[K_RIGHT] :
            MINI_PLAYER_Y -= 5 
            # MINI_PLAYER_X += 15    
    
    def Update(self):
        pass
    
    def Render(self, screen):
         # Field 
        gameBackground = pygame.image.load("assets/background/mediumModeBackground.png")
        gameBackground = pygame.transform.scale(gameBackground,(1024,800))
        screen.blit(gameBackground,(0,0))
        
        global SCORE
        # text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
        # textRect = text.get_rect()
        # textRect.center = (100,20)
        # #SCORE += SCORE_INCREMENT
        # screen.blit(text, textRect)
        # scoreBoard = ScoreBoard(screen, SCORE, 10, 10)
        # scoreBoard.render()
        
        global MINI_PLAYER_X 
        global MINI_PLAYER_Y
        
        
        
        
        
        
        
        self.playerPath = "assets/character/right/right1.png"
        self.player = MiniPlayer(self.playerPath, MINI_PLAYER_X, MINI_PLAYER_Y)
       
        
        bottomPlatform = pygame.sprite.Group()
        #leftCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/leftCorner.png"
        middleTilePath = "assets/miniplatform/winterTile/middleTile.png"
        #rightCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/rightCorner.png"
        #downTilePath = "ibm_blockchain/assets/miniplatform/winterTile/downTile.png"
        leftOverPath = "assets/miniplatform/winterTile/winterMiddleTile.png"
        # miniPlatform = MiniPlatform(platformPath,0,680) 
        
        # Bottom Platform
        for eachTileX in range(0,1100,50):
            
            bottomPlatform.add(MiniPlatform(middleTilePath,eachTileX,680))
            bottomPlatform.add (MiniPlatform(leftOverPath,eachTileX,730))
            bottomPlatform.add (MiniPlatform(leftOverPath,eachTileX,770))
           
           
            #bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,800))
        
         ## NPC Upper platform
        for eachTileX in range(650,1024,50):
            bottomPlatform.add(MiniPlatform(middleTilePath,eachTileX,580))
            bottomPlatform.add(MiniPlatform(leftOverPath,eachTileX,630))
                
        bottomPlatform.draw(screen)
        
        # collidedPlatform = gravityCheck(self.player,bottomPlatform)
        # # print("gravity check = ",len(gravityCheck(self.player,bottomPlatform)))
        
        # if len(collidedPlatform) > 0 : 
        #        print("in!")
        #        MINI_PLAYER_Y = collidedPlatform[0].rect.top-47
        #        print("IN =  ", collidedPlatform[0].rect)
        # else:
        #     MINI_PLAYER_Y += 9.8
        
        crystalPath = "assets/miniplatform/winterTile/object/Crystal.png"
        crystal = pygame.image.load(crystalPath)
        crystal = pygame.transform.scale(crystal,(100,100))
        crystalRect = crystal.get_rect(topleft=(100, 580))
        crystalRect2 = crystal.get_rect(topleft=(900, 485))
        crystalRect3 = crystal.get_rect(topleft=(900, 585))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(crystal, crystalRect)
        screen.blit(crystal,crystalRect3)
        
        
        
        snowmanPath = "assets/miniplatform/winterTile/object/SnowMan.png"
        snowman = pygame.image.load(snowmanPath)
        snowman = pygame.transform.scale(snowman,(100,50))
        snowmanRect = snowman.get_rect(topleft=(630, 535))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(snowman, snowmanRect)
        
        
        
        iglooPath = "assets/miniplatform/winterTile/object/Igloo.png"
        igloo = pygame.image.load(iglooPath)
        igloo = pygame.transform.scale(igloo,(210,150))
        iglooRect = igloo.get_rect(topleft=(800, 435))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(igloo, iglooRect)
        
        huskyPath = "assets/miniplatform/winterTile/object/sleepingHusky.png"
        husky = pygame.image.load(huskyPath)
        husky = pygame.transform.scale(husky,(100,50))
        huskyRect = husky.get_rect(topleft=(800, 545))
        screen.blit(husky, huskyRect)
        
        
        signPath = "assets/miniplatform/winterTile/object/Sign_2.png"
        sign = pygame.image.load(signPath)
        sign = pygame.transform.scale(sign,(100,100))
        signRect = sign.get_rect(topleft=(200, 580))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(sign, signRect)
        
        self.player.update(self.keyPress)
        self.player.draw(screen)
        
        treePath = "assets/miniplatform/winterTile/object/Tree_1.png"
        tree = pygame.image.load(treePath)
        tree = pygame.transform.scale(tree,(300,300))
        treeRect = tree.get_rect(topleft=(300, 385))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(tree, treeRect)
        
        smallTreePath = "assets/miniplatform/winterTile/object/Tree_1.png"
        smallTree = pygame.image.load(smallTreePath)
        smallTree = pygame.transform.scale(smallTree,(100,100))
        smallTreeRect = smallTree.get_rect(topleft=(300, 580))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(smallTree, smallTreeRect)
        
        smallTreePath = "assets/miniplatform/winterTile/object/Tree_1.png"
        smallTree = pygame.image.load(smallTreePath)
        smallTree = pygame.transform.scale(smallTree,(100,100))
        smallTreeRect = smallTree.get_rect(topleft=(500, 580))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(smallTree, smallTreeRect)
        
        rudolfPath = "assets/miniplatform/winterTile/object/petRudolf.png"
        rudolf = pygame.image.load(rudolfPath)
        rudolf = pygame.transform.scale(rudolf,(50,50))
        rudolfRect = rudolf.get_rect(topleft =(240,635))
        rudolfRect2 = rudolf.get_rect(topleft =(580,635))
        screen.blit(rudolf,rudolfRect)
        screen.blit(rudolf,rudolfRect2)
        
        # cokeYetiPath = "ibm_blockchain/assets/miniplatform/winterTile/object/cokeYeti.png"
        # cokeYeti = pygame.image.load(cokeYetiPath)
        # cokeYeti = pygame.transform.scale(cokeYeti,(80,80))
        # cokeYetiRect = cokeYeti.get_rect(topleft =(580,605))
        # screen.blit(cokeYeti,cokeYetiRect)
        
        
        
        # crystalPath = "ibm_blockchain/assets/miniplatform/winterTile/object/Crystal.png"
        # crystal = pygame.image.load(crystalPath)
        # crystal = pygame.transform.scale(crystal,(100,100))
        # crystalRect = crystal.get_rect(topleft=(100, 580))
        # crystalRect2 = crystal.get_rect(topleft=(900, 485))
        # # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        # screen.blit(crystal, crystalRect)
        # screen.blit(crystal, crystalRect2)
        
        # snowmanPath = "ibm_blockchain/assets/miniplatform/winterTile/object/SnowMan.png"
        # snowman = pygame.image.load(snowmanPath)
        # snowman = pygame.transform.scale(snowman,(100,50))
        # snowmanRect = snowman.get_rect(topleft=(630, 535))
        # # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        # screen.blit(snowman, snowmanRect)
        
         # mini Platform 1 
        # bottomPlatform = pygame.image.load("ibm_blockchain/assets/bottomPlatform.png")
        # bottomPlatform = pygame.transform.scale(bottomPlatform,(1024,120))
        # screen.blit(bottomPlatform,(0,680))
        
        # mediumNPC =  pygame.image.load("ibm_blockchain/assets/mediumNPC.png")
        # mediumNPC = pygame.transform.scale( mediumNPC, (100,100) )
        # screen.blit(mediumNPC,(850,600))  
        
        
        
        
        mediumNPCPath = "assets/npc/rogerMoore.png"
        mediumNPC = Npc (screen, "Roger",700, 485, 100, 100, mediumNPCPath)
        mediumNPC.render()
        
        miniPlayerRect = self.player.getMiniPlayerRect()
        pygame.draw.rect(screen, RED, miniPlayerRect,4) 
        
        miniNPCRect = mediumNPC.getNpcRect()
        
       
        pygame.mixer.init() 
        automaticReSpawn = pygame.mixer.Sound("assets/miniplatform/winterTile/sound/magicalPowerSound.wav") 
       
        
        if miniPlayerRect.colliderect(crystalRect3):
            # MINI_PLAYER_X -= 10
            automaticReSpawn.play(0)
            MINI_PLAYER_X = 0
            MINI_PLAYER_Y = 630
             
        
        
        
        screen.blit(crystal, crystalRect2)
        
        # pygame.mixer.init() 
        portal_sound = pygame.mixer.Sound("assets/background/music/effect/maplestory_portal.mp3") 
        
        hover_sound = pygame.mixer.Sound("assets/background/music/effect/CLICK_009.wav")
        global MEDIUMMODE_NPC_INDEX
        
        global IS_ROGERVOICE_PLAYED, rogerNPCDialogVoice, IS_SPACEBAR_PRESSED_4
        
        if miniNPCRect.colliderect(miniPlayerRect) and self.keyPress[K_SPACE]:
            IS_SPACEBAR_PRESSED_4 = True   
        
        
        # global MINI_PLAYER_X
        # print("BEFORE COMING IN ", TOWN_NPC_DIALOG_INDEX)
        if miniNPCRect.colliderect(miniPlayerRect) and IS_SPACEBAR_PRESSED_4 is True and MEDIUMMODE_NPC_INDEX>=0 :
            if IS_ROGERVOICE_PLAYED[MEDIUMMODE_NPC_INDEX] : 
                IS_ROGERVOICE_PLAYED[MEDIUMMODE_NPC_INDEX] = False 
                rogerNPCDialogVoice[MEDIUMMODE_NPC_INDEX].play()
            
            
            # portal_sound.play()
            # PLAYER_X -= 1 
            # PLAYER_Y -= 1
            filePath = mediumNPCPath
            
            dialog1_txt = open('assets/npc/npcVoice/roger/rogerDialog/rogerDialog1.txt','r')
            dialog1 = dialog1_txt.read()
            dialog1_txt.close()
            
            dialog2_txt = open('assets/npc/npcVoice/roger/rogerDialog/rogerDialog2.txt','r')
            dialog2 = dialog2_txt.read()
            dialog2_txt.close()
            
            dialog3_txt = open('assets/npc/npcVoice/roger/rogerDialog/rogerDialog3.txt','r')
            dialog3 = dialog3_txt.read()
            dialog3_txt.close()
            
            dialog4_txt = open('assets/npc/npcVoice/roger/rogerDialog/rogerDialog4.txt','r')
            dialog4 = dialog4_txt.read()
            dialog4_txt.close()
            
            dialog5_txt = open('assets/npc/npcVoice/roger/rogerDialog/rogerDialog5.txt','r')
            dialog5 = dialog5_txt.read()
            dialog5_txt.close()
            
            
            if len(dialog1) > 590: 
                raise Exception("theKingDialog1 exceeded 590 characters.", len(dialog1))
            if len(dialog2) > 590: 
                raise Exception("theKingDialog2 exceeded 590 characters.", len(dialog2))
            if len(dialog3) > 590: 
                raise Exception("theKingDialog3 exceeded 590 characters.", len(dialog3))
            if len(dialog4) > 590: 
                raise Exception("theKingDialog4 exceeded 590 characters.", len(dialog4))
            if len(dialog5) > 590: 
                raise Exception("theKingDialog5 exceeded 590 characters.", len(dialog5))
            
            
            
            
            
            # dialog1 = "Hey there, have you come here from Dr. Emma Norling? Congratulations! You finally have reached here and completed the game! "
            # dialog2 = """I'm Roger Moore, the Professor of Spoken Language Processing and Member of the Speech and Hearing (SpandH) research group at the Department of Computer Science. I have gained over 40 years’ experience in Speech Technology R&D and, although an engineer by training, much of my research has been based on insights from human speech perception and production."""
            # dialog3 = "Since 2004, I have been Professor of Spoken Language Processing at the University of Sheffield, and also holds Visiting Chairs at Bristol Robotics Laboratory and University College London Psychology & Language Sciences.  I was President of the European/International Speech Communication Association from 1997 to 2001, General Chair for INTERSPEECH-2009 and ISCA Distinguished Lecturer during 2014-15.      "
            # dialog4 = "We are currently working with IBM on Watson Text-To-Speech, especially cooperating with AI Group Project. The University of Sheffield is planning to reach top 1-tier list as Stanford, MIT, and Harvard. "
            # dialog5 = "This is what I've got to talk with you today. Do you want to go back to Dr. Emma Norling? (Automatically takes you to Dr. Emma Norling! If not, you can still leave with above exit button!)"
            # exitDialog = "It is said that you are not interested in our research with IBM. Talk to you later. (Emma is keeping push you behind.)"
            
            dialogStack = [Dialog(screen, filePath, "Dr. Roger Moore", dialog1, True, False, True, False, False),
                           Dialog(screen, filePath, "Dr. Roger Moore", dialog2, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr. Roger Moore", dialog3, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr. Roger Moore", dialog4, True, True, True, False, False),
                           Dialog(screen, filePath, "Dr. Roger Moore", dialog5, True, True, False, True, True)
                           
                        ]
            
            
            dialogStack[MEDIUMMODE_NPC_INDEX].render()
            endChatRect =  dialogStack[MEDIUMMODE_NPC_INDEX].drawEndChatButton()
            nextChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawNextButton()
            prevChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawPrevButton()
            yesChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawYesButton()
            noChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawNoButton()
            dialogStack[MEDIUMMODE_NPC_INDEX].drawNPCFigure()
            dialogStack[MEDIUMMODE_NPC_INDEX].drawDialogText()
            
            for event in self.events:
                    if event.type == pygame.MOUSEBUTTONDOWN :
                           
                           
                            if endChatRect is not None and endChatRect.collidepoint(pygame.mouse.get_pos()):
                                rogerNPCDialogVoice[MEDIUMMODE_NPC_INDEX].stop()
                                IS_SPACEBAR_PRESSED_4 = False 
                                MEDIUMMODE_NPC_INDEX = -1  
                                #print(MEDIUMMODE_NPC_INDEX)
                                hover_sound.play()
                                
                            if nextChatRect is not None and nextChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("nextChatRect")
                                hover_sound.play()
                                rogerNPCDialogVoice[MEDIUMMODE_NPC_INDEX].stop()
                                MEDIUMMODE_NPC_INDEX +=1 
                                IS_ROGERVOICE_PLAYED[MEDIUMMODE_NPC_INDEX] = True 
                               
                                print(MEDIUMMODE_NPC_INDEX)
                            if prevChatRect is not None and prevChatRect.collidepoint(pygame.mouse.get_pos()):
                                #print("prevChatRect")
                                rogerNPCDialogVoice[MEDIUMMODE_NPC_INDEX].stop()
                                hover_sound.play()
                                MEDIUMMODE_NPC_INDEX -=1
                                IS_ROGERVOICE_PLAYED[MEDIUMMODE_NPC_INDEX] = True 
                                #print(MEDIUMMODE_NPC_INDEX)
                                
                            if yesChatRect is not None and yesChatRect.collidepoint(pygame.mouse.get_pos()):
                                rogerNPCDialogVoice[MEDIUMMODE_NPC_INDEX].stop()
                                #print("yesChatRect")
                                hover_sound.play()
                                #print(MEDIUMMODE_NPC_INDEX)
                                portal_sound.play()
                                MINI_PLAYER_X, MINI_PLAYER_Y = 0 ,630
                                self.push(SecretPortalMediumNode())
                                
                            if  noChatRect is not None and noChatRect.collidepoint(pygame.mouse.get_pos()):  
                                rogerNPCDialogVoice[MEDIUMMODE_NPC_INDEX].stop()
                                IS_SPACEBAR_PRESSED_4 = False 
                                #print("nochatrect")
                                hover_sound.play()
                                #print(MEDIUMMODE_NPC_INDEX)
                                MEDIUMMODE_NPC_INDEX= -1  
                        
                    
            
            
            # self.pop()
            # self.push(GameIntroNode())
        else:    
            IS_ROGERVOICE_PLAYED[MEDIUMMODE_NPC_INDEX] = True 
            IS_SPACEBAR_PRESSED_4 = False 
            rogerNPCDialogVoice[MEDIUMMODE_NPC_INDEX].stop()
            MEDIUMMODE_NPC_INDEX = 0
        
        
         #Refresh 
        refreshButtonPath = "assets/button/homeIcon.png"
        refreshButton = pygame.image.load(refreshButtonPath)
        refreshButton = pygame.transform.scale(refreshButton,(40,40))
        refreshButtonRect = refreshButton.get_rect(topright=(1024-20, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(refreshButton, refreshButtonRect)
        
         #Refresh 
        returnButtonPath = "assets/button/goBackHomeScreen.png"
        returnButton = pygame.image.load(returnButtonPath)
        returnButton = pygame.transform.scale(returnButton,(40,40))
        returnButtonRect = returnButton.get_rect(topright=(1024-20-40, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(returnButton, returnButtonRect)
        
        #  # LeaderBoard 
        # leaderBoardButtonPath = "ibm_blockchain/assets/Leaderboard.png"
        # leaderBoardButton = pygame.image.load(leaderBoardButtonPath)
        # leaderBoardButton = pygame.transform.scale(leaderBoardButton,(40,40))
        # leaderBoardButtonRect = leaderBoardButton.get_rect(topright=(1024-20-40-40, 20))
        # # pygame.draw.rect(screen, RED, leaderBoardButtonRect,4) 
        # screen.blit(leaderBoardButton, leaderBoardButtonRect)
        
        
        # bottomPlatform = pygame.sprite.Group()
        # leftCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/leftCorner.png"
        # middleTilePath = "ibm_blockchain/assets/miniplatform/winterTile/middleTile.png"
        # rightCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/rightCorner.png"
        # downTilePath = "ibm_blockchain/assets/miniplatform/winterTile/downTile.png"
        # leftOverPath = "ibm_blockchain/assets/miniplatform/winterTile/winterMiddleTile.png"
        # # miniPlatform = MiniPlatform(platformPath,0,680) 
        
        # # Bottom Platform
        # for eachTileX in range(0,1100,50):
            
        #     bottomPlatform.add(MiniPlatform(middleTilePath,eachTileX,680))
        #     bottomPlatform.add (MiniPlatform(leftOverPath,eachTileX,730))
        #     bottomPlatform.add (MiniPlatform(leftOverPath,eachTileX,770))
           
           
        #     #bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,800))
        
        #  ## NPC Upper platform
        # for eachTileX in range(650,1024,50):
        #     bottomPlatform.add(MiniPlatform(middleTilePath,eachTileX,580))
        #     bottomPlatform.add(MiniPlatform(leftOverPath,eachTileX,630))
                
        # bottomPlatform.draw(screen)
        
        collidedPlatform = gravityCheck(self.player,bottomPlatform)
        # print("gravity check = ",len(gravityCheck(self.player,bottomPlatform)))
        
        if len(collidedPlatform) > 0 : 
               print("in!")
               MINI_PLAYER_Y = collidedPlatform[0].rect.top-47
               print("IN =  ", collidedPlatform[0].rect)
        else:
            MINI_PLAYER_Y += 9.8
        
        
        # iglooPath = "ibm_blockchain/assets/miniplatform/winterTile/object/Igloo.png"
        # igloo = pygame.image.load(iglooPath)
        # igloo = pygame.transform.scale(igloo,(210,150))
        # iglooRect = igloo.get_rect(topleft=(800, 435))
        # # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        # screen.blit(igloo, iglooRect)
        
        # signPath = "ibm_blockchain/assets/miniplatform/winterTile/object/Sign_2.png"
        # sign = pygame.image.load(signPath)
        # sign = pygame.transform.scale(sign,(100,100))
        # signRect = sign.get_rect(topleft=(200, 580))
        # # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        # screen.blit(sign, signRect)
        
        # treePath = "ibm_blockchain/assets/miniplatform/winterTile/object/Tree_1.png"
        # tree = pygame.image.load(treePath)
        # tree = pygame.transform.scale(tree,(300,300))
        # treeRect = tree.get_rect(topleft=(300, 385))
        # # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        # screen.blit(tree, treeRect)
        
        sign_directory = "assets/font/Satisfy-Regular.ttf"
        sign_font = pygame.font.Font(sign_directory, 20)
        authorSignature = sign_font.render('Kyungtae Han', True, BLACK)
        screen.blit(authorSignature, (900, 750))
        
         # Name Tag
        pygame.draw.rect(screen, (51,51,51), pygame.Rect(660, 600, 250, 43), border_radius = 10 )
        
        LIGHT_GREEN = (234,230,70)
        ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 12)
        answer1_content = "Dr. Roger Moore"
        answer1 =  ANSWER_FONT.render(answer1_content, True, LIGHT_GREEN)
        screen.blit(answer1,(680, 620))
        
       
        
        
        global USER_ID 
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(USER_ID)
        else: 
            pass
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(USER_ID)
        else: 
            pass
        
        
MEDIUM_HIDDEN_WELCOME_VOICE = pygame.mixer.Sound("assets/npc/npcVoice/roger/mediumHiddenWelcome.wav")

class SecretPortalMediumNode(SceneStack):
    def __init__(self):
        SceneStack.__init__(self)
        #self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
        #self.character = pygame.transform.scale( self.character, (40,40) )
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/SnowyVillage.mp3") 
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)
        
        global MEDIUM_HIDDEN_WELCOME_VOICE 
        MEDIUM_HIDDEN_WELCOME_VOICE.play()
        MEDIUM_HIDDEN_WELCOME_VOICE.set_volume(1.0)
        x,y = 200,400
        VELOCITY = 8
        
    def ProcessInput(self, events, pressed_keys):
        self.keyPress = pressed_keys
        self.events = events
        
        global MINI_PLAYER_X, MINI_PLAYER_Y
        global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_ACHIEVEMENT_OPEN
        global OPEN_STATS_VOICE, OPEN_LEADERBOARD_VOICE, CLOSE_STATS_VOICE, CLOSE_LEADERBOARD_VOICE, OPEN_ACHIEVEMENT_VOICE, CLOSE_ACHIEVEMENT_VOICE
        
        for event in events: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                # Move to the next scene when the user pressed Enter
                print("yes")
                self.push(GameOverNode())
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                MINI_PLAYER_Y -= 30     
            
            if event.type == pygame.KEYDOWN and event.key == K_1:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True   
                    OPEN_LEADERBOARD_VOICE.play()
                else: 
                    IS_LEADERBOARD_OPEN = False 
                    CLOSE_LEADERBOARD_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_2: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True   
                    OPEN_STATS_VOICE.play()
                else: 
                    IS_STATS_OPEN = False 
                    CLOSE_STATS_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True 
                    OPEN_ACHIEVEMENT_VOICE.play()  
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False 
                    CLOSE_ACHIEVEMENT_VOICE.play()   
                    #CLOSE_STATS_VOICE.play()     
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x, mouse_y = pygame.mouse.get_pos()
                global RETURN_HOME_VOICE, MINIGAME_HOME_VOICE
                # Home Exit 
                if (964<=mouse_x<=1004) and (20 <= mouse_y <= 60) : 
                    #RETURN_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(HomeNode())  
                if (924<=mouse_x<=964) and (20 <= mouse_y <= 60) : 
                    MINIGAME_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(GameIntroNode())      
    
    def Update(self):
        pass
    
    def Render(self, screen):
         # Field 
        gameBackground = pygame.image.load("assets/background/mediumModeBackground.png")
        gameBackground = pygame.transform.scale(gameBackground,(1024,800))
        screen.blit(gameBackground,(0,0))
        
        global SCORE
        # text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
        # textRect = text.get_rect()
        # textRect.center = (100,20)
        # #SCORE += SCORE_INCREMENT
        # screen.blit(text, textRect)
        scoreBoard = ScoreBoard(screen, SCORE, 10, 10)
        scoreBoard.render()
        
        global MINI_PLAYER_X 
        global MINI_PLAYER_Y
         
        self.playerPath = "assets/character/right/right1.png"
        self.player = MiniPlayer(self.playerPath, MINI_PLAYER_X, MINI_PLAYER_Y)
        
        unknownNPCPath = "assets/npc/leftdangerousNPC.png"
        unknownNPC = Npc (screen, "Juliet", 100, 105, 85, 85, unknownNPCPath)
        unknownNPC.render()
        miniNPCRect = unknownNPC.getNpcRect()
        
        # self.player.update(self.keyPress)
        # self.player.draw(screen)
        
        bottomPlatform = pygame.sprite.Group()
        #leftCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/leftCorner.png"
        middleTilePath = "assets/miniplatform/winterTile/middleTile.png"
        #rightCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/rightCorner.png"
        #downTilePath = "ibm_blockchain/assets/miniplatform/winterTile/downTile.png"
        leftOverPath = "assets/miniplatform/winterTile/winterMiddleTile.png"
        iceBoxPath = "assets/miniplatform/winterTile/object/IceBox.png"
        crateBoxPath = "assets/miniplatform/winterTile/object/Crate.png"
        
         # Bottom Platform
        for eachTileX in range(0,1100,50):
            bottomPlatform.add(MiniPlatform(middleTilePath,eachTileX,680))
            bottomPlatform.add (MiniPlatform(leftOverPath,eachTileX,730))
            bottomPlatform.add (MiniPlatform(leftOverPath,eachTileX,770))
        
        
        # Spawn Platform
        for eachTileX in range (0,200,50):
            bottomPlatform.add(MiniPlatform(middleTilePath, eachTileX,530))
            
            bottomPlatform.add(MiniPlatform(middleTilePath, eachTileX,180))
            
        
        # Opposite Side Spawn Platform     
        for eachTileX in range (600,1100,50):
            bottomPlatform.add(MiniPlatform(middleTilePath, eachTileX,530))
        
        # Upper Opposite Side     
        for eachTileX in range (750,1100,50):
            bottomPlatform.add(MiniPlatform(middleTilePath, eachTileX,330))
        
        # Jump Section to Opposite Side Spawn Platform 
        bottomPlatform.add(MiniPlatform(iceBoxPath,550,580))
        bottomPlatform.add(MiniPlatform(iceBoxPath,550,630))
        
        bottomPlatform.add(MiniPlatform(iceBoxPath,500,630))
        
        bottomPlatform.add(MiniPlatform(crateBoxPath,710,630))
        
        # CrateBox on spawn Platform Opposite Side 
        bottomPlatform.add(MiniPlatform(crateBoxPath,650,480))
        bottomPlatform.add(MiniPlatform(crateBoxPath,675,430))
        bottomPlatform.add(MiniPlatform(crateBoxPath,690,380))
        
        
        
        
        bottomPlatform.add(MiniPlatform(crateBoxPath,700,260))
        bottomPlatform.add(MiniPlatform(crateBoxPath,550,260))
        bottomPlatform.add(MiniPlatform(crateBoxPath,400,260))
        bottomPlatform.add(MiniPlatform(crateBoxPath,250,260))
        
           
        bottomPlatform.draw(screen)
        
        
        shrigenPath = "assets/miniplatform/shrigen.png"
        shrigen = pygame.image.load(shrigenPath)
        global SHRIGEN_X 
       
        global VEL_DX
        global VEL_DY
        SHRIGEN_X  = (SHRIGEN_X-VEL_DX)%1024
        # SHRIGEN_Y  = (SHRIGEN_Y+VEL_DY)%800
        
        miniPlayerRect = self.player.getMiniPlayerRect()
        pygame.draw.rect(screen, RED, miniPlayerRect,4) 
        
        
        shrigenRect = shrigen.get_rect(topright=(SHRIGEN_X, 480))
        shrigenRect2 = shrigen.get_rect(topright=(SHRIGEN_X, 280))
        pygame.draw.rect(screen, GREEN, shrigenRect,4)
        screen.blit(shrigen, shrigenRect)
        screen.blit(shrigen, shrigenRect2)
       
       
        crystalPath = "assets/miniplatform/winterTile/object/Crystal.png"
        crystal = pygame.image.load(crystalPath)
        crystal = pygame.transform.scale(crystal,(100,100))
        crystalRect = crystal.get_rect(topleft=(100, 580))
        crystalRect2 = crystal.get_rect(topleft=(900, 485))
        crystalRect3 = crystal.get_rect(topleft=(900, 585))
        crystalRect4 = crystal.get_rect(topleft=(900, 430))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        # screen.blit(crystal, crystalRect)
        screen.blit(crystal,crystalRect3) 
        screen.blit(crystal,crystalRect4) 
       
        
        pygame.mixer.init() 
        automaticReSpawn = pygame.mixer.Sound("assets/miniplatform/winterTile/sound/magicalPowerSound.wav") 
       
       
       
        
        if miniPlayerRect.colliderect(crystalRect3)  or miniPlayerRect.colliderect(crystalRect4):
            # MINI_PLAYER_X -= 10
            automaticReSpawn.play(0)
            MINI_PLAYER_X = 0
            MINI_PLAYER_Y = 530
        
        if shrigenRect.colliderect(miniPlayerRect):
            # MINI_PLAYER_X -= 10
            MINI_PLAYER_X -=10
        
        
         # mini Platform 1 
        # bottomPlatform = pygame.image.load("ibm_blockchain/assets/bottomPlatform.png")
        # bottomPlatform = pygame.transform.scale(bottomPlatform,(1024,120))
        # screen.blit(bottomPlatform,(0,680))
        
        # mediumNPC =  pygame.image.load("ibm_blockchain/assets/mediumNPC.png")
        # mediumNPC = pygame.transform.scale( mediumNPC, (100,100) )
        # screen.blit(mediumNPC,(850,600))  
        
        # mediumNPCPath = "ibm_blockchain/assets/rogerMoore.png"
        # mediumNPC = Npc (screen, "Roger",850, 587, 100, 100, mediumNPCPath)
        # mediumNPC.render()
        
       
       
        # miniNPCRect = mediumNPC.getNpcRect()
        
        
        pygame.mixer.init() 
        portal_sound = pygame.mixer.Sound("assets/background/music/effect/maplestory_portal.mp3") 
        
        hover_sound = pygame.mixer.Sound("assets/background/music/effect/CLICK_009.wav")
       
        # global MEDIUMMODE_NPC_INDEX
        # # global MINI_PLAYER_X
        # # print("BEFORE COMING IN ", TOWN_NPC_DIALOG_INDEX)
        # if miniNPCRect.colliderect(miniPlayerRect) and MEDIUMMODE_NPC_INDEX>=0 :
         
        #     # portal_sound.play()
        #     # PLAYER_X -= 1 
        #     # PLAYER_Y -= 1
        #     filePath = unknownNPCPath
            
        #     dialog1 = "Hey there, have you come here from Dr. Emma Norling? Congratulations! You finally have reached here and completed the game! "
        #     dialog2 = """I'm Roger Moore, the Professor of Spoken Language Processing and Member of the Speech and Hearing (SpandH) research group at the Department of Computer Science. I have gained over 40 years’ experience in Speech Technology R&D and, although an engineer by training, much of my research has been based on insights from human speech perception and production."""
        #     dialog3 = "Since 2004, I have been Professor of Spoken Language Processing at the University of Sheffield, and also holds Visiting Chairs at Bristol Robotics Laboratory and University College London Psychology & Language Sciences.  I was President of the European/International Speech Communication Association from 1997 to 2001, General Chair for INTERSPEECH-2009 and ISCA Distinguished Lecturer during 2014-15.      "
        #     dialog4 = "We are currently working with IBM on Watson Text-To-Speech, especially cooperating with AI Group Project. The University of Sheffield is planning to reach top 1-tier list as Stanford, MIT, and Harvard. "
        #     dialog5 = "This is what I've got to talk with you today. Do you want to go back to Dr. Emma Norling? (Automatically takes you to Dr. Emma Norling! If not, you can still leave with above exit button!)"
        #     exitDialog = "It is said that you are not interested in our research with IBM. Talk to you later. (Emma is keeping push you behind.)"
            
        #     dialogStack = [Dialog(screen, filePath, "Dr. Roger Moore", dialog1, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog2, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog3, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog4, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog5, True, True, False, True, True)
                           
        #                 ]
            
            
        #     dialogStack[MEDIUMMODE_NPC_INDEX].render()
        #     endChatRect =  dialogStack[MEDIUMMODE_NPC_INDEX].drawEndChatButton()
        #     nextChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawNextButton()
        #     prevChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawPrevButton()
        #     yesChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawYesButton()
        #     noChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawNoButton()
        #     dialogStack[MEDIUMMODE_NPC_INDEX].drawNPCFigure()
        #     dialogStack[MEDIUMMODE_NPC_INDEX].drawDialogText()
            
        #     for event in self.events:
        #             if event.type == pygame.MOUSEBUTTONDOWN :
                           
                           
        #                     if endChatRect is not None and endChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         MEDIUMMODE_NPC_INDEX = -1  
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                         hover_sound.play()
        #                         MINI_PLAYER_X -=10
        #                     if nextChatRect is not None and nextChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         print("nextChatRect")
        #                         hover_sound.play()
        #                         MEDIUMMODE_NPC_INDEX +=1 
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                     if prevChatRect is not None and prevChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         print("prevChatRect")
        #                         hover_sound.play()
        #                         MEDIUMMODE_NPC_INDEX -=1
        #                         print(MEDIUMMODE_NPC_INDEX)
                                
        #                     if yesChatRect is not None and yesChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         print("yesChatRect")
        #                         hover_sound.play()
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                         portal_sound.play()
        #                         MINI_PLAYER_X, MINI_PLAYER_Y = 0 ,630
        #                         self.push(HomeNode())
                                
        #                     if  noChatRect is not None and noChatRect.collidepoint(pygame.mouse.get_pos()):  
        #                         print("nochatrect")
        #                         hover_sound.play()
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                         MINI_PLAYER_X -=10
        #                         MEDIUMMODE_NPC_INDEX= -1  
                        
                    
            
            
        #     # self.pop()
        #     # self.push(GameIntroNode())
        # else:    
        #     MEDIUMMODE_NPC_INDEX = 0
        
        
         #Refresh 
        refreshButtonPath = "assets/button/homeIcon.png"
        refreshButton = pygame.image.load(refreshButtonPath)
        refreshButton = pygame.transform.scale(refreshButton,(40,40))
        refreshButtonRect = refreshButton.get_rect(topright=(1024-20, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(refreshButton, refreshButtonRect)
        
         #Refresh 
        returnButtonPath = "assets/button/goBackHomeScreen.png"
        returnButton = pygame.image.load(returnButtonPath)
        returnButton = pygame.transform.scale(returnButton,(40,40))
        returnButtonRect = returnButton.get_rect(topright=(1024-20-40, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(returnButton, returnButtonRect)
        
        #  # LeaderBoard 
        # leaderBoardButtonPath = "ibm_blockchain/assets/Leaderboard.png"
        # leaderBoardButton = pygame.image.load(leaderBoardButtonPath)
        # leaderBoardButton = pygame.transform.scale(leaderBoardButton,(40,40))
        # leaderBoardButtonRect = leaderBoardButton.get_rect(topright=(1024-20-40-40, 20))
        # # pygame.draw.rect(screen, RED, leaderBoardButtonRect,4) 
        # screen.blit(leaderBoardButton, leaderBoardButtonRect)
        
        
        # bottomPlatform = pygame.sprite.Group()
        # leftCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/leftCorner.png"
        # middleTilePath = "ibm_blockchain/assets/miniplatform/winterTile/middleTile.png"
        # rightCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/rightCorner.png"
        # downTilePath = "ibm_blockchain/assets/miniplatform/winterTile/downTile.png"
        # miniPlatform = MiniPlatform(platformPath,0,680) 
        
       
        # for eachTileX in range(0,1100,50):
        #     bottomPlatform.add (MiniPlatform(middleTilePath,eachTileX,750) )
        #     bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,800))
        #     bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,810))
        #     #bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,800))
           
            
        # bottomPlatform.draw(screen)
        collidedPlatform = gravityCheck(self.player,bottomPlatform)
        # print("gravity check = ",len(gravityCheck(self.player,bottomPlatform)))
        
        if len(collidedPlatform) > 0 : 
               print("in!")
               MINI_PLAYER_Y = collidedPlatform[0].rect.top-47
               print("IN =  ", collidedPlatform[0].rect)
        else:
            MINI_PLAYER_Y += 9.8
            
        self.player.update(self.keyPress)
        self.player.draw(screen)
        
        global IS_QUIZ_STARTED,IS_HIGHSCORE_UPDATED, ANSWER_CORRECT_VOICE, ANSWER_WRONG_VOICE, IS_QUIZVOICE_PLAYED_2
        
        if IS_QUIZ_STARTED:
            
            quiz1_content = "Q1. There are 4 types of BlockChain networks."
            quiz2_content = "Q2. Mutable records is the key element of BlockChain."
            quiz3_content = "Q3. Consortium networks is a key element of BlockChain."
            quiz4_content = "Q4. Permissioned Networks is a key element of BlockChain.  "
            quiz5_content = "Q5. Rubbish Thinking in blockchain is an example of use case."
            quiz6_content = "Q6. IBM Blockchain Platform Software is optimized to deploy on Blue Hat® OpenShift®."
            quiz7_content = "Q7. The IBM Blockchain Platform is NOT powered by Hyperledger technology."
            quiz8_content = "Q8. In Blockchain, each transaction is recorded as a block of data"
            quiz9_content = "Q9. In Blockchain, each block is disconnected to the ones before and after it"
            quiz10_content = "Q10. In Blockchain, transactions are blocked together in an reversible chain"
            quiz = Quiz(screen, 80, 80, quiz1_content,True)
            
            global QUIZ_INDEX
            
            quizStack = [Quiz(screen, 80, 80, quiz1_content,True),Quiz(screen, 80, 80, quiz2_content,False),
                         Quiz(screen, 80, 80, quiz3_content,True), Quiz(screen, 80, 80, quiz4_content,True),
                         Quiz(screen, 80, 80, quiz5_content,False),Quiz(screen, 80, 80, quiz6_content,False),
                         Quiz(screen, 80, 80, quiz7_content,False), Quiz(screen, 80, 80, quiz8_content,True),
                         Quiz(screen, 80, 80, quiz9_content,False) , Quiz(screen, 80, 80, quiz10_content,False) ]
        
            if QUIZ_INDEX is len(quizStack):
                if not IS_HIGHSCORE_UPDATED:
                    Sqlite().updateHighScore(3,SCORE) # ID TO UPDATE 
                    IS_HIGHSCORE_UPDATED = True 
                IS_QUIZ_STARTED = False 
                SCORE = 0
                pass
                # print("Dialogue")
                
            else:
                quizStack[QUIZ_INDEX].render()
                if IS_QUIZVOICE_PLAYED_2[QUIZ_INDEX] :
                    IS_QUIZVOICE_PLAYED_2[QUIZ_INDEX] = False 
                    quizVoice[QUIZ_INDEX].play()
                
                for event in self.events: 
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # Home Exit 
                        if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
                            # self.push(HomeNode()) 
                            print(quiz.checkAnswer(True))
                           
                            if quizStack[QUIZ_INDEX].checkAnswer(True):
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_CORRECT_VOICE.play()
                                SCORE += SCORE_INCREMENT*2
                                QUIZ_INDEX +=1
                                # quizStack[QUIZ_INDEX].render()
                            else:
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_WRONG_VOICE.play()
                                QUIZ_INDEX+=1
                        
                        elif (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
                            # self.push(GameIntroNode()) 
                            print(quiz.checkAnswer(False)) 
                            if quizStack[QUIZ_INDEX].checkAnswer(False):
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_CORRECT_VOICE.play()
                                SCORE += SCORE_INCREMENT*2
                                QUIZ_INDEX +=1
                            else:
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_WRONG_VOICE.play()
                                QUIZ_INDEX+=1 
                            
        
        
        
        
        
        unknownNPCRect = unknownNPC.getNpcRect()
        unknownQuizNPC(screen, self.events, self.keyPress,unknownNPCPath ,unknownNPCRect,miniPlayerRect)
        
        # global IS_QUIZ_STARTED
        # if IS_QUIZ_STARTED:
            
        #     quiz1_content = "Q1. Which of the following is IBM BlockChain?"
        #     quiz2_content = "Q2. Which of the following is IBM BlockChain?"
        #     quiz = Quiz(screen, 80, 80, quiz1_content,True)
            
        #     global QUIZ_INDEX
            
        #     quizStack = [Quiz(screen, 80, 80, quiz1_content,True),Quiz(screen, 80, 80, quiz2_content,True)]
        
        #     if QUIZ_INDEX is len(quizStack):
        #         IS_QUIZ_STARTED = False 
        #         pass
        #         # print("Dialogue")
                
        #     else:
        #         quizStack[QUIZ_INDEX].render()
        #         for event in self.events: 
        #             if event.type == pygame.MOUSEBUTTONDOWN :
        #                 mouse_x, mouse_y = pygame.mouse.get_pos()
        #                 # Home Exit 
        #                 if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
        #                     # self.push(HomeNode()) 
        #                     print(quiz.checkAnswer(True))
        #                     if quiz.checkAnswer(True):
                            
        #                         SCORE += SCORE_INCREMENT
        #                         QUIZ_INDEX +=1
        #                         # quizStack[QUIZ_INDEX].render()
                        
        #                 if (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
        #                     # self.push(GameIntroNode()) 
        #                     print(quiz.checkAnswer(False)) 
        #                     if quiz.checkAnswer(False):
                            
        #                         SCORE += SCORE_INCREMENT 
        #                         QUIZ_INDEX +=1
        
        global USER_ID 
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(USER_ID)
        else: 
            pass   
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(USER_ID)
        else: 
            pass     
        
        sign_directory = "assets/font/Satisfy-Regular.ttf"
        sign_font = pygame.font.Font(sign_directory, 20)
        authorSignature = sign_font.render('Kyungtae Han', True, BLACK)
        screen.blit(authorSignature, (900, 750))
        
        #  # Name Tag
        # pygame.draw.rect(screen, (51,51,51), pygame.Rect(760, 687, 250, 43), border_radius = 10 )
        
        # LIGHT_GREEN = (234,230,70)
        # ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 12)
        # answer1_content = "Dr. Roger Moore"
        # answer1 =  ANSWER_FONT.render(answer1_content, True, LIGHT_GREEN)
        # screen.blit(answer1,(790, 707))


IS_KINGVOICE_PLAYED = [True,True,True,True,True] 
kingNPCDialogVoice = [pygame.mixer.Sound("assets/npc/npcVoice/theKing/theKingDialog1.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/theKing/theKingDialog2.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/theKing/theKingDialog3.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/theKing/theKingDialog4.wav"),
                              pygame.mixer.Sound("assets/npc/npcVoice/theKing/theKingDialog5.wav")]
IS_SPACEBAR_PRESSED_3 = False   
        
class HardModeNode(SceneStack):
    def __init__(self):
        SceneStack.__init__(self)
        #self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
        #self.character = pygame.transform.scale( self.character, (40,40) )
        #x,y = 200,400
        #VELOCITY = 8
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/QueensGarden.mp3") 
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)
        
    def ProcessInput(self, events, pressed_keys):
        self.keyPress = pressed_keys
        self.events = events
        global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_ACHIEVEMENT_OPEN
        global OPEN_STATS_VOICE, OPEN_LEADERBOARD_VOICE, CLOSE_STATS_VOICE, CLOSE_LEADERBOARD_VOICE, OPEN_ACHIEVEMENT_VOICE, CLOSE_ACHIEVEMENT_VOICE
        
        for event in events: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                # Move to the next scene when the user pressed Enter
                print("yes")
                self.push(GameOverNode())
            if event.type == pygame.KEYDOWN and event.key == K_1:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True 
                    OPEN_LEADERBOARD_VOICE.play()  
                else: 
                    IS_LEADERBOARD_OPEN = False 
                    CLOSE_LEADERBOARD_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_2: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True   
                    OPEN_STATS_VOICE.play()
                else: 
                    IS_STATS_OPEN = False 
                    CLOSE_STATS_VOICE.play()
                    
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True  
                    OPEN_ACHIEVEMENT_VOICE.play() 
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False 
                    CLOSE_ACHIEVEMENT_VOICE.play()   
                    #CLOSE_STATS_VOICE.play()     
            
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x, mouse_y = pygame.mouse.get_pos()
                global RETURN_HOME_VOICE, MINIGAME_HOME_VOICE
                # Home Exit 
                if (964<=mouse_x<=1004) and (20 <= mouse_y <= 60) : 
                   # RETURN_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(HomeNode()) 
                if (924<=mouse_x<=964) and (20 <= mouse_y <= 60) : 
                    MINIGAME_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(GameIntroNode())   
                    
    
    def Update(self):
        pass
    
    def Render(self, screen):
         # Field 
        # field = pygame.image.load("ibm_blockchain/assets/field.png")
        # field = pygame.transform.scale( field, (1024,800) )
        # screen.blit(field,(0,0))
        screen.fill(BLACK)
        gameBackground = pygame.image.load("assets/miniplatform/hardmode/background.png")
        gameBackground = pygame.transform.scale(gameBackground,(1024,800))
        screen.blit(gameBackground,(0,0))
        
         # mini Platform 1 
        bottomPlatform = pygame.image.load("assets/miniplatform/bottomPlatform.png")
        bottomPlatform = pygame.transform.scale(bottomPlatform,(1024,120))
        screen.blit(bottomPlatform,(0,680))
        
        global SCORE
        # text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
        # textRect = text.get_rect()
        # textRect.center = (100,20)
        # #SCORE += SCORE_INCREMENT
        # screen.blit(text, textRect)
        
        
        
          
        path = "assets/npc/unknownStar.png"
        hardNPC = Npc (screen, "Unknown Star",900, 588, 100, 100, path)
        hardNPC.render()
        

        
        
         #Refresh 
        refreshButtonPath = "assets/button/homeIcon.png"
        refreshButton = pygame.image.load(refreshButtonPath)
        refreshButton = pygame.transform.scale(refreshButton,(40,40))
        refreshButtonRect = refreshButton.get_rect(topright=(1024-20, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(refreshButton, refreshButtonRect)
        
         #Refresh 
        returnButtonPath = "assets/button/goBackHomeScreen.png"
        returnButton = pygame.image.load(returnButtonPath)
        returnButton = pygame.transform.scale(returnButton,(40,40))
        returnButtonRect = returnButton.get_rect(topright=(1024-20-40, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(returnButton, returnButtonRect)
        
        # # LeaderBoard 
        # leaderBoardButtonPath = "ibm_blockchain/assets/Leaderboard.png"
        # leaderBoardButton = pygame.image.load(leaderBoardButtonPath)
        # leaderBoardButton = pygame.transform.scale(leaderBoardButton,(40,40))
        # leaderBoardButtonRect = leaderBoardButton.get_rect(topright=(1024-20-40-40, 20))
        # # pygame.draw.rect(screen, RED, leaderBoardButtonRect,4) 
        # screen.blit(leaderBoardButton, leaderBoardButtonRect)
        
        global MINI_PLAYER_X 
        global MINI_PLAYER_Y
        
        self.playerPath = "assets/character/right/right1.png"
        self.player = MiniPlayer(self.playerPath, MINI_PLAYER_X, MINI_PLAYER_Y)
        self.player.update(self.keyPress)
        self.player.draw(screen)
        
        hardNPCRect = hardNPC.getNpcRect()
        playerRect = self.player.getMiniPlayerRect()
        
        
        pygame.mixer.init() 
        portal_sound = pygame.mixer.Sound("assets/background/music/effect/maplestory_portal.mp3") 
        
        hover_sound = pygame.mixer.Sound("assets/background/music/effect/CLICK_009.wav")
        
        
        
        global IS_KINGVOICE_PLAYED, kingNPCDialogVoice 
        global HARDMODE_NPC_INDEX, IS_SPACEBAR_PRESSED_3
        
        if hardNPCRect.colliderect(playerRect) and self.keyPress[K_SPACE]:
            IS_SPACEBAR_PRESSED_3 = True    
        
        
        # global MINI_PLAYER_X
        # print("BEFORE COMING IN ", TOWN_NPC_DIALOG_INDEX)
        if hardNPCRect.colliderect(playerRect) and IS_SPACEBAR_PRESSED_3 is True and HARDMODE_NPC_INDEX>=0 :
            if IS_KINGVOICE_PLAYED[HARDMODE_NPC_INDEX] : 
                IS_KINGVOICE_PLAYED[HARDMODE_NPC_INDEX] = False 
                kingNPCDialogVoice[HARDMODE_NPC_INDEX].play()
            
            #sys.path.append("production/blockchain_house/ibm_blockchain/assets/npc/npcVoice/theKing/theKingDialog")
            
            theKingDialog1_txt = open('assets/npc/npcVoice/theKing/theKingDialog/theKingDialog1.txt','r')
            theKingDialog1 = theKingDialog1_txt.read()
            theKingDialog1_txt.close()
            
            theKingDialog2_txt = open('assets/npc/npcVoice/theKing/theKingDialog/theKingDialog2.txt','r')
            theKingDialog2 = theKingDialog2_txt.read()
            theKingDialog2_txt.close()
            
            theKingDialog3_txt = open('assets/npc/npcVoice/theKing/theKingDialog/theKingDialog3.txt','r')
            theKingDialog3 = theKingDialog3_txt.read()
            theKingDialog3_txt.close()
            
            theKingDialog4_txt = open('assets/npc/npcVoice/theKing/theKingDialog/theKingDialog4.txt','r')
            theKingDialog4 = theKingDialog4_txt.read()
            theKingDialog4_txt.close()
            
            theKingDialog5_txt = open('assets/npc/npcVoice/theKing/theKingDialog/theKingDialog5.txt','r')
            theKingDialog5 = theKingDialog5_txt.read()
            theKingDialog5_txt.close()
            
            if len(theKingDialog1) > 590: 
                raise Exception("theKingDialog1 exceeded 590 characters.", len(theKingDialog1))
            if len(theKingDialog2) > 590: 
                raise Exception("theKingDialog2 exceeded 590 characters.", len(theKingDialog2))
            if len(theKingDialog3) > 590: 
                raise Exception("theKingDialog3 exceeded 590 characters.", len(theKingDialog3))
            if len(theKingDialog4) > 590: 
                raise Exception("theKingDialog4 exceeded 590 characters.", len(theKingDialog4))
            if len(theKingDialog5) > 590: 
                raise Exception("theKingDialog5 exceeded 590 characters.", len(theKingDialog5))
            
            
            unknownFilePath = "assets/npc/rightdangerousNPC.png"
            theKingFilePath = "assets/npc/theKing.png"
            
            #dialog1 = "Hey there, have you come here from Dr. Emma Norling? Congratulations! You finally have reached here and completed the game! "
            dialog1 = theKingDialog1
            #dialog2 = """(Spy keeping silence and then start talking...) Is anybody crossing nearby? No? OK. It's time to take off my mask and serve my duty !!!! """
            dialog2 = theKingDialog2 
            #dialog3 = "I'm the King of this IBM BlockChain World, and my duty is to send you to Secret Hidden Map of IBM BlockChain. Are you ready to be there?"
            dialog3 = theKingDialog3 
            #dialog4 = "We, University of Sheffield, are currently working with IBM on Watson Text-To-Speech, especially cooperating with AI Group Project.  "
            dialog4 = theKingDialog4
            #dialog5 = "(Murmuring to you...) I'm gonna hide again. Are you ready to go to Hard Mode of IBM BlockChain Hidden Map? (Click Yes to start.)"
            dialog5 = theKingDialog5 
            exitDialog = "It is said that you are not interested in our research with IBM. Talk to you later. (Emma is keeping push you behind.)"
            
            dialogStack = [Dialog(screen, unknownFilePath, "The Unknown", dialog1, True, False, True, False, False),
                           Dialog(screen, unknownFilePath, "The Unknown", dialog2, True, True, True, False, False),
                           Dialog(screen, theKingFilePath, "The King", dialog3, True, True, True, False, False),
                           Dialog(screen, theKingFilePath, "The King", dialog4, True, True, True, False, False),
                           Dialog(screen, unknownFilePath, "The King", dialog5, True, True, False, True, True)
                           
                        ]
            
            
            dialogStack[HARDMODE_NPC_INDEX].render()
            endChatRect =  dialogStack[HARDMODE_NPC_INDEX].drawEndChatButton()
            nextChatRect = dialogStack[HARDMODE_NPC_INDEX].drawNextButton()
            prevChatRect = dialogStack[HARDMODE_NPC_INDEX].drawPrevButton()
            yesChatRect = dialogStack[HARDMODE_NPC_INDEX].drawYesButton()
            noChatRect = dialogStack[HARDMODE_NPC_INDEX].drawNoButton()
            dialogStack[HARDMODE_NPC_INDEX].drawNPCFigure()
            dialogStack[HARDMODE_NPC_INDEX].drawDialogText()
        
        
            for event in self.events:
                        if event.type == pygame.MOUSEBUTTONDOWN :
                            
                            
                                if endChatRect is not None and endChatRect.collidepoint(pygame.mouse.get_pos()):
                                    kingNPCDialogVoice[HARDMODE_NPC_INDEX].stop()
                                    HARDMODE_NPC_INDEX= 0 
                                    #print(EASYMODE_NPC_INDEX)
                                    hover_sound.play()
                                    IS_SPACEBAR_PRESSED_3 = False  
                                    #MINI_PLAYER_X -=10
                                if nextChatRect is not None and nextChatRect.collidepoint(pygame.mouse.get_pos()):
                                    #print("nextChatRect")
                                    hover_sound.play()
                                    kingNPCDialogVoice[HARDMODE_NPC_INDEX].stop()
                                    HARDMODE_NPC_INDEX +=1 
                                    IS_KINGVOICE_PLAYED[HARDMODE_NPC_INDEX] = True
                                    #print(EASYMODE_NPC_INDEX)
                                if prevChatRect is not None and prevChatRect.collidepoint(pygame.mouse.get_pos()):
                                    #print("prevChatRect")
                                    hover_sound.play()
                                    kingNPCDialogVoice[HARDMODE_NPC_INDEX].stop()
                                    HARDMODE_NPC_INDEX -=1
                                    IS_KINGVOICE_PLAYED[HARDMODE_NPC_INDEX] = True
                                    #print(EASYMODE_NPC_INDEX)
                                    
                                if yesChatRect is not None and yesChatRect.collidepoint(pygame.mouse.get_pos()):
                                    #print("yesChatRect")
                                    kingNPCDialogVoice[HARDMODE_NPC_INDEX].stop()
                                    hover_sound.play()
                                    #print(EASYMODE_NPC_INDEX)
                                    portal_sound.play()
                                    IS_SPACEBAR_PRESSED_3 = False  
                                    MINI_PLAYER_X, MINI_PLAYER_Y = 0 ,630
                                    self.push(SecretPortalHardNode1())
                                    
                                if  noChatRect is not None and noChatRect.collidepoint(pygame.mouse.get_pos()):  
                                    kingNPCDialogVoice[HARDMODE_NPC_INDEX].stop()
                                    #print("nochatrect")
                                    hover_sound.play()
                                    #print(EASYMODE_NPC_INDEX)
                                    #MINI_PLAYER_X -=10
                                    HARDMODE_NPC_INDEX= 0 
                                    IS_SPACEBAR_PRESSED_3 = False  
                            
                    
            
            
            # self.pop()
            # self.push(GameIntroNode())
        else:    
            IS_SPACEBAR_PRESSED_3 = False  
            IS_KINGVOICE_PLAYED[HARDMODE_NPC_INDEX] = True 
            kingNPCDialogVoice[HARDMODE_NPC_INDEX].stop()
            HARDMODE_NPC_INDEX = 0
        
        
        global USER_ID    
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(USER_ID)
        else: 
            pass
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(USER_ID)
        else: 
            pass
        
        
        sign_directory = "assets/font/Satisfy-Regular.ttf"
        sign_font = pygame.font.Font(sign_directory, 20)
        authorSignature = sign_font.render('Kyungtae Han', True, BLACK)
        screen.blit(authorSignature, (900, 750))
        # hardNPC =  pygame.image.load("ibm_blockchain/assets/hardnpc.png")
        # hardNPC = pygame.transform.scale( hardNPC, (250,200) )
        # screen.blit(hardNPC,(750,500)) 
        # quiz1_content = "Q1. Which of the following is IBM BlockChain?"
        # quiz2_content = "Q2. Which of the following is IBM BlockChain?"
        # quiz = Quiz(screen, 80, 80, quiz1_content,True)
        
        # global QUIZ_INDEX
        # quizStack = [Quiz(screen, 80, 80, quiz1_content,True),Quiz(screen, 80, 80, quiz2_content,True)]
       
        # if QUIZ_INDEX is len(quizStack):
        #     pass
        #     # print("Dialogue")
            
        # else:
        #     quizStack[QUIZ_INDEX].render()
        #     for event in self.events: 
        #         if event.type == pygame.MOUSEBUTTONDOWN :
        #             mouse_x, mouse_y = pygame.mouse.get_pos()
        #             # Home Exit 
        #             if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
        #                 # self.push(HomeNode()) 
        #                 print(quiz.checkAnswer(True))
        #                 if quiz.checkAnswer(True):
                        
        #                     SCORE += SCORE_INCREMENT
        #                     QUIZ_INDEX +=1
        #                     # quizStack[QUIZ_INDEX].render()
                    
        #             if (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
        #                 # self.push(GameIntroNode()) 
        #                 print(quiz.checkAnswer(False)) 
        #                 if quiz.checkAnswer(False):
                        
        #                     SCORE += SCORE_INCREMENT 
        #                     QUIZ_INDEX +=1
                            # quizStack[QUIZ_INDEX].render()
            
# class SecretPortalHardNode(SceneStack):
#     def __init__(self):
#         SceneStack.__init__(self)
#         self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
#         self.character = pygame.transform.scale( self.character, (40,40) )
#         x,y = 200,400
#         VELOCITY = 8
#         pygame.mixer.init() 
#         pygame.mixer.music.load("ibm_blockchain/assets/QueensGarden.mp3") 
#         pygame.mixer.music.play(-1,0.0)
        
#     def ProcessInput(self, events, pressed_keys):
#         self.keyPress = pressed_keys
#         for event in events: 
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
#                 # Move to the next scene when the user pressed Enter
#                 print("yes")
#                 self.push(GameOverNode())
                
#             if event.type == pygame.MOUSEBUTTONDOWN :
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Home Exit 
#                 if (964<=mouse_x<=1004) and (20 <= mouse_y <= 60) : 
#                     self.push(HomeNode()) 
#                 if (924<=mouse_x<=964) and (20 <= mouse_y <= 60) : 
#                     self.push(GameIntroNode())   
                    
    
#     def Update(self):
#         pass
    
#     def Render(self, screen):
#          # Field 
#         # field = pygame.image.load("ibm_blockchain/assets/field.png")
#         # field = pygame.transform.scale( field, (1024,800) )
#         # screen.blit(field,(0,0))
#         screen.fill(BLACK)
#         gameBackground = pygame.image.load("ibm_blockchain/assets/miniplatform/hardmode/background.png")
#         gameBackground = pygame.transform.scale(gameBackground,(1024,800))
#         screen.blit(gameBackground,(0,0))
        
#          # mini Platform 1 
#         # bottomPlatform = pygame.image.load("ibm_blockchain/assets/bottomPlatform.png")
#         # bottomPlatform = pygame.transform.scale(bottomPlatform,(1024,120))
#         # screen.blit(bottomPlatform,(0,680))
        
#         global SCORE
#         text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
#         textRect = text.get_rect()
#         textRect.center = (100,20)
#         #SCORE += SCORE_INCREMENT
#         screen.blit(text, textRect)
        
        
        
          
#         # path = "ibm_blockchain/assets/npc/unknownStar.png"
#         # hardNPC = Npc (screen, "Unknown Star",900, 588, 100, 100, path)
#         # hardNPC.render()
        
#          #Refresh 
#         refreshButtonPath = "ibm_blockchain/assets/homeIcon.png"
#         refreshButton = pygame.image.load(refreshButtonPath)
#         refreshButton = pygame.transform.scale(refreshButton,(40,40))
#         refreshButtonRect = refreshButton.get_rect(topright=(1024-20, 20))
#         # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
#         screen.blit(refreshButton, refreshButtonRect)
        
#          #Refresh 
#         returnButtonPath = "ibm_blockchain/assets/goBackHomeScreen.png"
#         returnButton = pygame.image.load(returnButtonPath)
#         returnButton = pygame.transform.scale(returnButton,(40,40))
#         returnButtonRect = returnButton.get_rect(topright=(1024-20-40, 20))
#         # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
#         screen.blit(returnButton, returnButtonRect)
        
#         # LeaderBoard 
#         leaderBoardButtonPath = "ibm_blockchain/assets/Leaderboard.png"
#         leaderBoardButton = pygame.image.load(leaderBoardButtonPath)
#         leaderBoardButton = pygame.transform.scale(leaderBoardButton,(40,40))
#         leaderBoardButtonRect = leaderBoardButton.get_rect(topright=(1024-20-40-40, 20))
#         # pygame.draw.rect(screen, RED, leaderBoardButtonRect,4) 
#         screen.blit(leaderBoardButton, leaderBoardButtonRect)
        
        
     
        
#         bottomPlatform = pygame.sprite.Group()
#         autumnTilePath = "ibm_blockchain/assets/miniplatform/winterTile/middleTile.png"
       
        
#          # Bottom Platform
#         for eachTileX in range(0,1100,50):
#             bottomPlatform.add(MiniPlatform(autumnTilePath,eachTileX,680))
#             bottomPlatform.add (MiniPlatform(autumnTilePath,eachTileX,730))
#             bottomPlatform.add (MiniPlatform(autumnTilePath,eachTileX,770))
        
#         bottomPlatform.draw(screen)
        
#         global MINI_PLAYER_X, MINI_PLAYER_Y
#         self.playerPath = "ibm_blockchain/assets/character/right/right1.png"
#         self.player = MiniPlayer(self.playerPath, MINI_PLAYER_X, MINI_PLAYER_Y)
      
        
        
#         collidedPlatform = gravityCheck(self.player,bottomPlatform)
#         # print("gravity check = ",len(gravityCheck(self.player,bottomPlatform)))
        
#         if len(collidedPlatform) > 0 : 
#                print("in!")
#                MINI_PLAYER_Y = collidedPlatform[0].rect.top-47
#                print("IN =  ", collidedPlatform[0].rect)
#         else:
#             MINI_PLAYER_Y += 9.8
        
        
       
        
#         # hardNPC =  pygame.image.load("ibm_blockchain/assets/hardnpc.png")
#         # hardNPC = pygame.transform.scale( hardNPC, (250,200) )
#         # screen.blit(hardNPC,(750,500)) 
#         self.player.update(self.keyPress)
#         self.player.draw(screen)


HARD_HIDDEN_WELCOME_VOICE = pygame.mixer.Sound("assets/npc/npcVoice/theKing/hardHiddenWelcome.wav")

class SecretPortalHardNode1(SceneStack):
    def __init__(self):
        SceneStack.__init__(self)
        #self.character =  pygame.image.load("ibm_blockchain/assets/ship.png")
        #self.character = pygame.transform.scale( self.character, (40,40) )
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/QueensGarden.mp3") 
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)
        
        global HARD_HIDDEN_WELCOME_VOICE 
        HARD_HIDDEN_WELCOME_VOICE.play()
        HARD_HIDDEN_WELCOME_VOICE.set_volume(1.0)
        
        #x,y = 200,400
        #VELOCITY = 8
        
    def ProcessInput(self, events, pressed_keys):
        self.keyPress = pressed_keys
        self.events = events
        
        global MINI_PLAYER_X, MINI_PLAYER_Y
        global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_ACHIEVEMENT_OPEN 
        global OPEN_STATS_VOICE, OPEN_LEADERBOARD_VOICE, CLOSE_STATS_VOICE, CLOSE_LEADERBOARD_VOICE, OPEN_ACHIEVEMENT_VOICE, CLOSE_ACHIEVEMENT_VOICE
        
        for event in events: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                # Move to the next scene when the user pressed Enter
                print("yes")
                self.push(GameOverNode())
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                MINI_PLAYER_Y -= 30     
            
            if event.type == pygame.KEYDOWN and event.key == K_1:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True   
                    OPEN_LEADERBOARD_VOICE.play()
                else: 
                    IS_LEADERBOARD_OPEN = False 
                    CLOSE_LEADERBOARD_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_2: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True   
                    OPEN_STATS_VOICE.play()
                else: 
                    IS_STATS_OPEN = False 
                    CLOSE_STATS_VOICE.play()
            
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True 
                    OPEN_ACHIEVEMENT_VOICE.play()  
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False 
                    CLOSE_ACHIEVEMENT_VOICE.play()   
                    #CLOSE_STATS_VOICE.play()     
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x, mouse_y = pygame.mouse.get_pos()
                global RETURN_HOME_VOICE, MINIGAME_HOME_VOICE
                # Home Exit 
                if (964<=mouse_x<=1004) and (20 <= mouse_y <= 60) :
                    #RETURN_HOME_VOICE.play() 
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(HomeNode())  
                if (924<=mouse_x<=964) and (20 <= mouse_y <= 60) : 
                    MINIGAME_HOME_VOICE.play()
                    MINI_PLAYER_X = 0
                    MINI_PLAYER_Y = 630
                    self.push(GameIntroNode())      
    
    def Update(self):
        pass
    
    def Render(self, screen):
         # Field 
        gameBackground = pygame.image.load("assets/miniplatform/hardmode/background.png")
        gameBackground = pygame.transform.scale(gameBackground,(1024,800))
        screen.blit(gameBackground,(0,0))
        
        global SCORE
        # text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
        # textRect = text.get_rect()
        # textRect.center = (100,20)
        # #SCORE += SCORE_INCREMENT
        # screen.blit(text, textRect)
        scoreBoard = ScoreBoard(screen, SCORE, 10, 10)
        scoreBoard.render()
        
        global MINI_PLAYER_X 
        global MINI_PLAYER_Y
         
        self.playerPath = "assets/character/right/right1.png"
        self.player = MiniPlayer(self.playerPath, MINI_PLAYER_X, MINI_PLAYER_Y)
        
        unknownNPCPath = "assets/npc/leftdangerousNPC.png"
        unknownNPC = Npc (screen, "Juliet", 100, 90, 100, 100, unknownNPCPath)
        unknownNPC.render()
        
        # self.player.update(self.keyPress)
        # self.player.draw(screen)
        
        bottomPlatform = pygame.sprite.Group()
        autumnTile1Path = "assets/miniplatform/hardmode/autumnTile1.png"
        autumnTile2Path = "assets/miniplatform/hardmode/autumnTile2.png"
        crateBoxPath = "assets/miniplatform/winterTile/object/Crate.png"
        
         # Bottom Platform
        for eachTileX in range(0,1100,50):
            bottomPlatform.add(MiniPlatform(autumnTile1Path,eachTileX,680))
            bottomPlatform.add (MiniPlatform(autumnTile2Path,eachTileX,730))
            bottomPlatform.add (MiniPlatform(autumnTile2Path,eachTileX,770))
        
        
        # Spawn Platform
        for eachTileX in range (0,300,50):
            bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,530))
            bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,330))
            
            bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,180))
        
        bottomPlatform.add(MiniPlatform(crateBoxPath,300,580))
        bottomPlatform.add(MiniPlatform(crateBoxPath,350,630))
        
        
        # for eachTileX in range (0,200,50):
        #     bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,430))
            
            # bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,180))
            
        
        # Opposite Side Spawn Platform     
        for eachTileX in range (750,1100,50):
            bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,530))
            bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,330))
            bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,180))
        
        bottomPlatform.add(MiniPlatform(crateBoxPath,700,580))
        bottomPlatform.add(MiniPlatform(crateBoxPath,650,630))
        
        bottomPlatform.add(MiniPlatform(crateBoxPath,600,530))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,500,530))
        bottomPlatform.add(MiniPlatform(crateBoxPath,400,530))
        
        bottomPlatform.add(MiniPlatform(crateBoxPath,600,330))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,500,530))
        bottomPlatform.add(MiniPlatform(crateBoxPath,400,330))
        
        bottomPlatform.add(MiniPlatform(crateBoxPath,600,180))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,500,530))
        bottomPlatform.add(MiniPlatform(crateBoxPath,400,180))
        
        
        
        # Upper Opposite Side     
        # for eachTileX in range (750,1100,50):
        #     bottomPlatform.add(MiniPlatform(autumnTile1Path, eachTileX,330))
        
        # # Jump Section to Opposite Side Spawn Platform 
        # bottomPlatform.add(MiniPlatform(iceBoxPath,550,580))
        # bottomPlatform.add(MiniPlatform(iceBoxPath,550,630))
        
        # bottomPlatform.add(MiniPlatform(iceBoxPath,500,630))
        
        # bottomPlatform.add(MiniPlatform(crateBoxPath,710,630))
        
        # # CrateBox on spawn Platform Opposite Side 
        # bottomPlatform.add(MiniPlatform(crateBoxPath,650,480))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,675,430))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,690,380))
        
        
        
        
        # bottomPlatform.add(MiniPlatform(crateBoxPath,700,260))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,550,260))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,400,260))
        # bottomPlatform.add(MiniPlatform(crateBoxPath,250,260))
        
           
        bottomPlatform.draw(screen)
        
        
        shrigenPath = "assets/miniplatform/shrigen.png"
        shrigen = pygame.image.load(shrigenPath)
        global SHRIGEN_X 
       
        global VEL_DX
        global VEL_DY
        velDx = 30
        SHRIGEN_X  = (SHRIGEN_X-velDx)%1024
        # SHRIGEN_Y  = (SHRIGEN_Y+VEL_DY)%800
        
        miniPlayerRect = self.player.getMiniPlayerRect()
        #pygame.draw.rect(screen, RED, miniPlayerRect,4) 
        
        
        shrigenRect = shrigen.get_rect(topright=(SHRIGEN_X, 480))
        shrigenRect2 = shrigen.get_rect(topright=(SHRIGEN_X, 280))
        shrigenRect3 = shrigen.get_rect(topright= (SHRIGEN_X,130))
        #pygame.draw.rect(screen, GREEN, shrigenRect,4)
        screen.blit(shrigen, shrigenRect)
        screen.blit(shrigen, shrigenRect2)
        #screen.blit(shrigen,shrigenRect3)
       
       
        crystalPath = "assets/miniplatform/winterTile/object/Crystal.png"
        crystal = pygame.image.load(crystalPath)
        crystal = pygame.transform.scale(crystal,(100,100))
        crystalRect = crystal.get_rect(topleft=(100, 580))
        crystalRect2 = crystal.get_rect(topleft=(900, 485))
        crystalRect3 = crystal.get_rect(topleft=(900, 585))
        crystalRect4 = crystal.get_rect(topleft=(900, 430))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        # screen.blit(crystal, crystalRect)
        screen.blit(crystal,crystalRect3) 
        screen.blit(crystal,crystalRect4) 
       
        path = "assets/npc/leftdangerousNPC.png"
        path2 = "assets/npc/rightdangerousNPC.png"
        
        hardNPC = Npc (screen, "Unknown Star",100, 440, 100, 100, path)
        hardNPC.render() 
        unknownNPCRect1 = hardNPC.getNpcRect()
        
        hardNPC1 = Npc (screen, "Unknown Star",100, 240, 100, 100, path)
        hardNPC1.render() 
        unknownNPCRect2 = hardNPC1.getNpcRect()
        
        hardNPC2 = Npc (screen, "Unknown Star",830, 240, 100, 100, path2)
        hardNPC2.render() 
        unknownNPCRect3 = hardNPC2.getNpcRect()
        
        hardNPC3 = Npc (screen, "Unknown Star",830, 440, 100, 100, path2)
        hardNPC3.render() 
        unknownNPCRect4 = hardNPC3.getNpcRect()
        
        hardNPC4 = Npc (screen, "Unknown Star",830, 90, 100, 100, path2)
        hardNPC4.render()
        unknownNPCRect5 = hardNPC4.getNpcRect()
        
        pygame.mixer.init() 
        automaticReSpawn = pygame.mixer.Sound("assets/miniplatform/winterTile/sound/magicalPowerSound.wav") 
       
        
       
        
        if miniPlayerRect.colliderect(crystalRect3)  or miniPlayerRect.colliderect(crystalRect4):
            # MINI_PLAYER_X -= 10
            automaticReSpawn.play(0)
            MINI_PLAYER_X = 100
            MINI_PLAYER_Y = 240
        
        if miniPlayerRect.colliderect(unknownNPCRect1) or miniPlayerRect.colliderect(unknownNPCRect2) or miniPlayerRect.colliderect(unknownNPCRect3) or miniPlayerRect.colliderect(unknownNPCRect4) or miniPlayerRect.colliderect(unknownNPCRect5) or shrigenRect2.colliderect(miniPlayerRect)  :  
            automaticReSpawn.play(0)
            MINI_PLAYER_X = 512
            MINI_PLAYER_Y = 400
                
        #or shrigenRect3.colliderect(miniPlayerRect)
        if shrigenRect.colliderect(miniPlayerRect) or shrigenRect3.colliderect(miniPlayerRect):
            # MINI_PLAYER_X -= 10
            MINI_PLAYER_X -= 20 
        
        
         # mini Platform 1 
        # bottomPlatform = pygame.image.load("ibm_blockchain/assets/bottomPlatform.png")
        # bottomPlatform = pygame.transform.scale(bottomPlatform,(1024,120))
        # screen.blit(bottomPlatform,(0,680))
        
        # mediumNPC =  pygame.image.load("ibm_blockchain/assets/mediumNPC.png")
        # mediumNPC = pygame.transform.scale( mediumNPC, (100,100) )
        # screen.blit(mediumNPC,(850,600))  
        
        # mediumNPCPath = "ibm_blockchain/assets/rogerMoore.png"
        # mediumNPC = Npc (screen, "Roger",850, 587, 100, 100, mediumNPCPath)
        # mediumNPC.render()
        
       
       
        # miniNPCRect = mediumNPC.getNpcRect()
        
        
        pygame.mixer.init() 
        #portal_sound = pygame.mixer.Sound("ibm_blockchain/assets/maplestory_portal.mp3") 
        
        #hover_sound = pygame.mixer.Sound("ibm_blockchain/assets/CLICK_009.wav")
        sign_directory = "assets/font/Satisfy-Regular.ttf"
        sign_font = pygame.font.Font(sign_directory, 20)
        authorSignature = sign_font.render('Kyungtae Han', True, BLACK)
        screen.blit(authorSignature, (900, 750))
        # global MEDIUMMODE_NPC_INDEX
        # # global MINI_PLAYER_X
        # # print("BEFORE COMING IN ", TOWN_NPC_DIALOG_INDEX)
        # if miniNPCRect.colliderect(miniPlayerRect) and MEDIUMMODE_NPC_INDEX>=0 :
         
        #     # portal_sound.play()
        #     # PLAYER_X -= 1 
        #     # PLAYER_Y -= 1
        #     filePath = mediumNPCPath
            
        #     dialog1 = "Hey there, have you come here from Dr. Emma Norling? Congratulations! You finally have reached here and completed the game! "
        #     dialog2 = """I'm Roger Moore, the Professor of Spoken Language Processing and Member of the Speech and Hearing (SpandH) research group at the Department of Computer Science. I have gained over 40 years’ experience in Speech Technology R&D and, although an engineer by training, much of my research has been based on insights from human speech perception and production."""
        #     dialog3 = "Since 2004, I have been Professor of Spoken Language Processing at the University of Sheffield, and also holds Visiting Chairs at Bristol Robotics Laboratory and University College London Psychology & Language Sciences.  I was President of the European/International Speech Communication Association from 1997 to 2001, General Chair for INTERSPEECH-2009 and ISCA Distinguished Lecturer during 2014-15.      "
        #     dialog4 = "We are currently working with IBM on Watson Text-To-Speech, especially cooperating with AI Group Project. The University of Sheffield is planning to reach top 1-tier list as Stanford, MIT, and Harvard. "
        #     dialog5 = "This is what I've got to talk with you today. Do you want to go back to Dr. Emma Norling? (Automatically takes you to Dr. Emma Norling! If not, you can still leave with above exit button!)"
        #     exitDialog = "It is said that you are not interested in our research with IBM. Talk to you later. (Emma is keeping push you behind.)"
            
        #     dialogStack = [Dialog(screen, filePath, "Dr. Roger Moore", dialog1, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog2, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog3, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog4, True, True, True, False, False),
        #                    Dialog(screen, filePath, "Dr. Roger Moore", dialog5, True, True, False, True, True)
                           
        #                 ]
            
            
        #     dialogStack[MEDIUMMODE_NPC_INDEX].render()
        #     endChatRect =  dialogStack[MEDIUMMODE_NPC_INDEX].drawEndChatButton()
        #     nextChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawNextButton()
        #     prevChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawPrevButton()
        #     yesChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawYesButton()
        #     noChatRect = dialogStack[MEDIUMMODE_NPC_INDEX].drawNoButton()
        #     dialogStack[MEDIUMMODE_NPC_INDEX].drawNPCFigure()
        #     dialogStack[MEDIUMMODE_NPC_INDEX].drawDialogText()
            
        #     for event in self.events:
        #             if event.type == pygame.MOUSEBUTTONDOWN :
                           
                           
        #                     if endChatRect is not None and endChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         MEDIUMMODE_NPC_INDEX = -1  
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                         hover_sound.play()
        #                         MINI_PLAYER_X -=10
        #                     if nextChatRect is not None and nextChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         print("nextChatRect")
        #                         hover_sound.play()
        #                         MEDIUMMODE_NPC_INDEX +=1 
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                     if prevChatRect is not None and prevChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         print("prevChatRect")
        #                         hover_sound.play()
        #                         MEDIUMMODE_NPC_INDEX -=1
        #                         print(MEDIUMMODE_NPC_INDEX)
                                
        #                     if yesChatRect is not None and yesChatRect.collidepoint(pygame.mouse.get_pos()):
        #                         print("yesChatRect")
        #                         hover_sound.play()
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                         portal_sound.play()
        #                         MINI_PLAYER_X, MINI_PLAYER_Y = 0 ,630
        #                         self.push(HomeNode())
                                
        #                     if  noChatRect is not None and noChatRect.collidepoint(pygame.mouse.get_pos()):  
        #                         print("nochatrect")
        #                         hover_sound.play()
        #                         print(MEDIUMMODE_NPC_INDEX)
        #                         MINI_PLAYER_X -=10
        #                         MEDIUMMODE_NPC_INDEX= -1  
                        
                    
            
            
        #     # self.pop()
        #     # self.push(GameIntroNode())
        # else:    
        #     MEDIUMMODE_NPC_INDEX = 0
        
        
         #Refresh 
        refreshButtonPath = "assets/button/homeIcon.png"
        refreshButton = pygame.image.load(refreshButtonPath)
        refreshButton = pygame.transform.scale(refreshButton,(40,40))
        refreshButtonRect = refreshButton.get_rect(topright=(1024-20, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(refreshButton, refreshButtonRect)
        
         #Refresh 
        returnButtonPath = "assets/button/goBackHomeScreen.png"
        returnButton = pygame.image.load(returnButtonPath)
        returnButton = pygame.transform.scale(returnButton,(40,40))
        returnButtonRect = returnButton.get_rect(topright=(1024-20-40, 20))
        # pygame.draw.rect(screen, RED, refreshButtonRect,4) 
        screen.blit(returnButton, returnButtonRect)
        
        #  # LeaderBoard 
        # leaderBoardButtonPath = "ibm_blockchain/assets/Leaderboard.png"
        # leaderBoardButton = pygame.image.load(leaderBoardButtonPath)
        # leaderBoardButton = pygame.transform.scale(leaderBoardButton,(40,40))
        # leaderBoardButtonRect = leaderBoardButton.get_rect(topright=(1024-20-40-40, 20))
        # # pygame.draw.rect(screen, RED, leaderBoardButtonRect,4) 
        # screen.blit(leaderBoardButton, leaderBoardButtonRect)
        
        
        # bottomPlatform = pygame.sprite.Group()
        # leftCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/leftCorner.png"
        # middleTilePath = "ibm_blockchain/assets/miniplatform/winterTile/middleTile.png"
        # rightCornerPath = "ibm_blockchain/assets/miniplatform/winterTile/rightCorner.png"
        # downTilePath = "ibm_blockchain/assets/miniplatform/winterTile/downTile.png"
        # miniPlatform = MiniPlatform(platformPath,0,680) 
        
       
        # for eachTileX in range(0,1100,50):
        #     bottomPlatform.add (MiniPlatform(middleTilePath,eachTileX,750) )
        #     bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,800))
        #     bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,810))
        #     #bottomPlatform.add (MiniPlatform(downTilePath,eachTileX,800))
           
            
        # bottomPlatform.draw(screen)
        collidedPlatform = gravityCheck(self.player,bottomPlatform)
        # print("gravity check = ",len(gravityCheck(self.player,bottomPlatform)))
        
        if len(collidedPlatform) > 0 : 
               print("in!")
               MINI_PLAYER_Y = collidedPlatform[0].rect.top-47
               print("IN =  ", collidedPlatform[0].rect)
        else:
            MINI_PLAYER_Y += 9.8
        
        global VELOCITY 
        VELOCITY = 4
            
        self.player.update(self.keyPress)
        self.player.draw(screen)
        
        global IS_QUIZ_STARTED,IS_HIGHSCORE_UPDATED, IS_QUIZVOICE_PLAYED_3, quizVoice, ANSWER_CORRECT_VOICE, ANSWER_WRONG_VOICE 
        
        if IS_QUIZ_STARTED:
            
            quiz1_content = "Q1. There are 4 types of BlockChain networks."
            quiz2_content = "Q2. Mutable records is the key element of BlockChain."
            quiz3_content = "Q3. Consortium networks is a key element of BlockChain."
            quiz4_content = "Q4. Permissioned Networks is a key element of BlockChain.  "
            quiz5_content = "Q5. Rubbish Thinking in blockchain is an example of use case."
            quiz6_content = "Q6. IBM Blockchain Platform Software is optimized to deploy on Blue Hat® OpenShift®."
            quiz7_content = "Q7. The IBM Blockchain Platform is NOT powered by Hyperledger technology."
            quiz8_content = "Q8. In Blockchain, each transaction is recorded as a block of data"
            quiz9_content = "Q9. In Blockchain, each block is disconnected to the ones before and after it"
            quiz10_content = "Q10. In Blockchain, transactions are blocked together in an reversible chain"
            quiz = Quiz(screen, 80, 80, quiz1_content,True)
            
            global QUIZ_INDEX
            
            quizStack = [Quiz(screen, 80, 80, quiz1_content,True),Quiz(screen, 80, 80, quiz2_content,False),
                         Quiz(screen, 80, 80, quiz3_content,True), Quiz(screen, 80, 80, quiz4_content,True),
                         Quiz(screen, 80, 80, quiz5_content,False),Quiz(screen, 80, 80, quiz6_content,False),
                         Quiz(screen, 80, 80, quiz7_content,False), Quiz(screen, 80, 80, quiz8_content,True),
                         Quiz(screen, 80, 80, quiz9_content,False) , Quiz(screen, 80, 80, quiz10_content,False) ]
        
            if QUIZ_INDEX is len(quizStack):
                if not IS_HIGHSCORE_UPDATED:
                    Sqlite().updateHighScore(3,SCORE)
                    IS_HIGHSCORE_UPDATED = True 
                IS_QUIZ_STARTED = False 
                SCORE = 0
                pass
                # print("Dialogue")
                
            else:
                quizStack[QUIZ_INDEX].render()
                if IS_QUIZVOICE_PLAYED_3[QUIZ_INDEX] :
                    IS_QUIZVOICE_PLAYED_3[QUIZ_INDEX] = False 
                    quizVoice[QUIZ_INDEX].play()
                for event in self.events: 
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # Home Exit 
                        if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
                            # self.push(HomeNode()) 
                            print(quiz.checkAnswer(True))
                            if quizStack[QUIZ_INDEX].checkAnswer(True):
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_CORRECT_VOICE.play()
                                SCORE += SCORE_INCREMENT*3
                                QUIZ_INDEX +=1
                                # quizStack[QUIZ_INDEX].render()
                            else:
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_WRONG_VOICE.play()
                                QUIZ_INDEX+=1
                        
                        elif (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
                            # self.push(GameIntroNode()) 
                            print(quiz.checkAnswer(False)) 
                            if quizStack[QUIZ_INDEX].checkAnswer(False):
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_CORRECT_VOICE.play()
                                SCORE += SCORE_INCREMENT*3 
                                QUIZ_INDEX +=1
                            else:
                                quizVoice[QUIZ_INDEX].stop()
                                ANSWER_WRONG_VOICE.play()
                                QUIZ_INDEX+=1 
       
        
        
        
        unknownNPCRect = unknownNPC.getNpcRect()
        unknownQuizNPC(screen, self.events, self.keyPress,unknownNPCPath ,unknownNPCRect,miniPlayerRect)
        
        
        
        
        # global IS_QUIZ_STARTED
        # if IS_QUIZ_STARTED:
            
        #     quiz1_content = "Q1. Which of the following is IBM BlockChain?"
        #     quiz2_content = "Q2. Which of the following is IBM BlockChain?"
        #     quiz = Quiz(screen, 80, 80, quiz1_content,True)
            
        #     global QUIZ_INDEX
            
        #     quizStack = [Quiz(screen, 80, 80, quiz1_content,True),Quiz(screen, 80, 80, quiz2_content,True)]
        
        #     if QUIZ_INDEX is len(quizStack):
        #         IS_QUIZ_STARTED = False 
        #         pass
        #         # print("Dialogue")
                
        #     else:
        #         quizStack[QUIZ_INDEX].render()
        #         for event in self.events: 
        #             if event.type == pygame.MOUSEBUTTONDOWN :
        #                 mouse_x, mouse_y = pygame.mouse.get_pos()
        #                 # Home Exit 
        #                 if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
        #                     # self.push(HomeNode()) 
        #                     print(quiz.checkAnswer(True))
        #                     if quiz.checkAnswer(True):
                            
        #                         SCORE += SCORE_INCREMENT
        #                         QUIZ_INDEX +=1
        #                         # quizStack[QUIZ_INDEX].render()
                        
        #                 if (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
        #                     # self.push(GameIntroNode()) 
        #                     print(quiz.checkAnswer(False)) 
        #                     if quiz.checkAnswer(False):
                            
        #                         SCORE += SCORE_INCREMENT 
        #                         QUIZ_INDEX +=1
        
        global USER_ID
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(USER_ID)
        else: 
            pass  
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(USER_ID)
        else: 
            pass      
        
        #  # Name Tag
        # pygame.draw.rect(screen, (51,51,51), pygame.Rect(760, 687, 250, 43), border_radius = 10 )
        
        # LIGHT_GREEN = (234,230,70)
        # ANSWER_FONT = pygame.font.Font(FONT_DIRECTORY, 12)
        # answer1_content = "Dr. Roger Moore"
        # answer1 =  ANSWER_FONT.render(answer1_content, True, LIGHT_GREEN)
        # screen.blit(answer1,(790, 707))
  
         
# class GameWinNode(SceneStack):
#     def __init__(self):
#         SceneStack.__init__(self)
#         pygame.mixer.init() 
#         pygame.mixer.music.load("ibm_blockchain/assets/gameOverWin.mp3") 
#         pygame.mixer.music.play(-1,0.0)
        
#     def ProcessInput(self, events, pressed_keys):
#         pass
#         # for event in events:
#         #     if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
#         #         # Move to the next scene when the user pressed Enter
#         #         self.SwitchToScene(GameScene())
    
#     def Update(self):
#         pass
    
#     def Render(self, screen):
#          # Field 
#         # field = pygame.image.load("ibm_blockchain/assets/field.png")
#         # field = pygame.transform.scale( field, (1024,800) )
#         # screen.blit(field,(0,0))
#         screen.fill(BLACK)
        
#         global SCORE
#         text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
#         textRect = text.get_rect()
#         textRect.center = (100,20)
#         #SCORE += SCORE_INCREMENT
#         screen.blit(text, textRect)
                
class GameOverNode(SceneStack):
    def __init__(self):
        SceneStack.__init__(self)
       
        pygame.mixer.init() 
        pygame.mixer.music.load("assets/background/music/gameOverWin.mp3") 
        pygame.mixer.music.play(-1,0.0)
        
        # self.button1_x, self.button1_y = WIDTH // 2, HEIGHT // 4
        # self.button2_x, self.button2_y = WIDTH // 2 - 30  , HEIGHT // 4 + 100
        # self.button3_x, self.button3_y = WIDTH // 2 -20  , HEIGHT // 4 + 200
        # x,y = 200,400
        # VELOCITY = 8
        # self.button1 = Button (
        #          "EASY (x 1)",
        #           (WIDTH/2-100, HEIGHT/2-100),
        #           font = 50,
        #           bg="navy",
        #           feedback="OK"
        # ) 
        
    def ProcessInput(self, events, pressed_keys):
        self.events = events 
        pygame.mixer.init() 
        portal_sound = pygame.mixer.Sound("assets/background/music/effect/maplestory_portal.mp3") 
        global IS_LEADERBOARD_OPEN, IS_STATS_OPEN, IS_ACHIEVEMENT_OPEN  
        
        for event in events: 
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                # Move to the next scene when the user pressed Enter
                portal_sound.play()
                self.push(HomeNode())
            
            if event.type == pygame.KEYDOWN and event.key == K_l:
                if not IS_LEADERBOARD_OPEN:
                    IS_LEADERBOARD_OPEN = True   
                else: 
                    IS_LEADERBOARD_OPEN = False 
            
            if event.type == pygame.KEYDOWN and event.key == K_s: 
                if not IS_STATS_OPEN:
                    IS_STATS_OPEN = True   
                else: 
                    IS_STATS_OPEN = False 
                    
            if event.type == pygame.KEYDOWN and event.key == K_3: 
                if not IS_ACHIEVEMENT_OPEN:
                    IS_ACHIEVEMENT_OPEN = True   
                    #OPEN_STATS_VOICE.play()
                else: 
                    IS_ACHIEVEMENT_OPEN = False    
                    #CLOSE_STATS_VOICE.play()     
                
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print("clicked")
            #     global DIALOG_COUNT 
            #     DIALOG_COUNT +=1 
            #     print(DIALOG_COUNT)
            
            # Dialog.hearClick(pygame.mouse.get_pos())
           
        # if pressed_keys[K_s] and not IS_LEADERBOARD_OPEN:
        #    IS_LEADERBOARD_OPEN = True      
        # else: 
        #    IS_LEADERBOARD_OPEN = False     
                
        
        #print(pygame.mouse.get_pos())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        resetSurface(screen)
        
        GAME_FONT2 = pygame.font.Font(FONT_DIRECTORY, 60)
        text = GAME_FONT2.render('GAME OVER', True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 4)

        GAME_FONT3 = pygame.font.Font(FONT_DIRECTORY, 42)
        text2 = GAME_FONT3.render('Please go back to home.', True, WHITE, BLACK)
        textRect2 = text2.get_rect()
        textRect2.center = (WIDTH // 2 - 30  , HEIGHT // 4 + 100)

        text3 = GAME_FONT3.render('Press Space Bar to continue', True, WHITE, BLACK)
        textRect3 = text3.get_rect()
        textRect3.center = (WIDTH // 2 -20  , HEIGHT // 4 + 200)
        
        screen.blit(text, textRect)   
        screen.blit(text2, textRect2)   
        screen.blit(text3, textRect3) 
        
        global SCORE
        text = GAME_FONT.render(f'Score: {SCORE}', True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (100,20)
        #SCORE += SCORE_INCREMENT
        screen.blit(text, textRect)  
        
        
        global IS_LEADERBOARD_OPEN    
       
        if IS_LEADERBOARD_OPEN : 
            LeaderBoard(screen).render()
        else: 
            pass
        #Stats(screen).render(3)
        
        
        global IS_STATS_OPEN
        if IS_STATS_OPEN : 
            Stats(screen).render(1)
        else: 
            pass
        
        #filePath = "ibm_blockchain/assets/easynpc1.png"
        
        global IS_ACHIEVEMENT_OPEN
        if IS_ACHIEVEMENT_OPEN : 
           Achievement(screen).render(1)
        else: 
            pass
        
         
        
        # dialogStack = [Dialog(screen, filePath, "Kevin", "I'm hungry", True, True, True, True, True)]
        
        # global TOWN_NPC_DIALOG_INDEX
        # dialogStack[TOWN_NPC_DIALOG_INDEX].render()
        # endChatRect =  dialogStack[TOWN_NPC_DIALOG_INDEX].drawEndChatButton()
        # nextChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawNextButton()
        # prevChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawPrevButton()
        # yesChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawYesButton()
        # noChatRect = dialogStack[TOWN_NPC_DIALOG_INDEX].drawNoButton()

        # for event in self.events:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if endChatRect.collidepoint(pygame.mouse.get_pos()):
        #             print("yes")
        #             global DIALOG_COUNT 
        #             DIALOG_COUNT +=1 
        #             print(DIALOG_COUNT)
        #         if nextChatRect.collidepoint(pygame.mouse.get_pos()):
        #             print("nextChatRect")
        #         if prevChatRect.collidepoint(pygame.mouse.get_pos()):
        #             print("prevChatRect")
        #         if yesChatRect.collidepoint(pygame.mouse.get_pos()):
        #             print("yesChatRect")
        #         if noChatRect.collidepoint(pygame.mouse.get_pos()):  
        #             print("nochatrect")  
                
                    #TOWN_NPC_DIALOG_INDEX +=1
        
        #dialogStack[0].hearClick()
        
        # quiz1_content = "Q1. Which of the following is IBM BlockChain?"
        # quiz = Quiz(screen, 80, 80, quiz1_content,True)
        # quiz.render()
        # for event in self.events: 
        #     if event.type == pygame.MOUSEBUTTONDOWN :
        #         mouse_x, mouse_y = pygame.mouse.get_pos()
        #         # Home Exit 
        #         if (92<=mouse_x<=525) and (268 <= mouse_y <= 585) : 
        #             # self.push(HomeNode()) 
        #             print(quiz.checkAnswer(True))
                
        #         if (542<=mouse_x<=969) and (264 <= mouse_y <= 585) : 
        #             # self.push(GameIntroNode()) 
        #             print(quiz.checkAnswer(False))  
        
        
        
        # print(pygame.mouse.get_pos())
        
        # Button
        #screen.blit(self.button1.surface, (self.button1_x, self.button1_y))

################################################ Scene End ################################################



# from assets.npc.npcVoice.emma.emmaVoiceGenerator import generateEmmaVoice

# from assets.npc.npcVoice.matthew.matthewVoiceGenerator import generateMatthewVoice 

# from assets.npc.npcVoice.theKing.kingVoiceGenerator import generateTheKingVoice

# print(sys.path)
# print("before = ",os.getcwd())
# os.chdir("../../../..")
# print("after = ",os.getcwd())


def BlockchainHouse(width, height, fps, starting_scene):
    # generateEmmaVoice()
    # generateMatthewVoice()
    # generateTheKingVoice()
    
    
    pygame.init()
    gameScreen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("IBM BlockChain House")
    clock = pygame.time.Clock()
    
    active_scene = starting_scene
    
    # pygame.mixer.init() 
    # pygame.mixer.music.load("ibm_blockchain/assets/FloralLife.mp3") 
    # pygame.mixer.music.play(-1,0.0)



    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.pop()
            else:
                if(len(filtered_events)>1):
                     filtered_events.clear()
                filtered_events.append(event)
        
        # dialogbox = Dialog(512, 400, 1000, 250, "Kev")
        # dialogbox.render()
        
         
        # gameScreen.fill(BLACK)
        # ball1 = Ball(x, y, 20, gameScreen, dx,dy)
        # ball1.render()
        # ball1.update()
       
        # x  = (x+dx)%1024
        # y  = (y+dy)%800
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(gameScreen)
        # print(PLAYER_X, PLAYER_Y)
        
        active_scene = active_scene.next
        
        
        
        pygame.display.flip()
        clock.tick(fps)

#print(__package__)

#BlockchainHouse(WIDTH, HEIGHT, FPS, HomeNode())




# def drawField(gameScreen):
#    field = pygame.image.load("./ibm-blockchain/assets/field.png")
#    field = pygame.transform.scale( field, (WIDTH,HEIGHT) )
#    gameScreen.blit(field,(0,0))
   
   
# def drawStatue(gameScreen): 
#    statue = pygame.image.load("./ibm-blockchain/assets/statue.png")
#    statue = pygame.transform.scale( statue, (100,100) ) 
#    gameScreen.blit(statue,(350,500))
#    gameScreen.blit(statue,(600,500))


# def drawRiver(gameScreen):
#     river = pygame.image.load("./ibm-blockchain/assets/river.png")
#     river = pygame.transform.scale(river,(100,100))
    
#     i = 600
#     STEP = 100
#     while(i<=1100) : 
#        gameScreen.blit(river,(i,600))
#        rect = river.get_rect()
#        rect.center = i+50,600+50
#        pygame.draw.rect(gameScreen, GREEN, rect,4)
#     #    print(rect)
#        gameScreen.blit(river,(i,700))
#        i+=STEP
       
#     j = 350
#     while(j>=-50) :
#        gameScreen.blit(river,(j,600))
#        gameScreen.blit(river,(j,700))
#        j-=STEP

# def drawTree(gameScreen):   
#   tree = pygame.image.load("./ibm-blockchain/assets/tree.png")
#   tree = pygame.transform.scale( tree, (100,100) )  
     
#   STEP = 100
#   i = 100 
#   while (i<500):
#     gameScreen.blit(tree,(0,i))
#     rect = tree.get_rect()
#     rect.center = 0+50,i+50
#     gameScreen.blit(tree,(100,i))
#     gameScreen.blit(tree,(200,i))
#     gameScreen.blit(tree,(300,i))
    
#     gameScreen.blit(tree,(630,i))
#     gameScreen.blit(tree,(730,i))
#     gameScreen.blit(tree,(830,i))
#     gameScreen.blit(tree,(930,i))
     
#     rect = tree.get_rect()
#    #  print(rect)
#     rect.center = i+50,600+50 
#     pygame.draw.rect(gameScreen, RED, rect,4)
#     i+=STEP

# def drawFence(gameScreen):
#    fence = pygame.image.load("./ibm-blockchain/assets/fence.png")
#    fence = pygame.transform.scale( fence, (20,20) )  
   
#    STEP = 100
#    i = 0               
#    while(i<500): 
#       gameScreen.blit(fence,(300,470)) 
#       i+=STEP 

# def drawChar():
#    x = 350
#    y = 400
#    character =  pygame.image.load("./ibm-blockchain/assets/ship.png")
#    character = pygame.transform.scale( character, (40,40) )
#    gameScreen.blit(character,(x,y))   
   
   
   
#    keyPress = pygame.key.get_pressed()
#    # Changing the coordinates of the player
#    if keyPress[K_LEFT]:
#         x -= 8
#    if keyPress[K_RIGHT]:
#         x += 8
#    if keyPress[K_UP]:
#         y -= 8
#    if keyPress[K_DOWN]:
#         y += 8           


# def startMainGame():

#     character =  pygame.image.load("./ibm-blockchain/assets/ship.png")
#     character = pygame.transform.scale( character, (40,40) )
#     x,y = 200,400
#     VELOCITY = 8


                
#     # Main Console                        
#     while not EXIT:
        
#         # Grass Field
#         drawField()
        
#         # Entrance Statues
#         drawStatue()
        
#         # River
#         drawRiver()
        
#         # Tree
#         drawTree()
        
#         # Fence
#         drawFence()
        
#         npcDesk = pygame.image.load("./ibm-blockchain/assets/npcDesk.png")
#         npcDesk = pygame.transform.scale(npcDesk,(235,100))
#         gameScreen.blit(npcDesk,(400,200))
        
#         npc = pygame.image.load("./ibm-blockchain/assets/char1.png")
#         npc = pygame.transform.scale(npc,(50,50))
#         gameScreen.blit(npc,(500,200))
        
        
#         sampleRect = Rect(512, 400, 100,100)
#         pygame.draw.rect(gameScreen, GREEN, sampleRect,4)
         
#         # Character
#         gameScreen.blit(character,(x,y))   
        
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 EXIT = True 
        
#         keyPress = pygame.key.get_pressed()
    
#     # Changing the coordinates of the player
#         if keyPress[K_LEFT]:
#             x -= VELOCITY
#         if keyPress[K_RIGHT]:
#             x += VELOCITY
#         if keyPress[K_UP]:
#             y -= VELOCITY
#         if keyPress[K_DOWN]:
#             y += VELOCITY  
        
            
#         rect = character.get_rect()
#         rect.center = x+10,y+10 
#         pygame.draw.rect(gameScreen, RED, rect,4)        
        
#         if rect.colliderect(sampleRect):
#             print("Collided")
            
            
#             x-=20
#             y-=20
            
#             # tkinterRoot = Tk()
#             # my_gui = Minigame1(tkinterRoot)
#             # tkinterRoot.mainloop()

            
#             # root = Tk()
#             # my_gui = Minigame1(root)
#             # root.mainloop()

        
        
        
#         pygame.display.flip()
        
        
        



        
        
    
