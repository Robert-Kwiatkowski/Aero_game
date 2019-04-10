# 1 - Import library
import pygame
from pygame.locals import *
import math
import random



# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Aero Game!')
keys = [False, False, False, False]
playerpos = [100, 100]
acc = [0, 0]
arrows = []
badtimer = 200
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194
pygame.mixer.init()

# 3 - Load image
player = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/statek.bmp")
grass = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/mglawica.jpg")
arrow = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/pocisk.bmp")
badguyimg1 = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/kamyk.png")
badguyimg = badguyimg1
healthbar = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/healthbar.png")
health = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/health.png")
gameover = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/gameover.png")
youwin = pygame.image.load("C:/Users/rober/desktop/gra-pjp2/youwin.png")
playerect=pygame.Rect(player.get_rect())


# 3.1 - Load audio
hit = pygame.mixer.Sound("C:/Users/rober/desktop/gra-pjp2/eksplozja.wav")
shoot = pygame.mixer.Sound("C:/Users/rober/desktop/gra-pjp2/pocisk.wav")
hit.set_volume(0.05)
shoot.set_volume(0.05)
#ygame.mixer.music.load('resources/audio/moonlight.wav')
#pygame.mixer.music.play(-1, 0.0)
#pygame.mixer.music.set_volume(0.25)

# 4 - keep looping through
running = 1
exitcode = 0
while running:
    badtimer -= 1
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the player on the screen at X:100, Y:100
    for x in range(int(width / width)):
        for y in range(int(height / height)):
            screen.blit(grass, (x * 100, y * 100))
        pass #poprawka po zlym kodzie??

    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - Draw projectiles
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    # 6.3 - Draw asteroids


    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        badtimer = 100 - (badtimer1)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5



    index = 0

    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        playerect.top = playerpos[1]
        playerect.left = playerpos[0]

        #while badguy[1] == playerpos[1] and badguy[0] == playerpos[0]:
           # healthvalue -= random.randint(5, 20)
            #badguys.pop(index)

        #if badguy[1] == playerpos[1]:
            #if badguy[0] == playerpos[0]:
               # healthvalue -= random.randint(5, 20)
                #badguys.pop(index)
            # kolizjatest


        badguy[0] -= 1
        # 6.3.1 - Make vectors from asteroids
        # 6.3.1 - Lose health
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        playerect.top = playerpos[1]
        playerect.left = playerpos[0]
        if badrect.colliderect(playerect):
            acc[0] += 1
            badguys.pop(index)
            healthvalue -= random.randint(5, 20)
            hit.play()
        if badrect.left<10:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # 6.3.3 - Next bad guy
        # 6.3.2 - Check for collisions
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)
                hit.play()
            index1 += 1
        # 6.3.3 - Next asteroid
        index += 1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
    # 6.4 - Draw clock
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((9000-pygame.time.get_ticks())/6), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)

    # 6.5 - Draw health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))


    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32,
                 playerpos1[1] + 32])
            shoot.play()

    # 9 - Move player
    if keys[0]:
        playerpos[1] -= 1
    elif keys[2]:
        playerpos[1] += 1
    if keys[1]:
        playerpos[0] -= 1
    elif keys[3]:
        playerpos[0] += 1

    # 10 - Win/Lose check
    if pygame.time.get_ticks() >= 9000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0

# 11 - Win/lose display
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    screen.blit(gameover, (0,0))

else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    screen.blit(youwin, (0,0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
