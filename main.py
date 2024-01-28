# Example file showing a circle moving on screen
import pygame
import dilute
<<<<<<< HEAD
<<<<<<< HEAD
import mixing
=======
from state import User
from datetime import datetime, timedelta
>>>>>>> 8fe7aa4 (States)
=======
import goofymarwo
>>>>>>> 8b52627 (I carried the team)

# pygame setup
pygame.init()
<<<<<<< HEAD
<<<<<<< HEAD
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
#
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
=======
screen = pygame.display.set_mode((1193, 498))
=======
screen = pygame.display.set_mode((800, 600))
>>>>>>> f005400 (combined dilute and main)
clock = pygame.time.Clock()
running = True
bg = pygame.transform.scale(pygame.image.load("background.jpg"), (800,600))
pygame.font.init()
my_font = pygame.font.SysFont('oldenglishtext', 30)
user = User()
display = False

icon_1 = pygame.Vector2(335 *0.67, 130 * 1.2 +40)
icon_2 = pygame.Vector2(834*0.67, 167* 1.2 + 40)
icon_3 = pygame.Vector2(465*0.67, 62* 1.2 + 40)
icon_4 = pygame.Vector2(728*0.67, 95* 1.2 + 40)

offset = pygame.Vector2(-55*0.67, 110* 1.2)
# create a surface object, image is drawn on it.
imp = pygame.image.load("pin.png")
imp1 = pygame.transform.scale(imp, (85, 85))
imp2 = pygame.transform.scale(imp, (85, 85))
imp3 = pygame.transform.scale(imp, (85, 85))
imp4 = pygame.transform.scale(imp, (85, 85))
text_surface_1 = my_font.render('Stage 1: Combine', False, (0,0,0), (255,255,255))
text_surface_2 = my_font.render('Stage 2: Ferment', False, (0,0,0), (255,255,255))
text_surface_3 = my_font.render('Stage 3: Dilute', False, (0,0,0), (255,255,255))
text_surface_4 = my_font.render('Stage 4: Bottle', False, (0,0,0), (255,255,255))

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aa6e90d (main-menu)

=======
>>>>>>> c984c89 (Added Dilution)
=======

score = 0

>>>>>>> f005400 (combined dilute and main)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
<<<<<<< HEAD

<<<<<<< HEAD
            if rec1.collidepoint(pos):
<<<<<<< HEAD
                mixing.mixing(screen, clock)
            elif rec2.collidepoint(pos):
                # fermenting
                print()
            elif rec3.collidepoint(pos):
                dilute.dilute(screen, clock)
<<<<<<< HEAD
            elif rec4.collidepoint(pos):
                # bottling
                print()
=======
=======
            if rec3.collidepoint(pos):
>>>>>>> 3a12e8f (move dilute to state 3)
=======
            
            if rec1.collidepoint(pos):
                score += mixing.mixing(screen, clock)
            if rec2.collidepoint(pos):
                # ferment
                print()
            if rec3.collidepoint(pos):
                score += dilute.dilute(screen, clock)
            if rec4.collidepoint(pos):
                # bottle
                print()
>>>>>>> f005400 (combined dilute and main)
=======
            if rec4.collidepoint(pos):
                score = goofymarwo.hacks(screen,clock)
                print (score)
>>>>>>> 8b52627 (I carried the team)

                ### This is kinda weird but basically this checks if the alcohol is at this stage or not
                ### if it is, then normal
                ### if not then no action available really...
                if user.state == 2:
                    score = dilute.dilute(screen, clock)
                    user.next_stage(score)
                else:
                    display = True
                    start_time = datetime.now()
>>>>>>> 8fe7aa4 (States)

<<<<<<< HEAD
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

=======
>>>>>>> aa6e90d (main-menu)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
<<<<<<< HEAD
    dt = clock.tick(60) / 1000
=======
    dt = clock.tick(60)
    screen.blit(bg, (0, 0))
    rec1 = screen.blit(imp1, icon_1)
    rec2 = screen.blit(imp2, icon_2)
    rec3 = screen.blit(imp3, icon_3)
    rec4 = screen.blit(imp4, icon_4)
    if rec1.collidepoint(pygame.mouse.get_pos()):
        imp1 = pygame.transform.scale(imp, (100,100))
        screen.blit(text_surface_1, icon_1 + offset)
    else:
        imp1 = pygame.transform.scale(imp, (85, 85))
    if rec2.collidepoint(pygame.mouse.get_pos()):
        imp2 = pygame.transform.scale(imp, (100,100))
        screen.blit(text_surface_2, icon_2 + offset)
    else:
        imp2 = pygame.transform.scale(imp, (85, 85))
    if rec3.collidepoint(pygame.mouse.get_pos()):
        imp3 = pygame.transform.scale(imp, (100,100))
        screen.blit(text_surface_3, icon_3 + offset)
    else:
        imp3 = pygame.transform.scale(imp, (85, 85))
    if rec4.collidepoint(pygame.mouse.get_pos()):
        imp4 = pygame.transform.scale(imp, (100,100))
        screen.blit(text_surface_4, icon_4 + offset)
    else:
        imp4 = pygame.transform.scale(imp, (85, 85))
>>>>>>> aa6e90d (main-menu)

    if display:
        error = my_font.render("Alcohol has passed this stage", True, (0,0,0), (255,255,255))
        err_rect = screen.blit(error, (500*0.67, 400))
        if start_time + timedelta(seconds=3) < datetime.now():
            display = False

pygame.quit()