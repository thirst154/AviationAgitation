import pygame
pygame.init()

class bullet():
    def __init__(self, posX,posY,velX,velY):
        self.name = 'bullet'
        self.posX = posX
        self.posY = posY
        self.velX = -velX 
        self.velY = -velY
        self.alive = 0
        self.width = self.height = self.diam = 2
    def update(self):
        self.alive += 1
        self.posX += self.velX * 1.5
        self.posY += self.velY * 1.5
    def show(self,screen):
         pygame.draw.circle(screen, (1,1,1), (int(self.posX),int(self.posY)), self.diam)
    def bounce(self, obst):
        if obst.width > obst.height:
            self.velY = self.velY * -1
            self.velX = self.velX * 1
        else:
            self.velY = self.velY * 1
            self.velX = self.velX * -1
    def outBounds(self):
        return self.posX > 1000 or self.posY > 1000 or self.alive > 3000
        
            


