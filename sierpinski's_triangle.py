import pygame as pg
import random
import math

pg.init()

def set_vars():
    global display, display_height, display_width
    global clock
    global white, black, red, green, blue
    global a, b, c, p
    global dot_size
    global typeface
    global dist_from_edge
    display_width = 1280
    display_height = 910
    display = pg.display.set_mode((display_width, display_height))
    pg.display.set_caption('Order from Chaos')
    clock = pg.time.Clock()

    white = (255,255,255)
    black = (0,0,0)

    red = (180,0,0)
    green = (0,180,0)
    blue = (0,0,180)

    a = (0,0)
    b = (0,0)
    c = (0,0)
    p = (0,0)

    dot_size = 5

    typeface = 'OpenSans-Semibold.ttf'

    dist_from_edge = 2

set_vars()

def quit_program():
    pg.quit()
    exit()

def clear_screen():
    display.fill(white)

def randomise_points():
    global a, b, c, p
    a = (random.randint(dist_from_edge, display_width - dist_from_edge),
         random.randint(dist_from_edge, display_height - dist_from_edge))
    b = (random.randint(dist_from_edge, display_width - dist_from_edge),
         random.randint(dist_from_edge, display_height - dist_from_edge))
    c = (random.randint(dist_from_edge, display_width - dist_from_edge),
         random.randint(dist_from_edge, display_height - dist_from_edge))
    p = (random.randint(dist_from_edge, display_width - dist_from_edge),
         random.randint(dist_from_edge, display_height - dist_from_edge))

def reset():
    clear_screen()
    randomise_points()

def text_objects(text, font, colour):
    surface = font.render(text, True, colour)
    return surface, surface.get_rect()

def text_display(text, size, colour, pos):
    font = pg.font.Font(typeface, size)
    text_surface, text_rect = text_objects(text, font, colour)
    text_rect.center = pos
    display.blit(text_surface, text_rect)

try:
    reset()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_program()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    reset()

        text_display('Press "R" to reset', 20, black, (120, 40))

        pg.draw.circle(display, red, a, dot_size)
        pg.draw.circle(display, green, b, dot_size)
        pg.draw.circle(display, blue, c, dot_size)
        pg.draw.circle(display, black, p, dot_size)

        dice_roll = random.randint(1,6)

        if dice_roll == 1 or dice_roll == 2:
            result = 'a'
        elif dice_roll == 3 or dice_roll == 4:
            result = 'b'
        elif dice_roll == 5 or dice_roll == 6:
            result = 'c'

        if result == 'a':
            p = (math.floor(p[0] + ((a[0] - p[0]) / 2)), math.floor(p[1] + ((a[1] - p[1]) / 2)))
        elif result == 'b':
            p = (math.floor(p[0] + ((b[0] - p[0]) / 2)), math.floor(p[1] + ((b[1] - p[1]) / 2)))
        else:
            p = (math.floor(p[0] + ((c[0] - p[0]) / 2)), math.floor(p[1] + ((c[1] - p[1]) / 2)))

        result = ''

        pg.display.update()
        clock.tick(50)

except KeyboardInterrupt:
    quit_program()