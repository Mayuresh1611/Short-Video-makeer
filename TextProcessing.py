import cv2 as cv
from PIL import ImageFont,  ImageDraw , Image , ImageFilter
import numpy as np

def drawGlow( img ,  position , text , font  , glow_radius, color = (255 , 255 , 255), glow_color = (255 , 255 , 255) , letterSpacing = 0):
    print(img.size)
    colored_bg = img
    text_image = Image.new('RGBA', img.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(text_image)
    
    transparency_values = [255, 80, 70, 60, 50, 40, 30, 20, 10]
    
    for i in range(len(transparency_values) - glow_radius, len(transparency_values)):
        # Create drawing context
        draw = ImageDraw.Draw(text_image)
        
        # Add text to the new blank image
        for char in text:
                draw.text(position, char, color , (255, 150, 100, transparency_values[i]), font ,
                stroke_width=i+1 ,align = 'center')
                width = draw.textlength(char, font) + letterSpacing
                position = (position[0]+width, position[1])

        colored_bg = Image.alpha_composite(colored_bg, text_image)
        
        text_image = Image.new('RGBA', colored_bg.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(colored_bg)
    for char in text:
                draw.text(position, char, color, font)
                width = draw.textlength(char, font) + letterSpacing
                position = (position[0]+width, position[1])
    return colored_bg

def putText( img , text:str , font:ImageFont , alignV="bottom"  , color = (255 , 255 , 255) ,  glow=False , letterSpacing = 0):
    """ 
    img : Matlike cv image
    text: string
    font: ImageFont
    alignV: vertical alignment ( bottom, center , top)
    glow = Glow effect on the text, true or false
    return : matlike (cv format imgage)

    """
    # convert cv image to PIL image
    imgPIL = Image.fromarray(cv.cvtColor(img , cv.COLOR_BGR2RGBA))

    # read the dimesions of the image
    imgWid, imgHeight = imgPIL.size 
    draw = ImageDraw.Draw(imgPIL)
    
    # arrange the text according to screen size 
    splitText = text.split()  
    Lines = []
    line = " " 
    while len(splitText) > 0:
        word = splitText[0]
        potenLine = line  + word + " "
        wordlen = font.getlength(word) + len(potenLine) * letterSpacing
        if wordlen > imgWid:
            raise ValueError
        if (font.getlength(potenLine) + len(potenLine) * letterSpacing) < imgWid:
            line = potenLine
            splitText.pop(0) 
        else:
            Lines.append(line)
            line = ""
    if len(line) > 0:
        Lines.append(line)

    # For each text
    if alignV == "center":
        buff =  -(font.size * int(len(Lines) // 2) + ((font.size * int(len(Lines) // 2)) // 2))
    elif alignV == "top":
        buff = 0
    else:
        buff = -(font.size * len(Lines)  + ((font.size * int(len(Lines) // 2)) // 2))

    for line in Lines:
        textWid = font.getlength(line) + len(line) * letterSpacing

        horiP = (imgWid - textWid) // 2
        
        if alignV == "center":
            vertP = ( imgHeight // 2 ) + buff
        elif alignV == "top":
            vertP = ( imgHeight // 10.8) + buff
        else:
            vertP = ( imgHeight // 1.1) + buff
        buff += font.size + (font.size // 2)

        
        if vertP > imgHeight:
            raise ValueError("Text overflows the screen height")
    

        textPosition = (horiP , vertP)
        print(textPosition)
        if glow:
            imgPIL = drawGlow(imgPIL , textPosition , text , font , 6 , (0 , 255 , 0) , letterSpacing )
        else:
            for char in line:
                draw.text(textPosition, char, color, font )
                width = draw.textlength(char, font) + letterSpacing
                textPosition = (textPosition[0]+width, textPosition[1])


    imgCV = cv.cvtColor(np.array(imgPIL) , cv.COLOR_RGB2BGR)
    return imgCV

