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
PictureScale = 80
PictureScale2 = PictureScale
PictureScale3 = 0
ColourManip = 1

# Change these depending on the picture
Width = 1280
Height = 720

screen = pygame.display.set_mode((Width, Height))

# Scales the pictures to fit the screen
Picture = pygame.transform.scale(Picture, (Width,Height))
Picture4 = pygame.transform.scale(Picture4, (Width,Height))
Picture2 = pygame.transform.scale(Picture2, (PictureScale, PictureScale))
Picture3 = pygame.transform.scale(Picture3, (PictureScale, PictureScale))

screen.blit(Picture, (0, 0))

pygame.display.update()

PXArray = pygame.PixelArray(screen)

# Defining some colours for later use
White = (255, 255, 255)
Black = (0,0,0)
Brown = (150, 80, 50)


"""Functions - Look at the end to see what key relates to which function"""

def invert():
    """ Inverts the colours of the current picture"""
    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Inverts the value
            Red = 255 - Red
            Green = 255 - Green
            Blue = 255 - Blue

            # Updates the Pixel Array
            PXArray[X, Y] = (Red, Green, Blue)



def grey_scale():
    """ GreyScales the current picture"""
    for Y in xrange(Height):
        for X in xrange(Width):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            Grey = (Red + Green + Blue)/3

            # Updates the Pixel Array
            PXArray[X, Y] = (Grey, Grey, Grey)



def less_red():
    """ Halfs the value of all the red pixels in current picture"""
    for Y in xrange(Height):
        for X in xrange(Width):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X, Y] = (Red/2, Green, Blue)



def grey_gradient():
    """ Creates a grey gradient effect"""
    ColourChange = 0
    Gradient = 1.25

    for X in xrange (Width):
        for Y in xrange (Height):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Gives new RGB values of ColourChange and Half of ColourChange if the current RGB value is below a cetain threshold
            if Red > 25 and Green > 25 and Blue > 25:
                Red =  ColourChange/2
                Green = ColourChange/2
                Blue =  ColourChange/2
            else:
                Red = ColourChange
                Green = ColourChange
                Blue = ColourChange

            # Updates the Pixel Array
            PXArray[X, Y] = (Red, Green, Blue)

        # Increments the ColourChange by the current gradient
        ColourChange += Gradient

        # When the ColourChanges reaches the total range of colours it flips the gradient to reverse the process
        if ColourChange == 255 or ColourChange == 0:
            Gradient *= -1



def wood_texture():
    """Creates an interesting texture that resembles wood or rain in some images"""
    ColourChange = 0

    for X in xrange (Width):
        for Y in xrange (Height):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b


            if Red > 25 and Green > 25 and Blue > 25:
                ColourChange += 1
                Red += ColourChange
                Green += ColourChange
                Blue += ColourChange
            else:
                ColourChange -= 1
                Red -= ColourChange
                Green -= ColourChange
                Blue -= ColourChange

            # When ColourChange hits a certain value this will reset it
            if ColourChange > 150:
                ColourChange = 0
            elif ColourChange < 0:
                ColourChange = 150

            # Makes sure that the RGB Values dont exceed the allowed range
            if Red > 255:
                Red = 255
            elif Red < 0:
                Red = 0

            if Green > 255:
                Green = 255
            elif Green < 0:
                Green = 0

            if Blue > 255:
                Blue = 255
            elif Blue < 0:
                Blue = 0

            # Updates the Pixel Array
            PXArray[X, Y] = (Red, Green, Blue)



def ghost_effect():
    """Creates a white fade effect that looks ghostly on certain pictures"""
    ColourChange = 0

    for X in xrange (Width):
        for Y in xrange (Height):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                ColourChange += 1
            else:
                ColourChange -= 1

            Red += ColourChange
            Green += ColourChange
            Blue += ColourChange

            # When ColourChange hits a certain value this will stop it exceeding the value
            if ColourChange > 150:
                ColourChange = 150
            if ColourChange < -100:
                ColourChange = -100

            # Makes sure that the RGB Values dont exceed the allowed range
            if Red > 255:
                Red = 255
            elif Red < 0:
                Red = 0
            if Green > 255:
                Green = 255
            elif Green < 0:
                Green = 0
            if Blue > 255:
                Blue = 255
            elif Blue < 0:
                Blue = 0

            # Updates the Pixel Array
            PXArray[X, Y] = (Red, Green, Blue)



def colour_distance_check(Colour1, Colour2, Tolerance):
   """Checks the distance between two colours, if the colours are within the tolerance it will return true"""

   (Red1, Green1, Blue1) = Colour1
   (Red2, Green2, Blue2) = Colour2

   # Colour distance equation
   ColourDistance = math.sqrt(((Red1 - Red2) ** 2) + ((Green1 - Green2) ** 2) + ((Blue1 - Blue2) ** 2))

   if ColourDistance < Tolerance:
       return True
   else:
       return False



def close_enough(Colour):
    """If a pixel is close to input Colour (set to brown currently) it will half the red value of that pixel"""
    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            CurrentColour = (Red, Green, Blue)

            CloseBrown = colour_distance_check(CurrentColour,Colour, 150)

            if CloseBrown:
                PXArray[X, Y] = ((Red / 2), Green, Blue)
            else:
                PXArray[X, Y] = (Red, Green, Blue)



def posterize(ColourVariance):
    """Posterizes the picture, level of Posterizsation depends on the ColourVariance"""
    ColourVariance = (255 / ColourVariance)

    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Runs the Posterize function for each different colour
            Red = colour_posterize(Red, ColourVariance)
            Green = colour_posterize(Green, ColourVariance)
            Blue = colour_posterize(Blue, ColourVariance)

            # Updates the Pixel Array
            PXArray[X, Y] = (Red, Green, Blue)



def colour_posterize(Colour,ColourVariance):
    """Posterizes each colour, Used in the Posterize function"""
    ColourCounter = 255

    while True:
        if ColourCounter < 0:
            ColourCounter = 0
        if Colour >= ColourCounter:
            return ColourCounter
        else:
            ColourCounter = ColourCounter - ColourVariance



def sepia_tint():
    """Creates a sepia tone effect"""
    grey_scale()

    for X in xrange (Width):
        for Y in xrange (Height):
            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            if Red <63:
                Red = Red * 1.1
                Blue = Blue * 0.9
            if Red > 62 and Red <192:
                Red = Red * 1.15
                Blue = Blue * 0.85
            if Red > 191:
                Red = Red * 1.08
                if Red > 255:
                    Red = 255
                Blue = Blue *0.93

            PXArray[X, Y] = (Red, Green, Blue)



def draw_edges():
    """Checks the difference between two pixels, if the difference is high the result will be a black pixel
    if there is no difference it will result in a white pixel. anywhere inbetween will be different shades of grey
    """
    for X in xrange (Width - 1):
        for Y in xrange (Height - 1):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            PixelSum = (Red + Green + Blue)

            # Gets the RGB Values of the next pixel
            Red2 = screen.get_at((X + 1, Y )).r
            Green2 = screen.get_at((X + 1, Y )).g
            Blue2 = screen.get_at((X + 1, Y)).b

            NextPixelSum = (Red2 + Green2 + Blue2)

            # Calculates the difference between the two pixel sums
            Difference = NextPixelSum - PixelSum

            # Converts negative numbers to positive
            if Difference < 0:
                Difference *=  -1

            # Makes sure the difference doesnt exceed the threshold
            if Difference > 255:
                Difference = 255

            # Inverts the difference value so it draws black lines on a white background instead of white on black
            Difference = 255 - Difference

            PXArray[X, Y] = (Difference, Difference, Difference)



def draw_edges_colour():
    """Variation on DrawEdges draws the edges in colour"""
    for X in xrange (Width - 1):
        for Y in xrange (Height - 1):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            PixelSum = (Red + Green + Blue)

            # Gets the RGB Values of the next pixel
            Red2 = screen.get_at((X + 1, Y )).r
            Green2 = screen.get_at((X + 1, Y )).g
            Blue2 = screen.get_at((X + 1, Y)).b

            NextPixelSum = (Red2 + Green2 + Blue2)

            # Calculates the difference between the two pixel sums
            Difference = NextPixelSum - PixelSum

            # Converts negative numbers to positive
            if Difference < 0:
                Difference *= -1

            # Makes sure the difference doesnt exceed the threshold
            if Difference > 255:
                Difference = 255

            # Inverts the difference value so it draws black lines on a white background instead of white on black
            Difference = 255 - Difference

            # Adds the difference onto the current RGB Values
            Red += Difference
            Green += Difference
            Blue += Difference

            # Makes sure the RGB values don't exceed the limit
            if Red > 255:
                Red = 255
            if Green > 255:
                Green = 255
            if Blue > 255:
                Blue = 255

            PXArray[X, Y] = (Red, Green, Blue)



def cel_shade():
    """Creates a cel shading effect, finds lines and outlines them"""

    for X in xrange(Width - 1):
        for Y in xrange(Height - 1):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            PixelSum = (Red + Green + Blue)

            # Gets the RGB Values of the next pixel
            Red2 = screen.get_at((X + 1, Y)).r
            Green2 = screen.get_at((X + 1, Y)).g
            Blue2 = screen.get_at((X + 1, Y)).b

            NextPixelSum = (Red2 + Green2 + Blue2)

            # Calculates the difference between the two pixel sums
            Difference = NextPixelSum - PixelSum

            # Converts negative numbers to positive
            if Difference < 0:
                Difference *= -1

            # Makes sure the difference doesnt exceed the threshold
            if Difference > 255:
                Difference = 255

            # Subtracts the difference from all the RGB Values
            Red -= Difference
            Green -= Difference
            Blue -= Difference

            # Makes sure that no RGB values are less than 0
            if Red < 0:
                Red = 0
            if Green < 0:
                Green = 0
            if Blue < 0:
                Blue = 0

            PXArray[X, Y] = (Red, Green, Blue)



def rainbow_matrix_style(Tolerance):
    """Creates an interesting result, takes the argument tolerance"""
    Counter = 0

    for X in xrange(Width):
        for Y in xrange(Height):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            PixelSum = (Red + Blue + Green)/3

            # Checks the sum of the pixels against the tolerance, if the sum is higher than the tolerance then the counter is incremented by 1
            if PixelSum > Tolerance:
                Counter += 1

            # Resets the counter when it reaches 3
            if Counter == 3:
                Counter = 0

            # When the Counter is 0 it will only draw the red pixel
            # When the Counter is 1 it will only draw the green pixel
            # When the Counter is 2 it will only draw the blue pixel
            if Counter == 0:
                PXArray[X, Y] = (Red, 0, 0)
            elif Counter == 1:
                PXArray[X, Y] = (0, Green, 0)
            elif Counter == 2:
                PXArray[X, Y] = (0, 0, Blue)



def rainbow_matrix_style_fill(Tolerance):
    """Variation on rainbow_matrix_style in which it fills a lot of the blanks"""
    rainbow_matrix_style(Tolerance)

    for Y in xrange(Height):
        for X in xrange(Width):

            Counter = 0
            ColourNotFound = True

            while ColourNotFound:
                if X - Counter >= 0:
                    Red = screen.get_at((X - Counter, Y)).r
                    Green = screen.get_at((X - Counter, Y)).g
                    Blue = screen.get_at((X - Counter, Y)).b

                    Colour = (Red + Green + Blue)/3
                    if Colour < 25: # This number can change a lot, wouldnt go higher than 50 though
                        Counter = Counter + 1
                    else:
                        ColourNotFound = False
                else:
                    ColourNotFound = False
            while Counter > 0:

                if X - Counter >= 0:
                    PXArray[X - Counter, Y] = (Red, Green, Blue)
                Counter = Counter - 1



def rainbow_matrix_style_z(Tolerance):
    """Another variation of rainbow_matrix_style, drags the pixels to the left"""
    rainbow_matrix_style(Tolerance)

    for Y in xrange(Height):
        for X in xrange(Width):

            Counter = 0
            ColourNotFound = True

            while ColourNotFound:
                if X - Counter >= 0:
                    Red = screen.get_at((X - Counter, Y)).r
                    Green = screen.get_at((X - Counter, Y)).g
                    Blue = screen.get_at((X - Counter, Y)).b

                    Colour = (Red + Green + Blue)/3
                    if Colour > 30:  # This number can change a lot, wouldnt go higher than 50 though
                        Counter = Counter + 4  # Changing this number does fun stuff (0-5 reconmended)

                while Counter > 0:

                    if X - Counter >= 0:
                        PXArray[X - Counter, Y] = (Red, Green, Blue)
                    Counter = Counter - 1
                else:
                    ColourNotFound = False



def Mirrors():
    """Mirrors the image along the vertical axis"""
    MirrorPointWidth = Width/2

    for Y in xrange(Height):
        for X in xrange(MirrorPointWidth):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[Width - X - 1, Y] = (Red, Green, Blue)


def HorizontalMirror():
    """"Mirrors the image along the horizontal axis"""
    MirrorPointHeight = Height / 2

    for Y in xrange(MirrorPointHeight):
        for X in xrange(Width):

            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X, Height - Y - 1] = (Red, Green, Blue)

def PixelatedWaterReflection():
    """"Mirrors the image along the horizontal axis"""
    MirrorPointHeight = Height / 2
    WaveAmount = 0
    WaveToggle = False

    for Y in xrange(MirrorPointHeight):
        for X in xrange(Width):
            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X, Height - Y - 1] = (Red, Green, Blue)

    for Y in xrange(MirrorPointHeight):
        for X in xrange(Width - 20):
            # Gets the RGB Values of the pixel
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b

            # Updates the Pixel Array
            PXArray[X  + WaveAmount, Height - Y - 1] = (Red, Green, Blue)
            if WaveToggle:
                WaveAmount -= 1
            else:
                WaveAmount += 1
            if WaveAmount == 11:
                WaveToggle = True
            elif WaveAmount == -11:
                WaveToggle = False

def phoenix_col(PictureScale2):
    """Makes a collage"""
    TargetX = 0
    for X in xrange(PictureScale * 2):
        TargetY = 0
        for Y in xrange(PictureScale):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            PXArray[TargetX + (PictureScale2 * 2), TargetY + PictureScale3] = (
            Red - Red / ColourManip, Green, Blue / ColourManip)
            TargetY = TargetY + 1
        TargetX = TargetX + 1
    PictureScale2 = PictureScale2 + PictureScale
    return PictureScale2

def change_picture(PicChange):
    """Changes the current picture displayed"""
    screen.fill(Black)
    screen.blit(PicChange, (0, 0))
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
            close_enough(Brown)                         # Can choose any colour using RGB value
        if event.type == KEYDOWN and event.key == K_p:
            posterize(2)                                # Try changing the value to alter the amount of posterization
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
            Mirrors()
        if event.type == KEYDOWN and event.key == K_b:
            HorizontalMirror()
        if event.type == KEYDOWN and event.key == K_h:
            PixelatedWaterReflection()
        if event.type == KEYDOWN and event.key == K_o:
            while PictureScale3 != Height:
                PictureScale2 = phoenix_col(PictureScale2)
                pygame.display.update()
                if PictureScale2 == Width / 2:
                    PictureScale2 = 0
                    PictureScale3 = PictureScale3 + PictureScale
                    ColourManip = ColourManip + 0.2
        if event.type == KEYDOWN and event.key == K_1:
            del PXArray
            change_picture(Picture)
            PXArray = pygame.PixelArray(screen)
        if event.type == KEYDOWN and event.key == K_2:
            del PXArray
            screen.fill(Black)
            screen.blit(Picture2, (0, 0))
            screen.blit(Picture3, (PictureScale, 0))
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

