import pygame as pg, random
from pygame_functions import *

hero_x_pos = 400
hero_y_pos = 320


class Hero():
    def __init__(self):
        self.hero = makeSprite('data/img/hero.png')
        self.deathsprite = addSpriteImage(self.hero,'data/img/death coin.png' )
        showSprite(self.hero)
        self.xpos = 400
        self.ypos = 320
        self.xspeed = 0
        self.yspeed = 0
        self.hero_health = 100
        self.mana = 100
        self.mana_potions = 1
        self.souls = 1
    def move(self):
        if keyPressed("up"):
            scrollBackground(0,10)
            transformSprite(self.hero, -180, 1)
        elif keyPressed("down"):
            scrollBackground(0,-10)
            transformSprite(self.hero, 360, 1)
        elif keyPressed("right"):
            scrollBackground(-10, 0)
            transformSprite(self.hero, -90, 1)
        elif keyPressed("left"):
            scrollBackground(10, 0)
            transformSprite(self.hero, 90, 1)
        hero_x_pos = self.xpos
        hero_y_pos = self.ypos
        moveSprite(self.hero, self.xpos, self.ypos, True)

    #def getheroypos():
       #return int(self.ypos)

    #def getheroxpos():
        #return int(self.xpos)

    def update(self):
        self.move()


class HeroWeapon():
    def __init__(self):
        self.hero_weapon = makeSprite('data/img/mad war axe.png')
        self.hero_weapon.x = 400
        self.hero_weapon.y = 280
        self.hero_weapon.xbasic = 400
        self.hero_weapon.xbasicatright = 350
        self.hero_weapon.xbasicatleft = 320
        self.hero_weapon.ybasic = 280
        self.hero_weapon.ybasicatdown = 250
        self.hero_weapon.xspeed = 0
        self.hero_weapon.yspeed = 0
        self.hero_weapon_attack = random.randint(5,20)#obrazenia topora
    def attack(self):
        if keyPressed("up") and keyPressed("c"):
            showSprite(self.hero_weapon)
            self.hero_weapon.yspeed = random.randint(-20, -1)
            moveSprite(self.hero_weapon, self.hero_weapon.x, self.hero_weapon.y, True)
            self.hero_weapon.y == self.hero_weapon.ybasic
            self.hero_weapon.y += self.hero_weapon.yspeed - 5
        elif keyPressed("down") and keyPressed("c"):
            showSprite(self.hero_weapon)
            self.hero_weapon.yspeed = random.randint(1, 20)
            moveSprite(self.hero_weapon, self.hero_weapon.x, self.hero_weapon.y, True)
            self.hero_weapon.y == self.hero_weapon.ybasicatdown
            self.hero_weapon.y += self.hero_weapon.yspeed + 5
        elif keyPressed("right") and keyPressed("c"):
            showSprite(self.hero_weapon)
            self.hero_weapon.xspeed = random.randint(1, 20)
            moveSprite(self.hero_weapon, self.hero_weapon.x, self.hero_weapon.y, True)
            self.hero_weapon.x == self.hero_weapon.xbasic
            self.hero_weapon.x += self.hero_weapon.xspeed + 5
        elif keyPressed("left") and keyPressed("c"):
            showSprite(self.hero_weapon)
            self.hero_weapon.xspeed = random.randint(-20, -1)
            moveSprite(self.hero_weapon, self.hero_weapon.x, self.hero_weapon.y, True)
            self.hero_weapon.x == self.hero_weapon.xbasic
            self.hero_weapon.x += self.hero_weapon.xspeed - 5
        else:
            self.hero_weapon.x = self.hero_weapon.xbasic
            self.hero_weapon.y = self.hero_weapon.ybasic
            moveSprite(self.hero_weapon, self.hero_weapon.xbasic, self.hero_weapon.ybasic, True)
            killSprite(self.hero_weapon)
            updateDisplay()

    def update(self):
        self.attack()

#enemies = [enemy() for i in range(40)]