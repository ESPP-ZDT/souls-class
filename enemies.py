import pygame as pg, random
from pygame_functions import *
from hero import *
#klasa tworzaca efekty, byc moze bedzie ja mozna wszedzie aplikowac, nie tylko w kontekscie danego enemy.



class BossRonexadas(): #tworzy bossa Ronexadasa
    def __init__(self, hero,heroweapon,hud):
        self.sprite = makeSprite(('data/img/sotfh 1.png'))#tworzy sprite ronexadasa
        self.deadronexadas = addSpriteImage(self.sprite,'data/img/death coin.png')
        showSprite(self.sprite)#pokazuje sprite ronexadasa
        #transformSprite(self.ronexadas, 90, 1)
        self.x = 340  # w jakim miejscu sie spawnuje x
        self.y = 0  # w jakim miejscu sie spawnuje y
        self.xspeed = 0 #predkosc poruszania sie w x ronexadasa
        self.yspeed = 0 #predkosc poruszania sie w y ronexadasa
        self.speed = 3 #predkosc ronexadasa w poruszaniu
        moveSprite(self.sprite, self.x, self.y, True)#rusza sprajtem
        self.min_dist = 1000 #minimalny dystans od ktorego ronexadas podchodzi do bohatera
        self.blood_particles = [] #lista tworzona do krwi
         #nie dziala
        self.hp = 1000 #punkty zycia ronexadasa(do przekminienia)
        self.id = id #id potwora, przy tworzeniu wielu
        self.hud = hud
        self.hero = hero #sprowadza sprite bohatera do kolizji
       #sprowadza zycie bohatera
        self.heroweapon = heroweapon
        #self.boss_damage = makeTextBox(self.ronexadas.x, self.ronexadas.y + 10, 40, 0, str(self.ronexadas.hp), 10, 12) #how do I update it update it when the collision happens?


    def move2(self):
        if keyPressed("up"):
            self.y += 10
            moveSprite(self.sprite, self.x, self.y, True)

        elif keyPressed("down"):
            self.y += -10
            moveSprite(self.sprite, self.x, self.y, True)
        elif keyPressed("right"):
            self.x += -10
            moveSprite(self.sprite, self.x, self.y, True)

        elif keyPressed("left"):
            self.x += 10
            moveSprite(self.sprite, self.x, self.y, True)



    def boss_collision(self):
        if touching(self.heroweapon.sprite, self.sprite):
            updateDisplay()
            if self.hp > 0:
                self.hp -= self.heroweapon.attack_dmg
                print('the boss has been hit, his hp is now' + str(self.hp))
                updateDisplay()
            else:
                changeSpriteImage(self.sprite, 1)

                    #hideSprite(drop)


                self.xspeed = 0
                self.yspeed = 0
                self.speed = 0
                #hideSprite(self.sprite)
        #if touching self.hero, self.ronexadas
        if touching(self.hero.sprite, self.sprite):
            if self.hp > 0:
                self.hero.health -= 100
                #Hero.take_damage(self.hero_health,10)


    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.delta_x = self.hero.xpos - self.y
        self.delta_x = self.hero.ypos - self.x

        if abs(self.delta_x) <= self.min_dist and abs(self.delta_x) <= self.min_dist:
            self.enemy_move_x = abs(self.delta_x) > abs(self.delta_x)
            if abs(self.delta_x) > self.x and abs(self.delta_x) > self.y:
                self.enemy_move_x = random.random() < 0.5
            self.enemy_move_x = random.random() < 0.3
            if self.enemy_move_x:
                self.x += min(self.delta_x, self.speed) if self.delta_x > 0 else max(self.delta_x, -self.speed)
            else:
                self.y += min(self.delta_x, self.speed) if self.delta_x > 0 else max(self.delta_x, -self.speed)

        moveSprite(self.sprite, self.x, self.y, True)
    def update(self):
        self.move2()
        self.move()

        self.boss_collision()


class Monster1(): #tworzy potworka
    def __init__(self, hero, heroweapon ,hud):
        self.sprite = makeSprite(('data/img/monster 1.png'))#tworzy sprite ronexadasa
        self.dead = addSpriteImage(self.sprite,'data/img/monster 1.png')
        showSprite(self.sprite)#pokazuje sprite ronexadasa
        #transformSprite(self.ronexadas, 90, 1)
        self.x = random.randrange(340,399)  # w jakim miejscu sie spawnuje x
        self.y = 0  # w jakim miejscu sie spawnuje y
        self.xspeed = 0 #predkosc poruszania sie w x ronexadasa
        self.yspeed = 0 #predkosc poruszania sie w y ronexadasa
        self.speed = 3 #predkosc ronexadasa w poruszaniu
        moveSprite(self.sprite, self.x, self.y, True)#rusza sprajtem
        self.min_dist = 100 #minimalny dystans od ktorego ronexadas podchodzi do bohatera
        self.blood_particles = [] #lista tworzona do krwi
         #nie dziala
        self.hp = 100 #punkty zycia ronexadasa(do przekminienia)
        self.id = id #id potwora, przy tworzeniu wielu
        self.hud = hud
        self.hero = hero #sprowadza sprite bohatera do kolizji
       #sprowadza zycie bohatera
        self.hero_weapon = heroweapon
        #self.boss_damage = makeTextBox(self.ronexadas.x, self.ronexadas.y + 10, 40, 0, str(self.ronexadas.hp), 10, 12) #how do I update it update it when the collision happens?


    def move2(self):
        if keyPressed("up"):
            self.y += 10
            moveSprite(self.sprite, self.x, self.y, True)

        elif keyPressed("down"):
            self.y += -10
            moveSprite(self.sprite, self.x, self.y, True)
        elif keyPressed("right"):
            self.x += -10
            moveSprite(self.sprite, self.x, self.y, True)

        elif keyPressed("left"):
            self.x += 10
            moveSprite(self.sprite, self.x, self.y, True)



    def boss_collision(self):
        if touching(self.hero_weapon.sprite, self.sprite):
            if self.hp > 0:
                self.hp -= self.hero_weapon.attack_dmg
                print('the boss has been hit, his hp is now' + str(self.hp))
            else:
                changeSpriteImage(self.sprite, 1)

                    #hideSprite(drop)


                self.xspeed = 0
                self.yspeed = 0
                self.speed = 0
                #hideSprite(self.sprite)
        #if touching self.hero, self.ronexadas
        if touching(self.hero.sprite, self.sprite):
            if self.hp > 0:
                self.hero.health -= 100
                #Hero.take_damage(self.hero_health,10)


    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.delta_x = self.hero.xpos - self.y
        self.delta_x = self.hero.ypos - self.x

        if abs(self.delta_x) <= self.min_dist and abs(self.delta_x) <= self.min_dist:
            self.enemy_move_x = abs(self.delta_x) > abs(self.delta_x)
            if abs(self.delta_x) > self.x and abs(self.delta_x) > self.y:
                self.enemy_move_x = random.random() < 0.5
            self.enemy_move_x = random.random() < 0.3
            if self.enemy_move_x:
                self.x += min(self.delta_x, self.speed) if self.delta_x > 0 else max(self.delta_x, -self.speed)
            else:
                self.y += min(self.delta_x, self.speed) if self.delta_x > 0 else max(self.delta_x, -self.speed)

        moveSprite(self.sprite, self.x, self.y, True)
    def update(self):
        self.move2()
        self.move()
        self.boss_collision()


class CrabAscendant(): #tworzy potworka
    def __init__(self, hero, heroweapon ,hud,id):
        self.sprite = makeSprite(('data/img/crab ascendant 2.png'))#tworzy sprite ronexadasa
        self.dead = addSpriteImage(self.sprite,'data/img/death coin.png')
        showSprite(self.sprite)#pokazuje sprite ronexadasa
        #transformSprite(self.ronexadas, 90, 1)
        self.x = random.randrange(340,399)  # w jakim miejscu sie spawnuje x
        self.y = random.randrange(-1000,-800)  # w jakim miejscu sie spawnuje y
        self.xspeed = 0 #predkosc poruszania sie w x ronexadasa
        self.yspeed = 0 #predkosc poruszania sie w y ronexadasa
        self.speed = 3 #predkosc ronexadasa w poruszaniu
        moveSprite(self.sprite, self.x, self.y, True)#rusza sprajtem
        self.min_dist = 600 #minimalny dystans od ktorego ronexadas podchodzi do bohatera
        #self.blood_particles = [] #lista tworzona do krwi
         #nie dziala
        self.hp = 300 #punkty zycia ronexadasa(do przekminienia)
        self.id = id #id potwora, przy tworzeniu wielu
        self.hud = hud
        self.hero = hero #sprowadza sprite bohatera do kolizji
       #sprowadza zycie bohatera
        self.hero_weapon = heroweapon
        #self.boss_damage = makeTextBox(self.ronexadas.x, self.ronexadas.y + 10, 40, 0, str(self.ronexadas.hp), 10, 12) #how do I update it update it when the collision happens?

    def move2(self):
        if keyPressed("up"):
            self.y += 10
            moveSprite(self.sprite, self.x, self.y, True)

        elif keyPressed("down"):
            self.y += -10
            moveSprite(self.sprite, self.x, self.y, True)
        elif keyPressed("right"):
            self.x += -10
            moveSprite(self.sprite, self.x, self.y, True)

        elif keyPressed("left"):
            self.x += 10
            moveSprite(self.sprite, self.x, self.y, True)
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.delta_x = self.hero.xpos - self.y
        self.delta_x = self.hero.ypos - self.x

        if abs(self.delta_x) <= self.min_dist and abs(self.delta_x) <= self.min_dist:
            self.enemy_move_x = abs(self.delta_x) > abs(self.delta_x)
            if abs(self.delta_x) > self.x and abs(self.delta_x) > self.y:
                self.enemy_move_x = random.random() < 0.5
            self.enemy_move_x = random.random() < 0.3
            if self.enemy_move_x:
                self.x += min(self.delta_x, self.speed) if self.delta_x > 0 else max(self.delta_x, -self.speed)
            else:
                self.y += min(self.delta_x, self.speed) if self.delta_x > 0 else max(self.delta_x, -self.speed)
    def boss_collision(self):
        if touching(self.hero_weapon.sprite, self.sprite):
            if self.hp > 0:
                self.hp -= self.hero_weapon.attack_dmg
                print('the boss has been hit, his hp is now' + str(self.hp))
            else:
                changeSpriteImage(self.sprite, 1)

                    #hideSprite(drop)


                self.xspeed = 0
                self.yspeed = 0
                self.speed = 0
                #hideSprite(self.sprite)
        #if touching self.hero, self.ronexadas
        if touching(self.hero.sprite, self.sprite):
            if self.hp > 0:
                self.hero.health -= 100
                #Hero.take_damage(self.hero_health,10)
    def update(self):
        self.move2()
        self.move()
        self.boss_collision()