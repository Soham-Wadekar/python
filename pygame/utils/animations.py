import pygame.image as img

walk_left = [img.load(f'sprites/player/L{i}.png') for i in range(1, 10)]
walk_right = [img.load(f'sprites/player/R{i}.png') for i in range(1, 10)]

walk_left_enemy = [img.load(f'sprites/enemy/L{i}.png') for i in range(1, 12)]
walk_right_enemy = [img.load(f'sprites/enemy/R{i}.png') for i in range(1, 12)]

bg = img.load('sprites/background/bg.jpg')
stand = img.load('sprites/player/standing.png')