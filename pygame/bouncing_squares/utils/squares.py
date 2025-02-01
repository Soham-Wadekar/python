from pygame.draw import rect
from pygame import mixer

from utils.colors import pink

mixer.init()

class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
        self.x_velocity = 15
        self.y_velocity = 15
        self.health = 100
        self.visible = True

    def draw(self, window):
        border = [max(0, int(c * 0.7)) for c in self.color]
        rect(window, border, (self.x, self.y, self.side, self.side))
        rect(window, self.color, (self.x + 10, self.y + 10, self.side - 20, self.side - 20))

    def move(self, window):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x <= 10 or self.x + self.side >= window.get_width() - 10:
            hit_sound = mixer.Sound("effects/wall_hit.wav")
            hit_sound.play()
            self.x_velocity *= -1
        if self.y <= 20 or self.y + self.side >= window.get_height() - 90:
            hit_sound = mixer.Sound("effects/wall_hit.wav")
            hit_sound.play()
            self.y_velocity *= -1

        if self.health <= 0:
            hit_sound.stop()

    def collide(self, other):
        if self.visible and other.visible and (
            self.x < other.x + other.side and
            self.x + self.side > other.x and
            self.y < other.y + other.side and
            self.y + self.side > other.y
        ):
            self.side = max(40, self.side - 6)
            other.side = max(40, other.side - 6)
            self.health = max(0, self.health - 10)
            other.health = max(0, other.health - 10)

            hit_sound = mixer.Sound("effects/hit.wav")
            hit_sound.play()

            overlap_x = min(self.x + self.side - other.x, other.x + other.side - self.x)
            overlap_y = min(self.y + self.side - other.y, other.y + other.side - self.y)

            if overlap_x < overlap_y:
                self.x_velocity *= -1
                other.x_velocity *= -1

                if self.x < other.x:
                    self.x -= overlap_x
                else:
                    self.x += overlap_x
            else:
                self.y_velocity *= -1
                other.y_velocity *= -1

                if self.y < other.y:
                    self.y -= overlap_y
                else:
                    self.y += overlap_y

            if self.health <= 0:
                self.visible = False
                self.side = 0
            if other.health <= 0:
                other.visible = False
                other.side = 0

    def ensure_in_bounds(self, window):
        if self.x < 0:
            self.x = 0
            self.x_velocity = abs(self.x_velocity)
        elif self.x + self.side > window.get_width():
            self.x = window.get_width() - self.side
            self.x_velocity = -abs(self.x_velocity)

        if self.y < 0:
            self.y = 0
            self.y_velocity = abs(self.y_velocity)
        elif self.y + self.side > window.get_height():
            self.y = window.get_height() - self.side
            self.y_velocity = -abs(self.y_velocity)

class HealthPowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.side = 20
        self.color = pink
        self.visible = True

    def draw(self, window):
        border = [max(0, int(c * 0.7)) for c in self.color]
        rect(window, border, (self.x, self.y, self.side, self.side))
        rect(window, self.color, (self.x + 4, self.y + 4, self.side - 8, self.side - 8))