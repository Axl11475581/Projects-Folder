import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Player position on screen and x/y movement variables
playerImg = pygame.image.load('player.png.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy position on screen and x/y movement variables
enemyImg = pygame.image.load('ufo.png')
enemyX = 370
enemyY = 480
enemyX_change = 0


def player(x, y):  # Function to display the player on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):  # Function to display the enemy on the screen
    screen.blit(enemyImg, (x, y))


# Game Loop (for game window)
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # For loop to keep the screen open and close when the x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    # Screen boundaries with player respawn
    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0

    player(playerX, playerY)
    pygame.display.update()
