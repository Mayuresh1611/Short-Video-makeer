import cv2 as cv
from PIL import ImageFont,  ImageDraw , Image , ImageFilter
import numpy as np

def drawGlow( img ,  position , text , font  , glow_radius , glow_color = (255 , 255 , 255) ):
    print(img.size)
    alphaimg = Image.new('RGBA' , img.size , (255 , 255 , 255 , 0)) 
    draw = ImageDraw.Draw(alphaimg)
    for i in range(1, glow_radius + 1):
        alpha = int(255 * (1 - i / (glow_radius + 1)))
        offset = i
        draw.text((position[0] - offset, position[1]), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
        draw.text((position[0] + offset, position[1]), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
        draw.text((position[0], position[1] - offset), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
        draw.text((position[0], position[1] + offset), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
      
    # Draw the main text on top
    draw.text(position, text, font=font, fill=(255 , 255 , 255))
    combined = Image.alpha_composite(img, alphaimg)
    return combined

def putText( img , text:str , font:ImageFont , alignV="bottom"  , glow=False ):
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
        if font.getlength(potenLine) < imgWid:
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
        textWid = font.getlength(line)

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
            imgPIL = drawGlow(imgPIL , textPosition , text , font , 6 , (0 , 255 , 0) )
        else:
            draw.text(textPosition, line, font=font, fill=(0 , 0 , 0))


    imgCV = cv.cvtColor(np.array(imgPIL) , cv.COLOR_RGB2BGR)
    return imgCV

