import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
    MOUSEMOTION,
    MOUSEBUTTONUP,
    MOUSEBUTTONDOWN,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT =  600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.font.init()
my_font = pygame.font.SysFont('oldenglishtext', 30)



class Pestle(pygame.sprite.Sprite):
    """
    self.surf
    self.rect
    self.collision_rect
    """
    is_held = False
    past = []

    def __init__(self):
        # Sets the actual surface of the pestle
        self.surf = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("Pestle2.png").convert(),35), (300,300))
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey("black", RLEACCEL)
        self.rect = self.surf.get_rect(center = (200,200))

        # Sets the collision surface of the pestle
        self.collision_rect = self.rect.copy()
        self.collision_rect.width /= 10
        self.collision_rect.x += self.collision_rect.width * 4.5
        self.collision_rect.height /= 1.40
        self.collision_rect.y += self.collision_rect.height / 5

    def held(self, point):
        if self.collision_rect.collidepoint(point):
            self.is_held = True


    def not_held(self):
        self.is_held = False

    def update(self, rel_pos, collision_funcs):
        if self.is_held:
            temp = self.collision_rect.copy()
            temp.move_ip(rel_pos)
            for func in collision_funcs:
                if func(temp):
                    
                    return
            self.rect.move_ip(rel_pos)
            self.collision_rect.move_ip(rel_pos)

    def update_grains(self, rel, barleys):
        temp = []
        if self.is_held:
            for barley in barleys:
                if barley.is_rect_colliding(self.collision_rect):
                    temp.append(barley)
                    if barley in self.past:
                        self.rect.move_ip((rel[0] * -2, rel[1] * -2))
                        self.collision_rect.move_ip((rel[0] * -2, rel[1] * -2))
                    else: 
                        barley.hits += 1
                    barley.speed = (barley.speed[0] + rel[0], barley.speed[1])

        self.past = temp

    def is_rect_colliding(self, rect):
        return self.collision_rect.colliderect(rect)

class Bowl(pygame.sprite.Sprite):
    """ 
    collision_rect_left
    collision_rect_right
    collision_rect_bot
    """

    def __init__(self):
        self.surf = pygame.transform.scale(pygame.image.load("mortar.png").convert(), (150,150))
        self.surf.set_colorkey("black", RLEACCEL)
        self.rect = self.surf.get_rect(center = (500,500))

        # set the inside rect where there are no collisions
        self.collision_rect_left = self.rect.copy()
        self.collision_rect_left.width *= 0.22
        self.collision_rect_right = self.collision_rect_left.copy()
        self.collision_rect_right.x += self.collision_rect_right.width * 3.6
        self.collision_rect_bot = self.rect.copy()
        self.collision_rect_bot.height *= 0.2
        self.collision_rect_bot.y += self.collision_rect_bot.height * 3.95

    def is_rect_colliding(self, rect):
        return self.collision_rect_left.colliderect(rect) or self.collision_rect_right.colliderect(rect) or self.collision_rect_bot.colliderect(rect) 

class Barley(pygame.sprite.Sprite):
    speed = (0,0.5)
    hits = 0
    surf = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("barley.png").convert(), (25,40)), 90)
    def __init__(self, pos = (450,20)):
        self.rect = self.surf.get_rect(center = pos)

    def update(self, collision_funcs):
        temp = self.rect.copy()
        temp.x += self.speed[0]
        temp.y += self.speed[1]
        for func in collision_funcs:
            if func(temp):
                self.speed = (0,self.speed[1] * -0.5)
                return
        self.rect.move_ip(self.speed)
        self.speed = (self.speed[0], self.speed[1]+0.1)
        self.update_hits()
    
    def update_hits(self):
        if self.hits == 5:
            print("ground")
            x = self.rect.x
            y = self.rect.y
            self.surf = pygame.transform.scale(self.surf, (25,20))
            self.rect = self.surf.get_rect(center = (x + 12.5, y + 10))
        elif self.hits == 10:
            x = self.rect.x
            y = self.rect.y
            self.surf = pygame.transform.scale(self.surf, (15,10))
            self.rect = self.surf.get_rect(center = (x + 7.5, y + 5))
        elif self.hits == 15:
            x = self.rect.x
            y = self.rect.y
            self.surf = pygame.transform.scale(self.surf, (8,5))
            self.rect = self.surf.get_rect(center = (x + 4, y + 2.5))

    def is_rect_colliding(self, rect):
        return self.rect.colliderect(rect)

class Button(pygame.sprite.Sprite):
    def __init__(self, text):
        self.text = text
        self.surf = my_font.render(text, True, (0,0,0), (255,255,255))

        

# Define the important items
clock = pygame.time.Clock()
pestle = Pestle()
bowl = Bowl()
barleys = [Barley()]
barleys_collision= [barleys[0].is_rect_colliding]
button = Button("Submit")



def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEBUTTONDOWN:
                pestle.held(event.pos)
                temp = Barley((520,20))
                barleys.append(temp)
                barleys_collision.append(temp.is_rect_colliding)
            elif event.type == MOUSEBUTTONUP:
                pestle.not_held()
            elif event.type == MOUSEMOTION:
                pestle.update(event.rel, [bowl.is_rect_colliding])
                pestle.update_grains(event.rel, barleys)



    
        screen.fill((255,0,0))

        screen.blit(pestle.surf, pestle.rect)
        screen.blit(bowl.surf, bowl.rect)

        pygame.draw.rect(screen, "green", pygame.Rect(pestle.collision_rect), 2)
        pygame.draw.rect(screen, "BLUE", pygame.Rect(bowl.collision_rect_left), 2)
        pygame.draw.rect(screen, "BLUE", pygame.Rect(bowl.collision_rect_right), 2)
        pygame.draw.rect(screen, "BLUE", pygame.Rect(bowl.collision_rect_bot), 2)
        pygame.draw.rect(screen, "green", pygame.Rect(bowl.rect), 2)

        for i in range(0, len(barleys)):
            barleys[i].update([bowl.is_rect_colliding] + barleys_collision[0:i] + barleys_collision[i+1:len(barleys)])
            screen.blit(barleys[i].surf, barleys[i].rect)
            pygame.draw.rect(screen, "blue", pygame.Rect(barleys[i].rect), 2)

        
        screen.blit(button.surf, (600, 500))


        pygame.display.update()
        pygame.display.flip()
        clock.tick(120)
        
loop()