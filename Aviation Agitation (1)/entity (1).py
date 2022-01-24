import pygame

pygame.init()

class entity():
    def __init__(self,posX,posY,w,h,img,Id):
        self.posX = posX
        self.posY = posY
        self.width = w
        self.height = h
        self.id = Id
        self.img = pygame.image.load(img)
        self.alive = 0
    def show(self,screen):
        screen.blit(self.img, (int(self.posX),int(self.posY)))
        self.alive += 1

