import pygame
from pygame.locals import *
def is_mandelbrot(c=0+0j):
    z=0+0j
    for i in range(250):
        if abs(z)<=2:
            z=z*z+c
        else:
            return False
    return True
def seq(start,end,num):
    delta=(end-start)/num
    i=start
    s=[]
    while i<=end:
        s.append(i)
        i+=delta
    return s



def draw_mandelbrot():
    pygame.init()
    screen=pygame.display.set_mode((360,360),0)
    pygame.display.set_caption("Mandelbrot")
    screen.fill((255,255,255))
    global size
    def generate(area):#-0.75,-0.1,0.01
        sx, sy, dlt=area
        size
        fractal = pygame.Surface((size,size))
        fractal.fill((255, 255, 255))
        i = 0
        load = 0
        for cx in seq(sx, sx+dlt, size):
            for cy in seq(sy, sy+dlt, size):
                if is_mandelbrot(complex(cx, cy)):
                    px = int((cx -sx) / dlt * size)
                    py = int((cy -sy) / dlt * size)
                    fractal.set_at((px, py), (0, 0, 0))
            load += 1
            print("{0:.2f}%".format(100 * load / size))
            screen.blit(fractal, (0, 0))
            pygame.display.flip()
        return fractal

    def get_coordinate(area, mx, my, mx1, my1):
        sx, sy, dlt = area
        cx = mx * dlt / size + sx
        cy = my * dlt / size + sy
        dlt1 = max([abs(mx1 - mx), abs(my1 - my)])
        dlt1=dlt1/size*dlt
        return (cx, cy, dlt1)

    areas = [(-2, -1.5, 3)]
    size=360
    fractal=generate(areas[0])
    #pygame.image.save(fractal,"mandelbrot(1).bmp")
    area=areas[0]
    newarea=area
    while True:
        ev=pygame.event.poll()
        if ev.type==pygame.QUIT:
            break
        if ev.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        if ev.type == pygame.MOUSEBUTTONUP:
            mx1, my1 = pygame.mouse.get_pos()
            newarea = get_coordinate(area, mx, my, mx1, my1)
            areas.append(newarea)
            fractal=generate(newarea)
            area = newarea
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

        if ev.type==KEYDOWN:
            if ev.key==K_r:
                area=areas[0]
                generate(area)
            elif ev.key==K_s:
                try:
                    name="mandelbrot("+str(newarea[0])+"_"+str(newarea[1])+"_"+str(newarea[2])+").bmp"
                    pygame.image.save(fractal,name)
                    print("image saved to {}".format(name))
                except:
                    print("fail to save")
            elif ev.key==K_BACKSPACE:
                del areas[-1]
                area=areas[-1]
                generate(area)


draw_mandelbrot()