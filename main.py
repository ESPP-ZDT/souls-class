import pygame as pg

import enemies
import hero
from pygame_functions import *
from hero import *
from settings import *
from deathscreen import *
from random import *
from hud import *
from enemies import *
from ghosts import *
from boosts import *
from particle_effects import *

#setAutoUpdate(False)



hero = Hero()
hero_weapon = HeroWeapon()
hud = Hud(hero)
ronexadas = BossRonexadas(hero, hero_weapon)
celestialwatcher = CelestialWatcher(hero)
pots = HeroPots(hero,hud)
hpboost = HpBoost(hero,hud)

while True:



    hero.update()
    celestialwatcher.update()

    hero.update()



    hero_weapon.update()
    pots.update()

    updateDisplay()
    hud.update()
    hpboost.update()
    ronexadas.update()




    updateDisplay()
    tick(60)
endWait()