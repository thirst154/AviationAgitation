import pygame, math,random
pygame.init()

class tank():
    def __init__(self,posX,posY,cont,img,settings):
        self.X = posX
        self.Y = posY
        self.settings = settings
        self.angle = random.randint(0,360)
        self.speed = 0
        self.rotationSpeed = 0.5
        self.velX = 0
        self.velY = 0
        self.toShoot = False
        self.width = 10
        self.height = 10
        self.alive = True
        self.mainSpeed = 1
        self.coll = True
        self.tick = 0
        self.toShoot = -999
        self.shoot = False
        self.img = pygame.image.load(img)
        self.cont = cont
        self.item = ''
    def show(self, screen):
        self.rect = self.img
        #rotates image based on self.angle
        image, rect = self.rot_center(self.rect,self.angle,self.X,self.Y)
        #pygame.draw.rect(screen, (0,255,0),(self.posX,self.posY,self.width,self.height))
        screen.blit(image, (rect))
    
    def update(self,keys):
        #self.toShoot += 1
        self.tick += 1
        up = keys[self.cont[0]] == 1
        down = keys[self.cont[1]] == 1
        left = keys[self.cont[2]] == 1
        right = keys[self.cont[3]] == 1 
        fire = keys[self.cont[4]] == 1
        mult = self.settings['speed']
        if left:
            self.angle += self.rotationSpeed 
            #LEFT
        if right:
            self.angle -= self.rotationSpeed 
            #RIGHT
        if up:
            self.speed = -self.rotationSpeed  * self.mainSpeed
            #UP
        if down:
            self.speed = self.rotationSpeed  * self.mainSpeed
            #DOWN
        if (not up == 1) and (not down == 1):
            self.speed = 0
        if fire:
            #print(self.toShoot+100, self.tick,self.toShoot+100 < self.tick)
            if self.toShoot+300 < self.tick:
                #print('triggerd')
                self.toShoot = self.tick
                self.shoot = True
        velX, velY = self.calcVel(self.X,self.Y,self.angle,self.speed)
        self.oldX = self.X
        self.oldY = self.Y
        self.X +=velX
        self.Y +=velY
        ##keeps angle between 1 - 360
        if self.angle == 0:
            self.angle = 359
            
        if self.angle == 360:
            self.angle == 1
        self.posX = self.X - self.width/2
        self.posY = self.Y - self.height/2
    def resetPos(self):
        self.X = self.oldX
        self.Y = self.oldY
    def rot_center(self, image, angle, x, y):
    
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

        return rotated_image, new_rect
    def calcVel(self,x,y,angle,speed):
        Radians = angle * math.pi / 180
        x = (speed*math.sin(Radians))
        y = (speed*math.cos(Radians))
        return x,y
    def getBulletinfo(self):
        self.toShoot += 1
        velX,velY = self.calcVel(self.X,self.Y,self.angle,0.3)
        #print(velX,velY)
        return velX,velY,self.X,self.Y

    def newPos(self, x,y):
        self.X = x
        self.Y = y

