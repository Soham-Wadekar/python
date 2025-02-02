import random
import pygame
from pygame.time import Clock
from pygame.draw import rect
from utils.colors import black, white, red, cyan

clock = Clock()

window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Bouncing square")

SPAWN_POWERUP = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_POWERUP, random.randint(3000, 6000))

powerups_list = ['heal', 'damage']

def draw_window(square_1, square_2, powerups):
    window.fill(black)

    rect(window, white, (0, 10, 500, 500), width=5)

    square_1.draw(window)
    square_2.draw(window)

    for hp in powerups:
        hp.draw(window)

    rect(window, red, (10, 530, square_1.health * 2.4, 10))
    for i in range(20):
        rect(window, black, (10 + 24 * i, 530, 24, 10), width=2, border_radius=2)
    rect(window, cyan, (10, 550, square_2.health * 2.4, 10))
    for i in range(20):
        rect(window, black, (10 + 24 * i, 550, 24, 10), width=2, border_radius=2)

    pygame.display.update()