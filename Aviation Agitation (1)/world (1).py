import pygame
import random
pygame.init()



def collide(a,b):
    g = a.posX < b.posX + b.width 
    h = a.posX + a.width > b.posX 
    j = a.posY < b.posY + b.height 
    k = a.posY + a.height > b.posY
    return g and h and j and k


class World():
    def __init__(self):
        self.items = []
    def show(self,screen):
        for ob in self.items:
            ob.show(screen)
    def add(self, ob):
        self.items.append(ob)
    def pop(self, ob):
        self.items.pop(ob)
    def isCollide(self, *args):
        for j in args:
            for i in self.items:
                if collide(i,j):
                    return i
        return False
    def select(self, i):
        self.items[self.items.index(i)].clr = (255,0,0)
    def create(self, sWidth,sHeight,chance):
        sclH = 12
        sclW = 16
        od = [0 for i in range(chance)]
        od[0] = 1
        for j in range(0,sHeight,int(sWidth/sclW)):
            for i in range(0,sWidth,int(sWidth/sclH)):
                if random.choice(od):
                   self.add(obst(i,j,i,j+sWidth/sclW))
                if random.choice(od):
                   self.add(obst(i,j,i+sWidth/sclH,j))
                #self.items.append(obst(0,j,sWidth,j))
                

class obst():
    def __init__(self,x1,y1,x2,y2):
        self.clr = (1,1,1)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.posX = x1
        self.posY = y1
    def show(self, screen):
        pygame.draw.line(screen, self.clr, (self.x1, self.y1), (self.x2,self.y2),2)
        #pygame.draw.rect(screen, (0,255,0),(self.posX,self.posY,self.width,self.height))
    def i(self):
        return str(self.x1) + str(self.y1) + str(self.x2) + str(self.y2)
