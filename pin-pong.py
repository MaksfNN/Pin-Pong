from random import randint
from pygame import *
from time import time as timer
mixer.init()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
FPS = 60
game = True
font.init()
font1 = font.SysFont("Arial", 34)
lose1 = font1.render("Игрок 1 проиграл ", 1, (255, 255, 255))
win1 = font1.render("Игрок 2 выйграл ", 1, (255, 255, 255))
lose2 = font1.render("Игрок 2 проиграл ", 1, (255, 255, 255))
win2 = font1.render("Игрок 1 выйграл ", 1, (255, 255, 255))
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
speed_x = 3
speed_y = 3
Sprite_1 = Player("player.png", 90, 230, 10, 35, 95)
Sprite_2 = Player("player.png", 600, 230, 10, 35, 95)
ball = GameSprite("ball1.png", 150, 150, 6, 40, 40)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0 or ball.rect.y > win_height - 40:
            speed_y *= -1
        if sprite.collide_rect(Sprite_1, ball):
            speed_x *= -1
        if sprite.collide_rect(Sprite_2, ball):
            speed_x *= -1
        window.blit(background, (0, 0))
        text = font1.render("Игрок 1", 1, (255, 255, 255))
        window.blit(text, (15, 10))
        text2 = font1.render("Игрок 2", 1, (255, 255, 255))
        window.blit(text2, (550, 10))
        Sprite_1.update1()
        Sprite_1.reset()
        Sprite_2.update()
        Sprite_2.reset()
        ball.reset()
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (150, 250))
            window.blit(win1, (150, 200))
        if ball.rect.x > win_width - 40:
            finish = True
            window.blit(lose2, (300, 250))
            window.blit(win2, (300, 200))
    clock.tick(FPS)
    display.update()