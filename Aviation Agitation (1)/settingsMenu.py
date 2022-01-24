import pygame
from GUI import button, toggelButton
pygame.init()
pygame.font.init()

displayWidth = 800
displayHeight = 600#pygame.FULLSCREEN
screen = pygame.display.set_mode((displayWidth, displayHeight),)

key = {'player1':32,'player2':109,'player3':271}
colors = ['red','blue','yellow','Lblue']
def startSettings(default):
    bg = pygame.image.load("assets/bg/settingsBg.png")
    menuFont = pygame.font.SysFont('couriernew',30)
    menuFont.set_bold(1)
    powerToggel = toggelButton(400,300,100,50,'Hello World',menuFont)
    play = True
    while play :
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        screen.blit(bg,[0,1])
        for i, player in enumerate(default['players']):
            screen.blit(pygame.image.load('assets/players/'+colors[int(player[1])]+'.png'),[(i*100)+100,200])
            k = key[player[0]]
            if keys[k] == 1:                
                x = player[1]
                if x > len(colors)-1:
                    x = 0
                else:
                    x += 0.01
                    #print(x, default['players'], player[0],player[1])
                player[1] = x
        powerToggel.update(pygame.mouse.get_pos(),pygame.event.get())
        powerToggel.show(screen)
        pygame.display.flip()
    return default
