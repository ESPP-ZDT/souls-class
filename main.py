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
while True:
    hero.update()
    celestialwatcher.update()
    ronexadas.update()

    hero_weapon.update()

    hud.update()



    updateDisplay()
    tick(60)
endWait()