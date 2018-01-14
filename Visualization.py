import pygame
from pygame.locals import *
import time
def allcolors():
    all_colors = pygame.Surface((4096, 4096), depth=24)
    for r in range(256):
        x = (r & 15) * 256
        y = (r >> 4) * 256
        for g in range(256):
            for b in range(256):
                all_colors.set_at((x + g, y + b), (r, g, b))
    pygame.image.save(all_colors, "allcolors.bmp")
def blend_color(color1,color2,blend_factor):
    r1,g1,b1=color1
    r2,g2,b2=color2
    r=r1+(r2-r1)*blend_factor
    b=b1+(b2-b1)*blend_factor
    g=g1+(g2-g1)*blend_factor
    return int(r),int(g),int(b)
def main():
    #game init
    pygame.init()
    SCREEN_SIZE=(400,300)
    screen = pygame.display.set_mode(SCREEN_SIZE,0)
    pygame.display.set_caption("fractal")

    #default var
    c = {"black": (0, 0, 0), "white": (255, 255, 255),"red":(255,0,0)}
    my_font=pygame.font.SysFont("Times New Roman",20)
    screen.fill(c["white"])
    pygame.display.update()

    #ftp
    count = 0
    rate = 0
    t0 = time.clock()


    while True:
        #pygame.event.set_blocked()
        event=pygame.event.wait()
        if event.type==pygame.QUIT:
            break
        p

    #ftp
    count += 1
    if count == 500:
        t1 = time.clock()
        rate = 500 / (t1 - t0)
        t0 = t1
        count = 0

main()