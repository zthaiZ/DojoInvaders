import sys
import pygame as pg
import random
import math
#images: https://www.flaticon.com/authors/freepik
#https: // www.flaticon.com/authors/smashimages
#BG Image: https://www.vecteezy.com/vector-art/156648-illustration-of-dojo-room

pg.init()
ICON_SIZE = 64

#Window/Screen
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
size = WINDOW_WIDTH, WINDOW_HEIGHT
screen = pg.display.set_mode(size)
icon = pg.image.load("images/kunais.png")
pg.display.set_caption('Dojo Invaders')
pg.display.set_icon(icon)

#Background
bg = pg.image.load("images/dojo.png")

#Player
player_icon = pg.image.load("images/ninja.png")
playerX, playerY = 370, 480
playerX_delta = 0

#Enemies
HITBOX = 27
enemies = []
enemyX = []
enemyY = []
enemyX_delta = []
enemyY_delta = []
enemy_count = 6
enemy_icon = pg.image.load("images/samurai.png")

#Lives
lives_count = 5
lives = []
livesX = []
livesY = 560
x_pos = 700
hp_icon = pg.image.load("images/love.png")


for i in range(lives_count):
    lives.append(hp_icon)
    livesX.append(x_pos)
    x_pos += 20

for i in range(enemy_count):
    enemies.append(enemy_icon)
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_delta.append(4)
    enemyY_delta.append(40)
    
#Weapon
weapon_icon = pg.image.load("images/shuriken.png")
weaponX, weaponY = 0, 480
weaponX_delta = 0
weaponY_delta = 10
weapon_state = "ready"

#Score
score_val = 0
scoreX = 10
scoreY = 10
font = pg.font.Font('freesansbold.ttf', 24)

def score(x, y):
    screen.blit(score, (x, y))

def throw_weapon(x, y):
    global weapon_state
    weapon_state = "throw"
    screen.blit(weapon_icon, (x+16, y+10))

def display_element(icon, x, y):
    screen.blit(icon, (x, y)) #draws player image

def isCollision(enemyX, enemyY, weaponX, weaponY):
    distance = math.sqrt(math.pow(enemyX-weaponX, 2) + math.pow(enemyY-weaponY, 2))
    if distance < HITBOX:
        return True
    return False


while 1:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_delta = -5
            if event.key == pg.K_RIGHT:
                playerX_delta = 5
            if event.key == pg.K_SPACE:
                if weapon_state == "ready":
                    weaponX = playerX
                    throw_weapon(weaponX, weaponY)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_delta = 0

    playerX += playerX_delta

    if playerX <= 0:
        playerX = 0
    elif playerX >= WINDOW_WIDTH-ICON_SIZE:
        playerX = WINDOW_WIDTH-ICON_SIZE

    # Weapon movement
    if weaponY <= 0:
        weaponY = 480
        weapon_state = "ready"

    if weapon_state == "throw":
        throw_weapon(weaponX, weaponY)
        weaponY -= weaponY_delta

    for i in range(enemy_count):
        enemyX[i] += enemyX_delta[i]

        if enemyX[i] <= 0:
            enemyX_delta[i] = 4
            enemyY[i] += enemyY_delta[i]

        elif enemyX[i] >= WINDOW_WIDTH-ICON_SIZE:
            enemyX_delta[i] = -4
            enemyY[i] += enemyY_delta[i]

        # Collision
        hit = isCollision(enemyX[i], enemyY[i], weaponX, weaponY)
        if hit:
            weaponY = 480
            weapon_state = "ready"
            score_val += 1
            enemyX[i], enemyY[i] = random.randint(0, 800), random.randint(50, 150)

        display_element(enemies[i], enemyX[i], enemyY[i])

    score = font.render("Score: " + str(score_val), True, (255, 255, 255))

    display_element(player_icon, playerX, playerY)

    display_element(score, scoreX, scoreY)

    for i in range(lives_count):
        display_element(lives[i], livesX[i], livesY)

    pg.display.update()
