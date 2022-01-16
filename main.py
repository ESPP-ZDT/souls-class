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
ronexadas = BossRonexadas(hero, hero_weapon,hud)
celestialwatcher = CelestialWatcher(hero)
pots = HeroPots(hero,hud)
hpboost = HpBoost(hero,hud)


hero_health = getattr(hero, 'hero_health')
while True:
    
    hero.update()
    celestialwatcher.update()
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