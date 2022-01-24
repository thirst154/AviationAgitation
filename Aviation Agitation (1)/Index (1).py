import pygame
from MENU import runMenu, runSettings
from game import startGame
pygame.init()
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))

toQuit = False 
menu = True
settings = False
default = {
    'numberOfPlayers':2,
    'randomMap':True,
    'isMap':True,
    'chance':5,
    'powerUps':False
    }


#main menu
while not toQuit:
    pos = (0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            toQuit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
    if menu:
        if (out := runMenu(screen,pos)) == '':
            pass
        elif out == 'settings':
            menu = False
            settings = True
            print("achived")
        elif out == 'start':
            menu = False
            startGame(default)
            pass
        elif out == 'quit':
            toQuit = True
    if settings:
        if (out :=runSettings(screen,pos,displayWidth,displayHeight)) == 'menu':
            menu=True
            settings = False
        else:
            pass
    
    pygame.display.flip()  

pygame.quit()
quit()
