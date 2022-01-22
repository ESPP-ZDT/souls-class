
from pygame_functions import *
from hero import Hero
import random
#hpboost - jak narazie jest to lampa, na ktora jak wejdziemy, dostajemy 10 hp.

class HpBoost():

    def __init__(self, hero,hud):
        self.sprite = makeSprite('data/img/crhvn lamp.png')#tworzy sprajta
        transformSprite(self.sprite, 90, 1)#obraca
        self.x = 340 # w jakim miejscu sie spawnuje x
        self.y = 200  # w jakim miejscu sie spawnuje y
        moveSprite(self.sprite, self.x, self.y, True) #rusza sprajtem
        showSprite(self.sprite) #wyswietla go
        self.hero = hero #sciaga z klasy bohatera sprajt bohatera
        self.hud = hud
        self.boost_touched = False#boolean z pomoca ktorego wylaczam sprite z interakcji


        #poruszanie hpboostem wzgledem bohatera
    def move(self):
        if keyPressed("up"):
            self.y += 10# karze przesuwac hpboost o 10 do gory
            moveSprite(self.sprite, self.x, self.y, True)#przesuwa

        elif keyPressed("down"):
            self.y += -10# karze przesuwac hpboost o 10 w dol
            moveSprite(self.sprite, self.x, self.y, True)#przesuwa
        elif keyPressed("right"):
            self.x += -10# karze przesuwac hpboost o 10 w prawo
            moveSprite(self.sprite, self.x, self.y, True)#przesuwa

        elif keyPressed("left"):
            self.x += 10# karze przesuwac hpboost o 10 w lewo
            moveSprite(self.sprite, self.x, self.y, True)#przesuwa
    #kolizje z bohaterem
    def healing_collision(self):
        if touching(self.hero.sprite, self.sprite) and self.boost_touched == False:
            self.hero.health += 100
            self.boost_touched = True

            killSprite(self.sprite)#zabija sprajt
            hideSprite(self.sprite)#znika sprajt, niekoniecznie potrzebne.
            self.sprite.kill()#kolejne wywolanie znikniecia sprajta
            print("healed 10 hp")



    def update(self):
        self.healing_collision() #wywoluje kolizje
        changeLabel(self.hud.display_health, str(self.hero.health), self.hud.hpcolor)#zmienia wartosc zycia w hudzie
        updateDisplay()
        self.move()


#jak zespawnowac wiele hpboostow na raz?