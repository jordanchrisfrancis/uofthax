
import pygame
import math


def rbf(percentage, height):
    mean_percentage = 40
    mean_height = 45
    percentage *= 100
    distance = (mean_height - height)**2 + (mean_percentage - percentage)**2
    power = distance/(2*25)
    return math.exp(-power)


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
                    return rbf(percentage, total_area/590) # this would be a score
                    
        pygame.display.flip()
        screen.fill((92,64,51))
        pygame.draw.rect(screen, (30, 0, 0), pygame.Rect(0*0.67, 400* 1.2, 1193*0.67, 100* 1.2))
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(220*0.67 + 50, 420* 1.2, 630*0.67, 20* 1.2))
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(220*0.67 + 50, 350* 1.2, 20*0.67, 90* 1.2))
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(830*0.67 + 50, 350* 1.2, 20*0.67, 90* 1.2))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(220*0.67  + 50,375* 1.2,20*0.67, 5* 1.2))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(830*0.67 + 50,375* 1.2,20*0.67, 5* 1.2))
        # pygame.draw.rect(screen, (0,255,0), (240, 385, 590, 35))

        dt = clock.tick(60) / 1000
        tap_rect = screen.blit(tap1, (200*0.67 + 50,250* 1.2))
        barrel_rect = screen.blit(barrel, (0*0.67, 200* 1.2))
        tap2_rect = screen.blit(tap2, (790*0.67 + 50, 250* 1.2))
        water_rect = screen.blit(water_tank, (700*0.67, 0* 1.2 + 50))
        finish = my_font.render("Submit", True, (0,0,0), (255,255,255))
        fin_rect = screen.blit(finish, (500*0.67, 100* 1.2))

        mouse = pygame.mouse.get_pressed()
        if mouse[0] == True and allow:
            pos = pygame.mouse.get_pos()
            if tap_rect.collidepoint(pos):
                screen.blit(orange_drop, (265*0.67 + 70,340* 1.2 - 25))
                total_area += rate*dt
                alcohol_area += rate*dt
            if tap2_rect.collidepoint(pos):
                screen.blit(blue_drop, (790*0.67 + 50, 340* 1.2 - 25))
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
            screen.blit(fail, (300 * 0.67,200* 1.2))
        pygame.draw.rect(screen, (red,115,blue), (240*0.67 + 50, (420-total_area/590) * 1.2, 590*0.67, (total_area/590) * 1.2))