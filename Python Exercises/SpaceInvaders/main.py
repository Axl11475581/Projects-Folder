import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Player position on screen and x/y movement variables
playerImg = pygame.image.load('player.png.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy position on screen with random package
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# Player's bullet position on screen with random package
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
# Ready state: you can't see the bullet on the screen.
# Fire state: the bullet is currently moving.
bullet_state = "ready"


def player(x, y):  # Function to display the player on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):  # Function to display the enemy on the screen
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
# Game Loop (for game window)
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    # For loop to keep the screen open and close when the x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Screen boundaries with player respawn + player movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0

    enemyX += enemyX_change
    # Screen boundaries for the enemy + movement cycle
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
