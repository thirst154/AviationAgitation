import pygame, random
from tank import tank
from bul import bullet
from world import World, obst, collide
from clouds import cloud
from GUI import button
from powerUps import powerUps

pygame.init()
pygame.font.init()

CONTROLS = {'player1':[119,115,97,100,32],'player2':[pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,109],'player3':[264,258,260,262,271]}
COLORS = ['red','blue','yellow','Lblue']

class game():
    def __init__(self, settings):
        self.settings = settings
        self.screenWidth = 800
        self.screenHeight = 500
        self.screen = pygame.display.set_mode([self.screenWidth,self.screenHeight+65])#pygame.FULLSCREEN
        self.ghostImage = pygame.image.load('assets/players/ghost.png').convert_alpha()
        if self.settings['maps']:
            self.backgrounds = {'assets/bg/farm.png':1,'assets/bg/beach.png':1,'assets/bg/white.png':0,'assets/bg/black.png':0,'assets/bg/space.png':3}
        else:
            self.backgrounds= {'assets/bg/white.png':0}
        self.Game = True
        self.numberOfPlayers = len(self.settings['players'])
        self.newGame()
        self.score = [0 for i in range(self.numberOfPlayers)]
        self.myfont = pygame.font.SysFont('Aharoni',50)
        self.fontColor=textColor = (1,1,1)
        self.quitButton = button(700,500,100,60,'QUIT',self.myfont)
    def newGame(self):
        
        self.m = World()
        self.bullets = []
        self.powerUps = []
        self.gameTick = 0
        self.players = []
        self.img = random.choice(list(self.backgrounds))
        self.bg = pygame.image.load(self.img).convert_alpha()
        self.powerManager = powerUps(self)

        
        self.deathTick = None
        #walls
        self.m.add(obst(0,0,self.screenWidth,0))
        self.m.add(obst(0,0,0,self.screenHeight))
        self.m.add(obst(0,self.screenHeight,self.screenWidth,self.screenHeight))
        self.m.add(obst(self.screenWidth-8,0,self.screenWidth-8,self.screenHeight))
        #obsts
        if self.settings['isMap']:
            self.m.create(self.screenWidth,self.screenHeight,self.settings['chance'])
        #players
        for player in self.settings['players']:
            self.players.append(tank(0,0,CONTROLS[player[0]],'assets/players/'+COLORS[player[1]]+'.png',self.settings))
        for i, player in enumerate(self.players):
            self.players[i].newPos(random.randint(30,self.screenWidth-30),random.randint(30,self.screenHeight-30))
            self.players[i].update([0 for i in range(323)])
            print(self.m.isCollide(self.players[i]))
            while self.m.isCollide(self.players[i]):
                print(self.players[i].posX, self.players[i].posY)
                self.players[i].newPos(random.randint(20,self.screenWidth-30),random.randint(20,self.screenHeight-30))
                self.players[i].update([0 for i in range(323)])

    def setScoreText(self):
        self.displayScore = ""
        controls = ['arrow','wasd','numpad']
        for i in range(self.numberOfPlayers):
            self.displayScore += str(controls[i])+":"+str(self.score[i])+"  "
        pygame.display.set_caption(self.displayScore)

    def updatePlayers(self):
        for i, player in enumerate(self.players):
            if player.alive:
                player.update(self.keys)
                    #print(keys[264]==1,keys[258]==1,keys[260]==1,keys[262]==1,keys[271]==1)
                if not self.m.isCollide(player) == False and player.coll:
                    player.resetPos()
                if player.coll == False:
                    player.show(self.screen,self.ghostImage)
                else:
                    player.show(self.screen)
                if player.shoot:
                    player.shoot = False
                    velX,velY,posX,posY = player.getBulletinfo()
                    self.bullets.append(bullet(posX,posY,velX,velY))
                    
            else:
                player.posX = self.screenWidth + 100
    def updateBullets(self):
        for b in self.bullets:
            b.update()
            b.show(self.screen)
            if b.outBounds():
                self.bullets.pop(self.bullets.index(b))
            for player in self.players:
                if collide(b, player) and b.alive > 100:
                    #pass
                    player.alive = False
                    self.deathTick = self.gameTick
                    self.bullets.pop(self.bullets.index(b))
            i = self.m.isCollide(b)
            if not i == False:
                b.bounce(i)
        
    def updateDeath(self):
        if self.deathTick != None:
            if self.gameTick-self.deathTick > 1000:
                playersAlive = 0
                for i, player in enumerate(self.players):
                    if player.alive == False:
                        playersAlive += 1
                for i, player in enumerate(self.players):
                    if playersAlive == len(self.players):
                        pass
                    elif player.alive == True:
                        self.score[i] += 1    
                self.newGame()
    def randomEvent(self, freq):
        c = [False for i in range(freq)]
        c.append(True)
        return random.choice(c)
    def gameLoop(self):
        self.screen.fill((1,1,1))
        self.gameTick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Game = False
        self.keys = pygame.key.get_pressed()
        self.screen.blit(self.bg, (0, 0))
        ########SCORE TEXT
        self.setScoreText()
        #######PLAYER UPDATE & SHOW                    
        self.updatePlayers()
        ##POWER UP manager
        self.powerManager.update(self)
        if self.randomEvent(5000):
            self.powerManager.createNewPowerUp(self)
        #######BULLET COLLISION
        self.updateBullets()
        #####QUIT BUTTON
        self.quitButton.show(self.screen)
        if pygame.mouse.get_pressed()[0] == 1:
            if self.quitButton.isClicked(pygame.mouse.get_pos()):
                self.Game = False
        ######MAP SHOW
        self.m.show(self.screen)
        ##SCORE SHOWERER
        textsurface = self.myfont.render(self.displayScore, False, self.fontColor)
        self.screen.blit(textsurface,(int(0),int(self.screenHeight+25)))
        pygame.display.flip()
        #######NEW MAP
        if self.keys[13]==1:
            self.newGame()
        #######DEATH CONTROL
        self.updateDeath()

def startGame(settings):
    GAME = game(settings)

    while GAME.Game:
        GAME.gameLoop()
