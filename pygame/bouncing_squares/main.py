import random
import pygame
from pygame import mixer
from pygame.font import SysFont

from utils.colors import red, cyan
from utils.squares import Square, Powerup
from utils.util_funcs import clock, window, powerups_list, SPAWN_POWERUP, draw_window

pygame.init()
mixer.init()

square_1 = Square(random.randint(50, 350), random.randint(60, 80), 160, red)
square_2 = Square(random.randint(50, 350), random.randint(260, 350), 160, cyan)

powerups = []

font = SysFont('comicsans', size=20, bold=True)

run = True
win_sound_played = False

while run:
    pygame.time.delay(100)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == SPAWN_POWERUP and len(powerups) < 5:
            powerups.append(Powerup(random.randint(20, 480), random.randint(20, 480), type=random.choice(powerups_list)))
            pygame.time.set_timer(SPAWN_POWERUP, random.randint(3000, 6000))

    if square_1.visible:
        square_1.move(window)
    if square_2.visible:
        square_2.move(window)

    if square_1.end or square_2.end:
            powerups.clear()
            if square_1.end and square_2.end:
                continue
            elif square_1.end:
                while square_1.side < 480:
                    square_1.x = window.get_width() // 2 - square_1.side // 2 - 5
                    square_1.y = window.get_height() // 2 - square_1.side // 2 - 45

                    draw_window(square_1, square_2, powerups)
                    pygame.display.update()

                    square_1.side += 10
                    pygame.time.delay(30)
            elif square_2.end:
                while square_2.side < 480:      
                    square_2.x = window.get_width() // 2 - square_2.side // 2 - 5
                    square_2.y = window.get_height() // 2 - square_2.side // 2 - 45

                    draw_window(square_1, square_2, powerups)
                    pygame.display.update()

                    square_2.side += 10
                    pygame.time.delay(30)

    square_1.collide(square_2)

    for powerup in powerups[:]:
        if powerup.visible:
            if (square_1.x < powerup.x + powerup.side and
                square_1.x + square_1.side > powerup.x and
                square_1.y < powerup.y + powerup.side and
                square_1.y + square_1.side > powerup.y):
                match powerup.type:
                    case 'heal':
                        health_gain = mixer.Sound('effects/health_gain.wav')
                        health_gain.play()
                        square_1.health = min(200, square_1.health + 10)
                        square_1.side = min(160, square_1.side + 6)
                    case 'damage':
                        damage = mixer.Sound('effects/damage.mp3')
                        damage.play()
                        square_1.health = max(0, square_1.health - 10)
                        square_1.side = max(40, square_1.side - 6)
                powerups.remove(powerup)
            elif (square_2.x < powerup.x + powerup.side and
                square_2.x + square_2.side > powerup.x and
                square_2.y < powerup.y + powerup.side and
                square_2.y + square_2.side > powerup.y):
                match powerup.type:
                    case 'heal':
                        health_gain = mixer.Sound('effects/health_gain.wav')
                        health_gain.play()
                        square_2.health = min(200, square_2.health + 10)
                        square_2.side = min(160, square_2.side + 6)
                    case 'damage':
                        damage = mixer.Sound('effects/damage.mp3')
                        damage.play()
                        square_2.health = max(0, square_2.health - 10)
                        square_2.side = max(40, square_2.side - 6)
                powerups.remove(powerup)
        
    else:         
        draw_window(square_1, square_2, powerups)

pygame.quit()