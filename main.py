import pygame as pygame
import random
from utilities import Character, Enemy, Bullet
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

# bullet
bullet_img = pygame.image.load('./media/bullet.png').convert_alpha()

# bullet Actions
all_bullets = []


def Fire_Bullet(posX, posY):
    ''' 
    @param:
        posX, posY -> coordinates of bullet when fired 
    doc:
        Instance of bullet fired is added to all_bullet list
    '''
    posX += 24
    all_bullets.append(Bullet(posX, posY, 16, 16, bullet_img))


def remove_bullet(arr: list, bullet_index: int) -> None:
    arr.pop(bullet_index)


def show_bullets():
    '''
     using  `all_bullets` list, to show bullets, and move
    '''
    for index, bullet in enumerate(all_bullets):
        win.blit(bullet.Img, (bullet.posX, bullet.posY))
        # remove bullet from all_bullet when move out of frame
        if bullet.posY + bullet.height < 0:
            remove_bullet(all_bullets, index)
        else:
            bullet.move_up(1)


# ArcadeShip
initialX, initialY = 250, 380
ArcadeShipImg = pygame.image.load('./media/shipimg64.png').convert_alpha()
ArcadeShip = Character(initialX, initialY, 64, 64, ArcadeShipImg)

loop_rate = 1000
ship_movement_rate = (1/loop_rate) * 3

# ArcadeShip Actions


def ShowArcadeShip():
    win.blit(ArcadeShip.Img, (ArcadeShip.posX, ArcadeShip.posY))


# Enemies
EnemyImg = pygame.image.load('./media/enemy32.png').convert_alpha()
enemy = Enemy(32, 32, EnemyImg, win_width, win_height/2)
no_of_enemy = 10 #win_width//enemy.width
Enemy_list = [Enemy(32, 32, EnemyImg, win_width, win_height//3) for _ in range(no_of_enemy)]


# Enemy Actions
def ShowEnemy():
    for enemy in Enemy_list:
        win.blit(enemy.Img, (enemy.posX, enemy.posY))
        enemy.move()



run = True
while run:
    win.fill(colors.Black)
    win.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            # if spacebar is pressed, fire bullet
            if event.key == pygame.K_SPACE:
                Fire_Bullet(ArcadeShip.posX, ArcadeShip.posY)

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

    show_bullets()
    ShowArcadeShip()
    ShowEnemy()
    pygame.display.update()
