import pygame as pygame
import random
from utilities import Character, Enemy
import colors
pygame.init()

win_width, win_height = 500, 500
win = pygame.display.set_mode((win_width, win_height))

# title and icon
pygame.display.set_caption("Space Wars")
icon = pygame.image.load('./media/game icon/alien.png')
pygame.display.set_icon(icon)

# ArcadeShip
initialX, initialY = 250, 380
ArcadeShipImg = pygame.image.load('./media/shipimg64.png')
ArcadeShip = Character(initialX, initialY, 64, 64, ArcadeShipImg)


# ArcadeShip Actions
def ShowArcadeShip():
    win.blit(ArcadeShip.Img, (ArcadeShip.posX, ArcadeShip.posY))


# Enemies
EnemyImg = pygame.image.load('./media/enemy32.png')
enemy = Enemy(32, 32, EnemyImg, win_width, win_height/2)


# Enemy Actions
def ShowEnemy():
    win.blit(enemy.Img, (enemy.posX, enemy.posY))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()
    win.fill(colors.Black)

    # refreshing movement thousand time, for better movement
    # set loop to 1, and remove move_right, move_left..etc parameters
    # for lower spec device
    for _ in range(1000):
        ''' arcade ship movement '''
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_RIGHT]:
            if ArcadeShip.posX + ArcadeShip.width < win_width:
                ArcadeShip.move_right(0.003)
        if key_press[pygame.K_LEFT]:
            if ArcadeShip.posX > 0:
                ArcadeShip.move_left(0.003)
        if key_press[pygame.K_UP]:
            if ArcadeShip.posY > 0:
                ArcadeShip.move_up(0.003)
        if key_press[pygame.K_DOWN]:
            if ArcadeShip.posY + ArcadeShip.height < win_height:
                ArcadeShip.move_down(0.003)
    enemy.move()
    ShowArcadeShip()
    ShowEnemy()
    pygame.display.update()
