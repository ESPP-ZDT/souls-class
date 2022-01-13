import pygame as pg, random
from pygame_functions import *
from hero import *
class BossRonexadas():
    def __init__(self):
        self.ronexadas = makeSprite(('data/img/apparotion.png'))
        self.deadronexadas = addSpriteImage(self.ronexadas,'data/img/death coin.png')
        transformSprite(self.ronexadas, 90, 1)
        self.ronexadas.x = 320  # w jakim miejscu sie spawnuje x
        self.ronexadas.y = 800  # w jakim miejscu sie spawnuje y
        self.ronexadas.xspeed = random.randint(1, 2) / 2
        self.ronexadas.yspeed = random.randint(1, 3) / 2
        self.ronexadas_speed = 3
        moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
        self.min_dist = 1000
        showSprite(self.ronexadas)
        self.ronexadas_hp = 100
        self.id = id
        self.heroxpos = hero_x_pos
        self.heroypos = hero_y_pos

    def get_hero_pos(self):
        self.heroxpos= hero_x_pos
        self.heroypos= hero_y_pos
    def move(self):
        self.ronexadas.x += self.ronexadas.xspeed
        self.ronexadas.y += self.ronexadas.yspeed
        self.get_hero_pos()
        delta_x = self.heroypos - self.ronexadas.y
        delta_y = self.heroxpos - self.ronexadas.x

        if abs(delta_x) <= self.min_dist and abs(delta_y) <= self.min_dist:
            enemy_move_x = abs(delta_x) > abs(delta_y)
            if abs(delta_x) > self.ronexadas.x and abs(delta_x) > self.ronexadas.y:
                enemy_move_x = random.random() < 0.5
            enemy_move_x = random.random() < 0.5
            if enemy_move_x:
                self.ronexadas.x += min(delta_x, self.ronexadas_speed) if delta_x > 0 else max(delta_x, -self.ronexadas_speed)
            else:
                self.ronexadas.y += min(delta_y, self.ronexadas_speed) if delta_y > 0 else max(delta_y, -self.ronexadas_speed)

        moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
    def update(self):
        self.move()


