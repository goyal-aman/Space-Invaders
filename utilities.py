class Character:
    '''
    posX, posY -> (x, y) cords
    widht, height -> (width, height) of character
    '''

    def __init__(self, posX, posY, width, height, character_img):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.Img = character_img

    def move_right(self, dx=0.1):
        self.posX += dx

    def move_left(self, dx=0.1):
        self.posX -= dx

    def move_up(self, dy=0.1):
        self.posY -= dy

    def move_down(self, dy=0.1):
        self.posY += dy

    def move(self, dx, dy):
        self.posX += dx
        self.posY += dy


class Enemy:
    import random
    import math
    '''
    posX, posY -> (x, y) cords
    widht, height -> (width, height) of character
    character_img -> image of character (python.pygame image object)
    Hrange, Vrange -> horizontal and vertical range where enemy can roam
    '''

    def __init__(self, width, height, character_img, Hrange, Vrange):
        self.posX = (self.random.randint(width, Hrange-width)//width)*width
        self.posY = (self.random.randint(0, Vrange)//height)*height
        self.width = width
        self.height = height
        self.Img = character_img
        self.Hrange = Hrange
        self.Vrange = Vrange
        self.dx = self.random.randint(5, 10)/10
        self.dy = self.math.floor(self.width)

    def move(self):
        # Horizontal movement logic
        # print(self.posX, self.posY)
        if self.posX+self.width > self.Hrange or self.posX <= 0:
            self.dx *= -1
            self.posY += self.dy
        self.posX += self.dx


class Bullet(Character):
    '''
    posX, posY -> (x, y) cords
    widht, height -> (width, height) of character
    character_img -> image of character (python.pygame image object)
    Hrange, Vrange -> horizontal and vertical range where enemy can roam
    state -> `to be defined later`
    '''

    def __init__(self, posX, posY, width, height, character_img, dy=1, state=None):
        Character.__init__(self, posX, posY, width, height, character_img)
        self.state = state
        self.dy = dy