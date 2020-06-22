import sys, pygame
#Icons: https://www.flaticon.com/authors/freepik

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

#Window/Screen
screen = pygame.display.set_mode(size)
icon = pygame.image.load("icons/kunais.png")
pygame.display.set_caption('Dojo Invaders')
pygame.display.set_icon(icon)

#Player
player_icon = pygame.image.load("icons/ninja.png")
playerX = 370
playerY = 480

def player():
    screen.blit(player_icon, (playerX, playerY)) #draws player image

while 1:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    player()
    pygame.display.update()
