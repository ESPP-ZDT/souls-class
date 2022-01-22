import pygame as pg, random
import pygame.sprite

from hud import *
from pygame_functions import *
from enemies import *
#from boosts import *

class Hero():
    def __init__(self):
        super().__init__()

        self.health = 1000
        self.sprite = makeSprite('data/img/hero.png')
        self.deathsprite = addSpriteImage(self.sprite,'data/img/death coin.png' )
        showSprite(self.sprite)
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
            scrollBackground(0,10)
            transformSprite(self.sprite, -180, 1)
        elif keyPressed("down"):
            scrollBackground(0,-10)
            transformSprite(self.sprite, 360, 1)
        elif keyPressed("right"):
            scrollBackground(-10, 0)
            transformSprite(self.sprite, -90, 1)
        elif keyPressed("left"):
            scrollBackground(10, 0)
            transformSprite(self.sprite, 90, 1)
        moveSprite(self.sprite, self.xpos, self.ypos, True)

    def get_hero_ypos(self):
       return int(self.ypos)

    def get_hero_xpos(self):
        return int(self.xpos)

    def update(self):
        #self.take_damage()
        #print(str(hero_hp))
        #print(str(self.hero_health))
        #self.get_hero_ypos()
        #self.get_hero_xpos()
        print(self.health)
        self.move()


class HeroWeapon(pygame.sprite.Group):
    def __init__(self):
        self.sprite = makeSprite('data/img/mad war axe.png')
        self.x = 400
        self.y = 280
        self.xbasic = 400
        self.xbasicatright = 350
        self.xbasicatleft = 320
        self.ybasic = 280
        self.ybasicatdown = 250
        self.xspeed = 0
        self.yspeed = 0
        self.attack_dmg = random.randint(5,20)#obrazenia topora

    def attack(self):
        if keyPressed("up") and keyPressed("c"):
            showSprite(self.sprite)
            self.yspeed = random.randint(-20, -1)
            moveSprite(self.sprite, self.x, self.y, True)
            self.y == self.ybasic
            self.y += self.yspeed - 5
        elif keyPressed("down") and keyPressed("c"):
            showSprite(self.sprite)
            self.yspeed = random.randint(1, 20)
            moveSprite(self.sprite, self.x, self.y, True)
            self.y == self.ybasicatdown
            self.y += self.yspeed + 5
        elif keyPressed("right") and keyPressed("c"):
            showSprite(self.sprite)
            self.xspeed = random.randint(1, 20)
            moveSprite(self.sprite, self.x, self.y, True)
            self.x == self.xbasic
            self.x += self.xspeed + 5
        elif keyPressed("left") and keyPressed("c"):
            showSprite(self.sprite)
            self.xspeed = random.randint(-20, -1)
            moveSprite(self.sprite, self.x, self.y, True)
            self.x == self.xbasic
            self.x += self.xspeed - 5
        else:
            self.x = self.xbasic
            self.y = self.ybasic
            moveSprite(self.sprite, self.xbasic, self.ybasic, True)
            hideSprite(self.sprite)
            killSprite(self.sprite)
            
            updateDisplay()

    def update(self):
        self.attack()

class HeroPots():
    def __init__(self,hero,hud):
        self.hero = hero
        self.hud = hud

    def use(self):
        #using soul
        if keyPressed("x") and self.hero.souls > 0:
            self.hero.souls -= 1
            print(str(self.hero.souls))
            self.hero.health += 100
            self.hero.mana += 100
            print(self.hero.mana)
            print(self.hero.health,self.hero.mana)
        #using mana potion
        if keyPressed("z") and self.hero.mana_potions > 0:
            self.hero.mana_potions -= 1
            self.hero.mana += 50
            # display manachange
            print(' used mana potion ' + 'manalevel is ' + str(self.hero.mana))

    def update(self):
        self.use()
        changeLabel(self.hud.display_health, str(self.hero.health), self.hud.hpcolor)
        changeLabel(self.hud.display_mana, str(self.hero.mana), self.hud.manacolor)
        changeLabel(self.hud.display_souls, str(self.hero.souls), self.hud.soulscolor)
        changeLabel(self.hud.display_manapotions, str(self.hero.mana_potions), self.hud.manacolor)





#enemies = [enemy() for i in range(40)]