
from pygame_functions import *
import random


class HpBoost():
    def __init__(self, hero, hud):
        self.hpboost = makeSprite('data/img/crhvn lamp.png')
        transformSprite(self.hpboost, 90, 1)
        self.hpboost.x = 340 # w jakim miejscu sie spawnuje x
        self.hpboost.y = 200  # w jakim miejscu sie spawnuje y
        self.hpboost.xspeed = random.randint(0, 0)
        self.hpboost.yspeed = random.randint(0, 0)
        moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)
        showSprite(self.hpboost)
        self.hero_health = hero.hero_health
        self.hero = hero.hero
        self.hpcolor = hud.hpcolor
        self.health_display = hud.display_health
        self.hero_health = hero.hero_health

    def boost_heal(self):
        if touching(self.hero, self.hpboost):
            self.hero_health += 130

    def move(self):
        if keyPressed("up"):
            self.hpboost.y += 10
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)

        elif keyPressed("down"):
            self.hpboost.y += -10
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)
        elif keyPressed("right"):
            self.hpboost.x += -10
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)

        elif keyPressed("left"):
            self.hpboost.x += 10
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)

    def healing_collision(self):
        if touching(self.hero, self.hpboost):
            self.hero_health = self.hero_health + 10
            print(str(self.hero_health))
            killSprite(self.hpboost)
            hideSprite(self.hpboost)
            self.hpboost.kill()



    def update(self):
        self.healing_collision()
        changeLabel(self.health_display, str(self.hero_health), self.hpcolor)
        updateDisplay()
        self.boost_heal()
        #changeLabel(self.health_display, str(self.hero_health), self.hpcolor)
        self.move()


#hpboosts =[HpBoost() for i in range(100)]