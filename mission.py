import sys
import pygame
import random
#Icons: https://www.flaticon.com/authors/freepik
#https: // www.flaticon.com/authors/smashicons

pygame.init()
ICON_SIZE = 64

#Window/Screen
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
size = WINDOW_WIDTH, WINDOW_HEIGHT
screen = pygame.display.set_mode(size)
icon = pygame.image.load("icons/kunais.png")
pygame.display.set_caption('Dojo Invaders')
pygame.display.set_icon(icon)

#Player
player_icon = pygame.image.load("icons/ninja.png")
playerX, playerY = 370, 480
playerX_delta = 0

#Enemy
enemy_icon = pygame.image.load("icons/samurai.png")
enemyX, enemyY = random.randint(0,800), random.randint(50, 150)
enemyX_delta = 3
enemyY_delta = 0

def character(icon, x, y):
    screen.blit(icon, (x, y)) #draws player image

while 1:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_delta = -5
            if event.key == pygame.K_RIGHT:
                playerX_delta = 5

        if event.type == pygame.KEYUP:
            playerX_delta = 0

    playerX += playerX_delta

    if playerX <= 0:
        playerX = 0
    elif playerX >= WINDOW_WIDTH-ICON_SIZE:
        playerX = WINDOW_WIDTH-ICON_SIZE

    enemyX += enemyX_delta

    if enemyX <= 0:
        enemyX_delta = 3
    elif enemyX >= WINDOW_WIDTH-ICON_SIZE:
        enemyX_delta = -3

    character(player_icon, playerX, playerY)
    character(enemy_icon, enemyX, enemyY)
    pygame.display.update()
