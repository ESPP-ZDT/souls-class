import pygame as pg, random
from pygame_functions import *
from hero import *
class BossRonexadas():
    def __init__(self, hero):
        self.ronexadas = makeSprite(('data/img/apparotion.png'))
        self.deadronexadas = addSpriteImage(self.ronexadas,'data/img/death coin.png')
        showSprite(self.ronexadas)
        transformSprite(self.ronexadas, 90, 1)
        self.ronexadas.x = 340  # w jakim miejscu sie spawnuje x
        self.ronexadas.y = 0  # w jakim miejscu sie spawnuje y
        self.ronexadas.xspeed = 0
        self.ronexadas.yspeed = 0
        self.ronexadas_speed = 3
        moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
        self.min_dist = 1000

        self.ronexadas_hp = 100
        self.id = id
        self.gethx = hero.get_hero_ypos()
        self.gethy = hero.get_hero_xpos()



    def move(self):
        self.ronexadas.x += self.ronexadas.xspeed
        self.ronexadas.y += self.ronexadas.yspeed
        self.delta_x = self.gethx - self.ronexadas.y
        self.delta_x = self.gethy - self.ronexadas.x

        if abs(self.delta_x) <= self.min_dist and abs(self.delta_x) <= self.min_dist:
            enemy_move_x = abs(self.delta_x) > abs(self.delta_x)
            if abs(self.delta_x) > self.ronexadas.x and abs(self.delta_x) > self.ronexadas.y:
                enemy_move_x = random.random() < 0.5
            enemy_move_x = random.random() < 0.5
            if enemy_move_x:
                self.ronexadas.x += min(self.delta_x, self.ronexadas_speed) if self.delta_x > 0 else max(self.delta_x, -self.ronexadas_speed)
            else:
                self.ronexadas.y += min(self.delta_x, self.ronexadas_speed) if self.delta_x > 0 else max(self.delta_x, -self.ronexadas_speed)

        moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
    def update(self):
        self.move()


