import pygame as pygame
import random
from utilities import Character, Enemy
import colors
pygame.init()

win_width, win_height = 700, 500
win = pygame.display.set_mode((win_width, win_height))

# title and icon
pygame.display.set_caption("Space Wars")
icon = pygame.image.load('./media/game icon/alien.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('./media/background.jpg').convert_alpha()
background = pygame.transform.scale(background, (win_width, win_height))

# ArcadeShip
initialX, initialY = 250, 380
ArcadeShipImg = pygame.image.load('./media/shipimg64.png')
ArcadeShip = Character(initialX, initialY, 64, 64, ArcadeShipImg)

loop_rate = 1000
ship_movement_rate = (1/loop_rate) * 3

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
    win.fill(colors.Black)
    win.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()

    # refreshing movement thousand time, for better movement
    # set loop_rate to 1,
    for _ in range(loop_rate):
        ''' arcade ship movement '''
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_RIGHT]:
            if ArcadeShip.posX + ArcadeShip.width < win_width:
                ArcadeShip.move_right(ship_movement_rate)
        if key_press[pygame.K_LEFT]:
            if ArcadeShip.posX > 0:
                ArcadeShip.move_left(ship_movement_rate)
        if key_press[pygame.K_UP]:
            if ArcadeShip.posY > 0:
                ArcadeShip.move_up(ship_movement_rate)
        if key_press[pygame.K_DOWN]:
            if ArcadeShip.posY + ArcadeShip.height < win_height:
                ArcadeShip.move_down(ship_movement_rate)

    enemy.move()
    ShowArcadeShip()
    ShowEnemy()
    pygame.display.update()
