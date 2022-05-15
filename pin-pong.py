from random import randint
from pygame import *
from time import time as timer
mixer.init()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
FPS = 60
game = True
clock = time.Clock()
display.set_caption("Пинг-понг")
background = transform.scale(image.load("pii.jpg"), (win_width, win_height))
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 95:
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 95:
            self.rect.y += self.speed
Sprite_1 = Player("player.png", 90, 230, 10, 35, 95)
Sprite_2 = Player("player.png", 600, 230, 10, 35, 95)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        Sprite_1.update()
        Sprite_1.reset()
        Sprite_2.update1()
        Sprite_2.reset()
    clock.tick(FPS)
    display.update()