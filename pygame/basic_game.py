import pygame
import pygame.image as img
from pygame.time import Clock

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sprite Animations")

clock = Clock()

walkRight = [img.load(f'sprites/R{i}.png') for i in range(1, 10)]
walkLeft = [img.load(f'sprites/L{i}.png') for i in range(1, 10)]
bg = img.load('sprites/bg.jpg')
char = img.load('sprites/standing.png')

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

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 7
        self.left = False
        self.right = False
        self.walk_count = 0

def redraw_game_window():
    # global hero.walk_count
    window.blit(bg, (0, 0))
    
    if hero.walk_count + 1 >= 27:
        hero.walk_count = 0
    
    if hero.left:
        window.blit(walkLeft[hero.walk_count//3], (hero.x, hero.y))
        hero.walk_count += 1
    elif hero.right:
        window.blit(walkRight[hero.walk_count//3], (hero.x, hero.y))
        hero.walk_count += 1
    else:
        window.blit(char, (hero.x, hero.y))

    pygame.display.update()

# Main loop
hero = Player(300, 410, 64, 64)

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and hero.x > hero.velocity:
        hero.x -= hero.velocity
        hero.left, hero.right = True, False
    elif keys[pygame.K_RIGHT] and hero.x < window.get_width() - hero.width - hero.velocity:
        hero.x += hero.velocity
        hero.left, hero.right = False, True
    else:
        hero.left, hero.right = False, False
        hero.walk_count = 0
    
    if not hero.is_jump:
        if keys[pygame.K_SPACE]:
            hero.is_jump = True
            hero.left, right = False, False
            hero.walk_count = 0
    else:
        if hero.jump_count >= -7:
            sign = 1
            if hero.jump_count < 0:
                sign = -1
            hero.y -= (hero.jump_count ** 2) / 2 * sign
            hero.jump_count -= 1
        else:
            hero.is_jump = False
            hero.jump_count = 7

    redraw_game_window()

pygame.quit()