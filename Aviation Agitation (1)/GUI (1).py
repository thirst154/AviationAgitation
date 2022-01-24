import pygame
pygame.init()

class baseButton:
    def __init__(self, posX,posY,w,h,text,font):
        self.posX = posX
        self.posY = posY
        self.width = w
        self.height = h
        self.text=text
        self.font = font
        self.rect = pygame.Surface((self.width,self.height),4) 
        self.textsurface = self.font.render(self.text, False, (1,1,1))
        self.colour = [112,112,112]
        self.rect.set_alpha(100)
    def show(self,screen):
        self.rect.fill(self.colour)
        screen.blit(self.textsurface,(int(self.posX+10),int(self.posY+30)))
        screen.blit(self.rect,(int(self.posX),int(self.posY)))

        
class toggelButton(baseButton):
    def update(self,POS,events):
        pos = (-100,-100)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = POS
        px, py = pos
        if px >= self.posX and px <= self.posX + self.width and py >= self.posY and py <= self.posY + self.height:
            if self.colour == [50,50,50]:
                self.colour = [112,112,112]
                self.value = True
            elif self.colour == [112,112,112]:
                self.colour = [90,90,90]
                self.value = False
    def getValue(self):
        return self.value
        
class button(baseButton):
    def isClicked(self, mousePos):
        if mousePos == (0,0):
            return False
        else:
            px = int(mousePos[0])
            py = int(mousePos[1])
            
            if px >= self.posX and px <= self.posX + self.width and py >= self.posY and py <= self.posY + self.height:
                self.colour = [1,1,1]
                return True
            return False

class slider():
    def __init__(self,posX,posY,w,value):
        self.posX = posX
        self.posY = posY
        self.width = w
        self.height = 50
        self.value = value
        self.mousePos = [posX,posY]
        self.diam = 15
    def show(self, screen):
        ##frame
        self.cornerX = self.posX-int(self.height/2)
        self.cornerY = self.posY-int(self.height/2)
        self.boxWidth = int(self.width+self.height)
        self.boxHeight = self.height
        pygame.draw.rect(screen, (1,1,1),(self.cornerX,self.cornerY,self.boxWidth,self.boxHeight),5)
        pygame.draw.rect(screen, (77,77,77),(self.cornerX,self.cornerY,self.boxWidth,self.boxHeight))

        
        ##Slider line
        pygame.draw.line(screen, (1,1,1), (self.posX, self.posY), (self.posX+self.width, self.posY),5)
        ##slider ball
        if self.mousePos[0] > self.posX+self.width:
            self.mousePos[0] = self.posX+self.width-1
        elif self.mousePos[0] < self.posX:
            self.mousePos[0] = self.posX+1
        pygame.draw.circle(screen, (7,7,7), (self.mousePos[0],self.posY), self.diam,2)
    def getValue(self):
        return (self.posX-self.mousePos[0])/(self.width-self.posX)
        
    def isClicked(self,mouse):
        if mouse == (0,0):
            return False
        else:
            px = int(mouse[0])
            py = int(mouse[1])
            
            if px >= self.cornerX and px <= self.cornerX + self.boxWidth and py >= self.cornerY and py <= self.cornerY + self.boxHeight:
                self.mousePos[0] = px
                return True
            return False
