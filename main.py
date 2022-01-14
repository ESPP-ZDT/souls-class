import pygame as pg
from pygame_functions import *
from hero import *
from settings import *
from deathscreen import *
from random import *
from hud import *
from enemies import *
from ghosts import *
setAutoUpdate(False)


hero = Hero()
hero_weapon = HeroWeapon()
hud = Hud(hero)
ronexadas = BossRonexadas(hero)
celestialwatcher = CelestialWatcher(hero)
pots = HeroPots(hero,hud)
while True:
    hero.update()
    celestialwatcher.update()
    ronexadas.update()
    hero.update()

    hero_weapon.update()
    pots.update()

    updateDisplay()
    hud.update()



    updateDisplay()
    tick(60)
endWait()