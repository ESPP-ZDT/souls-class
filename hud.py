import pygame as pg, sys, random
from pygame_functions import *
from settings import *
from hero import *
from pygame.locals import *


#klasa tworzaca hud


class Hud():
    def __init__(self, hero):
        self.hero = hero
        self.hpcolor = "red"
        self.display_health = makeLabel(str(self.hero.health),40,10,10,self.hpcolor,"Agency FB")
        self.manacolor = "blue"
        self.display_mana = makeLabel(str(self.hero.mana),40,60,10,self.manacolor,"Agency FB")
        self.soulscolor = "white"
        self.display_souls = makeLabel(str(self.hero.souls),40,120,10,self.soulscolor,"Agency FB")
        self.display_manapotions = makeLabel(str(self.hero.mana_potions),40, 160, 10, self.manacolor, 'Agency FB')


    def huddisplay(self):
        showLabel(self.display_health)
        showLabel(self.display_mana)
        showLabel(self.display_souls)
        showLabel(self.display_manapotions)
        changeLabel(self.display_health, str(self.hero.health), self.hpcolor)
        changeLabel(self.display_mana, str(self.hero.mana), self.manacolor)
        changeLabel(self.display_souls, str(self.hero.souls), self.soulscolor)



    def update(self):
        self.huddisplay()
