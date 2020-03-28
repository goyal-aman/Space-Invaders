class Character:
    def __init__(self, posX, posY, width, height, ship_img):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.Img = ship_img

    def move_right(self, dx=0.1):
        self.posX += dx

    def move_left(self, dx=0.1):
        self.posX -= dx

    def move_up(self, dy=0.1):
        self.posY -= dy

    def move_down(self, dy=0.1):
        self.posY += dy

    def move_character(self, dx, dy):
        self.posX += dx
        self.posY += dy
