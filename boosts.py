
from pygame_functions import *
from hero import Hero
import random
#hpboost - jak narazie jest to lampa, na ktora jak wejdziemy, dostajemy 10 hp.

class HpBoost():

    def __init__(self, hero,hud):
        self.hpboost = makeSprite('data/img/crhvn lamp.png')#tworzy sprajta
        transformSprite(self.hpboost, 90, 1)#obraca
        self.hpboost.x = 340 # w jakim miejscu sie spawnuje x
        self.hpboost.y = 200  # w jakim miejscu sie spawnuje y
        moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True) #rusza sprajtem
        showSprite(self.hpboost) #wyswietla go
        self.hero_health = hero.hero_health#sciaga z klasy bohatera poziom hp bohatera
        self.hero = hero.hero #sciaga z klasy bohatera sprajt bohatera
        self.hpcolor = hud.hpcolor #sciaga z klasy hud kolor tekstu zycia
        self.health_display = hud.display_health #sciaga z klasy hud wyswietlanie zycia bohatea
        self.boost_touched = False#boolean z pomoca ktorego wylaczam sprite z interakcji


        #poruszanie hpboostem wzgledem bohatera
    def move(self):
        if keyPressed("up"):
            self.hpboost.y += 10# karze przesuwac hpboost o 10 do gory
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)#przesuwa

        elif keyPressed("down"):
            self.hpboost.y += -10# karze przesuwac hpboost o 10 w dol
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)#przesuwa
        elif keyPressed("right"):
            self.hpboost.x += -10# karze przesuwac hpboost o 10 w prawo
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)#przesuwa

        elif keyPressed("left"):
            self.hpboost.x += 10# karze przesuwac hpboost o 10 w lewo
            moveSprite(self.hpboost, self.hpboost.x, self.hpboost.y, True)#przesuwa
    #kolizje z bohaterem
    def healing_collision(self, Hero):
        if touching(self.hero, self.hpboost) and self.boost_touched == False:
            #self.hero_health
            self.boost_touched = True
            print(str(self.hero_health))
            killSprite(self.hpboost)#zabija sprajt
            hideSprite(self.hpboost)#znika sprajt, niekoniecznie potrzebne.
            self.hpboost.kill()#kolejne wywolanie znikniecia sprajta




    def update(self):
        self.healing_collision(Hero) #wywoluje kolizje
        changeLabel(self.health_display, str(self.hero_health), self.hpcolor)#zmienia wartosc zycia w hudzie
        updateDisplay()
        self.move()


#jak zespawnowac wiele hpboostow na raz?