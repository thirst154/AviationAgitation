import pygame
import webbrowser
from GUI import button, slider
pygame.init()
pygame.font.init()

bg = pygame.image.load("assets/bg/menu-background.png")
#logo = pygame.image.load("assets\logo1.png")
#logo2 = pygame.image.load("assets\logo2.png")
#slide = slider(100,150,400,10)

player1 = pygame.image.load("assets/players/blue.png")
player2 = pygame.image.load("assets/players/red.png")
player3 = pygame.image.load("assets/players/yellow.png")
bg1 = pygame.image.load("assets/404.png")
blank = pygame.image.load("assets/players/blank.png")

menuFont = pygame.font.SysFont('couriernew',30)
menuFont.set_bold(1)
smallFont = pygame.font.SysFont('couriernew',20)
startButton = button(225,450,360,60,'Start',menuFont)
quitButton = button(700,500,70,60,'X',menuFont)
selected = {'p1':0,'p2':0,'p3':0}
x1 = 10
y1 = 10
x2 = 0.1
y2 = 0.1
def runMenu(screen,pos,keys):
    screen.blit(bg,[0,1])
    #screen.blit(logo,[10,10])
    if keys[32] == 1:
        selected['p1'] = 1
    if keys[109] == 1:
        selected['p2'] = 1
    if keys[271] == 1:
        selected['p3'] = 1
    if keys[13] == 1:
        screen.blit(bg1,[0,1])
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    #player1 keys[109]
    if selected['p1'] == 0:
        screen.blit(blank,[200,200])
        a = smallFont.render('Press SPACE to ready UP!', False, (1,1,1))
        screen.blit(a,(int(250),int(210)))
    else:
        screen.blit(player1,[200,200])
    #player2 keys[32]
    if selected['p2'] == 0:
        screen.blit(blank,[200,300])
        b = smallFont.render('Press M to ready UP!', False, (1,1,1))
        screen.blit(b,(int(250),int(310)))
    else:
        screen.blit(player2,[200,300])
    #player3 keys[271]
    if selected['p3'] == 0:
        screen.blit(blank,[200,400])
        a = smallFont.render('Press NUMPAD ENTER to ready UP!', False, (1,1,1))
        screen.blit(a,(int(250),int(410)))
    else:
        screen.blit(player3,[200,400])
    startButton.show(screen)
    quitButton.show(screen)
    if startButton.isClicked(pos) and selected != {'p1':0,'p2':0,'p3':0}:
        print('Clicked')
        return 'start', selected
    
    if quitButton.isClicked(pos):
        print('QUIT')
        return 'quit', selected

    return '',[0,0,0]

def runSettings(screen,pos):
    screen.blit(bg,[0,1])
    screen.blit(logo,[10,10])
    
    
