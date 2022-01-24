import pygame
from world import World, obst
pygame.init()


class mo():
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.width = 10
        self.height = 10
        self.clicked = False
    def update(self, pos):
        #self.clicked = False
        self.posX = pos[0]
        self.posY = pos[1]
        
screenWidth = 1000
screenHeight = 800
screen = pygame.display.set_mode([screenWidth,screenHeight])
undo = []
m = World()
m.create(screenWidth,screenHeight,1)
m.add(obst(0,0,screenWidth,0))
m.add(obst(0,0,0,screenHeight))
m.add(obst(0,screenHeight,screenWidth,screenHeight))
m.add(obst(screenWidth,0,screenWidth,screenHeight))
game = True
mouse = mo()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse.clicked == False:
                mouse.clicked = pygame.mouse.get_pos()
            else:
                mouse.clicked = False
        else:
            pass#mouse.clicked = False
    screen.fill((255,255,255))

    keys = pygame.key.get_pressed()
    print(len(keys))
    print([keys.index(i) for i in keys if i == 1])
    if keys[117]:
        m.add(undo[len(undo)-1])
    mouse.update(pygame.mouse.get_pos())
    select = m.isCollide(mouse)
    if select == False:
        pass
    else:
        m.select(select)
        if mouse.clicked != False:
            m.pop(m.items.index(select))
            undo.append(select)
    
    m.show(screen)
    
    pygame.display.flip()


pygame.quit()
quit()
