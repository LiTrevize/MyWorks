import pygame
def main():
    pygame.init()
    screen=pygame.display.set_mode((360,360),0)
    screen.fill((255,255,255))
    global size
    while True:
        ev=pygame.event.get()
        if not ev:
            print(ev)

a='ab'
a+='23'
print(a)