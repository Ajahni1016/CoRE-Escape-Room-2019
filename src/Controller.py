#This is where we will put all our imports:
#Regular
import pygame
import sys
import time
import random
import json

class Controller:
    def __init__(self, width=1920, height=1080):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        self.width = width
        self.height = height
        self.hasWon = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.hit=0
        self.blow=0
        #self.codes = ["test","temp","no","yes"]
        self.codes = ["navy","kelp","whale","drizzle"]
        self.locks = 0
        pygame.font.init()
        #INITIAL STATE
        self.state = "MENU"

    def mainLoop(self):
        """Controls the state of the game"""
        #print("Entering the main loop...")
        while True:
            if(self.state == "MENU"):
                self.menuLoop()
            if(self.state == "INPUT"):
                self.inputLoop()
            if(self.state == "GAME"):
                self.gameLoop()
            if(self.state == "WIN"):
                self.winLoop()

    def menuLoop(self):
        """This is the Menu Loop of the Game"""
        #print("Entering the menu loop...")
        while self.state == "MENU":
            self.locksRight = pygame.transform.smoothscale(pygame.image.load('assets/locks/AllLocked.png').convert_alpha(), (384,1080))
            self.locksLeft = pygame.transform.smoothscale(pygame.image.load('assets/locks/AllLocked.png').convert_alpha(), (384,1080))
            #BACKGROUND
            if "drizzle" not in self.codes:
                if "navy" not in self.codes:
                    self.locksRight = pygame.transform.smoothscale(pygame.image.load('assets/locks/NavyDrizzleUnlocked.png').convert_alpha(), (384,1080))
                else:
                    self.locksRight = pygame.transform.smoothscale(pygame.image.load('assets/locks/DrizzleUnlocked.png').convert_alpha(), (384,1080))
            elif "navy" not in self.codes:
                self.locksRight = pygame.transform.smoothscale(pygame.image.load('assets/locks/NavyUnlocked.png').convert_alpha(), (384,1080))

            if "kelp" not in self.codes:
                if "whale" not in self.codes:
                    self.locksLeft = pygame.transform.smoothscale(pygame.image.load('assets/locks/WhaleKelpUnlocked.png').convert_alpha(), (384,1080))
                else:
                    self.locksLeft = pygame.transform.smoothscale(pygame.image.load('assets/locks/KelpUnlocked.png').convert_alpha(), (384,1080))
            elif "whale" not in self.codes:
                self.locksLeft = pygame.transform.smoothscale(pygame.image.load('assets/locks/WhaleUnlocked.png').convert_alpha(), (384,1080))

            self.menuBG = pygame.transform.smoothscale(pygame.image.load('assets/EscapeRoomTitleScreenBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.menuBG, (0, 0))
            self.screen.blit(self.locksRight, (1536, 0))
            self.screen.blit(self.locksLeft, (0, 0))
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coords=pygame.mouse.get_pos()
                    #print(coords)
                    #CLICKING UNLOCK BUTTON
                    if((coords[0]>=660 and coords[0]<=1250) and (coords[1]>=545 and coords[1]<=705)):
                        if self.locks==4:
                            print("All 4 locks unlocked. Starting game!")
                            pygame.mixer.music.load('assets/sounds/mastermind.ogg')
                            pygame.mixer.music.play(0)
                            self.state = "GAME"
                            self.mainLoop()
                        else:
                            #print("Not all locks unlocked. Going to input screen.")
                            pygame.mixer.music.load('assets/sounds/click.ogg')
                            pygame.mixer.music.play(0)
                            self.state = "INPUT"
                            self.mainLoop()
            pygame.display.flip()

    def inputLoop(self):
        """This is the INPUT Loop of the Game"""
        #print("Entering the input loop...")
        rightOrWrong = 2
        myfont = pygame.font.Font('assets/HACKED.ttf', 200)
        answer = ""
        while self.state == "INPUT":
            #BACKGROUND
            if rightOrWrong == 2:
                self.helpScreen = pygame.transform.smoothscale(pygame.image.load('assets/InputScreen.png').convert_alpha(), (self.width,self.height))
            elif rightOrWrong==1:
                self.helpScreen = pygame.transform.smoothscale(pygame.image.load('assets/InputScreenUnlocked.png').convert_alpha(), (self.width,self.height))
            elif rightOrWrong==0:
                self.helpScreen = pygame.transform.smoothscale(pygame.image.load('assets/InputScreenLocked.png').convert_alpha(), (self.width,self.height))

            self.screen.blit(self.helpScreen, (0, 0))
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #KEYBOARD INPUT
                if event.type == pygame.KEYDOWN:
                    if rightOrWrong==2:
                        if event.unicode.isalpha():
                            answer += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            answer = answer[:-1]
                        # elif event.key == K_RETURN:
                        #     name = ""
                        #print(answer)
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coords=pygame.mouse.get_pos()
                    #print(coords)
                    #CLICKING BACK BUTTON
                    if((coords[0]>=495 and coords[0]<=675) and (coords[1]>=890 and coords[1]<=970)):
                        #print("Back Button Pressed")
                        pygame.mixer.music.load('assets/sounds/click.ogg')
                        pygame.mixer.music.play(0)
                        self.state = "MENU"
                        self.mainLoop()
                    #CLICKING ENTER BUTTON
                    if((coords[0]>=1246 and coords[0]<=1447) and (coords[1]>=890 and coords[1]<=970)):
                        if rightOrWrong == 2:
                            #print("Enter Button Pressed")
                            for i in range(0,len(self.codes)):
                                if answer.lower()==self.codes[i]:
                                    pygame.mixer.music.load('assets/sounds/unlock.ogg')
                                    pygame.mixer.music.play(0)
                                    self.codes[i]="2"
                                    self.locks+=1
                                    rightOrWrong=1
                            if rightOrWrong==2:
                                pygame.mixer.music.load('assets/sounds/wrong.ogg')
                                pygame.mixer.music.play(0)
                                rightOrWrong=0

            text = myfont.render(answer, True, (255, 255, 255))
            self.screen.blit(text, ((self.width//3)+115, (self.height//3)+75))
            pygame.display.flip()

    def insertCode(self, num, code):
        if len(code) < 4 and num not in code:
            code.append(num)

    def hitBlow(self, code, guess):
        print("Current guess is... ",*guess,sep='')
        self.hit = 0  #Right Number/Right Spot (Green Light)
        self.blow = 0 #Right Number/Wrong Spot (Blue Light)
        for i in range(0,4):
            if guess[i] in code:
                pygame.mixer.music.load('assets/sounds/unlock.ogg')
                pygame.mixer.music.play(0)
                if guess[i] == code[i]:
                    self.hit += 1
                else:
                    self.blow += 1

        if self.hit==0 and self.blow==0:
            pygame.mixer.music.load('assets/sounds/wrong.ogg')
            pygame.mixer.music.play(0)


        print("Hit: ", self.hit)
        print("Blow: ", self.blow)
        guess.clear()

    def gameLoop(self):
        """This is the Game Loop of the Game"""
        #print("Entering the game loop...")
        #SETTING THE CODE
        code = [0,0,0,0]
        guess = []
        options = [1,2,3,4,5,6,7,8,9]
        lightsOn = False
        pos = 0
        self.blueOn = pygame.transform.smoothscale(pygame.image.load('assets/BlueON.png').convert_alpha(), (321,322))
        self.greenOn = pygame.transform.smoothscale(pygame.image.load('assets/GreenON.png').convert_alpha(), (321,322))
        for i in range(0,4):
            index = random.randint(0,len(options)-1)
            code[i] = options[index]
            options.pop(index)
        code = [8,2,0,6]
        print("the code is ",*code,sep='')
        #TEXT FOR CODE TO SHOW ONS SCREEN
        myfont = pygame.font.Font('assets/digital.ttf', 200)
        value1=""
        value2=""
        value3=""
        value4=""
        #LOOP
        while self.state == "GAME":
            if self.hit==4:
                pygame.time.delay(2000)
                self.state="WIN"
            #BACKGROUND
            self.gameScreen = pygame.transform.smoothscale(pygame.image.load('assets/GameScreen.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.gameScreen, (0, 0))
            #TEXT
            text = myfont.render(value1, True, (255, 255, 255))
            self.screen.blit(text, (1050, 455))
            text = myfont.render(value2, True, (255, 255, 255))
            self.screen.blit(text, (1200, 455))
            text = myfont.render(value3, True, (255, 255, 255))
            self.screen.blit(text, (1350, 455))
            text = myfont.render(value4, True, (255, 255, 255))
            self.screen.blit(text, (1500, 455))
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coords=pygame.mouse.get_pos() #Coords[0] is X and coords[1] is Y
                    #print(coords)
                    if lightsOn==False:
                        if((coords[0]>=391 and coords[0]<=475) and (coords[1]>=689 and coords[1]<=757)):
                            #print("Clicked 0")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(0, guess)
                        elif((coords[0]>=272 and coords[0]<=340) and (coords[1]>=570 and coords[1]<=642)):
                            #print("Clicked 1")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(1, guess)
                        elif((coords[0]>=391 and coords[0]<=475) and (coords[1]>=570 and coords[1]<=642)):
                            #print("Clicked 2")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(2, guess)
                        elif((coords[0]>=511 and coords[0]<=585) and (coords[1]>=570 and coords[1]<=642)):
                            #print("Clicked 3")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(3, guess)
                        elif((coords[0]>=272 and coords[0]<=340) and (coords[1]>=446 and coords[1]<=516)):
                            #print("Clicked 4")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(4, guess)
                        elif((coords[0]>=391 and coords[0]<=475) and (coords[1]>=446 and coords[1]<=516)):
                            #print("Clicked 5")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(5, guess)
                        elif((coords[0]>=511 and coords[0]<=585) and (coords[1]>=446 and coords[1]<=516)):
                            #print("Clicked 6")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(6, guess)
                        elif((coords[0]>=272 and coords[0]<=340) and (coords[1]>=325 and coords[1]<=395)):
                            #print("Clicked 7")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(7, guess)
                        elif((coords[0]>=391 and coords[0]<=475) and (coords[1]>=325 and coords[1]<=395)):
                            #print("Clicked 8")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(8, guess)
                        elif((coords[0]>=511 and coords[0]<=585) and (coords[1]>=325 and coords[1]<=395)):
                            #print("Clicked 9")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            self.insertCode(9, guess)
                        elif((coords[0]>=511 and coords[0]<=585) and (coords[1]>=689 and coords[1]<=757)):
                            #print("Clicked Enter")
                            # pygame.mixer.music.load('assets/sounds/beep.ogg')
                            # pygame.mixer.music.play(0)
                            if len(guess)==4:
                                self.hitBlow(code, guess)
                                lightsOn = True
                    if self.hit != 4:
                        if((coords[0]>=272 and coords[0]<=340) and (coords[1]>=689 and coords[1]<=757)):
                            #print("Clearing List...")
                            pygame.mixer.music.load('assets/sounds/beep.ogg')
                            pygame.mixer.music.play(0)
                            guess.clear()
                            value1 = ""
                            value2 = ""
                            value3 = ""
                            value4 = ""
                            lightsOn = False


            #PRINTING CODE
            if len(guess)==1:
                value1 = str(guess[0])
            if len(guess)==2:
                value2 = str(guess[1])
            if len(guess)==3:
                value3 = str(guess[2])
            if len(guess)==4:
                value4 = str(guess[3])

            if lightsOn == True:
                for i in range(0,(self.hit)):
                    self.screen.blit(self.greenOn, (1636, 120+(i*175)-2.5))

                for i in range(0,(self.blow)):
                    self.screen.blit(self.blueOn, (676, 120+(i*175)-2.5))

            if self.hit==4:
                if self.hasWon == False:
                    pygame.mixer.music.load('assets/sounds/win.ogg')
                    pygame.mixer.music.play(0)
                    self.hasWon = True

            pygame.display.flip()


    def winLoop(self):
        """This is the Menu Loop of the Game"""
        print("Entering the menu loop...")
        pygame.mixer.music.load('assets/sounds/morseCode.ogg')
        pygame.mixer.music.play(0)
        while self.state == "WIN":
            #BACKGROUND
            self.menuBG = pygame.transform.smoothscale(pygame.image.load('assets/Escaped.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.menuBG, (0, 0))

            pygame.display.flip()
