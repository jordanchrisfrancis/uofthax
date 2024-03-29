try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame as pg
    from pygame import Vector2
    from socket import *
    from pygame.locals import *
except ImportError:
    print(f"error loading module: {error}")
    sys.exit(2)
    
#initialize screen and global objects
BLACK = (0, 0, 0)
windowsize = Vector2(800, 600)
windowcentre = windowsize // 2

pg.font.init()
my_font = pg.font.SysFont('oldenglishtext', 30)

screen = pg.display.set_mode((windowsize))
screen_rect = screen.get_rect()

reference_dict = {}
objects = []

rect1 = pg.Rect(0, 500, 800, 100)

class Button(pg.sprite.Sprite):
    def __init__(self, text, pos):
        self.text = text
        self.surf = my_font.render(text, True, (0,0,0), (255,255,255))
        self.rect = self.surf.get_rect()
        self.pos = pos
    

class Label(pg.sprite.Sprite):
    def __init__(self, text, pos):
        self.text = text
        self.surf = my_font.render(text, True, (0,0,0), (255,255,255))
        self.rect = self.surf.get_rect()
        self.pos = pos


def rotate_on_pivot(image, angle, pivot, origin):
    
    surf = pg.transform.rotate(image, angle)
    offset = pivot + (origin - pivot).rotate(-angle)
    rect = surf.get_rect(centre = offset)
    
    return surf, rect

#redo class
class Object:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.velocity = [0, 0]
        
        objects.append(self)
        
    def draw(self):
        screen.blit(pg.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.draw()
        
        
        
class barreltop(pg.sprite.Sprite): 
    is_held = False
    past_pos = None
    
    def __init__(self, pivot):
#        self.surf = pg.transform.scale(pg.image.load("data/barreltop.png").convert(), (200, 200))
               
        self.image_orig = pg.transform.scale(pg.image.load("data/barreltop.png").convert(), (200, 200))
        self.image = self.image_orig
        self.image.set_colorkey("black", RLEACCEL) 
        self.rect = self.image.get_rect(center = pivot)
        
        

    
    def held(self, point):
        if self.rect.collidepoint(point):
            self.is_held = True
            
    def not_held(self):
        self.is_held = False


    
    def update(self, mpos):
        mpos = pg.Vector2(mpos)
        center = pg.Vector2(self.rect.center)
        vector = mpos - center
        #grab data for second angle
        angle = vector.as_polar()[1]
        self.image = pg.transform.rotate(self.image_orig, -angle)
        #keep image in centre
        self.rect = self.image.get_rect(center=self.rect.center)

        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
def score(rotation):
    score = 0
    if 1000 > rotation > 380:
        score += 3
    elif 250 > rotation > 100:
        score += 2
    elif rotation > 90:
        score += 1
    if score > 25:
        return 25
    else:
        return score
        


        
    
    
def ferment(screen, clock):
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((windowsize))
    CUSTOMTIMER = pg.USEREVENT + 1
    
    activetop = False
    clock = pg.time.Clock()    
    pole = Vector2(screen_rect.center)
    #initial zero vector
    vec = Vector2()
    
    #sets polar coordinates
    vec.from_polar((100, -90))
    
    countline = vec[1]

    
    running = True
    screen.fill([188, 158, 130])

    pg.draw.rect(screen, (181, 101, 29), rect1)
    
    
    test_object = Object(100, 310, 200, 200, pg.image.load("data/barrelsprite.png"))
    
    bt = barreltop(windowcentre)
    rotation = 0
    frame_rate = 60 
    frame_count = 0
    start_time = 90
    
    label = Label("You have 250 rotations, spin the barrel top to close and ferment the whiskey!", (50, 100))
    label2 = Label("time is up! score tallied", (100, 150)) 
    submit = Button("Submit", (600, 500))
   

    while running:
    
        pos = pg.mouse.get_pos()

        pg.time.set_timer(CUSTOMTIMER, 25000)

        pg.draw.line(screen, (200, 90, 20), pole, pole+vec, 3)
        
        
            
        print(rotation)

           
        for obj in objects:
            obj.update()
        
        for event in pg.event.get():            
            if event.type == pg.MOUSEBUTTONDOWN:
                if submit.rect.collidepoint(event.pos):
                    return score(rotation)
                if event.button == 1:
                    if bt.rect.collidepoint(event.pos):
                        activetop = True
            if event.type == pg.MOUSEMOTION:
                if activetop == True:
                        bt.update(pos)
                        r, phi = (pos-pole).as_polar()
                        if phi >= -360:
                            rotation += 1
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    activetop = False
            if event.type == CUSTOMTIMER:
                screen.blit(label2.surf, label2.pos) 
                
                
            if event.type == pg.QUIT:
                running = False

            
        screen.blit(label.surf, label.pos)   
        submit.rect = screen.blit(submit.surf, submit.pos)


        dt = clock.tick(frame_rate) 
#        print(bt.angle)
        bt.draw(screen)
        pg.display.flip()


    
    





                


