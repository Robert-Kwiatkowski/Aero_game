import pygame, sys

from pygame.locals import *

pygame.init() #rozpocznij "dzialanie" kodu pygame

DISPLAYSURF = pygame.display.set_mode((800, 600)) # okno gry przechowane w zmiennej displaysurf
keys = [False, False, False, False]
playerpos = [400, 300]

pygame.display.set_caption('Aero Game!') #nazwa okna
player = pygame.image.load("statek.bmp") #tworzymy zmienna przechowujaca obraz statku
while True:  # main game loop
    DISPLAYSURF.blit(player, playerpos)  # dodajemy statek do tła gry
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #zamykaj najpierw "kod" pygame przed koncem aplikacji
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    if keys[0] == True:
        playerpos[1]-=0.2
        DISPLAYSURF.fill(0)
        DISPLAYSURF.blit(player, playerpos)
    elif keys[2] == True:
        playerpos[1]+=0.2
        DISPLAYSURF.fill(0)
        DISPLAYSURF.blit(player, playerpos)
    if keys[1] == True:
        playerpos[0]-=0.2
        DISPLAYSURF.fill(0)
        DISPLAYSURF.blit(player, playerpos)
    elif keys[3] == True:
        playerpos[0]+=0.2
        DISPLAYSURF.fill(0)
        DISPLAYSURF.blit(player, playerpos)
    pygame.display.update()








