####
#### Author: Derek Tominaga
#### Description: a program that draws a
#### picture backround, that moves with the
#### curser to emulate the idea of
#### Motion Parallax
####
from graphics import graphics
import random
def generate_color(gui):
    '''
    This function will uses 3 variables to generate
    a random color using get_color_string() imported
    from graphics.
    color_string: is varaiable that gets assigned
    the sting generated from get_color_string() and
    returns color_string
    gui: is a graphics object, used to draw
    '''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_string =  gui.get_color_string(red, green, blue)
    return color_string
def generate_sun(gui):
    '''
    This function takes in an argument and generates the first "layer"
    of the canvas. It generates the sun, and clouds in the canvas
    gui: is a graphis object, used to draw
    '''
    x_cord = (gui.mouse_x // 95)
    y_cord = (gui.mouse_y // 80)
    gui.ellipse(x_cord + 400, y_cord + 75, 55, 55, "yellow")
    gui.ellipse(x_cord + 250, y_cord + 50, 55, 25, "white")
    gui.ellipse(x_cord + 270, y_cord + 60, 55, 35, "white")
    gui.ellipse(x_cord + 230, y_cord + 60, 55, 25, "white")
    gui.ellipse(x_cord + 150, y_cord + 75, 55, 35, "white")
    gui.ellipse(x_cord + 110, y_cord + 65, 55, 35, "white")
    gui.ellipse(x_cord + 120, y_cord + 80, 55, 25, "white")
def generate_mountian_middle(gui, mount_color_1):
    '''
    This function takes two parameters to generate the second
    "layer" of the canvas. It generates the middle mountian
    with randomized color
    gui: is a graphics object, used to draw
    mount_color_1: randomly generated color string
    '''
    x_cord = (gui.mouse_x // 65)
    y_cord = (gui.mouse_y // 40)
    mountian_color = mount_color_1
    gui.triangle(x_cord + 250, y_cord + 100, x_cord + 75, y_cord + 450, x_cord + 425, y_cord + 450, mount_color_1)
def generate_mountian_sides(gui, mount_color_2, mount_color_3):
    '''
    This function takes three parameters to generate the third
    "layer" of the canvas. It generates the side mountians with
    randomized color.
    gui: is a graphics object, used to draw
    mount_color_2: randomly generated color string
    mount_color_3: randomly generated color string
    '''
    x_cord = (gui.mouse_x // 35)
    y_cord = (gui.mouse_y // 15)
    left_mountian = mount_color_2
    right_mountian = mount_color_3
    gui.triangle(x_cord + 75, y_cord + 150, x_cord - 175, y_cord + 500, x_cord + 325, y_cord + 500, mount_color_2)
    gui.triangle(x_cord + 425, y_cord + 150, x_cord + 175, y_cord + 500, x_cord + 675, y_cord + 500, mount_color_3)
def grass_trees_forground(gui):
    '''
    This function takes one parameter to generate the fourth
    "layer" of the canvas. It generates the grass, and medow
    with a pond and a tree.
    gui: is a graphics object, used to draw
    '''
    x_cord = (gui.mouse_x // 10)
    y_cord = (gui.mouse_y // 5)
    gui.rectangle(x_cord - 100, y_cord + 400, 600, 100, "Green2" )
    grass_count = -100
    while grass_count < 750:
        gui.line(grass_count, y_cord + 375, grass_count, y_cord + 450, "Green2", 2)
        grass_count += 7
    gui.rectangle(x_cord + 350, y_cord + 400, 20, 45, "brown4")
    gui.ellipse(x_cord + 360, y_cord + 375, 50, 75, "dark green")
    gui.ellipse(x_cord + 150, y_cord + 435, 200, 50, "blue")
    gui.ellipse(x_cord + 50, y_cord + 435, 40, 20, "grey")
    gui.ellipse(x_cord + 65, y_cord + 420, 30, 20, "grey")
    gui.ellipse(x_cord + 75, y_cord + 440, 45, 35, "grey")
def five_birds(x_cord, y_cord,gui):
    '''
    This function takes in three parametes to generate
    birds in the sky of the canvas.
    x_cord: is the "starting" x cooridnate
    y_cord: is the "starting" y cooridnate
    gui: is a graphics object, used to draw
    '''
    bird_count = 0
    while bird_count < 5:
        gui.line(x_cord + 10, y_cord + 100, x_cord + 25, y_cord + 110, "black", 2)
        gui.line(x_cord + 25, y_cord + 110, x_cord + 40, y_cord + 100, "black", 2)
        x_cord += 55
        y_cord += 15
        bird_count += 1
def main():
    '''
    This function generates the canvas and uses fucntions to
    generate layers 1 - 4 and the birds in the sky.
    it cycles through to show "movement" infinitaly
    '''
    gui = graphics (500, 500, "Motion Parallax")
    x_cord = -100
    y_cord = 0
    x_cord_offset = -600
    mount_color_1 = generate_color(gui)
    mount_color_2 = generate_color(gui)
    mount_color_3 = generate_color(gui)
    while True:
        gui.clear()
        gui.rectangle(0, 0, 500, 500, "SteelBlue2")
        generate_sun(gui)
        generate_mountian_middle(gui, mount_color_1)
        generate_mountian_sides(gui, mount_color_2, mount_color_3)
        grass_trees_forground(gui)
        five_birds(x_cord, y_cord, gui)
        five_birds(x_cord_offset, y_cord, gui)
        x_cord += 2
        x_cord_offset += 2
        if x_cord > 800:
            x_cord = -250
        if x_cord_offset > 800:
            x_cord_offset = -250
        gui.update_frame(60)
main()