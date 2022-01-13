#multidimensional ghostly apparitions sometimes appear to the hero, interjecting into reality fracture of crabheaven, screaming. Sometimes u can talk to them...
import pygame as pg, random
from pygame_functions import *

class CelestialWatcher():
    def __init__(self, hero):
        self.watcher = makeSprite(('data/img/celestialwatch.png'))
        showSprite(self.watcher)
        #transformSprite(self.ronexadas, 90, 1)
        self.watcher.x = 300  # w jakim miejscu sie spawnuje x
        self.watcher.y = 400  # w jakim miejscu sie spawnuje y
        self.watcher.xspeed = 10
        self.watcher.yspeed = 2
        self.watcher_speed = 3
        moveSprite(self.watcher, self.watcher.x, self.watcher.y, True)
        self.min_dist = 100

        #self.ronexadas_hp = 100
        self.id = id
        self.gethx = hero.get_hero_ypos()
        self.gethy = hero.get_hero_xpos()



    def move(self):
        self.watcher.x += self.watcher.xspeed
        self.watcher.y += self.watcher.yspeed
        self.delta_x = self.gethx - self.watcher.y
        self.delta_x = self.gethy - self.watcher.x

        if abs(self.delta_x) <= self.min_dist and abs(self.delta_x) <= self.min_dist:
            self.enemy_move_x = abs(self.delta_x) > abs(self.delta_x)
            if abs(self.delta_x) > self.watcher.x and abs(self.delta_x) > self.watcher.y:
                self.enemy_move_x = random.random() < 0.5
            self.enemy_move_x = random.random() < 0.3
            if self.enemy_move_x:
                self.watcher.x += min(self.delta_x, self.watcher_speed) if self.delta_x > 0 else max(self.delta_x, -self.watcher_speed)
            else:
                self.watcher.y += min(self.delta_x, self.watcher_speed) if self.delta_x > 0 else max(self.delta_x, -self.watcher_speed)

        moveSprite(self.watcher, self.watcher.x, self.watcher.y, True)
    def update(self):
        self.move()

