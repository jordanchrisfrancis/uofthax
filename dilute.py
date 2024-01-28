
import pygame

def dilute(screen: pygame.Surface, clock: pygame.time.Clock):
    # pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('oldenglishtext', 30)
    # screen = pygame.display.set_mode((1193, 498))
    # clock = pygame.time.Clock()
    running = True
    allow = True
    tap1 = pygame.transform.scale(pygame.image.load("tap.png"), (85,85))
    barrel = pygame.transform.scale(pygame.image.load("barrel.webp"), (200,200))
    water_tank = pygame.transform.scale(pygame.image.load("water_tank.png"), (500,500))
    tap2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load("tap.png"), True, False), (85,85))
    orange_drop = pygame.transform.scale(pygame.image.load("orange_drop.png"), (20,20))
    blue_drop = pygame.transform.scale(pygame.image.load("blue_drop.webp"), (20,20))

    total_area = 0
    length = 590
    rate = 3500
    percentage = 0
    water_area = 0
    alcohol_area = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if fin_rect.collidepoint(pos):
                    running = False
                    return 1 # this would be a score
                    
        pygame.display.flip()
        screen.fill((92,64,51))
        pygame.draw.rect(screen, (30, 0, 0), pygame.Rect(0, 400, 1193, 100))
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(220, 420, 630, 20))
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(220, 350, 20, 90))
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(830, 350, 20, 90))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(220,375,20, 5))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(830,375,20, 5))
        # pygame.draw.rect(screen, (0,255,0), (240, 385, 590, 35))

        dt = clock.tick(60) / 1000
        tap_rect = screen.blit(tap1, (200,250))
        barrel_rect = screen.blit(barrel, (0,200))
        water_rect = screen.blit(water_tank, (700, 0))
        tap2_rect = screen.blit(tap2, (790, 250))
        finish = my_font.render("Submit", True, (0,0,0), (255,255,255))
        fin_rect = screen.blit(finish, (500, 100))

        mouse = pygame.mouse.get_pressed()
        if mouse[0] == True and allow:
            pos = pygame.mouse.get_pos()
            if tap_rect.collidepoint(pos):
                screen.blit(orange_drop, (265,340))
                total_area += rate*dt
                alcohol_area += rate*dt
            if tap2_rect.collidepoint(pos):
                screen.blit(blue_drop, (790, 340))
                total_area += rate*dt
                water_area += rate*dt
        percentage = 0.6*alcohol_area/total_area if alcohol_area != 0 else 0
        if percentage < 0.45 and percentage > 0.35:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
        text_surface= my_font.render(str(round(percentage*100,1)), True, color, (255,255,255))
        screen.blit(text_surface, (0,0))
        if percentage > 0.4:
            red = -300 * percentage + 330
            blue = 35
        else:
            red = 362.5 * percentage + 65
            blue = -190 * percentage + 154
        if 420-total_area/590 <= 350:
            allow = False
            fail = my_font.render("That's More Than Enough Buddy!", True, (0,0,0), (255, 255, 255))
            screen.blit(fail, (300,200))
        pygame.draw.rect(screen, (red,115,blue), (240, 420-total_area/590, 590, total_area/590))