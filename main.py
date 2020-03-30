from typing import List
import pygame as pygame
import sys
import random
from utilities import Character, Enemy, Bullet
import colors
pygame.init()

# window variable
win_width, win_height = 700, 500
win = pygame.display.set_mode((win_width, win_height))

# title and icon
pygame.display.set_caption("Space Wars")
icon = pygame.image.load('./media/image/game icon/alien.png')
pygame.display.set_icon(icon)

# Background Image
background = pygame.image.load('./media/image/Background.jpg').convert_alpha()
background = pygame.transform.scale(background, (win_width, win_height))



# BackGround Music
pygame.mixer.music.load('./media/music/background.wav')
play_background_music = True
play_sound_effect = True
if play_background_music:
    pygame.mixer.music.play(-1)

# Sound Effects
bullet_sound = pygame.mixer.Sound('./media/music/laser.wav')
collision_sound = pygame.mixer.Sound('./media/music/explosion.wav')

def PlaySound(sound_name:str, isplaying:bool):
    if isplaying:
        sound_name.play()



# Bullet
bullet_img = pygame.image.load('./media/image/bullet.png').convert_alpha()
all_bullets = []

def Fire_Bullet(posX, posY):
    '''
    @param:
        posX, posY -> coordinates of bullet when fired
    doc:
        Instance of bullet fired is added to all_bullet list
    '''
    posX += 24
    PlaySound(bullet_sound, play_sound_effect)
    all_bullets.append(Bullet(posX, posY, 16, 16, bullet_img))

def remove_bullet(arr: list, bullet_index: int) -> None:
    arr.pop(bullet_index)

def ShowBullests():
    '''
     using  `all_bullets` list, to show bullets, and move
    '''
    for index, bullet in enumerate(all_bullets):
        win.blit(bullet.Img, (bullet.posX, bullet.posY))
        # remove bullet from all_bullet when move out of frame
        if bullet.posY + bullet.height < 0:
            remove_bullet(all_bullets, index)
        else:
            bullet.move_up(4)



# ArcadeShip
initialX, initialY = 250, 380
ArcadeShipImg = pygame.image.load('./media/image/shipimg64.png').convert_alpha()
ArcadeShip = Character(initialX, initialY, 64, 64, ArcadeShipImg)

loop_rate = 1000
ship_movement_rate = (1/loop_rate) * 3

def ShowArcadeShip():
    win.blit(ArcadeShip.Img, (ArcadeShip.posX, ArcadeShip.posY))



# Enemies
EnemyImg = pygame.image.load('./media/image/enemy32.png').convert_alpha()
enemy = Enemy(32, 32, EnemyImg, win_width, win_height/2)
no_of_enemy = 10  # win_width//enemy.width
Enemy_list = [Enemy(32, 32, EnemyImg, win_width, win_height//3)
              for _ in range(no_of_enemy)]

# Enemy Actions
def ShowEnemy():
    for enemy in Enemy_list:
        win.blit(enemy.Img, (enemy.posX, enemy.posY))
        enemy.move()



# Collisions
def BulletEnemyCollision(enemy_list: List[Enemy], bullet_list: List[Bullet]) -> bool:
    '''
    enemy_list : list of all Enemy Objects
    bullet_list : list of all Bullet Object
    '''
    for enemy_index, enemy in enumerate(enemy_list):
        for bullet_index, bullet in enumerate(bullet_list):
            if bullet.posX >= enemy.posX and bullet.posX <= enemy.posX+enemy.width:
                if bullet.posY >= enemy.posY and bullet.posY <= enemy.posY+enemy.height:
                    PlaySound(collision_sound, play_sound_effect)
                    collided_enemy = enemy_list.pop(enemy_index)
                    collided_bullet = bullet_list.pop(bullet_index)
                    ArcadeShip.increase_score()

def ShipEnemyCollision(enemy_list: List[Enemy], Ship: Character):
    for enemy_index, enemy in enumerate(enemy_list):
        if enemy.posX >= Ship.posX and enemy.posX <= Ship.posX+Ship.width:
            if enemy.posY >= Ship.posY and enemy.posY <= Ship.posY+Ship.height:
                gameOver('Collision With Enemy')



# message to print
font = pygame.font.SysFont(None, 32, 0)
def message_to_print(message: str, color: tuple, coordinates: tuple):
    text = font.render(message, True, color)
    win.blit(text, coordinates)



# gameover function
def gameOver(reason: str):
    print(f"Game Over: {reason}")


# main game function
run = True
while run:
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

    ShowBullests()
    ShowArcadeShip()
    ShowEnemy()

    # enemy and bullet collison detection and action
    BulletEnemyCollision(Enemy_list, all_bullets)
    ShipEnemyCollision(Enemy_list, ArcadeShip)
    
    # showing scores
    message_to_print(f"Score: {ArcadeShip.show_score()}", colors.White, (10, 10))
    
    pygame.display.update()
