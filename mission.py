import sys, pygame
#Icons: https://www.flaticon.com/authors/freepik

pygame.init()

ICON_SIZE = 64

speed = [2, 2]
black = 0, 0, 0

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

def player(x, y):
    screen.blit(player_icon, (x, y)) #draws player image

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

    player(playerX, playerY)
    pygame.display.update()
