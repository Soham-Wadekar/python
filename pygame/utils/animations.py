import pygame.image as img

walk_right = [img.load(f'sprites/R{i}.png') for i in range(1, 10)]
walk_left = [img.load(f'sprites/L{i}.png') for i in range(1, 10)]
bg = img.load('sprites/bg.jpg')
stand = img.load('sprites/standing.png')