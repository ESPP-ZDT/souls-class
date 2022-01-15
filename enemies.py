import pygame as pg, random
from pygame_functions import *
from hero import *

class BossRonexadas():
    def __init__(self, hero,heroweapon):
        self.ronexadas = makeSprite(('data/img/sotfh 1.png'))
        self.deadronexadas = addSpriteImage(self.ronexadas,'data/img/death coin.png')
        showSprite(self.ronexadas)
        #transformSprite(self.ronexadas, 90, 1)
        self.ronexadas.x = 340  # w jakim miejscu sie spawnuje x
        self.ronexadas.y = 0  # w jakim miejscu sie spawnuje y
        self.ronexadas.xspeed = 0
        self.ronexadas.yspeed = 0
        self.ronexadas_speed = 3
        moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
        self.min_dist = 100


        self.ronexadas_hp = 1000
        self.id = id
        self.gethx = hero.get_hero_ypos()
        self.gethy = hero.get_hero_xpos()
        self.hero_weapon = heroweapon.hero_weapon
        self.hero_weapon_attack = heroweapon.hero_weapon_attack
        #self.boss_damage = makeTextBox(self.ronexadas.x, self.ronexadas.y + 10, 40, 0, str(self.ronexadas_hp), 10, 12) #how do I update it update it when the collision happens?


    def move2(self):
        if keyPressed("up"):
            self.ronexadas.y += 20
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)

        elif keyPressed("down"):
            self.ronexadas.y += -20
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
        elif keyPressed("right"):
            self.ronexadas.x += -20
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)

        elif keyPressed("left"):
            self.ronexadas.x += 20
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)



    def boss_collision(self):

        if touching(self.hero_weapon, self.ronexadas):
            if self.ronexadas_hp >= 0:
                self.ronexadas_hp -= self.hero_weapon_attack
                #showTextBox(boss_damage)

                updateDisplay()

            else:
                changeSpriteImage(self.ronexadas, 1)
                # killSprite(ronexadas)
                # enemies.remove(ronexadas)
                self.ronexadas.xspeed = 0  # to nie dziala
                self.ronexadas.yspeed = 0  # to nie dziala
                    # updateDisplay()
                    # problem jest taki ze jak zabije jednego enemy, ruszaja sie dalej, zabijajac dalej trawiam na takiego, ktory sprawia ze przestaja sie ruszac

    def move(self):
        self.ronexadas.x += self.ronexadas.xspeed
        self.ronexadas.y += self.ronexadas.yspeed
        self.delta_x = self.gethx - self.ronexadas.y
        self.delta_x = self.gethy - self.ronexadas.x

        if abs(self.delta_x) <= self.min_dist and abs(self.delta_x) <= self.min_dist:
            self.enemy_move_x = abs(self.delta_x) > abs(self.delta_x)
            if abs(self.delta_x) > self.ronexadas.x and abs(self.delta_x) > self.ronexadas.y:
                self.enemy_move_x = random.random() < 0.5
            self.enemy_move_x = random.random() < 0.3
            if self.enemy_move_x:
                self.ronexadas.x += min(self.delta_x, self.ronexadas_speed) if self.delta_x > 0 else max(self.delta_x, -self.ronexadas_speed)
            else:
                self.ronexadas.y += min(self.delta_x, self.ronexadas_speed) if self.delta_x > 0 else max(self.delta_x, -self.ronexadas_speed)

        moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
    def update(self):
        self.move2()
        self.move()
        self.boss_collision()


