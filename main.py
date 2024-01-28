# Example file showing a circle moving on screen
import pygame
import dilute
import goofymarwo
from state import User
from datetime import datetime, timedelta
import mixing
import ferment

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
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
score_surface = my_font.render('Selling Price of Last Whiskey:' + str(user.final_score), False, (0,0,0), (255, 255, 255))


score = 0

while running:
    score_surface = my_font.render('Selling Price of Last Whiskey:' + str(round(user.final_score * 100, 2)), False, (0,0,0), (255, 255, 255))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            if rec1.collidepoint(pos):
                if user.state == 0:
                    score = mixing.mixing(screen, clock)
                    user.next_stage(score/25)
                else:
                    display = True
                    start_time = datetime.now()
            if rec2.collidepoint(pos):
                if user.state == 1:
                    score = ferment.ferment(screen, clock)
                    user.next_stage((score - 1)/2)
                else:
                    display = True
                    start_time = datetime.now()
            if rec3.collidepoint(pos):
                if user.state == 2:
                    score = dilute.dilute(screen, clock)
                    user.next_stage(score)
                else:
                    display = True
                    start_time = datetime.now()
            if rec4.collidepoint(pos):
                if user.state == 3:
                    score = goofymarwo.hacks(screen, clock)
                    user.next_stage(score)
                else:
                    display = True
                    start_time = datetime.now()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)
    screen.blit(bg, (0, 0))
    rec1 = screen.blit(imp1, icon_1)
    rec2 = screen.blit(imp2, icon_2)
    rec3 = screen.blit(imp3, icon_3)
    rec4 = screen.blit(imp4, icon_4)
    screen.blit(score_surface, (0,0))
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

    if display:
        error = my_font.render("Alcohol is not on this stage", True, (0,0,0), (255,255,255))
        err_rect = screen.blit(error, (500*0.67, 400))
        if start_time + timedelta(seconds=3) < datetime.now():
            display = False

pygame.quit()