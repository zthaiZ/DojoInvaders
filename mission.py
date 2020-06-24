import sys
import pygame
import random
import math
#images: https://www.flaticon.com/authors/freepik
#https: // www.flaticon.com/authors/smashimages
#BG Image: https://www.vecteezy.com/vector-art/156648-illustration-of-dojo-room

pygame.init()
ICON_SIZE = 64

#Window/Screen
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
size = WINDOW_WIDTH, WINDOW_HEIGHT
screen = pygame.display.set_mode(size)
icon = pygame.image.load("images/kunais.png")
pygame.display.set_caption('Dojo Invaders')
pygame.display.set_icon(icon)

#Background
bg = pygame.image.load("images/dojo.png")

#Player
player_icon = pygame.image.load("images/ninja.png")
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
enemy_icon = pygame.image.load("images/samurai.png")

#Lives
lives_count = 5
lives = []
livesX = []
livesY = 560
x_pos = 700
hp_icon = pygame.image.load("images/love.png")


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
weapon_icon = pygame.image.load("images/shuriken.png")
weaponX, weaponY = 0, 480
weaponX_delta = 0
weaponY_delta = 10
weapon_state = "ready"

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

score = 0

while 1:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_delta = -5
            if event.key == pygame.K_RIGHT:
                playerX_delta = 5
            if event.key == pygame.K_SPACE:
                if weapon_state is "ready":
                    weaponX = playerX
                    throw_weapon(weaponX, weaponY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
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

    if weapon_state is "throw":
        throw_weapon(weaponX, weaponY)
        weaponY -= weaponY_delta

    for i in range(enemy_count):
        enemyX[i] += enemyX_delta[i]

        if enemyX[i] <= 0:
            enemyX_delta[i] = 3
            enemyY[i] += enemyY_delta[i]

        elif enemyX[i] >= WINDOW_WIDTH-ICON_SIZE:
            enemyX_delta[i] = -3
            enemyY[i] += enemyY_delta[i]

        # Collision
        hit = isCollision(enemyX[i], enemyY[i], weaponX, weaponY)
        if hit:
            weaponY = 480
            weapon_state = "ready"
            score += 1
            enemyX[i], enemyY[i] = random.randint(0, 800), random.randint(50, 150)

        display_element(enemies[i], enemyX[i], enemyY[i])

    display_element(player_icon, playerX, playerY)

    for i in range(lives_count):
        display_element(lives[i], livesX[i], livesY)

    pygame.display.update()
