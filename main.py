# Example file showing a circle moving on screen
import pygame
import dilute
import mixing

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1193, 498))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("background.jpg")
pygame.font.init()
my_font = pygame.font.SysFont('oldenglishtext', 30)

icon_1 = pygame.Vector2(335, 130)
icon_2 = pygame.Vector2(834, 167)
icon_3 = pygame.Vector2(465, 62)
icon_4 = pygame.Vector2(728, 95)

offset = pygame.Vector2(-55, 110)
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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if rec1.collidepoint(pos):
                mixing.mixing(screen, clock)
            elif rec2.collidepoint(pos):
                # fermenting
                print()
            elif rec3.collidepoint(pos):
                dilute.dilute(screen, clock)
            elif rec4.collidepoint(pos):
                # bottling
                print()

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

pygame.quit()