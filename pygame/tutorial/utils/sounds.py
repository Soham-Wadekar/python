from pygame import mixer
from pygame.mixer import Sound, music

mixer.init()

bullet_sound = Sound('sprites/sounds/bullet.mp3')
hit_sound = Sound('sprites/sounds/hit.mp3')

bg_music = music.load('sprites/sounds/music.mp3')
music.set_volume(0.02)