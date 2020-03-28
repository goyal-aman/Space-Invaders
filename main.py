import pygame as pygame
pygame.init()

win_width, win_height = 500,500
win = pygame.display.set_mode((win_width, win_height))

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()
    
    pygame.display.update()
