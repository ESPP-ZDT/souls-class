import pygame as pg
from pygame_functions import *
from hero import *
from settings import *
from deathscreen import *
from random import *
from hud import *
from enemies import *
setAutoUpdate(False)


hero = Hero()
hero_weapon = HeroWeapon()
hud = Hud(hero)
ronexadas = BossRonexadas()
while True:
    hero.update()
    hero_weapon.update()
    hud.update()
    ronexadas.update()



    updateDisplay()
    tick(60)
endWait()