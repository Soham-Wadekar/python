import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Basic Movements")

x, y = 50, 440
width, height = 40, 60
velocity = 5
scale = 1.05

isJump = False
jump_count = 10

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

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < window.get_width() - width - velocity:
        x += velocity
    if not isJump:
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < window.get_height() - height - velocity:
            y += velocity
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump_count >= -10:
            sign = 1
            if jump_count < 0:
                sign = -1
            y -= (jump_count ** 2) / 2 * sign
            jump_count -= 1
        else:
            isJump = False
            jump_count = 10

    window.fill(bg_color)
    pygame.draw.rect(window, color, (x, y, width, height))
    pygame.display.update()

pygame.quit()