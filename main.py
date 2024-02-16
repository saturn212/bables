import random

import pygame as pg
import sys
import os
from random import randint

import pygame.sprite

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

        if pg.sprite.spritecollide(self, enemy_group, False):
            enemy = pg.sprite.spritecollide(self, enemy_group, False)[0]
            if enemy.image.get_height() <= self.image.get_height():
                enemy.kill()
                Enemy_1.food.eyes.kill()
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
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.timer_moove = 0
        self.pos = self.rect.center
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        self.food = None
        self.agr = False

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
            self.eyes.pos = self.rect.center
            self.eyes.image = pygame.transform.rotozoom(self.eyes.image, 0, 1.05)
            self.eyes.rect = self.eyes.image.get_rect()
            self.eyes.rect.center = self.eyes.pos
            self.agr = False
        else:
            self.agr = False

        if self.agr:
            if self.rect.center[0]>self.food.rect.center[0]:
                self.speed_x = -1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1
            else:
                self.speed_x = 1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1

class Enemy_2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.food =None
        self.agr = False
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
        if self.timer_moove / FPS > 3 and self.agr == False:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(-1, 1)
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
            self.eyes.pos = self.rect.center
            self.eyes.image = pygame.transform.rotozoom(self.eyes.image, 0, 1.05)
            self.eyes.rect = self.eyes.image.get_rect()
            self.eyes.rect.center = self.eyes.pos
            self.agr = False
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

        if self.agr:
            if self.rect.center[0]>self.food.rect.center[0]:
                self.speed_x = -1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1
            else:
                self.speed_x = 1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1



class Food(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = food_image
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 1190)
        self.rect.y = randint(10, 1190)

class Eyes(pygame.sprite.Sprite):
    def __init__(self, pos, block, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = eyes_image
        self.block = block
        self.rect = self.image.get_rect()

        self.rect.center = pos
        self.type = type
        self.pos = pos
    def update(self):
        self.rect.center = self.block.rect.center
        if self.type == 1:
            if(
                    pygame.sprite.spritecollide(self, food_group,  False)
                    and self.block.agr == False
            ):
                food = pygame.sprite.spritecollide(self, food_group, False)[0]
                self.block.agr = True
                self.block.food = food

        if self.type == 2:
            if(
                    (pygame.sprite.spritecollide(self, enemy_group,  False) or pygame.sprite.spritecollide(self, player_group, False))
                    and self.block.agr == False
            ):
                enemy = pygame.sprite.spritecollide(self, enemy_group, False)[0]
                self.block.agr = True
                self.block.food = enemy


class Spawn():
    def __init__(self):
        self.timer = 0

    def update(self):
        if len(food_group) < 10:
            food = Food()
            food_group.add(food)
        if len(enemy_group) < 10:
            pos = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
            enemy = Enemy_1(pos)
            eyes = Eyes(enemy.rect.center, enemy, 1)
            enemy.eyes = eyes
            eyes_group.add(eyes)
            enemy_group.add(enemy)
        if len(enemy_2_group) < 5:

            enemy = Enemy_2()
            eyes = Eyes(enemy.rect.center, enemy, 1)
            enemy.eyes = eyes
            eyes_group.add(eyes)
            enemy_2_group.add(enemy)



def lvlGAME():
    screen.fill(GRAY)
    player_group.update()
    player_group.draw(screen)
    eyes_group.update()
    eyes_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    enemy_2_group.update()
    enemy_2_group.draw(screen)
    food_group.update()
    food_group.draw(screen)
    spawner.update()
    pg.display.update()


def restart():
    global food_group, enemy_group, enemy_2_group, player_group, spawner, eyes_group
    player_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    enemy_2_group = pg.sprite.Group()
    food_group = pg.sprite.Group()
    player = Player(player_image, (200, 640))
    player_group.add(player)
    spawner = Spawn()
    eyes_group = pg.sprite.Group()

restart()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    lvlGAME()

    clock.tick(FPS)