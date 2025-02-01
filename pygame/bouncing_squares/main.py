import random
import pygame
from pygame import mixer
from pygame.time import Clock
from pygame.draw import rect
from pygame.font import SysFont

from utils.colors import red, cyan, black, white
from utils.squares import Square, HealthPowerUp

pygame.init()
mixer.init()

clock = Clock()

window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Bouncing square")

SPAWN_HP = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_HP, random.randint(3000, 6000))

def draw_window():
    if not game_end:
        window.fill(black)

        rect(window, white, (0, 10, 500, 510), width=5)

        square_1.draw(window)
        square_2.draw(window)

        for hp in health_powerups:
            hp.draw(window)

        text_1 = font.render(f"Red: {square_1.health}", 1, red)
        text_2 = font.render(f"Cyan: {square_2.health}", 1, cyan)

        window.blit(text_1, (10, 520))
        window.blit(text_2, (10, 550))

        pygame.display.update()

square_1 = Square(random.randint(20, 380), random.randint(30, 90), 100, red)
square_2 = Square(random.randint(20, 380), random.randint(290, 380), 100, cyan)

health_powerups = []

font = SysFont('comicsans', size=20, bold=True)

run = True
game_end = False
win_sound_played = False

while run:
    pygame.time.delay(100)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == SPAWN_HP and len(health_powerups) < 3 and not game_end:
            health_powerups.append(HealthPowerUp(random.randint(20, 480), random.randint(20, 480)))
            pygame.time.set_timer(SPAWN_HP, random.randint(3000, 6000))

    if square_1.visible:
        square_1.move(window)
    if square_2.visible:
        square_2.move(window)

    square_1.collide(square_2)

    for powerup in health_powerups[:]:
        if powerup.visible:
            if (square_1.x < powerup.x + powerup.side and
                square_1.x + square_1.side > powerup.x and
                square_1.y < powerup.y + powerup.side and
                square_1.y + square_1.side > powerup.y):
                health_gain = mixer.Sound('effects/health_gain.wav')
                health_gain.play()
                square_1.health = min(100, square_1.health + 10)
                square_1.side = min(100, square_1.side + 6)
                health_powerups.remove(powerup)
            elif (square_2.x < powerup.x + powerup.side and
                square_2.x + square_2.side > powerup.x and
                square_2.y < powerup.y + powerup.side and
                square_2.y + square_2.side > powerup.y):
                health_gain = mixer.Sound('effects/health_gain.wav')
                health_gain.play()
                square_2.health = min(100, square_2.health + 10)
                square_2.side = min(100, square_2.side + 6)
                health_powerups.remove(powerup)
    
    if not square_1.visible or not square_2.visible:
        if not win_sound_played:
            win_sound = mixer.Sound('effects/win.wav')
            win_sound.play()
            win_sound_played = True
        
        game_end = True
        health_powerups.clear()
        pygame.display.update()

    if game_end:
        if square_1.visible:
            win_color = square_1.color
            rect(window, win_color, (0, 10, 500, 510))
            pygame.display.update()
        elif square_2.visible:
            win_color = square_2.color
            rect(window, win_color, (0, 10, 500, 510))
            pygame.display.update()
        else:
            rect(window, white, (0, 10, 500, 510), width=10)
            pygame.display.update()
        
    else:         
        draw_window()

pygame.quit()