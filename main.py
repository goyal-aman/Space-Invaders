import pygame as pygame
from utilities import Character
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
ArcadeShipImg = pygame.image.load('./media/ShipImg.png')
ArcadeShip = Character(initialY, initialY, 50, 50, ArcadeShipImg)
ArcadeShip.Img = pygame.transform.scale(ArcadeShipImg, (50, 50))


# ArcadeShip Actions
def ShowArcadeShip():
    win.blit(ArcadeShip.Img, (ArcadeShip.posX, ArcadeShip.posY))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()
    win.fill(colors.Black)

    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_RIGHT]:
        if ArcadeShip.posX + 50 < win_width:
            ArcadeShip.move_right()
    if key_press[pygame.K_LEFT]:
        if ArcadeShip.posX > 0:
            ArcadeShip.move_left()
    if key_press[pygame.K_UP]:
        if ArcadeShip.posY > 0:
            ArcadeShip.move_up()
    if key_press[pygame.K_DOWN]:
        if ArcadeShip.posY + 50 < win_height:
            ArcadeShip.move_down()

    ShowArcadeShip()
    pygame.display.update()
