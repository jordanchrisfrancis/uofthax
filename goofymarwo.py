# Example file showing a circle moving on screen
import pygame
import math

def score(area):
    dis = (area-105000)**2
    print (dis)
    pow = dis/(25000)
    return math.exp(-pow)

def hacks(screen:pygame.Surface, clock: pygame.time.Clock):
# pygame setup
    # pygame.init()

    pygame.font.init()
    my_font = pygame.font.SysFont('oldenglishtext', 30)


    finish = my_font.render("Submit", True, (0,0,0), (255,255,255))
    fin_rect = finish.get_rect()

    # clock = pygame.time.Clock()
    running = True
    bg = pygame.image.load("brick2.jpeg").convert()
    tap1 = pygame.transform.scale(pygame.image.load("tap.png").convert(), (85,85))
    bg = pygame.transform.scale(bg, (800, 600))
    brown_drop = pygame.transform.scale(pygame.image.load("browndrop2.png").convert(), (20,20))
    brown_drop.set_colorkey("black")
    pygame.font.init()




    tap1 = pygame.transform.scale(pygame.image.load("tap.png"), (85,85))
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    bottle_pos = pygame.Vector2(400*0.67, 160*1.2)
    imp = pygame.image.load("bottle3.png").convert()
    imp.set_colorkey("white")
    imp1 = pygame.transform.scale(imp, (400, 350))
    rate = 500
    # clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    allow = True
    total_area = 0


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)


    
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if fin_rect.collidepoint(pos):
                    running = False
                    return score(total_area)

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        screen.blit(bg, (0, 0))
        rec1 = screen.blit(imp1, bottle_pos)
        tap_rect = screen.blit(tap1, (525*0.67,50*1.2))
        finish = my_font.render("Submit", True, (0,0,0), (255,255,255))





        mouse = pygame.mouse.get_pressed()
        if mouse[0] == True and allow:
            pos = pygame.mouse.get_pos()
            if tap_rect.collidepoint(pos):
                screen.blit((brown_drop), (590*0.67 + 20,137*1.2 - 20))
                if not total_area > 105000:
                    total_area += rate*dt

        

        pygame.draw.rect(screen, (150, 75, 0), (545*0.67 + 47, (475-total_area/590) + 30, 115, (total_area/590)))

        print(total_area)
        
        fin_rect = screen.blit(finish, (150 * 0.67,100 * 1.2))

        pygame.display.flip()
