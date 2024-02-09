import random

import pygame as pg
import sys
import os
from random import randint

pg.init()
WIDTH = 1200
HEIGHT = 800
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

font = pg.font.SysFont('aria', 30)
BLaCK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

from load import *


class Player(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = "top"
        self.speed = 5

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_w] and self.rect.top >= 0:

            self.rect.y -= self.speed
            self.dir = "top"
        elif key[pg.K_s] and self.rect.bottom <= 800:

            self.rect.y += self.speed
            self.dir = "bottom"

        if key[pg.K_a] and self.rect.left >= 0:

            self.rect.x -= self.speed
            self.dir = "left"

        elif key[pg.K_d] and self.rect.right <= 1200:

            self.rect.x += self.speed
            self.dir = "right"

        if pg.sprite.spritecollide(self, food_group, True):
            self.image = pg.transform.rotozoom(self.image, 0, 1.05)
            self.pos = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = self.pos


        if pg.sprite.spritecollide(self, enemy_2_group, False):
            enemy = pg.sprite.spritecollide(self, enemy_2_group, False)[0]
            if enemy.image.get_height() <= self.image.get_height():
                enemy.kill()
                self.image = pg.transform.rotozoom(self.image, 0, 1.05)
                self.pos = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = self.pos


class Enemy_1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.timer_moove = 0
        self.pos = self.rect.center
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

        self.rect.x = randint(10, 1190)
        self.rect.y = randint(10, 1190)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.timer_moove += 1
        if self.timer_moove / FPS > 3:
            self.speed_x = random.randint(-5, 5)
            self.speed_y = random.randint(-5, 5)
            self.timer_moove = 0
        if self.rect.left < 0:
            self.speed_x *= -1
        if self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > HEIGHT:
            self.speed_y *= -1

        if pg.sprite.spritecollide(self, food_group, True):
            self.image = pg.transform.rotozoom(self.image, 0, 1.05)
            self.pos = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = self.pos



class Enemy_2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_2_image
        self.timer_moove = 0
        self.rect = self.image.get_rect()
        self.pos = self.rect.center
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

        self.rect.x = randint(10, 1190)
        self.rect.y = randint(10, 1190)
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.timer_moove += 1
        if self.timer_moove / FPS > 3:
            self.speed_x = random.randint(-5, 5)
            self.speed_y = random.randint(-5, 5)
            self.timer_moove = 0
        if self.rect.left < 0:
            self.speed_x *= -1
        if self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top >= 0:
            self.speed_y *= -1
        if self.rect.bottom <= HEIGHT:
            self.speed_y *= -1

        if pg.sprite.spritecollide(self, food_group, True):
            self.image = pg.transform.rotozoom(self.image, 0, 1.05)
            self.pos = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

        if pg.sprite.spritecollide(self, enemy_group, False):
            enemy_2 = pg.sprite.spritecollide(self, enemy_group, False)[0]
            if enemy_2.image.get_height() <= self.image.get_height():
                enemy_2.kill()
                self.image = pg.transform.rotozoom(self.image, 0, 1.05)
                self.pos = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

        if pg.sprite.spritecollide(self, player_group, False):
            player = pg.sprite.spritecollide(self, player_group, False)[0]
            if player.image.get_height() <= self.image.get_height():
                player.kill()
                self.image = pg.transform.rotozoom(self.image, 0, 1.05)
                self.pos = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = self.pos



class Food(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = food_image
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 1190)
        self.rect.y = randint(10, 1190)


class Spawn():
    def __init__(self):
        self.timer = 0

    def update(self):
        if len(food_group) < 20:
            food = Food()
            food_group.add(food)
        if len(food_group) < 20:

            enemy = Enemy_1()
            enemy_group.add(enemy)
        if len(food_group) < 20:

            enemy = Enemy_2()
            enemy_2_group.add(enemy)



def lvlGAME():
    screen.fill(GRAY)
    player_group.update()
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    enemy_2_group.update()
    enemy_2_group.draw(screen)
    food_group.update()
    food_group.draw(screen)
    spawner.update()
    pg.display.update()


def restart():
    global food_group, enemy_group, enemy_2_group, player_group, spawner
    player_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    enemy_2_group = pg.sprite.Group()
    food_group = pg.sprite.Group()
    player = Player(player_image, (200, 640))
    player_group.add(player)
    spawner = Spawn()


restart()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    lvlGAME()

    clock.tick(FPS)
