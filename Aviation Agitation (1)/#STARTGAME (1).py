import pygame
from MENU import runMenu
from game import startGame
from settingsMenu import startSettings
pygame.init()

displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))#pygame.FULLSCREEN

toQuit = False 
menu = True
settings = False
default = {
    'players':[],#[['PLAYER#','COLOUR NAME'],['player2','RED']],
    'randomMap':True,
    'isMap':True,
    'chance':5,
    'powerUps':False,
    'speed':8,
    'maps':False,
    'breakOnWall':False
    }

colors = ['red','blue','yellow','Lblue']


#main menu
while not toQuit:
    pos = (0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            toQuit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
    if menu:
        out = runMenu(screen,pos,pygame.key.get_pressed())
        if out[0] == '':
            pass
        elif out[0] == 'start':
            menu = False
            if out[1]['p1'] == 1:
                default['players'].append(['player1',0])
            if out[1]['p2'] == 1:
                default['players'].append(['player2',1])
            if out[1]['p3'] == 1:
                default['players'].append(['player3',2])
            #default = startSettings(default)
            startGame(default)
            menu = True
        elif out[0] == 'quit':
            print('HELLOWORLDWWW')
            break
        
    pygame.display.flip()  

pygame.quit()
quit()

