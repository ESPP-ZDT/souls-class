import pygame as pg, random
from pygame_functions import *
from hero import *
#klasa tworzaca efekty, byc moze bedzie ja mozna wszedzie aplikowac, nie tylko w kontekscie danego enemy.
class Blood():
    def __init__(self, x , y, x_velocity, y_velocity, radius, color, gravity_scale):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.radius = radius
        self.color = color
        self.gravity_scale = gravity_scale * random.randrange(1,2)
        self.lifetime = random.randrange(25,75)
        self.gravity = random.randrange(4,10)
    def draw(self, screen):
        self.lifetime -= 1
        self.gravity -= self.gravity_scale
        self.x += self.x_velocity
        self.x += self.x_velocity * self.gravity
        pg.draw.circle(screen, self.color, (self.x,self.y),self.radius)



class BossRonexadas():
    def __init__(self, hero,heroweapon,hud):
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
        self.min_dist = 1
        self.blood_particles = []
        self.health_display = hud.display_health
        self.ronexadas_hp = 1000
        self.id = id
        self.hero = hero.hero
        self.hero_health = hero.hero_health
        self.gethx = hero.ypos
        self.gethy = hero.xpos
        self.hero_weapon = heroweapon.hero_weapon
        self.hero_weapon_attack = heroweapon.hero_weapon_attack
        self.hpcolor = hud.hpcolor
        #self.boss_damage = makeTextBox(self.ronexadas.x, self.ronexadas.y + 10, 40, 0, str(self.ronexadas_hp), 10, 12) #how do I update it update it when the collision happens?


    def move2(self):
        if keyPressed("up"):
            self.ronexadas.y += 10
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)

        elif keyPressed("down"):
            self.ronexadas.y += -10
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)
        elif keyPressed("right"):
            self.ronexadas.x += -10
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)

        elif keyPressed("left"):
            self.ronexadas.x += 10
            moveSprite(self.ronexadas, self.ronexadas.x, self.ronexadas.y, True)



    def boss_collision(self):
        if touching(self.hero_weapon, self.ronexadas):
            updateDisplay()
            if self.ronexadas_hp > 0:
                for i in range(30):
                   # self.blood_particles.append(
                        #Blood(self.ronexadas.x, self.ronexadas.y,  random.randrange(-8, 8), random.randrange(-2, 0), 3,
                              #(255, 30, 30), 1))
                    for Blood_ in self.blood_particles:
                        if Blood_.lifetime > 0:
                            Blood_.draw(screen)
                        else:
                            self.blood_particles.pop(self.blood_particles.index(Blood_))
                self.ronexadas_hp -= self.hero_weapon_attack
                print('the boss has been hit, his hp is now' + str(self.ronexadas_hp))
                updateDisplay()
            else:
                changeSpriteImage(self.ronexadas, 1)
                # enemies.remove(ronexadas)
                self.ronexadas.xspeed = 0
                self.ronexadas.yspeed = 0
                self.ronexadas_speed = 0
                hideSprite(self.ronexadas)
        #if touching self.hero, self.ronexadas
        if touching(self.hero, self.ronexadas):
            if self.ronexadas_hp > 0:
                pass
                #Hero.take_damage(self.hero_health,10)


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









