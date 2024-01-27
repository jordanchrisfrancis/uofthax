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
windowsize = Vector2(1280, 720)
windowcentre = windowsize // 2

screen = pg.display.set_mode((windowsize))

reference_dict = {}


objects = []


rect1 = pg.Rect(0, 700, 1280, 100)


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
        

    

        
    
    
def main():
    pg.init()
    activetop = False
    clock = pg.time.Clock()
    barrel = pg.transform.scale(pg.image.load("data/barreltop.png"), (200,200))
    
    
    running = True
    screen.fill([188, 158, 130])

    pg.draw.rect(screen, (181, 101, 29), rect1)
    
    
    test_object = Object(500, 500, 200, 200, pg.image.load("data/barrelsprite.png"))
    
    bt = barreltop(windowcentre)
    
#    surf_centre = (
 #       (windowsize[0]-bt.surf.get_width())/2,
  #      (windowsize[1]-bt.surf.get_height())/2
   # )


    while running:
        pos = pg.mouse.get_pos()

        fps = 60    
        for obj in objects:
            obj.update()
        
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bt.rect.collidepoint(event.pos):
                        activetop = True
            if event.type == pg.MOUSEMOTION:
                if activetop == True:
                        bt.update(pos)
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    activetop = False
            if event.type == pg.QUIT:
                running = False
        dt = clock.tick(fps)
#        print(bt.angle)

        bt.draw(screen)
        
        pg.display.flip()
        
main()

    
    





                

