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


#setAutoUpdate(False)



hero = Hero()
hero_weapon = HeroWeapon()
hud = Hud(hero)
#celestialwatcher = CelestialWatcher(hero)
#celestialwatchers = [CelestialWatcher(hero,id) for id in range(10)]
ronexadas = BossRonexadas(hero, hero_weapon,hud)
pots = HeroPots(hero,hud)
hpboost = HpBoost(hero,hud)


hero_health = getattr(hero, 'hero_health')
while True:

    hero.update()
   # [celestialwatcher.update() for celestialwatcher in celestialwatchers]
    hero.update()
    hero_weapon.update()
    #updateDisplay()


    pots.update()
    ronexadas.update()
    hpboost.update()
    hud.update()
    updateDisplay()
    if hero_health <= 0:
        showSprite(endscreen)
        break
    tick(60)
endWait()
