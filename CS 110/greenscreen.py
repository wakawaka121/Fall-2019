from os import _exit as exit
###
### Author: Derek Tominaga
### Description: This program reads in two ppm files. compares the brightness of
### colors channel. If criteria met pixels are "exchanged" generate overlay of two
### images. Then writes to to a file to make a ppm file.
###

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def image_comparison_exchange_red(gs_pixels,fi_pixels,channel_difference):
    """
    This function takes 3 parameters. It compares pixels from the screen against
    the channel_difference. If green * CD and blue * CD are less than the channel
    brightness use pixel from B, else from A. Returns pixels, 3d list of new image
    gs_pixels = 3d list of screen pixels
    fi_pixels = 3d list of image pixels
    channel_difference = float values from user input
    """
    pixels =  []
    #nested loop to itterate through 3d list to determine
    #which pixels gets selected for new image
    for i in range(len(gs_pixels)):
        rgb_pixel = []
        for j in range(len(gs_pixels[i])):
            if ((channel_difference)*gs_pixels[i][j][1] < gs_pixels[i][j][0] and
            (channel_difference)*gs_pixels[i][j][2] < gs_pixels[i][j][0]):
                rgb_pixel.append(fi_pixels[i][j])
            else:
                rgb_pixel.append(gs_pixels[i][j])
        pixels.append(rgb_pixel)

    return pixels

def image_comparison_exchange_green(gs_pixels,fi_pixels,channel_difference):
    """
    This function takes 3 parameters. It compares pixels from the screen against
    the channel_difference. If red * CD and blue * CD are less than the channel
    brightness use pixel from B, else from A. Returns pixels, 3d list of new image
    gs_pixels = 3d list of screen pixels
    fi_pixels = 3d list of image pixels
    channel_difference = float values from user input
    """
    pixels =  []
    #nested loop to itterate through 3d list to determine
    #which pixels gets selected for new image
    for i in range(len(gs_pixels)):
        rgb_pixel = []
        for j in range(len(gs_pixels[i])):
            if ((channel_difference)*gs_pixels[i][j][0] < gs_pixels[i][j][1] and
            (channel_difference)*gs_pixels[i][j][2] < gs_pixels[i][j][1]):
                rgb_pixel.append(fi_pixels[i][j])
            else:
                rgb_pixel.append(gs_pixels[i][j])
        pixels.append(rgb_pixel)

    return pixels

def image_comparison_exchange_blue(gs_pixels,fi_pixels,channel_difference):
    """
    This function takes 3 parameters. It compares pixels from the screen against
    the channel_difference. If green * CD and red * CD are less than the channel
    brightness use pixel from B, else from A. Returns pixels, 3d list of new image
    gs_pixels = 3d list of screen pixels
    fi_pixels = 3d list of image pixels
    channel_difference = float values from user input
    """
    pixels =  []
    #nested loop to itterate through 3d list to determine
    #which pixels gets selected for new image
    for i in range(len(gs_pixels)):
        rgb_pixel = []
        for j in range(len(gs_pixels[i])):
            if ((channel_difference)*gs_pixels[i][j][0] < gs_pixels[i][j][2] and
            (channel_difference)*gs_pixels[i][j][1] < gs_pixels[i][j][2]):
                rgb_pixel.append(fi_pixels[i][j])
            else:
                rgb_pixel.append(gs_pixels[i][j])
        pixels.append(rgb_pixel)

    return pixels

def write_to_file(result_pixels, out_file, gs_dimensions):
    """This function takes 3 parameters to write to a file
    result_pixels = 3d list of pixels in a ppm image
    out_file = string, name of the file to write to
    gs_dimensions = srting, containing width and height dimensions"""
    width_height = gs_dimensions.split()
    width = int(width_height[0])
    height = int(width_height[1])
    dimensions = str(width) + " " + str(height)
    write_string = ""
    new_line_count = 0
    pixel_to_file = open(out_file, "w")
    pixel_to_file.write("P3\n")
    pixel_to_file.write(dimensions + "\n")
    pixel_to_file.write("255\n")
    #nested loops to itterate through 3d list
    for i in range(len(result_pixels)):
        for j in range((len(result_pixels[i]))):
            for k in range(len(result_pixels[i][j])):
                    write_string += (str(result_pixels[i][j][k]) + " ")
                    new_line_count += 1
                    # 3 values per pixel, total values per line = width * 3
                    if new_line_count ==  width*3:
                        pixel_to_file.write(write_string + "\n")
                        write_string = ""
                        new_line_count = 0
    pixel_to_file.close()

def main():
    channel = input('Enter color channel\n')
    if channel != "r" and channel != "g" and channel != "b":
        print("Channel must be r, g, or b. Will exit.")
        exit(0)
    channel_difference = float(input('Enter color channel difference\n'))
    if channel_difference < 1.0 or channel_difference > 10.0:
        print("Invalid channel difference. Will exit.")
        exit(0)
    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')
    gs_dimensions = get_image_dimensions_string(gs_file)
    fi_dimensions = get_image_dimensions_string(fi_file)
    if gs_dimensions != fi_dimensions:
        print("Images not the same size. Will exit.")
        exit()
    out_file = input('Enter output file name\n')
    gs_pixels = load_image_pixels(gs_file)
    fi_pixels = load_image_pixels(fi_file)
    #decisions, based on channel input
    if channel == "r":
        result_pixels = image_comparison_exchange_red(gs_pixels, fi_pixels, channel_difference)
    if channel == "g":
        result_pixels = image_comparison_exchange_green(gs_pixels, fi_pixels, channel_difference)
    if channel == "b":
        result_pixels = image_comparison_exchange_blue(gs_pixels, fi_pixels, channel_difference)
    write_to_file(result_pixels, out_file, gs_dimensions)
    print("Output file written. Exiting.")
    exit(0)
main()