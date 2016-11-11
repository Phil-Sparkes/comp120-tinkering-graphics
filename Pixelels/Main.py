import pygame
import sys
import math
from pygame.locals import *

# Images
Picture = pygame.image.load("Parrots.jpeg")
Picture2 = pygame.image.load("PhoenixCol.png")
Picture3 = pygame.image.load("GodotCol.png")
Picture4 = pygame.image.load("Animu.png")
Picture5 = pygame.image.load("MonaLisa.jpg")
Picture6 = pygame.image.load("Stars.jpg")

Running = True
pygame.init()

# Used in the collage
PictureScale1 = 80
PictureScale2 = PictureScale1
PictureScale3 = 0
ColourManip = 1

# Change these depending on the picture
Width = 1280
Height = 720

screen = pygame.display.set_mode((Width, Height))

# Scales the pictures to fit the screen
Picture = pygame.transform.scale(Picture, (Width, Height))
Picture4 = pygame.transform.scale(Picture4, (Width, Height))
Picture2 = pygame.transform.scale(Picture2, (PictureScale1, PictureScale1))
Picture3 = pygame.transform.scale(Picture3, (PictureScale1, PictureScale1))

screen.blit(Picture, (0, 0))

pygame.display.update()

PXArray = pygame.PixelArray(screen)

# Defining some colours for later use
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 80, 50)


"""Functions - Look at the end to see what key relates to which function"""


def invert():
    """ Inverts the colours of the current picture"""
    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Inverts the value
            red = 255 - red
            green = 255 - green
            blue = 255 - blue

            # Updates the Pixel Array
            PXArray[X, Y] = (red, green, blue)


def grey_scale():
    """ greyScales the current picture"""
    for Y in xrange(Height):
        for X in xrange(Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            grey = (red + green + blue)/3

            # Updates the Pixel Array
            PXArray[X, Y] = (grey, grey, grey)


def less_red():
    """ Halfs the value of all the red pixels in current picture"""
    for Y in xrange(Height):
        for X in xrange(Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X, Y] = (red/2, green, blue)


def grey_gradient():
    """ Creates a grey gradient effect"""
    colour_change = 0
    gradient = 1.25

    for X in xrange(Width):
        for Y in xrange(Height):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Gives new RGB values of colour_change and Half of colour_change if the current RGB value is below a cetain threshold
            if red > 25 and green > 25 and blue > 25:
                red = colour_change/2
                green = colour_change/2
                blue = colour_change/2
            else:
                red = colour_change
                green = colour_change
                blue = colour_change

            # Updates the Pixel Array
            PXArray[X, Y] = (red, green, blue)

        # Increments the colour_change by the current gradient
        colour_change += gradient

        # When the colour_changes reaches the total range of colours it flips the gradient to reverse the process
        if colour_change == 255 or colour_change == 0:
            gradient *= -1


def wood_texture():
    """Creates an interesting texture that resembles wood or rain in some images"""
    colour_change = 0

    for X in xrange(Width):
        for Y in xrange(Height):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            if red > 25 and green > 25 and blue > 25:
                colour_change += 1
                red += colour_change
                green += colour_change
                blue += colour_change
            else:
                colour_change -= 1
                red -= colour_change
                green -= colour_change
                blue -= colour_change

            # When colour_change hits a certain value this will reset it
            if colour_change > 150:
                colour_change = 0
            elif colour_change < 0:
                colour_change = 150

            # Makes sure that the RGB Values dont exceed the allowed range
            if red > 255:
                red = 255
            elif red < 0:
                red = 0

            if green > 255:
                green = 255
            elif green < 0:
                green = 0

            if blue > 255:
                blue = 255
            elif blue < 0:
                blue = 0

            # Updates the Pixel Array
            PXArray[X, Y] = (red, green, blue)


def ghost_effect():
    """Creates a white fade effect that looks ghostly on certain pictures"""
    colour_change = 0

    for X in xrange(Width):
        for Y in xrange(Height):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            if red > 25 and green > 25 and blue > 25:
                colour_change += 1
            else:
                colour_change -= 1

            red += colour_change
            green += colour_change
            blue += colour_change

            # When colour_change hits a certain value this will stop it exceeding the value
            if colour_change > 150:
                colour_change = 150
            if colour_change < -100:
                colour_change = -100

            # Makes sure that the RGB Values dont exceed the allowed range
            if red > 255:
                red = 255
            elif red < 0:
                red = 0
            if green > 255:
                green = 255
            elif green < 0:
                green = 0
            if blue > 255:
                blue = 255
            elif blue < 0:
                blue = 0

            # Updates the Pixel Array
            PXArray[X, Y] = (red, green, blue)


def colour_distance_check(colour1, colour2, tolerance):
    """Checks the distance between two colours, if the colours are within the tolerance it will return true"""

    (red1, green1, blue1) = colour1
    (red2, green2, blue2) = colour2

    # Colour distance equation
    colour_distance = math.sqrt(((red1 - red2) ** 2) + ((green1 - green2) ** 2) + ((blue1 - blue2) ** 2))

    if colour_distance < tolerance:
        return True
    else:
        return False


def close_enough(colour):
    """If a pixel is close to input Colour (set to brown currently) it will half the red value of that pixel"""
    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            current_colour = (red, green, blue)

            close_brown = colour_distance_check(current_colour, colour, 150)

            if close_brown:
                PXArray[X, Y] = ((red / 2), green, blue)
            else:
                PXArray[X, Y] = (red, green, blue)


def posterize(colour_variance):
    """Posterizes the picture, level of Posterizsation depends on the colour_variance"""
    colour_variance = (255 / colour_variance)

    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Runs the Posterize function for each different colour
            red = colour_posterize(red, colour_variance)
            green = colour_posterize(green, colour_variance)
            blue = colour_posterize(blue, colour_variance)

            # Updates the Pixel Array
            PXArray[X, Y] = (red, green, blue)


def colour_posterize(colour, colour_variance):
    """Posterizes each colour, Used in the Posterize function"""
    colour_counter = 255

    while True:
        if colour_counter < 0:
            colour_counter = 0
        if colour >= colour_counter:
            return colour_counter
        else:
            colour_counter = colour_counter - colour_variance


def sepia_tint():
    """Creates a sepia tone effect"""
    grey_scale()

    for X in xrange(Width):
        for Y in xrange(Height):
            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            if red < 63:
                red *= 1.1
                blue *= 0.9
            if 62 < red < 192:
                red *= 1.15
                blue *= 0.85
            if red > 191:
                red *= 1.08
                if red > 255:
                    red = 255
                blue *= 0.93

            PXArray[X, Y] = (red, green, blue)


def draw_edges():
    """Checks the difference between two pixels, if the difference is high the result will be a black pixel
    if there is no difference it will result in a white pixel. anywhere inbetween will be different shades of grey
    """
    for X in xrange(Width - 1):
        for Y in xrange(Height - 1):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            pixel_sum = (red + green + blue)

            # Gets the RGB Values of the next pixel
            red2 = screen.get_at((X + 1, Y)).r
            green2 = screen.get_at((X + 1, Y)).g
            blue2 = screen.get_at((X + 1, Y)).b

            next_pixel_sum = (red2 + green2 + blue2)

            # Calculates the difference between the two pixel sums
            difference = next_pixel_sum - pixel_sum

            # Converts negative numbers to positive
            if difference < 0:
                difference *= -1

            # Makes sure the difference doesnt exceed the threshold
            if difference > 255:
                difference = 255

            # Inverts the difference value so it draws black lines on a white background instead of white on black
            difference = 255 - difference

            PXArray[X, Y] = (difference, difference, difference)


def draw_edges_colour():
    """Variation on DrawEdges draws the edges in colour"""
    for X in xrange(Width - 1):
        for Y in xrange(Height - 1):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            pixel_sum = (red + green + blue)

            # Gets the RGB Values of the next pixel
            red2 = screen.get_at((X + 1, Y)).r
            green2 = screen.get_at((X + 1, Y)).g
            blue2 = screen.get_at((X + 1, Y)).b

            next_pixel_sum = (red2 + green2 + blue2)

            # Calculates the difference between the two pixel sums
            difference = next_pixel_sum - pixel_sum

            # Converts negative numbers to positive
            if difference < 0:
                difference *= -1

            # Makes sure the difference doesnt exceed the threshold
            if difference > 255:
                difference = 255

            # Inverts the difference value so it draws black lines on a white background instead of white on black
            difference = 255 - difference

            # Adds the difference onto the current RGB Values
            red += difference
            green += difference
            blue += difference

            # Makes sure the RGB values don't exceed the limit
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255

            PXArray[X, Y] = (red, green, blue)


def cel_shade():
    """Creates a cel shading effect, finds lines and outlines them"""

    for X in xrange(Width - 1):
        for Y in xrange(Height - 1):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            pixel_sum = (red + green + blue)

            # Gets the RGB Values of the next pixel
            red2 = screen.get_at((X + 1, Y)).r
            green2 = screen.get_at((X + 1, Y)).g
            blue2 = screen.get_at((X + 1, Y)).b

            next_pixel_sum = (red2 + green2 + blue2)

            # Calculates the difference between the two pixel sums
            difference = next_pixel_sum - pixel_sum

            # Converts negative numbers to positive
            if difference < 0:
                difference *= -1

            # Makes sure the difference doesnt exceed the threshold
            if difference > 255:
                difference = 255

            # Subtracts the difference from all the RGB Values
            red -= difference
            green -= difference
            blue -= difference

            # Makes sure that no RGB values are less than 0
            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0

            PXArray[X, Y] = (red, green, blue)


def rainbow_matrix_style(tolerance):
    """Creates an interesting result, takes the argument tolerance"""
    counter = 0

    for X in xrange(Width):
        for Y in xrange(Height):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            pixel_sum = (red + blue + green)/3

            # Checks the sum of the pixels against the tolerance, if the sum is higher than the tolerance then the counter is incremented by 1
            if pixel_sum > tolerance:
                counter += 1

            # Resets the counter when it reaches 3
            if counter == 3:
                counter = 0

            # When the counter is 0 it will only draw the red pixel
            # When the counter is 1 it will only draw the green pixel
            # When the counter is 2 it will only draw the blue pixel
            if counter == 0:
                PXArray[X, Y] = (red, 0, 0)
            elif counter == 1:
                PXArray[X, Y] = (0, green, 0)
            elif counter == 2:
                PXArray[X, Y] = (0, 0, blue)


def rainbow_matrix_style_fill(tolerance):
    """Variation on rainbow_matrix_style in which it fills a lot of the blanks"""
    rainbow_matrix_style(tolerance)
    red = 0
    green = 0
    blue = 0
    for Y in xrange(Height):
        for X in xrange(Width):

            counter = 0
            colour_not_found = True

            while colour_not_found:
                if X - counter >= 0:
                    red = screen.get_at((X - counter, Y)).r
                    green = screen.get_at((X - counter, Y)).g
                    blue = screen.get_at((X - counter, Y)).b

                    colour = (red + green + blue)/3

                    # This number can change a lot, wouldnt go higher than 50 though
                    if colour < 25:
                        counter += 1
                    else:
                        colour_not_found = False
                else:
                    colour_not_found = False
            while counter > 0:

                if X - counter >= 0:
                    PXArray[X - counter, Y] = (red, green, blue)
                counter -= 1


def rainbow_matrix_style_z(tolerance):
    """Another variation of rainbow_matrix_style, drags the pixels to the left"""
    rainbow_matrix_style(tolerance)
    red = 0
    green = 0
    blue = 0
    for Y in xrange(Height):
        for X in xrange(Width):

            counter = 0
            colour_not_found = True

            while colour_not_found:
                if X - counter >= 0:
                    red = screen.get_at((X - counter, Y)).r
                    green = screen.get_at((X - counter, Y)).g
                    blue = screen.get_at((X - counter, Y)).b

                    colour = (red + green + blue)/3
                    # This number can change a lot, wouldnt go higher than 50 though
                    if colour > 30:
                        # Changing this number does fun stuff (0-5 reconmended)
                        counter += 4

                while counter > 0:

                    if X - counter >= 0:
                        PXArray[X - counter, Y] = (red, green, blue)
                    counter -= 1
                else:
                    colour_not_found = False


def mirrors():
    """Mirrors the image along the vertical axis"""
    mirror_point_width = Width/2

    for Y in xrange(Height):
        for X in xrange(mirror_point_width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[Width - X - 1, Y] = (red, green, blue)


def horizontal_mirror():
    """"Mirrors the image along the horizontal axis"""
    mirror_point_height = Height / 2

    for Y in xrange(mirror_point_height):
        for X in xrange(Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X, Height - Y - 1] = (red, green, blue)


def pixelated_water_reflection():
    """"Mirrors the image along the horizontal axis with a water effect"""
    mirror_point_height = Height / 2
    wave_amount = 0
    wave_toggle = False

    for Y in xrange(mirror_point_height):
        for X in xrange(Width):
            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X, Height - Y - 1] = (red, green, blue)

    for Y in xrange(mirror_point_height):
        for X in xrange(Width - 20):
            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X + wave_amount, Height - Y - 1] = (red, green, blue)
            if wave_toggle:
                wave_amount -= 1
            else:
                wave_amount += 1
            if wave_amount == 11:
                wave_toggle = True
            elif wave_amount == -11:
                wave_toggle = False


def phoenix_col(picture_scale2):
    """Makes a collage"""
    target_x = 0
    for X in xrange(PictureScale1 * 2):
        target_y = 0
        for Y in xrange(PictureScale1):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            PXArray[target_x + (picture_scale2 * 2), target_y + PictureScale3] = (red - red / ColourManip, green, blue / ColourManip)
            target_y += 1
        target_x += 1
    picture_scale2 += PictureScale1
    return picture_scale2


def change_picture(picture_change):
    """Changes the current picture displayed"""
    screen.fill(BLACK)
    screen.blit(picture_change, (0, 0))
    pygame.display.update()


# Press the key and it will run the corresponding function
while Running:
    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            Running = False
        if event.type == KEYDOWN and event.key == K_i:
            invert()
        if event.type == KEYDOWN and event.key == K_g:
            grey_scale()
        if event.type == KEYDOWN and event.key == K_r:
            less_red()
        if event.type == KEYDOWN and event.key == K_l:
            grey_gradient()
        if event.type == KEYDOWN and event.key == K_w:
            wood_texture()
        if event.type == KEYDOWN and event.key == K_s:
            ghost_effect()
        if event.type == KEYDOWN and event.key == K_c:
            close_enough(BROWN)                         # Can choose any colour using RGB value
        if event.type == KEYDOWN and event.key == K_p:
            posterize(5)                                # Try changing the value to alter the amount of posterization
        if event.type == KEYDOWN and event.key == K_q:
            sepia_tint()
        if event.type == KEYDOWN and event.key == K_e:
            draw_edges()
        if event.type == KEYDOWN and event.key == K_k:
            draw_edges_colour()
        if event.type == KEYDOWN and event.key == K_x:
            cel_shade()
        if event.type == KEYDOWN and event.key == K_m:
            rainbow_matrix_style(80)                    # Tolerance, value between 0 and 255. 80 is good number for parrot
        if event.type == KEYDOWN and event.key == K_f:
            rainbow_matrix_style_fill(80)               # Tolerance, value between 0 and 255. 80 is good number for parrot
        if event.type == KEYDOWN and event.key == K_z:
            rainbow_matrix_style_z(80)                  # Tolerance, value between 0 and 255. 80 is good number for parrot
        if event.type == KEYDOWN and event.key == K_n:
            mirrors()
        if event.type == KEYDOWN and event.key == K_b:
            horizontal_mirror()
        if event.type == KEYDOWN and event.key == K_h:
            pixelated_water_reflection()
        if event.type == KEYDOWN and event.key == K_o:
            PictureScale2 = 80
            PictureScale3 = 0
            ColourManip = 1
            while PictureScale3 != Height:
                PictureScale2 = phoenix_col(PictureScale2)
                pygame.display.update()
                if PictureScale2 == Width / 2:
                    PictureScale2 = 0
                    PictureScale3 += PictureScale1
                    ColourManip += 0.2
        if event.type == KEYDOWN and event.key == K_1:
            del PXArray
            change_picture(Picture)
            PXArray = pygame.PixelArray(screen)
        if event.type == KEYDOWN and event.key == K_2:
            del PXArray
            screen.fill(BLACK)
            screen.blit(Picture2, (0, 0))
            screen.blit(Picture3, (PictureScale1, 0))
            pygame.display.update()
            PXArray = pygame.PixelArray(screen)
        if event.type == KEYDOWN and event.key == K_3:
            del PXArray
            change_picture(Picture4)
            PXArray = pygame.PixelArray(screen)
        if event.type == KEYDOWN and event.key == K_4:
            del PXArray
            change_picture(Picture5)
            PXArray = pygame.PixelArray(screen)
        if event.type == KEYDOWN and event.key == K_5:
            del PXArray
            change_picture(Picture6)
            PXArray = pygame.PixelArray(screen)
        pygame.display.update()

pygame.quit()
sys.exit()
