import pygame
from pygame import display
from pygame.time import Clock
from utils.animations import *
from utils.colors import green, black
from utils.objects import Enemy, Player, Projectile
from utils.sounds import *

pygame.init()

window = display.set_mode((500, 500))
display.set_caption("Basic Game")

clock = Clock()
music.play(-1)

score = 0

def redraw_game_window():
    window.blit(bg, (0, 0))

    text = font.render(f"Score: {score}", 1, black)
    window.blit(text, (400, 20))

    player.draw(window)

    for bullet in bullets:
        bullet.draw(window)

    goblin.draw(window)

    display.update()

# Main loop
font = pygame.font.SysFont('comicsans', size=20, bold=True)

player = Player(300, 410, 64, 64)
goblin = Enemy(100, 415, 64, 64, 450)
shoot_loop = 0
bullets = []

run = True
while run:
    clock.tick(27)

    if goblin.visible:
        if player.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and player.hitbox[1] + player.hitbox[3] > goblin.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > goblin.hitbox[0] and player.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                hit_sound.play()
                player.hit(window)
                score -= 2

    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 10:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hit_sound.play()
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot_loop == 0:
        bullet_sound.play()
        if player.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 5:
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 5, green, facing))

        shoot_loop = 1

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