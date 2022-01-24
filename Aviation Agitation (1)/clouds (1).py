import pygame, random

class cloud():
    def __init__(self,posX,posY,img):
        self.posX = posX
        self.posY = posY
        self.img = img
        self.width = 3000
        self.height = 800
        self.velX = random.randint(5,10)/100
        self.velY = random.randint(0,5)/100

    def update(self, mapWidth, mapHeight):
        if self.posX > mapWidth or self.posY > mapHeight:
            return False
        #print(self.posX, self.velX)
        self.posX += self.velX
        self.posY += self.velY
        return True
    def show(self, screen):
        screen.blit(self.img, (int(self.posX),int(self.posY)))
