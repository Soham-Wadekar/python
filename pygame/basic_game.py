import pygame
from pygame.time import Clock
from utils.animations import *
from utils.colors import red

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Basic Game")

clock = Clock()

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                window.blit(walk_left[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                window.blit(walk_right[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.left:
                window.blit(walk_left[0], (self.x, self.y))
            else:
                window.blit(walk_right[0], (self.x, self.y))

class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 10 * facing
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

def redraw_game_window():
    window.blit(bg, (0, 0))
    player.draw(window)

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()

# Main loop
player = Player(300, 410, 64, 64)
bullets = []

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if player.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 5:
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 5, red, facing))

    if keys[pygame.K_LEFT] and player.x > player.velocity:
        player.x -= player.velocity
        player.left, player.right = True, False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < window.get_width() - player.width - player.velocity:
        player.x += player.velocity
        player.left, player.right = False, True
        player.standing = False
    else:
        player.standing = True
        player.walk_count = 0
    
    if not player.is_jump:
        if keys[pygame.K_UP]:
            player.is_jump = True
            player.left, right = False, False
            player.walk_count = 0
    else:
        if player.jump_count >= -10:
            sign = 1
            if player.jump_count < 0:
                sign = -1
            player.y -= (player.jump_count ** 2) / 2 * sign
            player.jump_count -= 1
        else:
            player.is_jump = False
            player.jump_count = 10

    redraw_game_window()

pygame.quit()