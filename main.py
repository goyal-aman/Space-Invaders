from typing import List
import pygame as pygame
import sys
import random
from utilities import Character, Enemy, Bullet, Button
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
    posX += 24  # centering bullet with respect to ship
    PlaySound(bullet_sound, play_sound_effect)  # laser sound on bullet fire
    all_bullets.append(Bullet(posX, posY, 16, 16, bullet_img))

def remove_bullet(all_bullet: list, bullet_index: int) -> None:
    '''  Takes all_bullets list, and remove bullet object at bullet_index   '''
    all_bullet.pop(bullet_index)

def ShowBullests():
    '''
     using  `all_bullets` list, to show bullets, and move
    
    @algorithm:
    -display all bullet object in all_bullets list
    - remove them if they move out of frame or move them up
    '''
    for index, bullet in enumerate(all_bullets):
        win.blit(bullet.Img, (bullet.posX, bullet.posY))
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

def newEnemy():
    ''' returns new enemy object, with random (x,y) coords '''
    return Enemy(32, 32, EnemyImg, win_width, win_height/2)

no_of_enemy = 10  # win_width//enemy.width
Enemy_list = [newEnemy() for _ in range(no_of_enemy)]

# Enemy Actions
def ShowEnemy():
    '''
    @algorithm:
    -show enemy object from `Enemy_list`
    -move enemy 
    '''
    for enemy in Enemy_list:
        win.blit(enemy.Img, (enemy.posX, enemy.posY))
        enemy.move()

# Leveup
level = 1
def LevelUp():
    '''
    @algorithm:
    -> if all enemies are destroyed ( len(Enemy_list)==0 )
        then, add 50% more enemy, 
              increment `level`
              reset ArcadeShip to initial position
    '''
    global Enemy_list, no_of_enemy, level
    if len(Enemy_list)==0:
        level+=1
        no_of_enemy = no_of_enemy+ no_of_enemy//2
        Enemy_list = [newEnemy() for _ in range(no_of_enemy)]
        ArcadeShip.posX = initialX
        ArcadeShip.posY = initialY

# Collisions
def BulletEnemyCollision(enemy_list: List[Enemy], bullet_list: List[Bullet]) -> bool:
    '''
    enemy_list : list of all Enemy Objects
    bullet_list : list of all Bullet Object

    @algorithm:
    -check if any bullet has same coordinates as any enemy:
        if yes:
            remove enemy from enemy list
            remove bullet from bullet list
            increment score
    '''
    for enemy_index, enemy in enumerate(enemy_list):
        for bullet_index, bullet in enumerate(bullet_list):
            if bullet.posX >= enemy.posX and bullet.posX <= enemy.posX+enemy.width:
                if bullet.posY >= enemy.posY and bullet.posY <= enemy.posY+enemy.height:
                    # PlaySound(collision_sound, play_sound_effect)
                    collided_enemy = enemy_list.pop(enemy_index)
                    collided_bullet = bullet_list.pop(bullet_index)
                    ArcadeShip.increase_score()

                    # adding two more enemy for each enemy destroyed
                    # enemy_list.append(newEnemy())
                    # enemy_list.append(newEnemy())

def ShipEnemyCollision(enemy_list: List[Enemy], Ship: Character):
    '''
    enemy_list : list of all Enemy Objects
    Ship : ArcadeShip object

    @algorithm
    -check if any enemy has same coordinates as ArcadeShip:
        if yes:
            return True
    '''
    for enemy_index, enemy in enumerate(enemy_list):
        if enemy.posX >= Ship.posX and enemy.posX <= Ship.posX+Ship.width:
            if enemy.posY >= Ship.posY and enemy.posY <= Ship.posY+Ship.height:
                return True #gameOver('Collision With Enemy')



# message to print
def message_to_print(message: str, color: tuple, coordinates: tuple, bold=0):
    '''
    message : message to print
    color   : color of the message | rgb
    coordinates : (x,y) coordinates where to print/render
    bold : default value 0 (no bold)
    '''
    font = pygame.font.SysFont(None, 32,bold)
    text = font.render(message, True, color)
    win.blit(text, coordinates)



# gameover function
def gameOver(reason: str):
    win.blit(background, (0,0))
    message_to_print(f"You Lost. Your Score: {ArcadeShip.show_score()}", colors.White, (25, 25))
    message_to_print("Press any key to continue...", colors.White, (25,50))
    pygame.display.update()
    pygame.time.wait(2000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                pygame.quit()


        pygame.display.update()
    


def WelcomeScreen():
    win.blit(background, (0,0))
    pygame.display.update()
    start_button = Button(colors.Lime, win_width//2-75, win_height//3, 159,50, 'Start',32,50, 15)
    quit_button = Button(colors.Red, win_width//2-75, start_button.posY+start_button.height+2, 159,50, 'Quit',32, 50, 15)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            # gets mouse position
            mouse_pos = pygame.mouse.get_pos()

            # start button
            if start_button.ishover(mouse_pos):
                start_button.color=colors.LimeGreen
            else:
                start_button.color=colors.Lime
            
            # quit button
            if quit_button.ishover(mouse_pos):
                quit_button.color=colors.FireBrick
            else:
                quit_button.color= colors.Red
            


            # mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.ishover(mouse_pos):
                    pygame.time.wait(500)
                    gameLoop()
                if quit_button.ishover(mouse_pos):
                    pygame.quit()
            

        start_button.draw(win, (255, 255, 255))
        quit_button.draw(win, (255, 255, 255))
        pygame.display.update()

# main game function
def gameLoop():
    win.blit(background, (0,0))
    message_to_print('Destroy Most Enemies', colors.Red, (200, win_height//3), 1)
    pygame.display.update()
    pygame.time.wait(2000)

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
            # if key_press[pygame.K_UP]:
            #     if ArcadeShip.posY > 0:
            #         ArcadeShip.move_up(ship_movement_rate)
            # if key_press[pygame.K_DOWN]:
            #     if ArcadeShip.posY + ArcadeShip.height < win_height:
            #         ArcadeShip.move_down(ship_movement_rate)

        ShowBullests()
        ShowArcadeShip()
        ShowEnemy()

        LevelUp()

        # enemy and bullet collison detection and action
        BulletEnemyCollision(Enemy_list, all_bullets)
        if ShipEnemyCollision(Enemy_list, ArcadeShip):
            gameOver("Collided with ship")
        
        # showing scores
        message_to_print(f"Score: {ArcadeShip.show_score()}", colors.White, (10, 10))
        message_to_print(f"Level: {level}", colors.White, (win_width-100, 10))

        pygame.display.update()

WelcomeScreen()
