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
from boosts import *


setAutoUpdate(False)


hero = Hero()
hero_weapon = HeroWeapon()
hud = Hud(hero)

monsters = Monster1(hero, hero_weapon,hud)
ascendants = CrabAscendant(hero, hero_weapon,hud, 1)

#celestialwatchers = [BossRonexadas(hero,hud,id) for id in range(10)]
ronexadas = BossRonexadas(hero, hero_weapon,hud)
pots = HeroPots(hero,hud)
hpboost = HpBoost(hero,hud)


while True:
    hud.update()

    hero_weapon.update()
    hero.update()
    #updateDisplay()
    monsters.update()
    ascendants.update()
    pots.update()
    ronexadas.update()
    hpboost.update()

    updateDisplay()

    if hero.health <= 0:
        showSprite(endscreen)
        break
    tick(60)
endWait()
