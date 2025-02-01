import pygame
from pygame.font import SysFont
from pygame.draw import rect, circle
from utils.animations import *
from utils.colors import red, black

class Player:
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
        self.hitbox = (self.x + 20, self.y + 12, 28, 52)

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

        self.hitbox = (self.x + 20, self.y + 12, 28, 52)
        # rect(window, red, self.hitbox, width=2)

    def hit(self, window):
        self.x = 60
        self.walk_count = 0
        hit_msg = SysFont('comicsans', 30)
        text = hit_msg.render("-2 pts", 1, red)
        window.blit(text, (450 - window.get_width() // 2, window.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(1000)

class Enemy:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.velocity = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 100
        self.visible = True

    def draw(self, window):
        self.move()

        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0
            
            if self.velocity < 0:
                window.blit(walk_left_enemy[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                window.blit(walk_right_enemy[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

            rect(window, black, (self.hitbox[0] - 16, self.hitbox[1] - 20, 50, 5))
            rect(window, red, (self.hitbox[0] - 16, self.hitbox[1] - 20, 50 - (0.5 * (100 - self.health)), 5))
            self.hitbox = (self.x + 20, self.y, 28, 60)
            # rect(window, red, self.hitbox, width=2)

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walk_count = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walk_count = 0

    def hit(self):
        if self.health > 10:
            self.health -= 10
        else:
            self.visible = False               
        

class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 10 * facing
    
    def draw(self, window):
        circle(window, self.color, (self.x, self.y), self.radius)