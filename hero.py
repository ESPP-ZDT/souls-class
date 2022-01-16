import pygame as pg, random
from hud import *
from pygame_functions import *
from enemies import *
#from boosts import *


class Hero():
    def __init__(self):

        self.hero_health = 100
        self.hero = makeSprite('data/img/hero.png')
        self.deathsprite = addSpriteImage(self.hero,'data/img/death coin.png' )
        showSprite(self.hero)
        #transformSprite(self.hero, 90, 1)
        self.xpos = 400
        self.ypos = 320
        self.xspeed = 0
        self.yspeed = 0

        self.mana = 100
        self.mana_potions = 1
        self.souls = 1
        
    #def take_damage(self.hero_health, damage):
       #self.hero_health -= damage
        

    def move(self):
        if keyPressed("up"):
            scrollBackground(0,5)
            transformSprite(self.hero, -180, 1)
        elif keyPressed("down"):
            scrollBackground(0,-5)
            transformSprite(self.hero, 360, 1)
        elif keyPressed("right"):
            scrollBackground(-5, 0)
            transformSprite(self.hero, -90, 1)
        elif keyPressed("left"):
            scrollBackground(5, 0)
            transformSprite(self.hero, 90, 1)
        hero_x_pos = self.xpos
        hero_y_pos = self.ypos
        moveSprite(self.hero, self.xpos, self.ypos, True)

    def get_hero_ypos(self):
       return int(self.ypos)

    def get_hero_xpos(self):
        return int(self.xpos)

    def update(self):
        #self.take_damage()
        #print(str(hero_hp))
        print(str(self.hero_health))
        self.get_hero_ypos()
        self.get_hero_xpos()
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
            hideSprite(self.hero_weapon)
            killSprite(self.hero_weapon)
            
            updateDisplay()

    def update(self):
        self.attack()

class HeroPots():
    def __init__(self,hero,hud):
        self.hero_health = hero.hero_health
        self.hpcolor = hud.hpcolor
        self.mana = hero.mana
        self.mana_potions = hero.mana_potions
        self.display_manapotions = hud.display_manapotions
        self.mana_color = hud.manacolor
        self.souls = hero.souls
        self.souls_color = hud.soulscolor
        self.health_display = hud.display_health
        self.mana_display = hud.display_mana
        self.souls_display = hud.display_souls

    def use(self):
        #using soul
        if keyPressed("x") and self.souls > 0:
            self.souls -= 1
            print(str(self.souls))
            self.hero_health += 100
            self.mana += 100
            print(self.mana)
            print(self.hero_health,self.mana)
        #using mana potion
        if keyPressed("z") and self.mana_potions > 0:
            self.mana_potions -= 1
            self.mana += 50
            # display manachange
            print(' used mana potion ' + 'manalevel is ' + str(self.mana))

    def update(self):
        self.use()
        changeLabel(self.health_display, str(self.hero_health), self.hpcolor)
        changeLabel(self.mana_display, str(self.mana), self.mana_color)
        changeLabel(self.souls_display, str(self.souls), self.souls_color)
        changeLabel(self.display_manapotions, str(self.mana_potions), self.mana_color)





#enemies = [enemy() for i in range(40)]