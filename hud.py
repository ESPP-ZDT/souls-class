import pygame as pg, sys, random
from pygame_functions import *
from settings import *
from hero import *
from pygame.locals import *


#klasa tworzaca hud


class Hud():
    def __init__(self, hero):
        self.hero_health = hero.hero_health
        self.mana = hero.mana
        self.mana_potions = hero.mana_potions
        self.souls = hero.souls
        self.hpcolor = "red"
        self.display_health = makeLabel(str(self.hero_health),40,10,10,self.hpcolor,"Agency FB")
        self.manacolor = "blue"
        self.display_mana = makeLabel(str(self.mana),40,60,10,self.manacolor,"Agency FB")
        self.soulscolor = "white"
        self.display_souls = makeLabel(str(self.souls),40,120,10,self.soulscolor,"Agency FB")
        self.display_manapotions = makeLabel(str(self.mana_potions),40, 160, 10, self.manacolor, 'Agency FB')


    def huddisplay(self):
        showLabel(self.display_health)
        showLabel(self.display_mana)
        showLabel(self.display_souls)
        showLabel(self.display_manapotions)

    def update(self):
        self.huddisplay()
