import sys 
import pygame as pg
pg.init()

#initialize pygame package

screenwidth = 1280
screenheight = 900

rect1 = pg.Rect(200, 100, 150, 100)
screen = pg.display.set_mode((screenwidth, screenheight))

clock = pg.time.Clock()
# game clock, runs framerate

value = True

while value:
    clock.tick(60)
    screen.fill((255, 255, 255))
    
    pg.draw.rect(screen, (255, 0, 255), rect1)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            value = False
    
    pg.display.flip()
    #updates screen
    
pg.quit()