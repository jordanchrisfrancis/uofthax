import pygame as pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
)

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load("player.png").convert(), (100, 100))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Clickable(pygame.sprite.Sprite):
    def __init__(self):
        super(Clickable, self).__init__()
        self.surf = pygame.Surface((50 * 2, 50 * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.surf, (0,255,0), (50, 50), 50, 100)
        self.rect = self.surf.get_rect(center = (200,200))

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def change_color(self, color):
        x = self.rect.x
        y = self.rect.y
        self.surf = pygame.Surface((50 * 2, 50 * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.surf, color, (50, 50), 50, 100)
        self.rect = self.surf.get_rect(center = (x+50,y+50))

    def bigger(self):
        x = self.rect.x
        y = self.rect.y
        self.surf = pygame.transform.scale(self.surf, (200,200))
        self.rect = self.surf.get_rect(center = (x+100, y+100))

    def smaller(self):
        x = self.rect.x
        y = self.rect.y
        self.surf = pygame.transform.scale(self.surf, (50,50))
        self.rect = self.surf.get_rect(center = (x+25,y+25))

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((50,100))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        

        



SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600


screen =  pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Player()
click = Clickable()
wall = Wall()


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("ESCAPE")
                running = False
    screen.fill((255,255,255))

    pressed_keys = pygame.key.get_pressed()

    click.update(pressed_keys)

    if click.rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            print("Click")
            click.change_color((0,0,255))
        else:
            print("Over")
            click.bigger()
    else:
        click.smaller()
        
    screen.blit(click.surf, click.rect)
    screen.blit(wall.surf, wall.rect)

    


    pygame.display.flip()
    clock.tick(30)

pygame.quit()