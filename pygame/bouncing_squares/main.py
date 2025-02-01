import random
import pygame
from pygame.time import Clock
from pygame.draw import rect
from pygame.font import SysFont

from utils.colors import red, cyan, black, white
from utils.squares import Square

pygame.init()

clock = Clock()

window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Bouncing square")

def draw_window():
    window.fill(black)

    rect(window, white, (0, 10, 500, 510), width=5)

    square_1.draw(window)
    square_2.draw(window)

    text_1 = font.render(f"Red: {square_1.health}", 1, red)
    text_2 = font.render(f"Cyan: {square_2.health}", 1, cyan)

    window.blit(text_1, (10, 520))
    window.blit(text_2, (10, 550))

    pygame.display.update()

square_1 = Square(random.randint(20, 380), random.randint(30, 90), 100, red)
square_2 = Square(random.randint(20, 380), random.randint(290, 380), 100, cyan)

font = SysFont('comicsans', size=20, bold=True)

run = True
while run:
    pygame.time.delay(100)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if square_1.visible:
        square_1.move(window)
    if square_2.visible:
        square_2.move(window)

    square_1.collide(square_2)
    
    draw_window()

pygame.quit()