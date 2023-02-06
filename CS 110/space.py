from graphics import graphics
import random

def draw_stars(gui):
    ''' Draw some white circles.
    gui: A graphics object. Draw with this.
    '''
    gui.ellipse( 10, 210, 7, 7, 'white')
    gui.ellipse(110, 350, 7, 7, 'white')
    gui.ellipse(210,  50, 7, 7, 'white')
    gui.ellipse(430, 250, 7, 7, 'white')
    gui.ellipse(305, 410, 7, 7, 'white')
    gui.ellipse(250, 220, 7, 7, 'white')
    gui.ellipse(470, 450, 7, 7, 'white')
    gui.ellipse(50, 450, 7, 7, 'white')
    gui.ellipse(450, 80, 7, 7, 'white')
    gui.ellipse(30, 70, 7, 7, 'white')

def draw_tie_fighter(gui):
    ''' Draw a tie fighter.
    gui: A graphics object. Draw with this.
    '''
    pass

def main():
    gui = graphics(500, 500, 'Example')
    color_string = ''
    i = 0
    while True:
        gui.clear()
        gui.rectangle(-10, -10, 520, 520, 'black')
        draw_stars(gui)
        draw_tie_fighter(gui)
        gui.update_frame(30)

main()
