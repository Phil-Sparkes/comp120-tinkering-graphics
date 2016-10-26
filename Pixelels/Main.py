import pygame, sys, math
from pygame.locals import *

#key I, G, R, L, W, S, C, P, Q, E, K, Z, F, X
#Pretty much most the keyboard now
#Look at the end to see what key relates to which function

Picture = pygame.image.load("PhoenixCol.png") #Just change the image name to use different images
Picture2 = pygame.image.load("GodotCol.png")
Running = True
pygame.init()

PictureScale = 80
PictureScale2 = PictureScale
PictureScale3 = 0
ColourManip = 1
Width = 1280   #Change these depending on the picture
Height = 720

Screen = pygame.display.set_mode((Width, Height))
#Picture =pygame.transform.scale(Picture, (Width,Height))   #Scales the picture to fit the screen
Picture =pygame.transform.scale(Picture, (PictureScale,PictureScale))
Picture2 =pygame.transform.scale(Picture2, (PictureScale,PictureScale))
Screen.blit(Picture, (0, 0))
Screen.blit(Picture2, (PictureScale, 0))
pygame.display.update()

PXArray = pygame.PixelArray(Screen)
#PXArray = pygame.PixelArray(Picture)

White = (255, 255, 255)
Black = (0,0,0)
Brown = (150, 80, 50)    #Defined some colours for later use

#Inverts the colours
def Invert():

    for Y in range(0, Height):
        for X in range(0, Width):

            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            Red = 255 - Red
            Green = 255 - Green
            Blue = 255 - Blue

            PXArray[X, Y] = (Red, Green, Blue)

#Greyscale
def GreyScale():

    for Y in xrange(Height):
        for X in xrange(Width):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            grey = (Red + Green + Blue)/3

            PXArray[X, Y] = (grey, grey, grey)

#halves all the red values
def LessRed():

    for Y in xrange(Height):
        for X in xrange(Width):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            PXArray[X, Y] = (Red/2, Green, Blue)

#does weird stuff, dont trust this one
def ColourTest():
    ColourChange = 0
    Gradient = 1.25
    GradientChange = Gradient
    #Gradient = 1.25
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                Red =  ColourChange/2
                Green = ColourChange/2
                Blue =  ColourChange/2
            else:
                Red = ColourChange
                Green = ColourChange
                Blue = ColourChange
            PXArray[X, Y] = (Red, Green, Blue)
        ColourChange = ColourChange + Gradient
        if ColourChange == 255:
            Gradient = -GradientChange
        elif ColourChange == 0:
            Gradient = GradientChange

#Somehow it makes a wood texture or otherstuff but still looks good, dont ask how
def WoodTex():
    ColourChange = 0
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                ColourChange = ColourChange + 1
                Red = Red + ColourChange
                Green = Green + ColourChange
                Blue = Blue + ColourChange
            else:
                ColourChange = ColourChange - 1
                Red = Red - ColourChange
                Green = Green - ColourChange
                Blue = Blue - ColourChange
            if ColourChange > 150:
                ColourChange = 0
            if ColourChange < -0:
                ColourChange = 150

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
            PXArray[X, Y] = (Red, Green, Blue)

#2spooky5u white fade ghostly effect
def Spooky():
    ColourChange = 0
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                ColourChange = ColourChange + 1
            else:
                ColourChange = ColourChange - 1
            Red = Red + ColourChange
            Green = Green + ColourChange
            Blue = Blue + ColourChange
            if ColourChange > 150:
                ColourChange = 150
            if ColourChange < 0:
                ColourChange = 0

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
            PXArray[X, Y] = (Red, Green, Blue)

#Checks the distance between two colours, if the colours are within the tolerance it will return true
def ColourDistanceCheck(Colour1, Colour2, Tolerance):

   (Red1, Green1, Blue1) = Colour1
   (Red2, Green2, Blue2) = Colour2

   ColourDistance = math.sqrt(((Red1 - Red2) ** 2) + ((Green1 - Green2) ** 2) + ((Blue1 - Blue2) ** 2))
   if ColourDistance < Tolerance:
       return True
   else:
       return False

#if A pixel is close to input Colour (set to brown currently) it will half the red value of that pixel
def CloseEnough(Colour):
    for Y in range(0, Height):
        for X in range(0, Width):

            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            CurrentColour = (Red, Green, Blue)
            CloseBrown = False

            CloseBrown = ColourDistanceCheck(CurrentColour,Colour, 150)

            if CloseBrown:
                PXArray[X, Y] = ((Red / 2), Green, Blue)
            else:
                PXArray[X, Y] = (Red, Green, Blue)

#Posterizes the picture, level of Posterizsation depends on the ColourVariance
def Posterize(ColourVariance):
    ColourVariance = (255 / ColourVariance)

    for Y in range(0, Height):
        for X in range(0, Width):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            Red = ColourPolz(Red,ColourVariance)
            Green = ColourPolz(Green, ColourVariance)
            Blue = ColourPolz(Blue, ColourVariance)

            PXArray[X, Y] = (Red, Green, Blue)

#Posterizes each colour, Used in the Posterize function
def ColourPolz(Colour,ColourVariance):
    ColourCounter = 255
    while True:
        if ColourCounter < 0:
            ColourCounter = 0
        if Colour >= ColourCounter:
            return ColourCounter
        else:
            ColourCounter = ColourCounter - ColourVariance

#Sepia
def SepiaTint():
    GreyScale()
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

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

#Draws the edges
def DrawEdges():
    for X in xrange (Width - 1):
        for Y in xrange (Height - 1):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            PixelSum = (Red + Green + Blue)

            Red2 = Screen.get_at((X + 1, Y )).r
            Green2 = Screen.get_at((X + 1, Y )).g
            Blue2 = Screen.get_at((X + 1, Y)).b

            NextPixelSum = (Red2 + Green2 + Blue2)
            Difference = NextPixelSum - PixelSum

            if Difference < 0:
                Difference = Difference * - 1
            if Difference > 255:
                Difference = 255
            Difference = 255 - Difference
            PXArray[X, Y] = (Difference, Difference, Difference)

#Variation on DrawEdges draws the edges but in colour, doesnt work well on some images. try it on parrot
def DrawEdgesColour():
    for X in xrange (Width - 1):
        for Y in xrange (Height - 1):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            PixelSum = (Red + Green + Blue)

            Red2 = Screen.get_at((X + 1, Y )).r
            Green2 = Screen.get_at((X + 1, Y )).g
            Blue2 = Screen.get_at((X + 1, Y)).b

            NextPixelSum = (Red2 + Green2 + Blue2)
            Difference = NextPixelSum - PixelSum

            if Difference < 0:
                Difference = Difference * - 1
            if Difference > 255:
                Difference = 255
            Difference = 255 - Difference

            Red = Red + Difference
            Green = Green + Difference
            Blue = Blue + Difference

            if Red > 255:
                Red = 255
            if Green > 255:
                Green = 255
            if Blue > 255:
                Blue = 255


            PXArray[X, Y] = (Red, Green, Blue)

#Kinda cell shades it, work in progress, press multiple times for thicker lines
def CelShadeSorta():
    for X in xrange(Width - 1):
        for Y in xrange(Height - 1):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            PixelSum = (Red + Green + Blue)

            Red2 = Screen.get_at((X + 1, Y)).r
            Green2 = Screen.get_at((X + 1, Y)).g
            Blue2 = Screen.get_at((X + 1, Y)).b

            NextPixelSum = (Red2 + Green2 + Blue2)
            Difference = NextPixelSum - PixelSum

            if Difference < 0:
                Difference = Difference * - 1
            if Difference > 255:
                Difference = 255

            Red = Red - Difference
            Green = Green - Difference
            Blue = Blue - Difference

            if Red < 0:
                Red = 0
            if Green < 0:
                Green = 0
            if Blue < 0:
                Blue = 0

            PXArray[X, Y] = (Red, Green, Blue)

#RainbowMatrixStyle. looks cool, made by accident
def RainbowMatrixStyle (Tolerance):
    Counter = 0
    for X in xrange(Width):
        for Y in xrange(Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            Colour = (Red + Blue + Green)/3

            if Colour > Tolerance:
                Counter = Counter + 1
            if Counter == 3:
                Counter = 0
            if Counter == 0:
                PXArray[X, Y] = (Red, 0, 0)
            elif Counter == 1:
                PXArray[X, Y] = (0, Green, 0)
            elif Counter == 2:
                PXArray[X, Y] = (0, 0, Blue)

#Variation on RainbowMatrix where it fills a lot of the blanks
def RainbowMatrixStyleFill():
    RainbowMatrixStyle(80)  #Remember to change this, 80 is good number for parrot
    for Y in xrange(Height):
        for X in xrange(Width):
            Counter = 0
            ColourNotFound = True
            while ColourNotFound:
                if X - Counter >= 0:
                    Red = Screen.get_at((X - Counter, Y)).r
                    Green = Screen.get_at((X - Counter, Y)).g
                    Blue = Screen.get_at((X - Counter, Y)).b

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

#Accidently made this one. Another variation of RainbowMatrixStyle, cool effect so decided to keep it
def RainbowMatrixStyleZ():
    RainbowMatrixStyle(80)   #Remember to change this, 80 is good number for parrot
    for Y in xrange(Height):
        for X in xrange(Width):
            Counter = 0
            ColourNotFound = True
            while ColourNotFound:
                if X - Counter >= 0:
                    Red = Screen.get_at((X - Counter, Y)).r
                    Green = Screen.get_at((X - Counter, Y)).g
                    Blue = Screen.get_at((X - Counter, Y)).b

                    Colour = (Red + Green + Blue)/3
                    if Colour > 30:  # This number can change a lot, wouldnt go higher than 50 though
                        Counter = Counter + 4  #Changing this number does fun stuff (0-5 reconmended)

                while Counter > 0:

                    if X - Counter >= 0:
                        PXArray[X - Counter, Y] = (Red, Green, Blue)
                    Counter = Counter - 1
                else:
                    ColourNotFound = False

def Mirrors():
    MirrorPoint = Width/2
    for Y in xrange(Height):
        for X in xrange(MirrorPoint):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b
            PXArray[Width - X - 1, Y] = (Red, Green, Blue)


#Makes a Collage
def PhoenixCol(PictureScale2):
    TargetX=0

    for X in xrange(PictureScale*2):
        TargetY = 0
        for Y in xrange(PictureScale):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b
            PXArray[TargetX + (PictureScale2 * 2), TargetY + PictureScale3] = (Red - Red/ColourManip, Green, Blue/ColourManip)
            TargetY = TargetY + 1
        TargetX = TargetX + 1
    PictureScale2 = PictureScale2 + PictureScale
    return PictureScale2
#Press the keys and it does stuff
while Running:
    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            Running = False
        if event.type == KEYDOWN and event.key == K_i:
            Invert()
        if event.type == KEYDOWN and event.key == K_g:
            GreyScale()
        if event.type == KEYDOWN and event.key == K_r:
            LessRed()
        if event.type == KEYDOWN and event.key == K_l:
            ColourTest()
        if event.type == KEYDOWN and event.key == K_w:
            WoodTex()
        if event.type == KEYDOWN and event.key == K_s:
            Spooky()
        if event.type == KEYDOWN and event.key == K_c:
            CloseEnough(Brown) # Can choose any colour using RGB value
        if event.type == KEYDOWN and event.key == K_p:
            Posterize(10)  # Try changing the value to alter the amount of posterization
        if event.type == KEYDOWN and event.key == K_q:
            SepiaTint()
        if event.type == KEYDOWN and event.key == K_e:
            DrawEdges()
        if event.type == KEYDOWN and event.key == K_k:
            DrawEdgesColour()
        if event.type == KEYDOWN and event.key == K_x:
            CelShadeSorta()
        if event.type == KEYDOWN and event.key == K_m:
            RainbowMatrixStyle(80)  #Tolerance, value between 0 and 255. 80 is good number for parrot
        if event.type == KEYDOWN and event.key == K_f:
            RainbowMatrixStyleFill()
        if event.type == KEYDOWN and event.key == K_z:
            RainbowMatrixStyleZ()
        if event.type == KEYDOWN and event.key == K_n:
            Mirrors()
        if event.type == KEYDOWN and event.key == K_b:
            while PictureScale3 != Height:
                PictureScale2 = PhoenixCol(PictureScale2)
                pygame.display.update()
                if PictureScale2 == Width/2:
                    PictureScale2 = 0
                    PictureScale3 = PictureScale3 + PictureScale
                    ColourManip = ColourManip + 0.2
                    print ColourManip
                    print PictureScale3
        pygame.display.update()
pygame.quit()
sys.exit()

