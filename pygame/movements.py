import pygame
import random

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Basic Movements")

x, y = 50, 50
width, height = 40, 60
velocity = 5
scale = 1.05

colors = {
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'white': (255, 255, 255)
}

color = colors['white']
bg_color = colors['black']

# Main loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:               # Red cross on the window
            run = False

    keys = pygame.key.get_pressed()

    x = (x - velocity if keys[pygame.K_LEFT] else x + velocity if keys[pygame.K_RIGHT] else x) % window.get_width()
    y = (y - velocity if keys[pygame.K_UP] else y + velocity if keys[pygame.K_DOWN] else y) % window.get_height()

    height, width = ((height * scale, width * scale) if keys[pygame.K_w] else (height / scale, width / scale) if keys[pygame.K_s] else (height, width))
    
    if keys[pygame.K_a]:
        velocity *= 2

    if keys[pygame.K_d]:
        velocity /= 2    

    if keys[pygame.K_q]:
        color = random.choice(list(colors.keys()))

    window.fill(bg_color)
    pygame.draw.rect(window, color, (x, y, width, height))
    pygame.display.update()

pygame.quit()