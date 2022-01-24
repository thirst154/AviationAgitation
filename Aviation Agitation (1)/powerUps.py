import pygame, random
from entity import entity
from world import collide
pygame.init()

IMAGES = ['assets/PU/'+str(i)+'.png' for i in range(1,9,1)]

ID = {1:'noWalls',
      2:'Bomb',
      3:'Shield',
      4:'randomPos',
      5:'landMine',
      6:'miniGun',}

class powerUps():
    def __init__(self,game):
        self.items = []
        self.ammo = []
        self.screenW = game.screenWidth
        self.screenH = game.screenHeight
        
    def createNewPowerUp(self,game):
        self.items.append(self.randomItem())
        while game.m.isCollide(self.items[len(self.items)-1]):
            self.items.pop(len(self.items)-1)
            self.items.append(self.randomItem())
    def randomItem(self):
        img = random.choice(IMAGES)
        Id = IMAGES.index(img) 
        return entity(random.randint(0,self.screenW),random.randint(0,self.screenH),40,40,img,Id)
    def delItem(self, item):
        self.items.pop(self.items.index(item))
    def update(self,game):
        for i in self.items:   
            i.show(game.screen)
            for players in game.players:
                if collide(players, i):
                    players.item = ID[i.id]
                    self.delItem(i)
            if i.alive > 10000:
                self.delItem(i)
